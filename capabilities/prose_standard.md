---
name: prose_standard
type: Assembled / Conditional（工作模式整包单位 · 可激活）
source: 外部 Skill dsh-prose-standard（deepseek-ai/deepseek-harness · Human 提供）；原文见 evolution/intake/dsh-prose-standard/SKILL.md
trigger:
  - 写 / 评审 / 恢复 / 精简 / 审计散文与注释（Markdown、JSDoc、代码与测试注释、提示词、描述、诊断、CLI/UI 字符串）
  - 决定某处该不该有注释 / 某段该保留、删除、恢复还是重构
  - "trim the prose" / "this comment is unnecessary" / "restore this doc" / "audit the prose" 类指令
  - 编辑提示词、可见字符串、诊断文本（措辞即行为）
activation: 开工 bootstrap 能力检索（task_start.py 查 capabilities/INDEX.md）命中本 trigger →
  读本文件全文 → 把"散文与注释编辑标准"完整流程装载为当前任务工作模式：先确认显式 scope 与
  mode → 排除第三方依赖与冻结归档、派生物先改源 → 编辑前识别并保留完整命题 → 按 12 类位置覆盖
  必需契约 → 词检查 → 七步工作流 → 边界决策；按最后"检查清单"自测后汇报
status: Assembled + Delivered（可激活）；真实散文编辑消费 Q1–Q5 UNKNOWN
  （无自然编辑任务触发，显式不宣称已帮助）
decision_ref: D-028 / D-037
knowledge_ref:
  - domains/ai-os/patterns/prose_standard.md（方法层知识 · Searchable ·
    边界论证 / 不携带清单 / 与既有知识互补关系 / 边界案例沉淀区）
  - evolution/intake/dsh-prose-standard/SKILL.md（原文 · 若真实项目即 deepseek-harness
    类仓库直接装载原文）
---

# 散文与注释编辑标准 — 完整工作模式（Prose Standard · Assembled / Conditional）

> 本文件 = **可激活的完整工作模式单位**（剔除死引用后的整包，不是方法层摘录）。
> 装载条件与激活方式见 frontmatter `trigger` / `activation`；命中后按下面完整流程执行。
> 方法层知识（可检索、含边界论证与不携带清单）保留在
> `domains/ai-os/patterns/prose_standard.md`（Reference）——本文件与它互为同一对象的不同
> 承载（D-034：Physical placement 是承载，不是语义身份）。
> 原文：deepseek-ai/deepseek-harness `.agents/skills/dsh-prose-standard/SKILL.md`
> 。**剔除**：deepseek-harness 专属路径/表单/命令
> （死引用）；**保留**：编辑标准与完整流程（剔除 ≠ 拆解）。

---

name: prose_standard
description: Use when writing, reviewing, restoring, trimming, or auditing prose in a repository or document set, including deciding where documentation or comments are required across Markdown, JSDoc, code and test comments, prompts, descriptions, diagnostics, and CLI or UI strings.
tools: ["Read", "Grep", "Glob", "Bash", "Git"]

【V2 注】tools 映射：Read/Grep/Glob/Bash/Git = carrier 工具层文件 I/O、搜索与 git 执行。

## When to load this working mode

Write enough to preserve the contract, then remove reasoning transcripts, repetition, and
decoration. A contract is an obligation, invariant, precondition, postcondition, or compatibility
promise that a caller, callee, implementer, producer, or consumer relies on. This working mode
owns editorial judgment and required prose coverage; use `doc_standards` for placement, budgets,
bilingual pairs, and documentation gates, and `cot_leakage_trim` for hunting and fixing
reasoning-transcript leakage. It is guidance, not a script.

【V2 注】原文 `dsh-doc-standards` / `dsh-trim-cot-leakage` 子 skill 引用已映射到 V2 独立收编的
`doc_standards`（D-024）/ `cot_leakage_trim`（D-030）pattern——工作关系不变，引用去 repo 化。

Treat `contract`, `boundary`, `shape`, `surface`, `seam`, `gate`, and `vocabulary` as terms to
check before use, not banned words. First ask whether the exact rule, API, field set, type,
validation, timing point, component split, or failure states the fact better. Keep a term when it
names the exact technical subject, including caller/callee contracts and security/process
boundaries.

Comments describe non-obvious contracts or rationale that code cannot express; they do not
restate what code already implies.

## Inputs and exclusions

Require an explicit `scope`. If it is missing, report the required input and stop; do not infer a
repository-wide scope or begin an interview.

Accept `mode: automatic | interactive`; default to `automatic`. Enter interactive mode only when
the user explicitly requests questions or calibration.

`mode` controls questions, not write authority. Review and audit tasks report findings without
editing; explicitly requested write, fix, or trim tasks apply clear changes.

Always exclude third-party dependency directories from discovery, review, and edits, even when
the requested scope is the whole repository. Do not follow a symlink into them. Put exclusions
after inclusion globs so a later include cannot re-admit them: for example, end ripgrep commands
with `--glob '!<depdir>/**'`, and give Git commands an explicit `:(exclude)<depdir>/**` pathspec.
If the requested scope contains only such directories, report that no eligible files remain.

【V2 注】原文 `vendor/` 具体路径约定是 deepseek-harness 专属（死引用已剔除）——原则保留：排除
规则放包含 glob 之后，避免重新纳入；V2 用仓库实际的第三方依赖目录名。

Also exclude frozen archived snapshots from prose review and edits. Archived snapshots are frozen;
inspect an exact target only to understand a historical inbound citation, never to modernize its
prose or outbound links.

【V2 注】原文 `.agents/notes/archived/` 树是 deepseek-harness 专属（死引用已剔除）——V2 对应：
`task_cards/archive` 等 archived 目录（冻结归档，只读）。

Treat generated catalogs, snapshots, and fixtures as derivative. Edit the owning source or
scenario first, then regenerate the artifact. When a generator extracts a summary from owner
prose, make the extracted sentence complete for that surface. Bilingual pairs have no permanent
owner: either language may be the authored side for an update. Follow the applicable `AGENTS.md`
writing rules, update the counterpart minimally, and re-record the pair.

【V2 注】原文 `docs/AGENTS.md#writing-rules` 轻量路径链是 repo 专属（死引用已剔除）——V2 用
适用 AGENTS.md 的 Writing 规则。

## Preserve the complete proposition

Before editing, identify every proposition in the passage. Preserve each relevant:

- actor and action;
- condition, timing, and ordering;
- modality such as must, may, or never;
- negative guarantee and exception;
- ownership, side effect, failure mode, and consequence.

Remove adjectives, repetition, and narration only when every factual clause survives and the
result is clearer. A smaller word count alone is not an improvement.

Keep a complete local contract at the point of use: behavior, failure, ownership, and consequence
that a caller or maintainer needs there. Aggressively link to the owning document for
architecture, rationale, algorithms, history, or extended examples. One explanation has one home;
essential contract facts may repeat locally.

Keep non-obvious rationale when omitting it could plausibly cause misuse or an incorrect
simplification. Otherwise state the consequence and link the rationale home.

## Required coverage by prose location

This is not a one-way shortening pass. Add or restore prose when code, types, and structure do not
communicate a required contract below. Do not add a comment when those facts are already obvious
locally.

- **Public JSDoc:** document caller-visible return distinctions, throws or rejections, side
  effects, ownership, timing, cancellation, and durability.
- **Internal comments:** orient non-local structure and obviously complicated local structure,
  including invariants, race ordering, ownership, security boundaries, and surprising failure
  behavior. Delete control-flow narration and code restatement.
- **Module comments:** state the module's role, dependencies, responsibilities, and non-obvious
  architecture choices; link architecture choices to their owning explanation.
- **Tests:** explain only non-obvious test design—why a fixture, assertion, platform
  accommodation, real entry path, or indirect observation is necessary. Delete walkthroughs and
  inventories.
- **Cookbooks:** include prerequisites, required actions, the real entry path, observable
  verification, and concise warnings.
- **READMEs:** include the consumer contract: configuration, semantics, failures, limitations,
  extension points, and model-visible effects. Quote stable model-visible text owned by the
  package; link generated catalogs and cross-package owners. Keep durable gaps and maintainer
  traps, not ordinary cleanup inventories. Follow the project's package-README requirements.
  【V2 注】原文 `cookbook/adding-a-package.md` 表单是 repo 专属（死引用已剔除）——V2 无仓库
  表单，按 README 消费方契约覆盖要求执行（prose_standard pattern 的 12 类覆盖节）。
- **Agent Notes:** retain unique rationale, mechanisms, alternatives, consequences, shipped
  verification evidence, and named coverage gaps. Implemented Agent Notes state shipped reality
  in the present tense; remove planning checklists, not evidence of what pins the decision.
  【V2 注】V2 对应承重记录：task card / pattern / SUCCESS_LOG——同规则。
- **Postmortems:** retain the incident sequence, evidence, causal chain, impact, and prevention.
  Remove repeated persuasion or implementation detail that does not establish causality.
- **Skills and agent instructions:** state behavioral guardrails and explicit scope limitations
  such as "guidance, not a script/checklist." Keep the workflow concise and link its source of
  truth.
- **Examples and configuration comments:** explain access limits, non-obvious wiring or load
  order, security stance, replay behavior, exceptions, and likely misuse. Do not narrate entries
  that the configuration already shows.
- **Prompts and visible strings:** treat wording as behavior. Inspect generated output and run
  behavior validation or state why no snapshot applies.
- **Diagnostics:** name the failing subject or path, violated rule, and correction when it is
  non-obvious. Remove internal execution narration.

Preserve searchable mechanism names and meaningful modal, temporal, or negative emphasis.
Normalize decorative emphasis only.

## Workflow

1. Confirm the scope, mode, current branch or PR base, and applicable `AGENTS.md` files. Do not
   inspect unrelated branches.
2. Read the documentation standard and the owning code or document before judging a passage. For
   calibration or unfamiliar cases, read the distilled examples.
   【V2 注】原文 `references/examples.md` 是 repo 专属文件（死引用已剔除）——V2 边界案例沉淀在
   `domains/ai-os/patterns/prose_standard.md` 的边界案例区。
3. Inspect the requested scope, not only the largest files. Use searches and word counts to find
   candidates, then judge passages semantically.
4. Classify each candidate as keep, add, trim, restore, restructure, or defer. Apply clear
   changes only when the task authorizes edits; do not manufacture edits to satisfy a deletion
   target.
5. Update the owner before derivative artifacts. Re-check analogous passages after learning a new
   rule.
6. Run the narrow relevant checks, documentation gates, `git diff --check`, and behavior tests
   for visible strings. Verify the final diff contains no third-party-dependency path and report
   any accidental match rather than claiming a clean exclusion history.
7. Report the inspected scope, clear changes, deliberate keeps, deferred cases, and checks
   actually run.

## Borderline decisions

A case is borderline only when at least two versions satisfy the complete-proposition rule but
trade accepted principles, and this working mode does not already resolve the tradeoff. A rewrite
with one proposition-preserving answer is not borderline.

In automatic mode, apply clear edits when authorized and report genuine borderline cases without
asking questions. Do not weaken a proposition to make progress.

In interactive mode, group analogous passages under the governing principle. Present two or three
viable versions, recommend one, and state the factual or structural difference. Do not offer
inferior distractors. Use the user's requested channel; when calibrating a PR through inline
comments, place the recommended provisional version in the diff and attach the alternatives to
that exact line.

After the user decides, distill the principle and versions into the distilled examples, without
PR history or reviewer narration, and apply the learned rule to every analogous passage in scope.

【V2 注】"distilled examples" 落点 = `domains/ai-os/patterns/prose_standard.md` 边界案例区。

## 检查清单（散文/注释编辑中自测）

- [ ] scope 显式了吗（缺失则报告所需输入并停止）？
- [ ] 编辑前识别了每个命题（actor/action、条件/时序、模态、负向保证、所有权/失败）？
- [ ] 删除只发生在每个事实子句都存活且更清晰时；没有为"字少"而删？
- [ ] 非显然契约在局部完整保留；架构/理由/历史链接到唯一归属（一个解释一个家）？
- [ ] 12 类位置覆盖检查过了吗（公开 JSDoc/内部注释/模块注释/测试/cookbook/README/Agent Notes/
      postmortem/skills 指令/示例与配置注释/提示词与可见字符串/诊断）？
- [ ] 没有复述代码已明示的内容；没有控制流叙述/测试走读/评审历史/推理转录？
- [ ] 第三方依赖目录与冻结归档被排除；派生物先改源再重新生成？
- [ ] 只应用了任务授权的编辑；borderline 如实报告、未弱化命题？
- [ ] 汇报列了检查范围、明确改动、刻意保留、延后案例与实际跑过的检查？

---

## Reference（知识侧 · 多关系）

- **方法层知识（Searchable）**：`domains/ai-os/patterns/prose_standard.md` ——
  可迁移方法层、触发/条件/动作 frontmatter、**不携带清单**（repo 专属死引用全列）、与
  `doc_standards` / `cot_leakage_trim` / `simplification_audit` / senior-engineer Review 面 /
  knowledge-space-maintenance 的互补边界、边界案例沉淀区。需要边界论证或检索命中时回读本
  pattern。
- **原文（Source preservation）**：`evolution/intake/dsh-prose-standard/SKILL.md` ——
  若未来真实项目就是 deepseek-harness 类仓库，直接装载原文（含全部 repo 专属约定）。
- **触发关系**：本单位 = 完整工作模式（Assembled / Conditional）；命中 trigger 装载执行完整
  流程；知识检索（experience_push）命中的是 domains pattern（Reference），二者互补不重复。

