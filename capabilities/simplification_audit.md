---
name: simplification_audit
type: Assembled / Conditional（工作模式整包单位 · 可激活）
source: 外部 Skill dsh-find-simplifications（deepseek-ai/deepseek-harness · Human 提供）；原文见 evolution/intake/dsh-find-simplifications/SKILL.md
trigger:
  - "find things to simplify" / "找简化候选" / "简化这个代码库" / 减面 / 去冗余 / 删死代码
  - 重构前先做全量简化候选审计（dead / duplicated / speculative / over-built /
    added-then-removed / hand-rolled-where-dependency-exists）
  - 评审中发现复杂度 / 投机泛化 / 重复表示，需要证据支撑的移除提案
  - 审计 / 归并已被取代的 Agent Notes（task card / pattern / SUCCESS_LOG 承重记录；V2 由
    knowledge-space-maintenance Lifecycle facet 承接裁决）
  - 把另一个 PR / 分支里有价值的简化想法折叠进来
  - 写内联 TODO / FIXME / XXX 简化注记（小清理）
activation: 开工 bootstrap 能力检索（task_start.py 查 capabilities/INDEX.md）命中本 trigger →
  读本文件全文 → 把"证据驱动的代码简化审计"完整流程装载为当前任务工作模式：先读仓库上下文 →
  强候选判据 → 广泛 survey（并行子代理分域或自模拟广度）→ 信任与生命周期边界审计 →
  依赖替换净删除衡量 → 每个候选先分类消费者再证明或拒绝 → 记录收编（knowledge-space-
  maintenance Lifecycle facet 承接）→ 提案写作（task card proposed）→ 内联 TODO 纪律 →
  验证汇报；按最后"检查清单"自测后汇报
status: Assembled + Delivered（可激活）；真实简化审计消费 Q1–Q5 UNKNOWN
  （无自然"找简化候选"任务触发，显式不宣称已帮助）
decision_ref: D-025 / D-042
knowledge_ref:
  - domains/ai-os/patterns/simplification_audit.md（方法层知识 · Searchable ·
    边界论证 / 不携带清单 / 与既有知识互补关系 / 边界案例沉淀区）
  - evolution/intake/dsh-find-simplifications/SKILL.md（原文 · 若真实项目即 deepseek-harness
    类仓库直接装载原文）
---

# 证据驱动的代码简化审计 — 完整工作模式（Finding DeepSeek Harness Simplifications · Assembled / Conditional）

> 本文件 = **可激活的完整工作模式单位**（剔除死引用后的整包，不是方法层摘录）。
> 装载条件与激活方式见 frontmatter `trigger` / `activation`；命中后按下面完整流程执行。
> 方法层知识（可检索、含边界论证与不携带清单）保留在
> `domains/ai-os/patterns/simplification_audit.md`（Reference）——本文件与它互为同一对象的
> 不同承载（D-034：Physical placement 是承载，不是语义身份）。
> 原文：deepseek-ai/deepseek-harness `.agents/skills/dsh-find-simplifications/SKILL.md`
> 。**剔除**：deepseek-harness 专属路径/文件/命令
> （死引用）；**保留**：完整简化审计流程（剔除 ≠ 拆解）。

---

name: simplification_audit
description: Use when working in a repository to find non-obvious simplification candidates, write proposed Agent Notes or inline TODO/FIXME/XXX notes, audit or coalesce superseded Agent Notes, or fold worthwhile simplification ideas from another PR; especially for dead, duplicated, speculative, over-built, added-then-removed, or hand-rolled-where-a-dependency-exists surfaces.
tools: ["Read", "Grep", "Glob", "Bash", "Git"]

【V2 注】tools 映射：Read/Grep/Glob/Bash/Git = carrier 工具层文件 I/O、搜索与 git 执行。

# 找简化候选 — 完整工作模式（Finding Simplifications）

This working mode helps turn a broad "find things to simplify" request into evidence-backed
proposals that remove or collapse existing surface area. It is guidance, not a checklist:
follow the code, keep judgment active, and prefer a few well-proven candidates over a pile of
thin guesses.

## Start With Repo Context

- Read the applicable `AGENTS.md`, especially the pre-release stance and the conventions
  (including the tests-are-not-golden-truth and notes-are-not-golden-truth doctrines), plus the
  project's defensive-patterns and testing conventions.
  【V2 注】原文 `AGENTS.md`、`docs/defensive-patterns.md`、`docs/testing.md` 是 repo 专属
  （死引用已剔除）——V2 对应：适用 AGENTS.md（项目/仓库拥有契约；AI-OS = `D:\AI-os\AGENTS.md`
  宪法与 Writing 纪律）+ 项目实际约定文档；tests-are-not-golden-truth 与
  Agent-Notes-are-not-golden-truth 教义保留为原则（V2 承重记录同样不是"存在即真理"）。
- Skim the applicable architecture doc before judging anything under the main code areas;
  simplifications that fight the service map or event taxonomy need extra evidence.
  【V2 注】原文 `docs/architecture.md` 与 `packages/` 布局是 repo 专属（死引用已剔除）——V2
  对应：项目架构文档 + 主代码面（workspace 项目 / AI-OS `tools/` 等）。
- Use the proposal tree and its rules to understand intentional architecture; the most relevant
  implemented examples are recorded proposals that pin protected seams (drop a mutable session
  summary, shared persistence write coordinator, capability seams, twin adapters / dual
  persistence backends).
  【V2 注】原文 `.agents/notes/` 树（README 规则 + implemented/architecture 具体例子）是 repo
  专属（死引用已剔除）——V2 对应：task card / pattern / SUCCESS_LOG 承重记录树（含 proposed /
  implemented 状态语义）；"受保护 seam（双 LLM 适配器 / 双持久化后端）默认有意保留"作为原则
  保留，不做删除提议，除非用户显式覆盖约束；受保护 seam 内部的未用方法/钩子仍可合法移除，
  只要不折叠受保护设计本身。

## What Counts As A Strong Candidate

A strong simplification removes, folds, or demotes something real and has clear evidence that
the current design costs more than it buys:

- A public method, event, config knob, registry notification, helper, package, durable event, or
  test artifact has no production consumer.
- Tests or docs are the only consumers, and the behavior they pin is not load-bearing.
- Two representations mirror the same fact, especially across durable session events and
  transient `agent/*` events.
  【V2 注】`agent/*` 事件是 deepseek-harness 特有事件面（死引用已剔除）——双表示镜像判据保留，
  具体事件面以项目实际为准。
- A seam has methods every implementation must support but no consumer uses.
- A separate package exists only for test/demo/support code and adds publish or dependency
  overhead.
- A feature implements speculative product generality: multi-session/session-load, background
  job rosters, live registry invalidation, mid-turn steering, tool-owned UI rendering, and
  similar designs with no product owner.
- An invariant, rollback path, set of expected outputs, or special-case test exists only to
  protect an unused API.
- Hand-rolled code reimplements what a well-maintained external package or a builtin at the
  engine floor already provides, and the swap would delete the implementation plus its dedicated
  tests（V2：依赖策略见 dependency policy 原则——`domains/ai-os/patterns/simplification_audit.md`
  §5 + 既有记录 seam）。
- The simplified behavior may differ slightly, but the new behavior is still reasonable and
  easier to explain.

Thin candidates are usually not enough for a durable proposal: deleting one typo, running a
dead-code scanner once, removing an intentionally documented backend/adapter, or flagging "this
looks complex" without call-site proof.
【V2 注】原文"knip 一次"是 repo 专属工具（死引用已剔除）——原则保留：扫描器一次结果 ≠ 候选
证据；V2 用 rg 精确符号 + 读调用点。

## Survey Broadly

Use parallel subagents when the user asks for breadth or many candidates. Give each agent a
domain and require evidence, not guesses. Useful domains:

- Agent loop and session log: turn/step boundaries, steering, abort/cancel, durable events,
  replay, load/resume.
- Automation and human UI APIs: prompt settlement and teardown on the protocol side; transcript
  rendering and interaction state on the UI side.
- LLM/tools/system prompt: stream/generate APIs, assemblers, registries, tool schema defaults,
  presentation hooks.
- Execution and tool running: foreground/background split, job ownership, output spill files,
  executor methods.
- Packages/examples/scripts/tests: package splits, static inventories, redundant snapshot
  expected outputs, support packages.

If subagents are unavailable, simulate the same breadth yourself. Do not let the first good
candidate stop the survey.
【V2 注】"subagents"映射 = V2 的并行子任务能力（按需使用；不可用则自模拟同广度）。

Start with the largest production-code deltas. A broad simplification audit that stops after
obvious unused symbols can miss the files where duplicated lifecycle or defensive machinery
carries most of the cost.

## Audit Trust And Lifecycle Boundaries

For every defensive copy, freeze, validator, and callback capture, name where the value came
from and who owns it next. Same-process typed service/plugin calls ordinarily borrow readonly
values; parsers, config loaders, queues, model/tool JSON, durable files, workers, processes,
and wire decoders own or validate their data. Tests built around hostile getters, fake typed
objects, callback replacement, or mutation after a same-process handoff are evidence of a
potentially speculative contract, not automatic justification for keeping it.

For complex asynchronous code, draw the ownership graph and map each sentinel, readiness
promise, cancellation path, disposer, and state flag to a distinct owner or transition. When
several mechanisms mirror the same liveness or settlement fact, propose one transaction or
lifecycle controller instead. Preserve separate machinery where it protects synchronous
publication and rollback, callback containment, first-terminal-outcome arbitration,
worker/process ownership, or dispose-to-quiescence.

## Hand-Rolled Code Versus A Dependency

Introducing a dependency is a valid simplification move, not a policy exception: the dependency
policy owns the bar. When surveying, ask of protocol parsers, framers, retry/backoff loops, glob
matchers, diff engines, and similar infrastructure: does a well-maintained package or a builtin
at the engine floor already do this?
【V2 注】原文 `notes/implemented/process/2026-07-26-dependencies-over-hand-rolling.md` 是 repo
专属记录（死引用已剔除）——V2 对应：`simplification_audit` pattern §5（手写轮子 vs 依赖判据）
+ 既有已记录 seam（受保护设计需击败记录理由）。

Prove a dependency-swap candidate like any other, plus:

- Read the hand-rolled implementation and name the exact surface the package covers; residual
  semantics the package does not cover count against the swap and stay in the proposal.
- Check the package's health honestly (maintenance, adoption, transitive footprint) and prefer
  builtins when the engine floor has them.
- Check the proposal tree first: recorded seams are settled — a swap that collapses one needs to
  beat the recorded rationale, not just cite the policy.
- Weigh net deletion: implementation plus dedicated tests plus docs, minus the glue that
  remains. A wrapper that relocates the same complexity is not a win.

## Prove Or Reject Each Candidate

For every symbol or behavior, classify consumers before writing:

- Production corpus: main source trees, example source, runtime scripts, and loader/config
  paths.
- Non-production corpus: tests, README/docs, proposals, snapshots, generated expected outputs,
  and comments.
- Ambiguous corpus: examples and scripts that may be product smoke paths. Inspect usage before
  classifying.

Use `rg` first. Good searches include the exact symbol, event name, package name, config key,
method name with both `.name(` and `name(`, and any wire strings. Then read the call sites.
A dead-code scanner can help, but it is not a substitute for understanding public interfaces,
dynamic event names, tests, docs, and loader paths.
【V2 注】原文 `knip` 是 repo 专属工具（死引用已剔除）——原则保留：扫描器只定位候选路径，
不替代语义审查。

Reject or downgrade a candidate when:

- A production caller exists and the simplification would be a feature decision rather than a
  cleanup.
- The API is explicitly justified by an implemented proposal or a hard-won defensive pattern,
  and the new evidence does not beat that reason.
- The removal would force unrelated churn without actually reducing the public API or required
  behavior.
- The idea is correct but tiny. Add a targeted TODO/FIXME/XXX instead, using the urgency
  semantics in the applicable conventions.
  【V2 注】原文 `docs/development.md` 的 urgency 语义是 repo 专属（死引用已剔除）——V2 对应：
  项目约定中的 TODO/FIXME/XXX 语义；AI-OS 自身按 task card / pattern 记录惯例。

## Coalesce Superseded Notes

Audit the proposal tree when the user asks to reduce or coalesce it, or when the simplification
being implemented makes an owning note obsolete. Do not expand every code-simplification survey
into a repository-wide note audit.

Use the record-lifecycle skill for retention judgment and archive mechanics.
【V2 注】原文 `dsh-archive-agent-notes` 子 skill 引用已映射到 V2 的
`knowledge-space-maintenance` Lifecycle / Archive facet（D-022，maintenance-skills/
knowledge-maintenance/SKILL.md）——保留/归档/删除的**执行者**；本工作模式只补充判据，不重开
facet、不抢裁决。V2 的"Agent Notes"对应 task card / pattern / SUCCESS_LOG 承重记录。

Follow the deletion rule in the proposal rules; do not duplicate or weaken it here. For each
candidate chain:

1. Identify the current owner from shipped code, configuration, generated catalogs, package
   docs, newer proposals, and inbound links; dates and titles are discovery hints, not proof.
2. Classify the old note as fully or partially superseded. Any surviving behavior, current
   contract, durable format, compatibility obligation, or independently current rejected
   alternative makes it partial. Rationale that can be transferred to the current owner does not
   by itself make supersession partial.
3. For full supersession, move every unique rationale, alternative, consequence, shipped
   verification evidence, and named coverage gap into the current owner. An inventory that only
   describes deleted implementation mechanics is not one of those decision facts.
4. Repair every inbound link, then delete the superseded notes together.
5. Search exact filenames, symbols, config keys, event names, and wire strings after the edit.
   Keep partial supersessions cross-linked and current.

An added-then-removed feature is a common full-supersession case. Let the removal note own the
history only when the feature is absent from production code, configuration, schemas, durable
or wire formats, migration, and compatibility behavior; no current documentation presents it as
available; and no test exercises it as supported behavior. Removal rationale and tests that
enforce absence may remain. Preserve why the feature originally existed, why that motivation no
longer justified it, alternatives to full removal, the capability given up, conditions for
reintroduction, and evidence that removal is complete. Old tests and implementation mechanics
that verified only the deleted behavior are not current verification evidence.

Reject consolidation when the removal is only one transport, default, implementation, or
presentation of a feature; when persisted data or compatibility handling survives; or when the
removal note does not yet carry enough rationale to prevent accidental reintroduction. A current
negative design decision may legitimately need its own note even though the removed
implementation is gone.

## Write The Proposal

Create one file per durable proposal, following the lifecycle and classification rules.
【V2 注】原文 `.agents/notes/<lifecycle>/<class>/yyyy-mm-dd-topic.md` 树与
`.agents/notes/README.md` 规则是 repo 专属（死引用已剔除）——V2 对应：proposed 类提案 =
`task_cards/` proposed 卡（任务文件模板 `任务文件模板_v1.3.md` 形态 / task card 模板）；
lifecycle = proposed → implemented → archived；classification 按任务卡/项目卡目录。Keep prose
paragraphs on one physical line and use relative Markdown links（V2 同）。

Prefer this structure, adjusting when the idea needs it:

- `# Proposal: <action-oriented title>`（V2：`# TASK_CARD` 或任务文件形态，标题动作导向）
- `Status: proposed`
- `## Problem`: name the current API, cite the relevant files, and state the consumer evidence.
  Separate production callers from tests/docs.
- `## Proposal`: say exactly what to remove, fold, demote, or rehome. Include tests, docs,
  READMEs, JSDoc, event-taxonomy, snapshot, and generated-file cleanup when relevant.
- `## Why not keep it?` or `## What we give up`: make the strongest counterargument legible.
- `## Acceptance criteria`: observable end state and gates.
- `## Risks`: public API changes, behavior changes, future product wants, and why the tradeoff is
  still reasonable.

Be concrete enough that an implementing task can follow the trail. Avoid vague "simplify this
package" proposals. When a proposal overlaps an existing one, consolidate the useful details
into the existing one rather than creating a duplicate.

## Inline TODO Notes

Use inline TODO/FIXME/XXX only for small, local cleanups that are clearly useful but not durable
design decisions. Keep them short and actionable:

- Name the smell with a stable tag, e.g. `TODO(double-default)` or `XXX(unused-default)`.
- Explain why it is safe to revisit and what action would simplify it.
- Do not add TODOs for speculative complaints or for behavior that needs a proposal-level
  decision.

## When Folding Another PR Or Branch

Diff the sibling branch against the shared base, not against the current branch, so you see its
independent contribution. For each item:
【V2 注】原文 `origin/master` 是 GitHub 远端基线（死引用已剔除）——V2 无远端时用本地共享基线
（如 main/master 或上游分支）作对照；原则保留：对比独立贡献，不对比当前分支自身。

- Port non-overlapping proposals or TODOs that meet the quality bar.
- Consolidate overlapping material into the existing proposal that owns the topic.
- Do not port duplicate or lower-confidence proposals just to preserve the count.
- Update the summary so reviewers see the true candidate count and scope.
- Close the duplicate PR only when the user asked you to, or when you clearly own that
  housekeeping.
  【V2 注】PR 语义在 V2 无远端时为"变更集/交付物"；关闭重复 PR 对应"不把重复候选并入交付"。

## Validation And Reporting Hygiene

For docs-only proposal work, run at least the project's doc-sync/consistency check if one
exists, lint if present, and `git diff --check`. For code comments or skill changes, also run
the relevant validator when one exists. Select any other evidence from the outgoing diff.
【V2 注】原文 `pnpm run doc-sync` / `pnpm run lint` 与 pre-push hook 是 repo 专属（死引用已
剔除）——V2 对应：项目实际的既有检查 + `git diff --check`（通用保留）；V2 无对应命令时明确
列出实际跑过的检查，不声称没跑过的门禁。

When opening or updating a PR, summarize:
【V2 注】PR 汇报在 V2 无远端/CI 时为交付汇报——结构保留。

- How many proposals and inline notes were added, consolidated, retained as partial
  supersessions, or deleted.
- The main areas surveyed.
- What was intentionally excluded.
- Which checks passed.

For each consolidation group, name the old and current owners, state the evidence for full
supersession, and explain why deletion is safe. If an added-then-removed scan finds no
qualifying note, report that result and the representative partial cases retained.

Use a draft PR while the survey is still expanding; mark ready only when the candidate set,
review responses, and validation are settled.
【V2 注】V2 无 PR 平台——"draft → ready"对应"候选集与验证未定稿前不宣称交付完成"。

## 检查清单（简化审计任务中自测）

- [ ] 先读了仓库上下文（适用 AGENTS.md / README / 架构与约定）再判断？
- [ ] 每个候选都有消费证据（rg 精确符号 + 调用点）而不是"看起来复杂"？
- [ ] 生产调用者 / 已记录理由 / 无关 churn / 太小→TODO 的拒绝理由都写了吗？
- [ ] 强候选面都覆盖了吗（无生产消费者 / 仅测试文档消费者 / 双表示镜像 / 无消费者 seam /
      投机泛化 / 仅保护未用 API 的防御机制 / 手写轮子 vs 依赖 / 简化后行为合理且更好解释）？
- [ ] survey 停了第一个候选吗（并行子代理分域或自模拟广度；先看最大生产代码 delta）？
- [ ] 防御机制审计命名了"值从哪来、下一步归谁"；保护性机制（发布+回滚 / 回调封闭 / 首终局
      仲裁 / worker-进程所有权 / dispose-to-quiescence）保留了吗？
- [ ] 依赖替换按净删除衡量、包健康与残余语义都查了吗（优先 builtin；先查已记录 seam）？
- [ ] 小清理走的是带稳定标签的内联 TODO，而不是提案文件？
- [ ] 提案有 Problem / Proposal / Why not 或 What we give up / Acceptance / Risks，且能指引
      实现吗？
- [ ] 记录收编（如涉及）走了 knowledge-space-maintenance Lifecycle facet 判据（完整替代 /
      拒绝归并），没有把简化 survey 扩成全库审计？
- [ ] 汇报列了新增/合并/保留/删除数、survey 范围、显式排除与实际跑过的检查（不声称没跑过
      的门禁）？

---

## Reference（知识侧 · 多关系）

- **方法层知识（Searchable）**：`domains/ai-os/patterns/simplification_audit.md` ——
  可迁移方法层、触发/条件/动作 frontmatter、**不携带清单**（repo 专属死引用全列）、与
  `code-review` / senior-engineer Coding 面 / knowledge-space-maintenance Lifecycle facet /
  `testing-tdd` / `prose_standard` 的互补边界、边界案例沉淀区。需要边界论证或检索命中时回读
  本 pattern。
- **原文（Source preservation）**：`evolution/intake/dsh-find-simplifications/SKILL.md` ——
  若未来真实项目就是 deepseek-harness 类仓库，直接装载原文（含全部 repo 专属约定）。
- **触发关系**：本单位 = 完整工作模式（Assembled / Conditional）；命中 trigger 装载执行
  完整流程；知识检索（experience_push）命中的是 domains pattern（Reference），二者互补
  不重复。
- **协同单位 / 对象**：`code-review`（五轴分级机制）+ senior-engineer Review 面（深度纪律）
  ——评审回答"这次改动对不对"、本模式回答"哪些既有面值得移除/折叠"；senior-engineer Coding
  面 = "怎么改得更好"实现侧，本模式 = "哪些可以删/减"审计侧；`knowledge-space-maintenance`
  Lifecycle / Archive facet = 记录收编执行者（本模式只补充 added-then-removed 判据）；
  `prose_standard` = 提案触达文档/注释时的编辑判断；`testing-tdd` REFACTOR = 保持绿下清理的
  局部实践。
