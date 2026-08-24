#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI-OS 收尾自动写回脚本（无感最小集第 2 项）
============================================
设计来源：AI-OS_无感使用设计_2026-08-15.md §3.4（E-6：状态写回自动化，不靠 Agent 手动填状态字段）
2026-08-21 reshape：V2 已删除 CURRENT_GOAL.md（被 task_cards 替代）——写回对象改为**任务卡 Event Log**。
2026-08-21 修正：git 事实取自**任务卡 Goal 中定位的项目目录**（有独立 git 用其提交；untracked/无 git 用项目内最近修改文件），不再取根仓库旧提交（off-topic 噪音）。
2026-08-22 A19 reshape：收尾写回后检查 SUCCESS_LOG 是否已为本任务追加 Entry，无则提示（把账本触发放进收尾路径；Phase 1 实证：Agent 收尾无 SUCCESS_LOG 概念）。
2026-08-22 Learning Closure reshape：收尾时把"是否值得沉淀经验"放进决策空间（只加判断入口，不强制产生 Knowledge；Phase 1-4 实证：沉淀概念从未进入 Agent 收尾 reasoning）。

做什么：
  任务收尾运行时，从 git 提取本次实际改动，把收尾事件追加到指定任务卡（TASK-*.md）的
  Event Log——Agent 不需要记得手动登记收尾，事实由 git 生成。

为什么这样设计（对第一纪元死因）：
  - resume.py 死于"无自动触发点"——本脚本被设计为收尾链的一环，挂在 git 提交/收尾流程上，
    不依赖 Agent 记得跑。
  - K-027 实证：状态字段是最容易遗漏的（Agent 写内容字段忠实、状态字段漏改）——自动写回消灭遗漏。

用法：
  python tools/wrapup_sync.py [TASK-ID] [--dry-run]
  TASK-ID 例如 TASK-20260821-008（不传则扫描 active 找最近更新的 Executing 卡）。

输出：
  dry-run: 只打印将更新的内容，不写文件。
  正式:    在任务卡 Event Log 追加一条收尾事件（最近提交 + 改动文件 + 未提交提醒），返回改动行数。
"""
import subprocess
import sys
import os
import datetime
import re
import time

from _root_guard import guard
guard(__file__)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARDS_DIR = os.path.join(ROOT, "task_cards")
ACTIVE_DIR = os.path.join(CARDS_DIR, "active")


def git(cmd, cwd):
    # Windows 默认 GBK 解码会炸中文提交信息（实测 2026-08-16）——git 输出按 UTF-8 解
    r = subprocess.run(["git"] + cmd, cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    return r.stdout.strip(), r.returncode


def find_project_dir(card_path):
    """从任务卡 Goal/正文提取项目路径（Windows 盘符路径），返回第一个存在的目录。"""
    with open(card_path, "r", encoding="utf-8") as f:
        text = f.read()
    m = re.search(r"## Goal\s*\n(.*?)(?=\n## |\Z)", text, re.S)
    goal = m.group(1) if m else text
    candidates = re.findall(r"[A-Za-z]:[\\/][^\s`\"'<>|]+", goal) + \
                 re.findall(r"[A-Za-z]:[\\/][^\s`\"'<>|]+", text)
    seen = set()
    for p in candidates:
        norm = p.replace("/", "\\").rstrip("\\.,;:)]}") if p else p
        if norm in seen:
            continue
        seen.add(norm)
        if os.path.isdir(norm):
            return norm
    return None


def nearest_git_root(path):
    """从 path 向上找最近的含 .git 的目录。"""
    cur = os.path.abspath(path)
    while True:
        if os.path.isdir(os.path.join(cur, ".git")):
            return cur
        parent = os.path.dirname(cur)
        if parent == cur:
            return None
        cur = parent


def recent_project_files(project_dir, limit=5):
    """项目内最近修改的代码/文档文件（mtime 事实，供 untracked 项目使用）。"""
    entries = []
    for root, dirs, files in os.walk(project_dir):
        dirs[:] = [d for d in dirs if d not in ("__pycache__", ".git", "node_modules", "data", "demo")]
        for name in files:
            if name.endswith((".py", ".md", ".json", ".html")):
                p = os.path.join(root, name)
                try:
                    entries.append((os.path.getmtime(p), p))
                except OSError:
                    pass
    entries.sort(reverse=True)
    rels = []
    for _, p in entries[:limit]:
        try:
            rels.append(os.path.relpath(p, project_dir).replace("\\", "/"))
        except ValueError:
            rels.append(p)
    return rels


def git_facts(project_dir):
    """返回 (last_msg, files_desc, dirty_desc)。git 事实优先取项目目录的提交；untracked/无 git 用 mtime。"""
    git_root = nearest_git_root(project_dir)
    if git_root:
        rel = os.path.relpath(project_dir, git_root)
        status, _ = git(["status", "--porcelain", "--", rel], git_root)
        untracked = any(l.startswith("??") for l in status.splitlines())
        if not untracked:
            last_msg, _ = git(["log", "-1", "--pretty=format:%h %s"], git_root)
            files, _ = git(["-c", "core.quotepath=false", "diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD", "--", rel], git_root)
            file_list = [f for f in files.splitlines() if f.strip() and f.startswith(rel)]
            names = ", ".join(f.replace(rel + os.sep, "", 1).replace("\\", "/") for f in file_list[:3])
            files_desc = f"{names} 等 {len(file_list)} 个文件" if len(file_list) > 3 else (names or "（无）")
            dirty, _ = git(["status", "--porcelain", "--", rel], git_root)
            dirty_n = len([l for l in dirty.splitlines() if l.strip()])
            return last_msg or "（无提交）", files_desc, f"未提交 {dirty_n} 项"
    # untracked 或不在 git 仓库内：用项目内最近修改文件（mtime 事实）
    rels = recent_project_files(project_dir)
    names = ", ".join(rels)
    files_desc = f"{names} 等 {len(rels)} 个文件" if len(rels) > 3 else (names or "（无）")
    return "（项目未纳入独立 git / untracked）", files_desc, "项目未 commit（任务纪律）"


def find_target_card(task_id):
    """TASK-ID -> active 卡路径；未指定则找最近更新的 Executing 卡。"""
    if task_id:
        p = os.path.join(ACTIVE_DIR, f"{task_id}.md")
        return p if os.path.isfile(p) else None
    best, best_mtime = None, 0.0
    if os.path.isdir(ACTIVE_DIR):
        for name in os.listdir(ACTIVE_DIR):
            if not name.endswith(".md"):
                continue
            p = os.path.join(ACTIVE_DIR, name)
            try:
                mtime = os.path.getmtime(p)
            except OSError:
                continue
            if mtime > best_mtime:
                best, best_mtime = p, mtime
    return best


def append_event_log(card_path, entry_line):
    """在任务卡的 Event Log 表格末尾追加一行；无 Event Log 小节则追加到文件末尾。"""
    with open(card_path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
    # 找 "## Event Log" 小节内的最后一行表格行
    in_event = False
    last_table_idx = -1
    for i, line in enumerate(lines):
        if line.strip().startswith("## Event Log"):
            in_event = True
            continue
        if in_event and line.strip().startswith("## "):
            break
        if in_event and line.strip().startswith("|"):
            last_table_idx = i
    if last_table_idx >= 0:
        lines.insert(last_table_idx + 1, entry_line)
    else:
        lines.append("")
        lines.append("## Event Log")
        lines.append("")
        lines.append("| Time | State | Reason | Changed By |")
        lines.append("|------|-------|--------|:----------:|")
        lines.append(entry_line)
    with open(card_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    return 1


def check_success_log(card_path):
    """A19：检查本次任务是否已在 SUCCESS_LOG 追加 Entry；无则提示显式确认。"""
    log_path = os.path.join(ROOT, "AI-OS_SUCCESS_LOG.md")
    if not os.path.isfile(log_path):
        print("[wrapup] 提示：AI-OS_SUCCESS_LOG.md 不存在——收尾时应创建并追加 Entry")
        return
    with open(log_path, "r", encoding="utf-8") as f:
        text = f.read()
    task_id = os.path.basename(card_path).removesuffix(".md")
    if task_id not in text:
        print(f"[wrapup] 提示：本任务 {task_id} 尚未在 AI-OS_SUCCESS_LOG.md 追加 Entry。")
        print("        有消费语境但没消费 → 请显式追加 footprint = NONE 的 Entry（宁留缺口不事后造数据）。")
        print("        无消费语境 → 请追加 Entry 并标注 NOT_APPLICABLE。")
    else:
        print(f"[wrapup] SUCCESS_LOG 已包含 {task_id} 的 Entry（收口完整）")


def check_learning_closure(card_path):
    """Learning Closure（A04/A05/A13 最小 reshape）：把'是否值得沉淀'放进收尾决策空间。

    只增加判断入口，不强制生成 Knowledge：
      - 无 → 显式确认"无值得沉淀"（有效输出，不是失败）
      - 有 → 走 A05 结构化判定 → A04 审查 → 才进入 domains
    """
    print("[wrapup] 沉淀检查（Learning Closure）：本任务是否有值得沉淀的经验/规则/教训？")
    print("        无 → 在 SUCCESS_LOG 显式确认'无值得沉淀'即可（'无'也是有效输出）。")
    print("        有 → 走 A05 结构化判定（原因/条件/行为/结果/可复用性）→ A04 审查 → 才进入 domains。")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    task_id = args[0] if args else None
    dry = "--dry-run" in sys.argv

    card_path = find_target_card(task_id)
    if not card_path:
        print(f"[wrapup] 未找到任务卡（{'TASK-' + task_id if task_id else 'active 无候选'}）——跳过")
        return 0

    # git 事实：优先取任务卡定位的项目目录（有独立 git 用提交；untracked 用 mtime 最近文件）
    project_dir = find_project_dir(card_path) or ROOT
    last_msg, files_desc, dirty_desc = git_facts(project_dir)

    now = datetime.datetime.now().strftime("%H:%M")
    today = datetime.date.today().isoformat()
    entry_line = (
        f"| {now} | Executing | 收尾写回（wrapup_sync {today}，项目 {os.path.basename(project_dir)}）："
        f"提交 `{last_msg}`；改动 {files_desc}；{dirty_desc} | Worker |"
    )

    if dry:
        print(f"[wrapup] DRY-RUN——将追加到 {os.path.basename(card_path)} Event Log：")
        print(entry_line)
        print("[wrapup] 收尾检查（E6）：若本次没有值得沉淀的经验，请确认“无相关经验值得记录”——"
              "空结果本身是信号，不硬写，但要过一遍。")
        return 0

    append_event_log(card_path, entry_line)
    print(f"[wrapup] 已写回 {card_path} Event Log（+1 行）")
    print("[wrapup] 收尾检查（E6）：若本次没有值得沉淀的经验，请确认“无相关经验值得记录”——"
          "空结果本身是信号，不硬写，但要过一遍。")
    check_success_log(card_path)
    check_learning_closure(card_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
