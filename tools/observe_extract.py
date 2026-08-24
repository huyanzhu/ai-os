#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
observe_extract.py — Observation Extraction（V2 第一代新能力 NC-001，最小 realization）

输入：Codex session JSONL
输出：结构化观察摘要——能力使用 Trace / token 成本（按任务段差分）/ 时间 / 推理片段（Why）/ Artifact

2026-08-22 P1 完善：
  - Phase/Task 过滤：按 task_started→task_complete 切段，token 用 total 差分（本段最后 - 上段最后）
  - Artifact 提取：从 apply_patch / exec_command 文件操作中提取涉及文件路径

只读，不修改任何文件；不做成观察系统（不建仪表盘/不自动监控）。
"""
import json
import os
import sys

from _root_guard import guard
guard(__file__)


# 已知 AI-OS 工具/能力映射（最小，可扩展）
TOOL_PATTERNS = {
    "task_card": "A16 Task Card",
    "experience_push": "A18 experience_push",
    "wrapup": "A22 wrapup",
    "SUCCESS_LOG": "A19 SUCCESS_LOG",
    "ONBOARD": "C02 ONBOARD",
    "TOOL_RUNTIME": "C03 TOOL_RUNTIME",
    "README": "入口 README",
    "AGENTS": "F01 宪法",
    "MAP": "G03 MAP",
}

REASON_KW = ["task_card", "experience_push", "wrapup", "SUCCESS_LOG", "沉淀", "建卡", "收尾", "pattern"]
ARTIFACT_CMD = ["Set-Content", "Add-Content", "Move-Item", "New-Item", "Copy-Item", "Remove-Item"]
PATH_RE = r"[A-Za-z]:[\\/][^\s`\"'<>|,;]+"


def parse_session(path):
    """按任务段切分：每段 = task_started → task_complete。
    返回 segments: [{calls, tokens(diff), times, reasonings, artifacts}]"""
    import re
    segments = []
    cur = None
    prev_total = 0
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            try:
                obj = json.loads(line)
            except Exception:
                continue
            p = obj.get("payload", {})
            t = p.get("type")
            if t == "task_started":
                cur = {"calls": [], "totals": [], "times": [("start", p.get("started_at"))], "reasonings": [], "artifacts": []}
                continue
            if t == "task_complete":
                if cur is not None:
                    total = cur["totals"][-1] if cur["totals"] else None
                    cur["token"] = (total - prev_total) if (total is not None and prev_total) else total
                    prev_total = total or prev_total
                    cur["times"].append(("end", p.get("completed_at")))
                    segments.append(cur)
                    cur = None
                continue
            if cur is None:
                continue
            if t in ("function_call", "custom_tool_call"):
                name = p.get("name", "")
                raw_args = p.get("arguments") or p.get("input") or ""
                if isinstance(raw_args, dict):
                    raw_args = json.dumps(raw_args, ensure_ascii=False)
                cmd = ""
                try:
                    cmd = json.loads(raw_args).get("cmd", "") if isinstance(raw_args, str) and raw_args.strip().startswith("{") else ""
                except Exception:
                    cmd = ""
                if name == "apply_patch" or (cmd and "apply_patch" in cmd):
                    for m in re.finditer(r"\*\*\* (?:Update|Add|Delete) File: ([^\n\r]+)", raw_args):
                        cur["artifacts"].append(m.group(1).strip())
                if cmd:
                    cur["calls"].append((p.get("name", ""), cmd))
                    if any(k in cmd for k in ARTIFACT_CMD):
                        paths = re.findall(PATH_RE, cmd)
                        cur["artifacts"].extend(paths)
            elif t == "token_count":
                info = p.get("info", {})
                total = info.get("total_token_usage", {}).get("total_tokens")
                if total is not None:
                    cur["totals"].append(total)
            elif t == "reasoning":
                rt = p.get("reasoning_text") or ""
                if not rt:
                    c = p.get("content")
                    if c:
                        rt = " ".join(x.get("text", "") for x in c if x.get("type") == "reasoning_text")
                if rt:
                    cur["reasonings"].append(rt)
    return segments


def main():
    if len(sys.argv) < 2:
        print("usage: python tools/observe_extract.py <session.jsonl>")
        return 1
    path = sys.argv[1]
    if not os.path.isfile(path):
        print(f"[observe_extract] 文件不存在：{path}")
        return 1
    segments = parse_session(path)
    print(f"=== Observation Extraction: {os.path.basename(path)} ===")
    print(f"任务段数: {len(segments)}")
    sel = None
    if "--task" in sys.argv:
        try:
            sel = int(sys.argv[sys.argv.index("--task") + 1])
        except (IndexError, ValueError):
            pass
    for i, seg in enumerate(segments):
        if sel is not None and i != sel:
            continue
        print(f"\n--- Task 段 {i} ---")
        print(f"调用总数: {len(seg['calls'])}")
        usage = {}
        for _name, cmd in seg["calls"]:
            for pat, cap in TOOL_PATTERNS.items():
                if pat in cmd:
                    usage[cap] = usage.get(cap, 0) + 1
        for cap, cnt in sorted(usage.items(), key=lambda x: -x[1]):
            print(f"  {cap}: {cnt}")
        print(f"token（本段差分）: {seg.get('token', 'UNKNOWN')}")
        print(f"time: {seg['times'] if seg['times'] else 'UNKNOWN'}")
        hits = [r for r in seg["reasonings"] if any(k in r for k in REASON_KW)]
        print(f"推理片段: {len(hits)}/{len(seg['reasonings'])}")
        uniq_artifacts = sorted(set(seg["artifacts"]))
        print(f"Artifact 文件（去重）: {len(uniq_artifacts)}")
        for a in uniq_artifacts[:10]:
            print(f"  {a}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
