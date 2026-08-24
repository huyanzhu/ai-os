# -*- coding: utf-8 -*-
"""
_root_guard.py — V2 tools 结构断言（D-036 补充 · 双保险 · 2026-08-24 · v2 2026-08-24）

为什么存在：
  D-036 已把 v1 镜像工具移入 D:\\AI\\tools\\_v1-archived\\ 并 fail-closed；
  本 guard 是第二道保险：任何 V2 工具启动时断言所在目录树具备 AI-OS V2 结构
  （AGENTS.md + capabilities/INDEX.md + domains/patterns），否则立即失败退出，
  避免静默读取错误语料树。

  v2（2026-08-24 发布验证修正）：不再硬编码 D:\\AI-os 绝对路径——发布版 clone
  到任意路径必须可正常使用；结构验证仍可区分 v1 树（v1 无 capabilities/INDEX.md）。

用法（每个 V2 工具在解析 ROOT 之前调用）：
  from _root_guard import guard
  guard(__file__)

只读，无副作用。
"""
import os
import sys

TOOLS_DIR = os.path.normcase(os.path.realpath(os.path.dirname(os.path.abspath(__file__))))
ROOT_DIR = os.path.dirname(TOOLS_DIR)

# V2 结构标志（v1 树缺少 capabilities/INDEX.md，结构验证即可区分）
V2_MARKERS = (
    os.path.join(ROOT_DIR, "AGENTS.md"),
    os.path.join(ROOT_DIR, "capabilities", "INDEX.md"),
    os.path.join(ROOT_DIR, "domains", "patterns"),
)


def guard(script_file):
    script_dir = os.path.normcase(os.path.realpath(os.path.dirname(os.path.abspath(script_file))))
    if script_dir != TOOLS_DIR:
        sys.exit(
            f"[root-guard] FAIL-CLOSED: script not inside tools dir {TOOLS_DIR}; "
            f"refusing to run (script: {os.path.abspath(script_file)})."
        )
    missing = [os.path.relpath(m, ROOT_DIR) for m in V2_MARKERS if not os.path.exists(m)]
    if missing:
        sys.exit(
            f"[root-guard] FAIL-CLOSED: ROOT {ROOT_DIR} is not an AI-OS V2 tree "
            f"(missing: {', '.join(missing)}); refusing to run."
        )
