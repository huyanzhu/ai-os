# -*- coding: utf-8 -*-
"""
task_card.py — task_cards 最小工具（2026-08-20 · V2 第一形态）

三个动作（create / list / archive），轻量：
  create  <title>    -> 复制模板到 active/，命名 TASK-YYYYMMDD-NNN.md
  list               -> 列出 active/ 卡片
  archive <TASK-ID> [--confirm] -> 从 active/ 移到 archive/（仅当任务已完成且已获用户确认）

不做：自动推断字段 / 自动写入状态 / 自动生命周期 / 自动分析内容 / telemetry / 与 CURRENT_GOAL 同步。
原则（用户 2026-08-20）：最小工具降低使用摩擦，内容和行为保持真实；字段与生命周期由真实使用观察决定。
2026-08-21：归档增加"任务完成 + 用户确认"门槛（--confirm），未确认拒绝归档；编号同时扫描 active+archive 防覆盖。
"""

import os
import re
import shutil
import sys
from datetime import date, datetime

from _root_guard import guard
guard(__file__)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARDS_DIR = os.path.join(ROOT, "task_cards")
ACTIVE_DIR = os.path.join(CARDS_DIR, "active")
ARCHIVE_DIR = os.path.join(CARDS_DIR, "archive")
TEMPLATE = os.path.join(CARDS_DIR, "_TASK_CARD_template.md")


def _next_id(prefix="TASK"):
    """生成 TASK-YYYYMMDD-NNN（按 active + archive 内同日已有编号递增，防止归档后 ID 复用覆盖）。"""
    today = date.today().strftime("%Y%m%d")
    pattern = re.compile(rf"^{prefix}-{today}-(\d{{3}})\.md$")
    max_n = 0
    for d in (ACTIVE_DIR, ARCHIVE_DIR):
        if os.path.isdir(d):
            for f in os.listdir(d):
                m = pattern.match(f)
                if m:
                    max_n = max(max_n, int(m.group(1)))
    return f"{prefix}-{today}-{max_n + 1:03d}"


def cmd_create(title, project=None):
    if not os.path.isfile(TEMPLATE):
        print(f"[task_card] 模板缺失：{TEMPLATE}")
        return 1
    task_id = _next_id()
    target_dir = os.path.join(ACTIVE_DIR, project) if project else ACTIVE_DIR
    if project:
        os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, f"{task_id}.md")
    with open(TEMPLATE, "r", encoding="utf-8") as src:
        content = src.read()
    # 仅替换最表面的 Task ID 示例，不推断任何其他字段
    content = content.replace("TASK-YYYYMMDD-001", task_id)
    content = content.replace("YYYY-MM-DD HH:mm", datetime.now().strftime("%Y-%m-%d %H:%M"))
    if title:
        content = content.replace("# TASK_CARD", f"# TASK_CARD — {title}")
    with open(target, "w", encoding="utf-8") as dst:
        dst.write(content)
    print(f"[task_card] created: {task_id}  ({target})")
    return 0


def cmd_list():
    """列出 active：项目文件夹（目录名天然可关联）+ 卡片（TASK-ID + 标题/Goal 摘要）。"""
    entries = sorted(e for e in os.listdir(ACTIVE_DIR) if not e.startswith("."))
    dirs = [e for e in entries if os.path.isdir(os.path.join(ACTIVE_DIR, e))]
    files = [e for e in entries if os.path.isfile(os.path.join(ACTIVE_DIR, e))]
    if not entries:
        print("[task_card] active: (none)")
        return 0
    print("[task_card] active:")
    for d in dirs:
        print(f"  {d}/  —  [项目文件夹]")
    for f in files:
        print(f"  {f}  —  {_card_summary(f.removesuffix('.md'))}")
    return 0


def _card_summary(task_id):
    """读卡文件，返回标题（# TASK_CARD — xxx）；无标题则取 Goal 首行；均无则标注。"""
    path = os.path.join(ACTIVE_DIR, f"{task_id}.md")
    try:
        with open(path, "r", encoding="utf-8") as fh:
            fallback = None
            in_goal = False
            for line in fh:
                s = line.strip()
                if s.startswith("# TASK_CARD"):
                    rest = s.replace("# TASK_CARD", "", 1).strip(" —-\t")
                    if rest:
                        return rest
                    fallback = "(untitled)"
                    continue
                if s == "## Goal":
                    in_goal = True
                    continue
                if in_goal:
                    if s.startswith("## ") or s.startswith("```"):
                        if s.startswith("## "):
                            break
                        continue
                    if s:
                        return s[:90]
            return fallback or "(untitled)"
    except OSError:
        return "(unreadable)"


def cmd_archive(task_id, confirm=False):
    task_id = task_id.removesuffix(".md")
    src = os.path.join(ACTIVE_DIR, f"{task_id}.md")
    if not os.path.isfile(src):
        print(f"[task_card] not found in active: {task_id}")
        return 1
    if not confirm:
        print(
            "[task_card] 归档被拒绝：归档 = 任务已完成且已获用户确认。\n"
            "  - 若任务/项目尚未完成（例如阶段一完成、后续还有阶段），请保持 active，不要归档。\n"
            "  - 确认已完成并已获用户确认后，重新运行：\n"
            "      python tools/task_card.py archive <TASK-ID> --confirm"
        )
        return 1
    dst = os.path.join(ARCHIVE_DIR, f"{task_id}.md")
    if os.path.isfile(dst):
        print(f"[task_card] 归档目标已存在，拒绝覆盖：{dst}（请先处理冲突）")
        return 1
    shutil.move(src, dst)
    print(f"[task_card] archived: {task_id}（已确认：任务完成 + 用户确认）")
    return 0


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 1
    cmd = argv[1]
    if cmd == "create":
        args = argv[2:]
        project = None
        if "--project" in args:
            i = args.index("--project")
            if i + 1 < len(args):
                project = args[i + 1]
                args = args[:i] + args[i + 2:]
        title = " ".join(args)
        return cmd_create(title, project)
    if cmd == "list":
        return cmd_list()
    if cmd == "archive":
        confirm = "--confirm" in argv[2:]
        ids = [a for a in argv[2:] if not a.startswith("--")]
        if len(ids) < 1:
            print("usage: task_card.py archive TASK-YYYYMMDD-NNN [--confirm]")
            return 1
        return cmd_archive(ids[0], confirm=confirm)
    print(f"unknown command: {cmd}")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
