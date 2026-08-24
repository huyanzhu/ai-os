---
name: doc_standards
type: Assembled / Conditional（工作模式整包单位 · 可激活）
source: 外部 Skill dsh-doc-standards（deepseek-ai/deepseek-harness · Human 提供）；原文见 evolution/intake/dsh-doc-standards/SKILL.md
trigger:
  - 写 / 移动 / 评审 / 审计仓库文档（README / 导航 / 报告 / 项目文档）
  - 决定一篇文档放哪个层级 / 写成教程还是参考 / 写多长
  - 文档太长 / 重复 / 含会话视角残留（reasoning transcript leakage）
  - "improve the docs" / "audit the docs" / "where should this be documented" /
    "this doc is too long" 类指令
  - 文档预算 / 长度 / 语料审计类失败信号（verify-doc-budgets 类；V2 用词数探针等价）
activation: 开工 bootstrap 能力检索（task_start.py 查 capabilities/INDEX.md）命中本 trigger →
  读本文件全文 → 把"文档放置与预算标准"完整流程装载为当前任务工作模式：结构先行 → 用途分类
  （教程 vs 参考）→ 教程前置条件 → 拆分混合形式 → 放置约束 → 语料审计廉价探针 → 预算
  relocate-condense-raise → 验证汇报；按最后"检查清单"自测后汇报
status: Assembled + Delivered（可激活）；真实文档消费 Q1–Q5 UNKNOWN
  （无自然"文档编写/移动/审计"任务触发，显式不宣称已帮助）
decision_ref: D-024 / D-041
knowledge_ref:
  - domains/ai-os/patterns/doc_standards.md（方法层知识 · Searchable ·
    边界论证 / 不携带清单 / 与既有知识互补关系 / 边界案例沉淀区）
  - evolution/intake/dsh-doc-standards/SKILL.md（原文 · 若真实项目即 deepseek-harness
    类仓库直接装载原文）
---

# 文档放置与预算标准 — 完整工作模式（Documentation Standards · Assembled / Conditional）

> 本文件 = **可激活的完整工作模式单位**（剔除死引用后的整包，不是方法层摘录）。
> 装载条件与激活方式见 frontmatter `trigger` / `activation`；命中后按下面完整流程执行。
> 方法层知识（可检索、含边界论证与不携带清单）保留在
> `domains/ai-os/patterns/doc_standards.md`（Reference）——本文件与它互为同一对象的不同
> 承载（D-034：Physical placement 是承载，不是语义身份）。
> 原文：deepseek-ai/deepseek-harness `.agents/skills/dsh-doc-standards/SKILL.md`
> 。**剔除**：deepseek-harness 专属路径/文件/命令
> （死引用）；**保留**：完整文档标准工作流（剔除 ≠ 拆解）。

---

name: doc_standards
description: Use when writing, moving, reviewing, or auditing documentation in a repository — choosing hierarchy and detail, separating tutorials from references, checking tutorial progression, trimming doc slop, responding to a documentation-budget failure, or requests like "improve the docs", "audit the docs", "where should this be documented", or "this doc is too long".
tools: ["Read", "Grep", "Glob", "Bash", "Git"]

【V2 注】tools 映射：Read/Grep/Glob/Bash/Git = carrier 工具层文件 I/O、搜索与 git 执行。

## When to load this working mode

The documentation rules live in the applicable `AGENTS.md`. This workflow covers placement,
corpus audits, budgets, and validation across Markdown, JSDoc, and code comments. It is
guidance, not a script; use `prose_standard` for required coverage and editorial judgment,
and never treat length alone as a defect.

【V2 注】原文 `docs/AGENTS.md` 与 `dsh-prose-standard` 子 skill 引用是 repo 专属（死引用已
剔除）——V2 对应：适用 AGENTS.md（项目/文档拥有契约；AI-OS = `D:\AI-os\AGENTS.md` 宪法写作
规则）+ `prose_standard`（D-028 方法层 + D-037 物化，domains/ai-os/patterns/
prose_standard.md + capabilities/prose_standard.md）。

## Sources of truth (read, don't re-summarize)

- Applicable `AGENTS.md` — hierarchy, tutorial/reference forms, taxonomy, budgets, and slop
  checklist.
  【V2 注】原文 `docs/AGENTS.md` 是 repo 专属（死引用已剔除）——V2 对应：适用 AGENTS.md
  （项目/文档拥有契约）+ 本对象方法层 pattern（`doc_standards`）。
- `knowledge-space-maintenance` — when a decision earns a record entry, how to file it, and
  what goes inside one (the header block, per-lifecycle skeleton, and Alternatives-considered
  mandate); when an incident earns a postmortem-style record.
  【V2 注】原文 `.agents/notes/README.md`、`docs/postmortem/README.md` 与
  verify-agent-note-format 门禁是 repo 专属（死引用已剔除）——V2 对应：记录归档/生命周期由
  knowledge-space-maintenance（D-022 Lifecycle/Archive facet，maintenance-skills/
  knowledge-maintenance/SKILL.md）承接；事故复盘 = task card / decisions 记录，无独立
  postmortem 基建。
- `bilingual_doc_pairing` — the bilingual pairing rules; editing either side of a pair
  obligates the counterpart in the same change.
  【V2 注】原文 `docs/i18n/README.md` 是 repo 专属（死引用已剔除）——V2 对应：
  `bilingual_doc_pairing`（D-029，domains/ai-os/patterns/bilingual_doc_pairing.md）。
- Root `AGENTS.md` — the standing orders whose budget discipline this skill protects.
  【V2 注】原文根 `AGENTS.md` 是 repo 专属（死引用已剔除）——V2 对应：`D:\AI-os\AGENTS.md`
  （宪法：写作/存储纪律等 standing orders）。
- Frozen archives — historical snapshots excluded from editorial maintenance and evolving
  documentation gates.
  【V2 注】原文 Archived Agent Notes（`.agents/notes/archived/`）是 repo 专属（死引用已
  剔除）——V2 对应：冻结归档快照（archived task cards / 冻结语料），排除在语料审计与编辑之外。

## Review structure before prose

Apply the standard's authoring order to every human-facing document in scope. Do not apply
this structural pass to working-memory records (V2：task card / 决策记录等承重记录)。Classify
a postmortem-style record as a reference scoped to one incident; preserve its required
chronological evidence without treating chronology as a teaching sequence.

1. Locate the document in the repository and navigation trees. State its own subject and
   identify its direct children.
2. Set the permitted level of detail. Keep full detail about the document's subject,
   summarize direct children by purpose, responsibility, and high-level behavior, and move
   deeper explanations to their owning descendants with links. Treat test infrastructure as
   descendant-owned unless it is the document's subject.
3. Classify the document from its intended use, not its path or title. A tutorial must lead
   through ordered work to an observable outcome; a reference must support lookup within an
   explicit scope without requiring sequential reading.
4. For a tutorial, privately classify the starting reader and concepts as beginner,
   intermediate, or advanced. Trace each concept to its prerequisites, reorder premature
   material, and move optional advanced detail to a later tutorial or reference.
5. Split substantial mixed forms. Put a small secondary form in a clearly labeled section.

Then check constraints that make placement expensive or wrong:

- Paired docs cost a counterpart update on every edit — prefer an unpaired home for content
  that will churn.
  【V2 注】原文 `pnpm run verify-translation-pairing --list` 是 repo 专属命令（死引用已
  剔除）——V2 对应：`bilingual_doc_pairing` 配对纪律（改一侧欠另一侧）；V2 无配对验证器，
  手工核验对应面并如实汇报。
- Generated catalogs are never hand-edited; if the fact belongs there, change the generator's
  source.
- Before renaming or moving any doc, grep for inbound references: link targets AND `#fragment`
  anchors onto Markdown files (heading slugs and explicit `<a id>`), plus citations from
  code comments and strings.
  【V2 注】原文 verify-md-links / verify-doc-refs 是 repo 专属门禁（死引用已剔除）——V2
  对应：移动/重命名前用搜索工具（Grep/Glob）查入站链接 + 锚点引用（含代码/字符串里的引用），
  机制保留、实现用项目既有工具。
- A move is atomic: remove from the old home, add to the new home, and fix every inbound link
  in the same change.

## Audit the corpus

After the structural pass, hunt the standard's slop checklist with the cheapest probes first.
Verify and state the actual change scope before applying semantic judgment; after a retarget
or base merge, rerun the report and audit prose introduced by the new base.

【V2 注】原文 `pnpm --silent run change-scope --base <verified-base-ref>` 与 PR live base
核验是 repo 专属（死引用已剔除）——V2 对应：git status / git diff 核对实际改动路径后再做
语义判断；无远端/CI 时不做 PR 基态核对，如实说明。

1. Measure: `git ls-files '*.md' ':(exclude)vendor/**' | xargs wc -w | sort -rn | head -30`
   to spot unbudgeted outliers.
   【V2 注】原文 `pnpm run verify-doc-budgets --list` + 该 wc 流水线是 repo 专属（死引用已
   剔除）——V2 对应：用项目既有搜索/词数工具扫范围内 Markdown（排除冻结归档），找未预算的
   越界 outlier；无 verify-doc-budgets 门禁时说明"无此门禁，用词数探针等价"。
2. Hunt reasoning-transcript leakage — narrated history, dead design-session citations,
   review choreography, control-flow narration, test walkthroughs — with `cot_leakage_trim`,
   which defines the taxonomy, recall batteries, and rules for what to keep or delete.
   Preserve only a non-obvious contract or durable rationale; the same rationale repeated
   beside sibling methods keeps one home.
   【V2 注】原文 `dsh-trim-cot-leakage` 子 skill 引用已独立收编为 `cot_leakage_trim`
   （D-030 方法层 + D-039 物化，capabilities/cot_leakage_trim.md + domains pattern）——
   命中泄漏猎杀时装载该单位执行完整分类与修复流程。
3. Hunt duplication by grepping distinctive phrases. Keep one home and replace other copies
   with links.
4. Replace hand-written catalogs, test/status inventories, and JSDoc restatements with the
   authoritative tree, script, or generated reference.
5. In implemented records (V2：归档 task card / pattern / SUCCESS_LOG 承重记录), remove
   migration plans, acceptance-task checklists, and future-tense spec language. Keep concise
   verification contracts that identify the behaviors and tiers pinning the shipped decision,
   plus named coverage gaps.
6. If removing prose changes a promised behavior rather than its explanation, use a proposed
   record first (V2：proposed task card / 决策草案，判据见 `simplification_audit`).
   【V2 注】原文 `dsh-find-simplifications` 子 skill 引用已独立收编为 `simplification_audit`
   （D-025，domains/ai-os/patterns/simplification_audit.md）——记录收编判据由 Lifecycle
   facet（D-022）承接，本 skill 仅补充。

Exclude frozen archives from corpus audits and edits. Active prose may repair, redirect, or
delete an inbound link, but never follow an archive-wide cleanup into the frozen target.

## Keep every load-bearing rule

Keep every load-bearing rule, preferably as one to three lines plus a link to its rationale.
Cut stories, duplicates, status notes, and the path used to derive the rule. Do not create a
new explanation merely to relocate disposable reasoning.

## When documentation-budget checks go red

Apply the ordered relocate → condense → raise policy: move the content to its more appropriate
owner, condense it, or raise the budget and explain why. This working mode only supplies the
workflow probes above.

【V2 注】原文 `docs/AGENTS.md` 的 relocate-condense-raise 政策是 repo 专属（死引用已剔除）——
V2 对应：预算纪律见 `doc_standards` pattern 与适用 AGENTS.md；V2 无 pnpm verify-doc-budgets
门禁，超长信号用词数探针 + 人工裁决，提预算必须说明理由。

## Validation and reporting hygiene

Run at least the cheapest existing checks: the project's doc-sync/consistency check if one
exists, lint if present, and `git diff --check`. JSDoc/code changes may regenerate derived
catalogs — regenerate from source, never hand-edit. If a paired doc changed, follow the
lightweight routine in `bilingual_doc_pairing` (V2 无配对验证器：手工核对对应面并如实汇报).
The report should give word deltas, explain any deliberately long exception, and list checks
actually run.

【V2 注】原文 `pnpm run doc-sync` / `pnpm run lint` / `pnpm run verify-translation-pairing
--write <pair>` 是 repo 专属命令（死引用已剔除）——V2 对应：项目实际的同步/lint 门禁
（机制 = 提交前跑既有检查 + `git diff --check`；`git diff --check` 通用保留）；V2 无对应
命令时明确列出实际跑过的检查，不声称没跑过的门禁。

## 检查清单（文档工作中自测）

- [ ] 写之前定位了吗：主题 + 直接子文档 + 允许的细节层级？
- [ ] 是按用途（教程/参考）分类的，不是按路径/标题？
- [ ] 教程的前置条件 / 起始读者判定过了吗；过早材料移走了吗？
- [ ] 移动/重命名时入站链接在同一改动里修完了吗？
- [ ] 手编过生成目录/清单吗（应该改源/生成器）？
- [ ] 保留的是承重规则（1-3 行 + 链接），删掉的是故事/重复/状态注记/推导？
- [ ] 删措辞没有改变承诺行为吗（改变则先走 proposed 记录）？
- [ ] 汇报里列了实际跑过的检查与词数增量吗？

---

## Reference（知识侧 · 多关系）

- **方法层知识（Searchable）**：`domains/ai-os/patterns/doc_standards.md` ——
  可迁移方法层、触发/条件/动作 frontmatter、**不携带清单**（repo 专属死引用全列）、与
  `doc_site_projection` / `prose_standard` / `cot_leakage_trim` / `bilingual_doc_pairing` /
  `simplification_audit` / `knowledge-space-maintenance` / `doc-generation` 的互补边界、
  边界案例沉淀区。需要边界论证或检索命中时回读本 pattern。
- **原文（Source preservation）**：`evolution/intake/dsh-doc-standards/SKILL.md` ——
  若未来真实项目就是 deepseek-harness 类仓库，直接装载原文（含全部 repo 专属约定）。
- **触发关系**：本单位 = 完整工作模式（Assembled / Conditional）；命中 trigger 装载执行
  完整流程；知识检索（experience_push）命中的是 domains pattern（Reference），二者互补
  不重复。
- **协同单位**：`prose_standard`（编辑判断 / 完整命题）、`cot_leakage_trim`（会话视角泄漏
  猎杀）、`bilingual_doc_pairing`（配对同步）、`doc_site_projection`（发布投影）、
  `simplification_audit`（简化提案判据）——doc 族分工链（发现 → 编辑判断 → 配对同步 →
  泄漏修复 → 发布投影）。
