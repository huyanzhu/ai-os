---
name: cot_leakage_trim
type: Assembled / Conditional（工作模式整包单位 · 可激活）
source: 外部 Skill dsh-trim-cot-leakage（deepseek-ai/deepseek-harness · Human 提供）；原文见 evolution/intake/dsh-trim-cot-leakage/SKILL.md
trigger:
  - 审计/修复读起来像泄漏的推理转录的散文（死设计会话引用 (decision N) / 审计码 (audit C2) /
    未提交草稿的 §N / 变更叙述 used to no longer this cut / 栈与 PR 视角 a later PR in this stack /
    评审编排 rejected in review v5 of this note / 评审者定向辩护 / 控制流叙述 / 对冲与计划残留 /
    工作语言碎片）
  - "trim the chain-of-thought" / "this reads like a reasoning transcript" / 清理会话视角残留
  - 在评论、JSDoc、文档、Agent Notes 中移除作者会话视角、保留仓库视角
  - 判定某段"是不是泄漏"、某条引用"该保留还是删除"
activation: 开工 bootstrap 能力检索（task_start.py 查 capabilities/INDEX.md）命中本 trigger →
  读本文件全文 → 把"会话推理转录猎杀"完整流程装载为当前任务工作模式：确认显式 scope 与排除 →
  逐段跑 HEAD 视角测试 → 按八类泄漏分类并修复 → 应用保留规则 → 先改拥有者再派生物 → 删除前枚举
  命题并检查过纠正陷阱 → 重跑探针与触碰表面门禁；按最后"检查清单"自测后汇报
status: Assembled + Delivered（可激活）；真实会话视角泄漏猎杀消费 Q1–Q5 UNKNOWN
  （无自然任务触发，显式不宣称已帮助）
decision_ref: D-030 / D-039
knowledge_ref:
  - domains/ai-os/patterns/cot_leakage_trim.md（方法层知识 · Searchable ·
    边界论证 / 不携带清单 / 与既有知识互补关系 / 边界案例沉淀区）
  - evolution/intake/dsh-trim-cot-leakage/SKILL.md（原文 · 若真实项目即 deepseek-harness
    类仓库直接装载原文）
---

# 会话推理转录猎杀 — 完整工作模式（Trimming Chain-of-Thought Leakage · Assembled / Conditional）

> 本文件 = **可激活的完整工作模式单位**（剔除死引用后的整包，不是方法层摘录）。
> 装载条件与激活方式见 frontmatter `trigger` / `activation`；命中后按下面完整流程执行。
> 方法层知识（可检索、含边界论证与不携带清单）保留在
> `domains/ai-os/patterns/cot_leakage_trim.md`（Reference）——本文件与它互为同一对象的不同
> 承载（D-034：Physical placement 是承载，不是语义身份）。
> 原文：deepseek-ai/deepseek-harness `.agents/skills/dsh-trim-cot-leakage/SKILL.md`
> 。**剔除**：deepseek-harness 专属路径/文件/命令
> （死引用）；**保留**：完整审计修复流程（剔除 ≠ 拆解）。

---

name: cot_leakage_trim
description: Use when auditing or fixing prose that reads like a leaked reasoning transcript — dead design-session citations such as (decision N), audit item codes, or §N of uncommitted drafts; change narration such as "used to", "no longer", "this cut"; stack or review vantage ("a later PR in this stack", "rejected in review"); reviewer-addressed justifications; control-flow narration; or hedged planning residue in comments, JSDoc, docs, or Agent Notes.
tools: ["Read", "Grep", "Glob", "Bash", "Git"]

【V2 注】tools 映射：Read/Grep/Glob/Bash/Git = carrier 工具层文件 I/O、搜索与 git 执行。

## When to load this working mode

Chain-of-thought leakage is prose whose vantage is the authoring session rather than the repository:
it cites artifacts only that session could see, narrates the change instead of the state, or argues
with a reviewer who has left. The fix is never deletion alone when a passage carries factual clauses —
restate each so it stands at HEAD, then delete the transcript around it; a passage carrying none (an
audit code, control-flow narration) is deleted outright. **REQUIRED BACKGROUND:** `prose_standard`
(D-028) owns the complete-proposition rule this skill applies; the committed-artifact-citations
principle（一个解释一个家 + 承重记录引用规则）owns the citation rule's rationale. It is guidance,
not a script.

【V2 注】原文 `dsh-prose-standard` 子 skill 引用已映射到 V2 独立收编的 `prose_standard`（D-028，
capabilities/prose_standard.md + domains pattern）；原文 committed-artifact-citations 注记是
deepseek-harness 专属文件（死引用已剔除）——引用规则理由由 V2 既有纪律承接（一个解释一个家 +
task card / pattern / SUCCESS_LOG 承重记录引用规则）。

## The one test

For every suspect passage ask: **could a reader at HEAD, with no access to any session transcript,
PR thread, or uncommitted draft, resolve every reference and verify every claim?** If no, restate the
surviving facts from the repository's vantage and delete the rest. If yes, it is not leakage, however
historical it sounds — but resolvability only clears this skill's bar: on current-state surfaces
(READMEs, docs, JSDoc) a resolvable change story is still change narration, and class 3 routes it to
its sanctioned home.

## Taxonomy

1. **Dead design-session citations** — `(decision 7)`, `(audit C2)`, `design §4.7`, `plan §1.4`,
   phase labels (`T4`, `W3`, `P-I`), "the design ledger", "(B ruling)". If the decision has a
   committed owner, cite it by name and path; otherwise delete the citation and restate its factual
   clause to stand alone.
2. **Stack and PR vantage** — "a later PR in this stack", "this PR adds", "the previous commit".
   State the shipped mechanism or the extension point; deferred work moves to a `TODO` marker or an
   issue reference.
3. **Change narration and version stamps** — "used to", "no longer", "the old X", and indexical
   stamps ("v1", "this cut", "today", "now" contrasting with a past state). State the present
   behavior; a fixed regression becomes a present-tense counterfactual ("without X, Y happens"),
   never repo history ("used to Y").
4. **Review choreography** — "Rejected in review:", "the reviewer confirmed", draft ordinals ("v5 of
   this note"), round attributions. Keep the surviving decision and rationale as plain fact; delete
   who said it when.
5. **Reviewer-addressed justification** — "the cast is safe — it simply…", "this is correct
   because…". A comment arguing its own correctness addresses a reviewer, not a maintainer. State the
   invariant that makes the code safe, or delete the comment if the code shows it.
6. **Restatement and derivation transcripts** — control-flow narration ("first we X, then we Y"),
   test walkthroughs, proofs of obvious branches. Delete; keep only a non-obvious contract or
   invariant.
7. **Hedges and planning residue** — "probably fine for now", "should be enough", deferrals with no
   marker. Promote to `TODO`/`FIXME` or restate as the actual bound; delete the hedge.
8. **Authoring-language slips** — untranslated working-language fragments (端, 设计稿,
   `---- 私有 ----` separators) in prose whose language is otherwise English, or the reverse in a zh
   counterpart. Translate or delete.

## What is not leakage

Unaided citation passes fail in both directions by deleting durable references and keeping dead ones.
Apply these keep rules as written; the distilled examples in
`domains/ai-os/patterns/cot_leakage_trim.md` calibrate each:

【V2 注】原文 `references/examples.md` 是 repo 专属文件（死引用已剔除）——V2 边界案例沉淀在
`domains/ai-os/patterns/cot_leakage_trim.md`。

- **Issue references** — `#1470`, `TODO(name):`, "issue #N owns the follow-up" resolve at HEAD; keep
  them on any surface, including READMEs. Do not relocate them to Agent Notes.
- **Merged-PR and issue citations inside Agent Notes and postmortems** — sanctioned evidence per the
  documentation standard's change-story routing.
  【V2 注】原文 `docs/AGENTS.md` 标准之家是 repo 专属（死引用已剔除）——V2 用适用 AGENTS.md 的
  change-story 路由（task card / pattern / SUCCESS_LOG 承重记录同规则）。
- **Suppression justifications** — `oxlint-disable … -- reason`, coverage-ignore reasons, empty-catch
  explanations are required prose; fix a false reason, never delete it.
  【V2 注】`oxlint-disable` 是具体工具（死引用已剔除）——抑制理由原则保留：修正虚假理由，绝不删除。
- **Counterfactual-present regression pins** — "without X, Y happens", "a naive X would…".
- **Measured bounds** — "(measured: 512 nests ≈ 0.15s)" calibrating a constant; the provenance word
  "measured" is load-bearing.
- **Runtime old/new states** — "the old connection drains before the new one accepts" is runtime
  lifecycle, not change history.
- **Historical stage names inside a note's change-story sections** — "the first cut shipped X" is
  current-state-safe there; indexical stamps ("this cut") stay banned everywhere.
- **External references that resolve outside the repo by design** — standards sections (RFC 9110
  §10.1.5), Figma frame names; the §-ban covers uncommitted internal drafts, not external standards
  or committed docs that own their §-numbering.
- **Project voice and genre forms** — "we" as project voice; a note's Alternatives-considered section.

## Workflow

1. Scope and exclusions per `prose_standard` (D-028): require an explicit scope; never touch
   third-party dependency directories, frozen archived snapshots, or recorded fixtures and snapshots —
   recorded model output and sealed history keep their original voice.
   【V2 注】原文 `vendor/` 与 `.agents/notes/archived/` 具体路径是 deepseek-harness 专属（死引用
   已剔除）——V2 对应：仓库实际第三方依赖目录、`task_cards/archive` 等 archived 目录（冻结归档，
   只读）。
2. Audit read-only first: run the recall probes covering hidden surfaces (with hidden-mode search so
   task cards and notes are searched), then judge every hit semantically. The probes are probes, not
   the definition — each review round of the original purge found cases the probes missed, so also
   read the densest prose in scope (module JSDoc, READMEs, Agent Notes) without a pattern in hand.
   【V2 注】原文 `references/recall-batteries.md` 与 `--hidden` 遍历 `.agents/` 约定是 repo 专属
   （死引用已剔除）——V2 等价：rg/Select-String 覆盖隐藏面（任务卡/笔记等）。
3. Fix owner-first per surface: generated catalogs → fix the source JSDoc or generator template, then
   regenerate; type-equivalence fences → fix the source JSDoc, then re-paste both bilingual pages;
   bilingual pairs → update the counterpart and re-record per `bilingual_doc_pairing` (D-029);
   model-visible strings → wording is behavior, so flag for a snapshot-backed change instead of
   silently rewording.
   【V2 注】原文 `verify-type-equiv` 钉住与 `dsh-translate-docs` 子 skill 引用是 repo 专属（死引用
   已剔除）——V2 原则保留：先改源再派生物；双语配对工作流指向 `bilingual_doc_pairing`（D-029）。
4. Before deleting anything, enumerate the passage's propositions (prose-standard) and check the
   overcorrection traps: trims that flip an obligation into an endorsement, promote a hypothetical to
   a shipped feature, delete a true fact, or drop provenance.
   【V2 注】过纠正陷阱校准示例在 `domains/ai-os/patterns/cot_leakage_trim.md`。
5. Verify: re-run the probes expecting only sanctioned keeps, this skill's own directory, and the
   owning note's quoted evidence; confirm every remaining citation resolves at HEAD; run the gates for
   touched surfaces (doc-sync for docs, type-equivalence verification, translation-pairing
   verification).
   【V2 注】`doc-sync` / `verify-type-equiv` / `verify-translation-pairing` 是 repo 专属门禁命令
   （死引用已剔除）——V2 用触碰表面的既有验证入口（无对应物时手工核验并如实汇报）。

## 检查清单（会话推理转录猎杀中自测）

- [ ] 对每个可疑段落跑了 HEAD 视角测试（无会话转录/PR 线程/未提交草稿的读者能否解析每个引用、
      核验每个声明）？
- [ ] 泄漏按八类分类了吗（死设计引用/栈 PR 视角/变更叙述与版本戳/评审编排/评审者辩护/复述转录/
      对冲计划残留/语言碎片），每类按对应规则修复？
- [ ] 删除前重述了每个事实子句（先重述存活事实，再删转录；不带事实子句的才直接删）？
- [ ] 保留规则应用了吗（issue 引用/承重记录证据/抑制理由/反事实钉/测量出处/运行时新旧/变更故事
      阶段名/外部标准引用/项目声音）？
- [ ] 检查了过纠正陷阱（义务→背书、假说→已交付、删真事实、丢出处）？
- [ ] 先改拥有者再改派生物（生成物先改源再重新生成；模型可见字符串标记快照支撑变更而非静默改写）？
- [ ] 验证过了吗（重跑探针只剩受认可的保留；剩余引用在 HEAD 可解析；跑过触碰表面的既有门禁并
      如实汇报）？

---

## Reference（知识侧 · 多关系）

- **方法层知识（Searchable）**：`domains/ai-os/patterns/cot_leakage_trim.md` ——
  可迁移方法层、触发/条件/动作 frontmatter、**不携带清单**（repo 专属死引用全列）、与
  `prose_standard` / `doc_standards` / `bilingual_doc_pairing` / senior-engineer Review 面 /
  knowledge-space-maintenance 的互补边界、边界案例沉淀区。需要边界论证或检索命中时回读本
  pattern。
- **原文（Source preservation）**：`evolution/intake/dsh-trim-cot-leakage/SKILL.md` ——
  若未来真实项目就是 deepseek-harness 类仓库，直接装载原文（含全部 repo 专属约定）。
- **触发关系**：本单位 = 完整工作模式（Assembled / Conditional）；命中 trigger 装载执行完整
  流程；知识检索（experience_push）命中的是 domains pattern（Reference），二者互补不重复。
