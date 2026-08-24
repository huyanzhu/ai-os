# -*- coding: utf-8 -*-
"""
experience_push.py — AI-OS minimal experience push (load-bearing candidate v0.2)

WHAT IT IS
  A read-only retrieval CLI: given the Agent's current task (typed, OR derived
  automatically from live git state via --auto), it surfaces the most relevant
  past experience NEXT TO the Agent, which then decides whether to use it.
  Sources, in trust order:
    1. the PROVEN ledger (AI-OS_SUCCESS_LOG.md) - highest trust: append-only
       record of REAL observed outcomes (success AND honest failure), each
       reality-tested against an actual Agent session. By AI-OS L1
       ("verifiable assistance"), reality-tested > curated declarations.
    2. the pain ledger (curated memory) - every entry exists because a cost
       recurred; a solved problem must never be paid twice
    3. declarative patterns / experiences / task cards

--auto is the "keep doing it" mode: the query is derived from recent repo
state (last 3 commit subjects + changed files + CURRENT_GOAL intent), so
experience arrives without being hand-typed. CAVEAT: the query is seeded by
the Agent's OWN recent commits + goal, so --auto ECHOES recent focus rather
than independently reconstructing state - a rear-view mirror, not an impartial
recovery. (It does not avoid carrier self-certification; it only indirects it.)

WHAT IT IS NOT (discipline locks)
  - NOT a Runtime daemon: no background process, no watching, no state.
  - NOT a knowledge injector: it prints candidates; it never modifies context,
    files, or Agent behavior.
  - NOT a new state owner: writes nothing. Zero mutation. (v1F-safe)

USAGE
  python tools/experience_push.py "描述当前任务, 如: git bash 杀不掉 node 进程 端口占用"
  python tools/experience_push.py -n 3 "orphan branch 隔离历史"
  python tools/experience_push.py --auto            # query derived from git state
  python tools/experience_push.py --auto "额外线索"  # git state + extra hint

VALIDATION (why this exists)
  This is the Q1-Q5 Existence Validation candidate. Each real use should end
  with an honest Review answer: did it actually help? (see AGENTS.md rule 5)
"""
import argparse
import io
import os
import re
import subprocess
import sys

from _root_guard import guard
guard(__file__)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SOURCES = [
    ("pattern", os.path.join(ROOT, "domains"), ("patterns",)),
    ("experience", os.path.join(ROOT, "domains"), ("experiences",)),
    ("experience", os.path.join(ROOT, "domains", "experiences"), None),
    ("pattern", os.path.join(ROOT, "domains", "patterns"), None),
    ("task_card", os.path.join(ROOT, "task_cards"), None),
]

# frontmatter field weights
FIELD_WEIGHTS = {
    "trigger": 3.0,
    "keywords": 3.0,
    "alias": 3.0,
    "title": 2.0,
    "rule_id": 2.0,
    "condition": 2.0,
}
BODY_WEIGHT = 1.0
# The pain ledger (curated memory) is the highest-trust source: every entry
# exists BECAUSE a cost recurred. A solved problem must never be paid twice.
LEDGER_WEIGHT = 4.0
# The PROVEN ledger = AI-OS_SUCCESS_LOG.md: append-only record of REAL observed
# outcomes (success AND honest failure). By AI-OS L1 ("verifiable assistance"),
# reality-tested > curated declarations, so it outranks the declarative ledger.
PROVEN_LEDGER_WEIGHT = 5.0
CJK = re.compile(u"[\u4e00-\u9fff]")


def tokenize(text):
    """ASCII words + CJK bigrams, lowercased."""
    text = text.lower()
    tokens = set(re.findall(r"[a-z0-9_\-\.]{2,}", text))
    cjk_runs = re.findall(u"[\u4e00-\u9fff]{2,}", text)
    for run in cjk_runs:
        for i in range(len(run) - 1):
            tokens.add(run[i:i + 2])
    return tokens


def parse_frontmatter(raw):
    """Very small YAML-ish frontmatter reader: returns {field: text}."""
    fm = {}
    if not raw.startswith("---"):
        return fm, raw
    end = raw.find("\n---", 3)
    if end < 0:
        return fm, raw
    block = raw[3:end]
    body = raw[end + 4:]
    current = None
    for line in block.splitlines():
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", line)
        if m:
            current = m.group(1).strip().lower()
            fm[current] = m.group(2).strip()
        elif current and line.strip().startswith("-"):
            fm[current] = fm.get(current, "") + " " + line.strip().lstrip("- ").strip()
        elif current and line.startswith("  "):
            fm[current] = fm.get(current, "") + " " + line.strip()
    return fm, body


def collect_files():
    files = []
    for kind, base, subdirs in SOURCES:
        if not os.path.isdir(base):
            continue
        if subdirs is None:
            for name in sorted(os.listdir(base)):
                if name.endswith(".md"):
                    files.append((kind, os.path.join(base, name)))
        else:
            for domain in sorted(os.listdir(base)):
                for sub in subdirs:
                    d = os.path.join(base, domain, sub)
                    if os.path.isdir(d):
                        for name in sorted(os.listdir(d)):
                            if name.endswith(".md"):
                                files.append((kind, os.path.join(d, name)))
    return files


def ledger_files():
    """Return [(abs_path, weight)] for the experience ledger, trust-ordered.

    Trust tiers:
      5.0 PROVEN   - AI-OS_SUCCESS_LOG.md (observed reality; each entry is a
                     real Agent-session outcome, tagged [MECHANISM]/[PRODUCT-Q1])
      4.0 DECLARED - curated memory (project .workbuddy/memory/MEMORY.md, inside
                     the current environment) - curated declarations
      4.0 EXTERNAL - any AIOS_EXTERNAL_MEMORY env paths (opt-in; NOT read by
                     default, so a fresh clone never depends on host user memory)
    Missing files are skipped. See AI-OS_SUCCESS_LOG.md for provenance rules.

    Local-first, external-memory opt-in: the environment is self-sufficient by
    default; external memory is an explicitly configured provider.
    """
    declared = [
        os.path.join(ROOT, ".workbuddy", "memory", "MEMORY.md"),
    ]
    proven = [os.path.join(ROOT, "AI-OS_SUCCESS_LOG.md")]
    entries = [(p, PROVEN_LEDGER_WEIGHT) for p in proven]
    entries += [(p, LEDGER_WEIGHT) for p in declared]
    external = os.environ.get("AIOS_EXTERNAL_MEMORY")
    if external is not None:
        ext_paths = [p for p in external.split(os.pathsep) if p]
        if not ext_paths:
            ext_paths = [os.path.expanduser(os.path.join("~", ".workbuddy", "MEMORY.md"))]
        for p in ext_paths:
            ap = os.path.abspath(os.path.expanduser(p))
            print(f"[experience_push] external memory enabled: {ap}")
            entries.append((ap, LEDGER_WEIGHT))
    seen, out = set(), []
    for p, w in entries:
        ap = os.path.abspath(p)
        if ap not in seen and os.path.isfile(ap):
            seen.add(ap)
            out.append((ap, w))
    return out


def collect_ledger_chunks():
    """Split curated memory into per-bullet chunks, each tagged with its section
    header, so retrieval surfaces the specific lesson, not the whole file.
    Returns (path, weight, header, text)."""
    chunks = []
    for path, weight in ledger_files():
        try:
            with io.open(path, "r", encoding="utf-8", errors="replace") as f:
                lines = f.read().splitlines()
        except OSError:
            continue
        header = ""
        buf = []
        for line in lines:
            stripped = line.strip()
            if line.startswith("#"):
                if buf:
                    chunks.append((path, weight, header, " ".join(buf)))
                    buf = []
                header = line.lstrip("# ").strip()
            elif re.match(r"^-\s", line):
                if buf:
                    chunks.append((path, weight, header, " ".join(buf)))
                buf = [stripped.lstrip("- ").strip()]
            elif stripped and buf:
                buf.append(stripped.lstrip("- ").strip())
        if buf:
            chunks.append((path, weight, header, " ".join(buf)))
    return chunks


def disp_path(path):
    try:
        rp = os.path.relpath(path, ROOT)
    except ValueError:
        return path
    if rp.startswith(".."):
        home = os.path.expanduser("~")
        if path.startswith(home):
            return "~" + path[len(home):].replace("\\", "/")
        return path
    return rp


def score_file(query_tokens, raw):
    fm, body = parse_frontmatter(raw)
    score = 0.0
    matched = set()
    for field, weight in FIELD_WEIGHTS.items():
        if field in fm:
            ftokens = tokenize(fm[field])
            hits = query_tokens & ftokens
            if hits:
                score += weight * len(hits)
                matched |= hits
    btokens = tokenize(body[:4000])
    bhits = query_tokens & btokens
    if bhits:
        score += BODY_WEIGHT * len(bhits)
        matched |= bhits
    return score, matched, fm


def extract_action(raw):
    """Pull the action.do lines from frontmatter if present, else first heading."""
    m = re.search(r"action:\s*\n\s*do:\s*\n((?:\s*-\s.*\n)+)", raw)
    if m:
        lines = [l.strip().lstrip("- ").strip() for l in m.group(1).splitlines() if l.strip()]
        return " / ".join(lines[:3])
    m = re.search(r"^#+\s*(.+)$", raw, re.M)
    return m.group(1).strip() if m else ""


def preview_text(path, action, limit=260):
    """Return candidate content (action lines preferred, else body) so the
    experience lands IN the Agent's attention space — not just a filename it
    would have to open (2026-08-21: Consumption 缺口修复 #1)."""
    try:
        with io.open(path, "r", encoding="utf-8", errors="replace") as f:
            raw = f.read()
    except OSError:
        return action or ""
    m = re.search(r"action:\s*\n\s*do:\s*\n((?:\s*-\s.*\n)+)", raw)
    if m:
        lines = [l.strip().lstrip("- ").strip() for l in m.group(1).splitlines() if l.strip()]
        text = " / ".join(lines)
    else:
        fm, body = parse_frontmatter(raw)
        text = body.strip()
    text = re.sub(r"\s+", " ", text)
    return text[:limit] + ("…" if len(text) > limit else "")


def _git(args):
    try:
        out = subprocess.check_output(
            ["git"] + args, cwd=ROOT, stderr=subprocess.DEVNULL)
        return out.decode("utf-8", "replace")
    except Exception:
        return ""


def _goal_intent():
    """Read active task cards' Goal sections as INTENT for --auto.
    2026-08-24 R1：替换已死的 CURRENT_GOAL.md 钩子——意图源 = task_cards/active 各卡 ## Goal。
    """
    out = []
    base = os.path.join(ROOT, "task_cards", "active")
    if not os.path.isdir(base):
        return ""
    for root, _dirs, files in os.walk(base):
        for name in sorted(files):
            if not name.endswith(".md") or name.startswith("_"):
                continue
            p = os.path.join(root, name)
            try:
                raw = io.open(p, "r", encoding="utf-8", errors="replace").read()
            except OSError:
                continue
            m = re.search(r"^##\s+Goal\s*\n(.*?)(?=^##\s|\Z)", raw, re.M | re.S)
            if m:
                out.append(re.sub(r"\s+", " ", m.group(1)).strip()[:200])
    return " ".join(out)


def auto_query():
    """Build a query from the live repo state instead of a hand-typed one.

    This is the point of --auto: the query is derived from live repo state
    (changed files + recent commit subjects + persisted goal intent) rather
    than hand-typed by the Agent. A hand-typed query risks the Agent steering
    retrieval toward what it already believes; --auto instead anchors to recent
    activity. CAVEAT: the anchor IS the Agent's own recent commits + goal, so
    --auto reinforces recent focus (echo) - it does not independently recover
    state or suggest next steps. Goal intent (CURRENT_GOAL.md) aligns retrieval
    with WHAT the Agent is trying to do, not just WHAT files changed.
    """
    parts = []
    changed = _git(["diff", "--name-only", "HEAD"]) + "\n" + \
        _git(["diff", "--name-only", "--cached"])
    for line in changed.splitlines():
        line = line.strip()
        if not line:
            continue
        base = os.path.splitext(os.path.basename(line))[0]
        parts.append(base.replace("_", " ").replace("-", " "))
    subjects = _git(["log", "-3", "--format=%s"])
    parts.append(subjects)
    intent = _goal_intent()
    if intent:
        parts.append(intent)
    return " ".join(parts).strip()


def _context_query(context_path):
    """Build a query from the REAL working context (1.2 signal fix).

    --auto uses repo-wide git state at ROOT, which echoes AI-OS's own commits
    (rear-view mirror) — useless when the Agent is working inside a sub-project
    like projects/ai-consultant. --context instead derives the query from files
    recently touched in the given project dir (mtime-based), so retrieval tracks
    what the Agent is ACTUALLY working on, not what AI-OS committed last.
    """
    parts = []
    try:
        entries = []
        for root, dirs, files in os.walk(context_path):
            dirs[:] = [d for d in dirs if d not in ("node_modules", ".git", "data", "searxng", "dist", "build")]
            for name in files:
                if name.endswith((".js", ".py", ".html", ".md", ".json")):
                    p = os.path.join(root, name)
                    try:
                        entries.append((os.path.getmtime(p), p))
                    except OSError:
                        pass
        entries.sort(reverse=True)
        for _, p in entries[:15]:
            base = os.path.splitext(os.path.basename(p))[0]
            parts.append(base.replace("_", " ").replace("-", " "))
        parts.append(os.path.basename(os.path.abspath(context_path)))
        readme = os.path.join(context_path, "README.md")
        if os.path.isfile(readme):
            with io.open(readme, "r", encoding="utf-8", errors="replace") as f:
                head = f.read(500)
            m = re.search(r"^#\s+(.+)$", head, re.M)
            if m:
                parts.append(m.group(1))
    except OSError:
        return ""
    return " ".join(parts).strip()


def main():
    if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description="Surface relevant past experience near the Agent (read-only).")
    ap.add_argument("query", nargs="*", help="describe the current task / problem")
    ap.add_argument("-n", type=int, default=5, help="max results (default 5)")
    ap.add_argument("--min", type=float, default=4.0, help="minimum relevance score (default 4.0)")
    ap.add_argument("--auto", action="store_true",
                    help="derive the query from live git state (changed files + recent commits)")
    ap.add_argument("--context", type=str, default=None,
                    help="real working context dir (e.g. projects/ai-consultant): derive query from recently touched files there (1.2 signal fix, beats --auto rear-view)")
    args = ap.parse_args()
    query = " ".join(args.query)
    if args.context:
        ctx = _context_query(args.context)
        query = (query + " " + ctx).strip() if query else ctx
        if not query:
            print("[experience_push] --context: empty (no recent files in %s)" % args.context)
            return 0
    elif args.auto:
        auto = auto_query()
        query = (query + " " + auto).strip() if query else auto
        if not query:
            print("[experience_push] --auto: no git signal (clean tree, no recent commits)")
            return 0
    qtokens = tokenize(query)
    if not qtokens:
        print("[experience_push] empty query after tokenization")
        return 1

    results = []
    for kind, path in collect_files():
        try:
            with io.open(path, "r", encoding="utf-8", errors="replace") as f:
                raw = f.read()
        except OSError:
            continue
        score, matched, fm = score_file(qtokens, raw)
        if score > 0:
            title = fm.get("title", "") or os.path.basename(path)
            results.append((score, kind, path, title, matched, extract_action(raw)))

    for path, weight, header, text in collect_ledger_chunks():
        ctokens = tokenize(header + " " + text)
        hits = qtokens & ctokens
        if hits:
            score = weight * len(hits)
            kind = "proven" if weight >= PROVEN_LEDGER_WEIGHT else "ledger"
            title = header if header else kind
            results.append((score, kind, path, title, hits, text[:160]))

    # R2：按 (path, title) 去重保留最高分（修复 ledger 同 Entry 多 bullet 重复候选）
    seen = {}
    for r in results:
        key = (disp_path(r[2]), r[3])
        if key not in seen or r[0] > seen[key][0]:
            seen[key] = r
    results = list(seen.values())

    results.sort(key=lambda r: -r[0])
    top = [r for r in results if r[0] >= args.min][: args.n]
    if not top:
        print("[experience_push] no relevant past experience found for: %s" % query)
        print("[experience_push] 无相关经验值得记录（空结果即信号：本身是 Observation 候选；"
              "有真实踩坑/信念改变才沉淀，不硬写）")
        return 0

    print("[experience_push] 命中 %d 条相关经验（请采纳）：" % len(top))
    print("    以下经验与当前任务相关，内容摘要已列在下方——请在实现前阅读并采纳；")
    print("    需要全文时打开 file 路径（read-only，不注入上下文）。\n")
    for score, kind, path, title, matched, action in top:
        rel = disp_path(path)
        print("- [%.1f][%s] %s" % (score, kind, title))
        print("    file : %s" % rel)
        if kind in ("proven", "ledger"):
            # R2：账本候选的"内容" = chunk 文本本身（不再是文件头样板）
            if action:
                print("    内容 : %s" % action)
        else:
            if action:
                print("    do   : %s" % action)
            preview = preview_text(path, action)
            if preview:
                print("    内容 : %s" % preview)
        print("    hit  : %s" % ", ".join(sorted(matched)[:8]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
