#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
task_start.py — Unified Task-start Discovery（A18 大改最小实现 · 2026-08-23 · D-009）

任务开始时的统一发现入口，一次列出四类对象，标注来源与消费语义：
  ① 任务卡（Task Memory） → 恢复 / 继续
  ② 知识 / 经验（Knowledge） → 读 / 采纳
  ③ 能力 / Skill（Capability Space） → 使用 / 装配 / 装载（按 trigger 命中判断）

知识检索复用 experience_push 的打分逻辑（同源，不重复实现）；任务卡走递归 active
扫描（补上"任务卡不入索引"缺陷）；能力来自 capabilities/INDEX.md。
只读，不修改任何文件。

空结果不静默（2026-08-25 · 空态引导补全）：无 active 任务卡 / 知识未命中 /
能力 trigger 全未命中时，分别输出下一步引导（含可执行命令），替代静默空输出。
依据既有经验：空态必须有下一步（ui-beautification 空态门禁）、空结果即信号
（E6）、Next Action 要具体到物理动作（skill_pack_direction）。
"""
import argparse
import io
import os
import re
import sys

from _root_guard import guard
guard(__file__)

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import experience_push as ep


def task_cards():
    """active/ 递归扫描任务卡（含项目卡），返回 (relpath, title, goal)。"""
    base = os.path.join(ROOT, "task_cards", "active")
    out = []
    if not os.path.isdir(base):
        return out
    for root, _dirs, files in os.walk(base):
        for name in sorted(files):
            if not name.endswith(".md") or name.startswith("_"):
                continue
            p = os.path.join(root, name)
            try:
                raw = io.open(p, "r", encoding="utf-8", errors="replace").read()
            except OSError:
                continue
            m = re.search(r"^#\s+(.+)$", raw, re.M)
            title = m.group(1).strip() if m else os.path.basename(p)
            gm = re.search(r"^##\s+Goal\s*\n(.*?)(?=^##\s|\Z)", raw, re.M | re.S)
            goal = re.sub(r"\s+", " ", gm.group(1)).strip()[:180] if gm else ""
            out.append((os.path.relpath(p, ROOT).replace("\\", "/"), title, goal))
    return out


def knowledge(query_tokens, n=5, min_score=4.0):
    """复用 experience_push 的语料/账本打分，返回 (score, kind, rel, title, matched)。"""
    results = []
    for kind, path in ep.collect_files():
        try:
            raw = io.open(path, "r", encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        score, matched, fm = ep.score_file(query_tokens, raw)
        if score > 0:
            title = fm.get("title", "") or os.path.basename(path)
            results.append((score, kind, ep.disp_path(path), title, matched))
    for path, weight, header, text in ep.collect_ledger_chunks():
        hits = query_tokens & ep.tokenize(header + " " + text)
        if hits:
            score = weight * len(hits)
            kind = "proven" if weight >= ep.PROVEN_LEDGER_WEIGHT else "ledger"
            results.append((score, kind, ep.disp_path(path), header or kind, hits))
    results.sort(key=lambda r: -r[0])
    return [r for r in results if r[0] >= min_score][:n]


def capabilities(query_tokens):
    """解析 capabilities/INDEX.md 表格，返回 (name, hit, trigger, activation)。"""
    idx = os.path.join(ROOT, "capabilities", "INDEX.md")
    out = []
    if not os.path.isfile(idx):
        return out
    raw = io.open(idx, "r", encoding="utf-8", errors="replace").read()
    for line in raw.splitlines():
        if not line.startswith("|") or line.startswith("|---") or line.startswith("| #"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 3:
            continue
        name = cells[1] if len(cells) > 1 else cells[0]
        trig = cells[3] if len(cells) > 3 else ""
        act = cells[4] if len(cells) > 4 else ""
        hit = bool(query_tokens & ep.tokenize(trig))
        out.append((name, hit, trig[:140], act[:140]))
    return out


def main():
    if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description="Unified task-start discovery (read-only).")
    ap.add_argument("query", nargs="*", help="任务描述；配合 --auto 或单独使用")
    ap.add_argument("--auto", action="store_true", help="从 git 状态 + 最近 active 任务卡意图派生查询")
    ap.add_argument("-n", type=int, default=5, help="知识候选条数（默认 5）")
    args = ap.parse_args()

    query = " ".join(args.query)
    if args.auto:
        auto = ep.auto_query()
        query = (query + " " + auto).strip() if query else auto
    qtokens = ep.tokenize(query)

    print("=== 统一开工发现（task_start）===")
    print("查询: %s\n" % (query or "(空)"))

    print("--- ① 任务卡（恢复 / 继续）---")
    cards = task_cards()
    if not cards:
        print("  （无 active 任务卡）")
        print("  下一步: python tools/task_card.py create \"<任务一句话>\" 建卡")
        print("         （任务卡 = 工作记忆：目标/状态/下一步，是每轮开工恢复上下文的锚点）")
    else:
        for rel, title, goal in cards[:8]:
            print("- [任务卡] %s :: %s" % (rel, title))
            if goal:
                print("    goal: %s" % goal)

    print("\n--- ② 知识 / 经验（读 / 采纳）---")
    if qtokens:
        hits = knowledge(qtokens, n=args.n)
        if not hits:
            print("  （知识未命中）")
            print("  下一步: 换更具体的任务描述重跑（python tools/task_start.py \"<描述>\"），")
            print("         或 python tools/experience_push.py \"<描述>\" 手工检索；")
            print("         空结果即信号：真实踩坑/信念改变才沉淀 Observation，不硬写。")
        for score, kind, rel, title, matched in hits:
            print("- [知识/%s] %.1f %s :: %s" % (kind, score, rel, title))
    else:
        print("  （无查询，跳过知识检索；可手写查询或 --auto）")
        print("  下一步: 加任务描述重跑（python tools/task_start.py \"<描述>\"），")
        print("         或 --auto 从 git 状态派生查询（python tools/task_start.py --auto）。")

    print("\n--- ③ 能力 / Skill（使用 / 装配 / 装载）---")
    caps = capabilities(qtokens)
    if not caps:
        print("  （capabilities/ 无注册单位）")
        print("  下一步: 属正常——能力由 evolution 按真实需求生长，注册表完整不是目标；")
        print("         有需要时经 evolution 裁决后在 capabilities/INDEX.md 注册新单位。")
    else:
        hit_any = False
        for name, hit, trig, act in caps:
            if hit:
                hit_any = True
            print("- [能力] %s（trigger %s）" % (name, "命中" if hit else "未命中"))
            if trig:
                print("    trigger: %s" % trig)
            if act:
                print("    activation: %s" % act)
        if not hit_any:
            print("  全部 trigger 未命中 → 下一步: 换更接近 trigger 词的任务描述重试，")
            print("         或直接读 capabilities/INDEX.md 手动浏览/装配所需单位。")

    print("\n来源与消费语义：任务卡=恢复/继续；知识=读/采纳；能力=使用/装配；Skill=装载/激活。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
