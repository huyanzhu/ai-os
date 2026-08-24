---
name: pre_push_evidence_gate
type: Assembled / Conditional（工作模式整包单位 · 可激活）
source: 外部 Skill dsh-pre-push-checks（deepseek-ai/deepseek-harness · Human 提供）；原文见 evolution/intake/dsh-pre-push-checks/SKILL.md
trigger:
  - push / force-push / 推送到远端之前
  - 历史重写（rebase / amend / 改写已发布分支）后推送之前
  - 标记 ready for review 或声称"检查通过 / 准备就绪"之前
  - 批处理刚刚发布重写分支（级联 rebase / sync 类），需要立即验证
  - 面对"该跑哪些测试/检查"的选择，或有反射式跑全量套件的冲动
activation: 开工 bootstrap 能力检索（task_start.py 查 capabilities/INDEX.md）命中本 trigger →
  读本文件全文 → 把"推送前证据闸门"完整流程装载为当前任务工作模式：先确认 outgoing 范围 →
  按行为变更面选最小充分证据 → 覆盖度量纪律 → 全量复演仅三情况 → 历史重写保护
  （force-with-lease，绝不 raw --force）→ 发布后验证例外 → 失败即停 → 推送后远端核对；
  按最后"检查清单"自测通过后才允许推进
status: Assembled + Delivered（可激活）；真实推前检查消费 Q1–Q5 UNKNOWN
  （V2 无远端/CI/自然推送任务，显式不宣称已帮助）
decision_ref: D-027 / D-037
knowledge_ref:
  - domains/ai-os/patterns/pre_push_evidence_gate.md（方法层知识 · Searchable ·
    边界论证 / 不携带清单 / 与既有知识互补关系）
  - evolution/intake/dsh-pre-push-checks/SKILL.md（原文 · 若真实项目即 deepseek-harness
    类仓库直接装载原文）
---

# 推送前证据闸门 — 完整工作模式（Pre-Push Evidence Gate · Assembled / Conditional）

> 本文件 = **可激活的完整工作模式单位**（剔除死引用后的整包，不是方法层摘录）。
> 装载条件与激活方式见 frontmatter `trigger` / `activation`；命中后按下面完整流程执行。
> 方法层知识（可检索、含边界论证与不携带清单）保留在
> `domains/ai-os/patterns/pre_push_evidence_gate.md`（Reference）——本文件与它互为同一
> 对象的不同承载（D-034：Physical placement 是承载，不是语义身份）。
> 原文：deepseek-ai/deepseek-harness `.agents/skills/dsh-pre-push-checks/SKILL.md`
> 。**剔除**：pnpm/gh 等 V2 无对应物的 repo 专属命令
> （死引用）；**保留**：流程整体（剔除 ≠ 拆解）。

---

name: pre_push_evidence_gate
description: Use before pushing, force-pushing, marking ready for review, or claiming checks pass on a branch, and immediately after a batched publish rewrites branches, to select the smallest tests and checks that cover the outgoing or just-published diff without reflexively running the full repository suite.
tools: ["Read", "Grep", "Glob", "Bash", "Git"]

【V2 注】tools 映射：Read/Grep/Glob/Bash/Git = carrier 工具层文件 I/O、搜索与 git 执行；
V2 当前 `D:\AI-os` 本身无远端——本工作模式面向任何真实项目（未来有远端/CI/PR 平台时装载）。

## When to load this working mode

- Before any `push` / `force-push` to a remote.
- Before rewriting history (rebase / amend / rewriting a published branch) and pushing it.
- Before marking something "ready for review" or claiming "checks pass / ready".
- Immediately after a batched publish rewrites branches (cascading rebase / sync), when validation must follow publication.
- When facing "which tests/checks should I run" and feeling the reflex to run the whole suite.

Use this working mode to run relevant local evidence **once** before a push. The sole ordering
exception is a batched publish (e.g. a stack-sync command) that publishes a cascading rebase
before the rewritten layers can be validated; validate them immediately afterward and do not
merge until the evidence passes. Git hooks are intentionally narrow: pre-commit fixes staged
lint, checks staged whitespace, and guards vendored-source metadata; pre-push runs only the
incremental repository typecheck. CI owns exhaustive coverage and the platform matrix.

【V2 注】hook 实现（staged lint / whitespace / vendored-source metadata / 增量 typecheck）是
deepseek-harness 专属机制，V2 不携带具体实现——只保留"hook 管窄检查、CI 管穷尽覆盖"原则。

## Inspect the outgoing change

1. Confirm the checkout and branch.

```sh
git status --short --branch
git rev-parse --show-toplevel
```

2. Verify the live PR base or stack parent, fetch that ref, and inspect the complete scope against it.

【V2 注】`pnpm --silent run change-scope --base <verified-base-ref>` 是 deepseek-harness 专属
命令（死引用已剔除）。V2 用等价机制：先核实 base ref（来自实时远端或栈状态，不猜测、不自动
fetch 猜测），再用仓库的变更范围工具（类 change-scope）或等价手段检查完整 outgoing 范围——
**已提交路径相对 resolved merge base + 暂存/未暂存/未跟踪路径描述当前 worktree**，两类分开。
命令的版本化 JSON 记录已提交路径；staged/unstaged/untracked 描述当前 worktree。base 被合并/
变化后：重跑报告，重新评估合并后范围影响的行为，只重跑被该合并失效的检查。

## Select relevant evidence

There is no universal local baseline beyond the hooks. Every behavior change needs the narrowest
available test or purpose-built check that would fail for its regression; add broader checks only
for surfaces the diff actually reaches.

- **Package or script behavior:** run the owning test file or focused test name. Add adjacent
  package tests when a shared contract changes; leave repository-wide coverage to CI unless the
  change is genuinely cross-cutting or the user requests it.
  【V2 注】"owning Vitest 文件"中的 Vitest 是示例 runner；V2 用项目既有测试运行器的等价聚焦能力。
- **Documentation, Agent Notes, catalogs, or doc-linked comments:** run the documentation-sync
  check; run full lint when the documentation workflow requires it.
  【V2 注】`pnpm run doc-sync` 是 repo 专属命令（死引用已剔除）——V2 用项目文档工作流的等价
  "文档同步检查"（类 doc-sync）。
- **Model-, editor-, CLI-, or terminal-visible output:** run the focused keyless snapshot or real
  runnable-example scenario that owns the output.
- **Package manifests, public exports, build configuration, worker/bin entries, or built runtime
  paths:** run the build, the relevant hygiene checks, and the owning built-artifact smoke.
  【V2 注】`pnpm run build` 同理为示例；V2 用项目既有构建与冒烟入口。
- **Real provider or agent behavior:** run the relevant end-to-end target when credentials are
  available; never print secrets.
  【V2 注】`pnpm run test:e2e` 为示例；e2e 入口以项目为准。

Do not manually repeat a passing check merely because commit or push follows. In particular, do
not run typecheck immediately before pushing solely to duplicate the pre-push hook.

### Focus unit coverage on the affected source

Test selection and coverage selection are separate. A test-runner filter chooses which tests run,
while the repository configuration otherwise measures every source file. When unit coverage is
relevant, name both the owning tests and the source files or package whose coverage those tests
must prove:

```sh
<runner> run packages/<group>/<package>/tests/<behavior>.spec.ts \
  --coverage \
  --coverage.include='packages/<group>/<package>/src/**/*.ts'
```

【V2 注】`pnpm exec vitest` 命令链是 deepseek-harness 专属（死引用已剔除）；机制保留——
**同时点名 owning 测试（执行范围）与 `--coverage.include` 等价参数（源范围）**，二者不可互相
替代。使用精确源文件当行为真限于单模块；多文件/多包重复 include；配置的按文件覆盖率阈值仍
适用于选中源范围。

When the owning tests are unclear, use the test runner's dependency graph to discover a candidate
set, then inspect the selected tests before treating the run as evidence:

```sh
<runner> related packages/<group>/<package>/src/<changed>.ts \
  --run \
  --coverage \
  --coverage.include='packages/<group>/<package>/src/<changed>.ts'
```

【V2 注】`vitest related` 类依赖图**发现不了**只经配置/动态加载/子进程/worker/构建产物/外部
provider 触达的行为——那些要显式选 owning 测试。不用 `--passWithNoTests`、不降低阈值、不收窄
include 隐藏未覆盖的受影响文件；选中范围失败只因一个聚焦测试没覆盖它时，补其他 owning 测试，
或只在被排除模块确实不可能受影响时收窄源范围。

## Full local rehearsal

Run the complete local approximation only when the user explicitly requests it, while diagnosing
a CI failure, or when the change spans the repository so broadly that no narrower set is credible.
Use the current workflow and package scripts as the inventory; do not recreate removed aggregates.

【V2 注】"已删除的 `check:pre-push` 聚合"是 deepseek-harness 仓库历史（死引用已剔除）——原则
保留：全量复演仅三情况（用户明确要求 / 诊断 CI 失败 / 变更横跨仓库到无更窄集可信）。

## Protect history-rewriting pushes

Rebase is allowed for standalone and stacked PR branches, including after review. Before a
standalone history rewrite, fetch the current remote branch and record its exact OID; publish
with `--force-with-lease=<branch>:<observed-oid>` so a concurrent update aborts the push.
Stack-publishing commands (e.g. a stack push/sync) supply lease protection for their managed
branches. Raw `--force` is never allowed.

【V2 注】`gh stack push` / `gh stack sync` 是 GitHub 栈插件专属（死引用已剔除）——机制保留：
任何栈式 PR 平台用其原生发布命令，租约保护（并发更新中止推送）由平台供给；**raw `--force`
永不使用**。

After any rewritten push, fetch the live heads again and re-audit unresolved review threads,
approvals, mergeability, and checks. Commit hashes and inline-comment anchors from before the
rewrite are not current evidence.

### Post-sync validation

Some batched publish commands fetch, cascade-rebase, and push as one operation, so local validation
cannot be placed between rewrite and publication. Before running one, require a clean worktree and
record the official stack order and exact remote heads. After it returns:

1. Re-query every branch head and the official stack order.
2. Inspect the changed scope of every rewritten layer against its live PR base.
3. Run the relevant evidence selected by this working mode for each affected layer.
4. Keep every PR unmerged and report validation as pending until all selected checks pass.

If post-sync evidence fails, leave the lease-protected published heads in place, repair the
failure, validate the repair, and publish the correction. Do not claim the sync made the stack
ready merely because the command succeeded.

## Handle failures

If a relevant check fails before an ordinary push, stop and fix or explain the blocker. Do not
push and hope CI differs. For the post-sync exception, block the merge and follow the repair
procedure above.

If a failure looks environment-specific, prove it:

- Record the exact command, failing test, and platform-specific mismatch.
- Confirm the relevant non-platform evidence.
- Prefer fixing cross-platform nondeterminism when the check is required.
- Bypass a local hook only when the user explicitly asks or agrees, and report exactly what failed
  and why CI is expected to differ.

## Push procedure

For ordinary and standalone rebase pushes:

1. Run the selected relevant checks once.
2. Commit normally and inspect any files changed by the pre-commit fixer before continuing.
3. Push normally, or use the exact lease for an authorized rewritten branch, so the incremental
   typecheck hook runs.
4. Verify the remote ref matches local `HEAD`.

```sh
git rev-parse HEAD origin/$(git branch --show-current)
```

For PR platforms, inspect remote CI after the push via the platform's check query. Report pending
checks as pending. Inspect failures before attributing them to the branch or the environment.

【V2 注】`gh pr checks` 是 GitHub 专属（死引用已剔除）——机制保留：push 后查平台 CI，
pending 如实报告；检查失败先归因再判环境。

When the platform reports "no checks reported" and the head-event query returns zero runs, read
mergeability before suspecting the push or a dropped platform event:

```sh
gh pr view <number> --json mergeable,mergeStateStatus
```

【V2 注】`gh pr view` 具体查询同样是 GitHub 专属（死引用已剔除）——**诊断语义保留**：平台对
CONFLICTING/DIRTY PR 不产生 workflow 运行，缺失信号 = 冲突而非基础设施；**解决冲突是唯一修复**
（空 commit / `--allow-empty` 推送 / draft-ready 反复 / revert-restore 弹跳都停在零运行且加
垃圾历史）；本地无法合并时用 `git merge-tree --write-tree HEAD origin/<base>` 确认冲突路径。

For stack-sync style batched publishes, use the post-sync validation sequence instead of
pretending the ordinary order was possible.

## 检查清单（推送/声称通过前自测）

- [ ] base ref 来自实时远端/栈状态（不猜测、不自动 fetch 猜测）；已提交路径与 worktree 路径分开检查了？
- [ ] 每个行为变更选了该回归会失败的最窄 owning 测试/定向检查；只对 diff 真正到达的表面积加宽？
- [ ] 没有反射式跑全量套件？没有重复已通过的检查 / 重复 hook 已做的工作？
- [ ] 覆盖度量点名了 owning 测试 + 源范围；没有用 --passWithNoTests / 降阈值 / 收窄 include 隐藏未覆盖文件？
- [ ] 历史重写前记录了远端精确 OID，用 force-with-lease=<branch>:<observed-oid> 发布，没 raw --force？
- [ ] 重写推送后重新 fetch live heads 并重审了评审线程/批准/可合并性/检查（旧哈希/锚点未当证据）？
- [ ] 批处理发布后按层跑证据、保持未 merge、pending 如实报告；失败保留租约 heads 修复再发布？
- [ ] 相关检查失败即停（没 push 后指望 CI）；环境特定失败记录了确切命令/失败测试/平台差异？
- [ ] 推送后核对了 `git rev-parse HEAD origin/<branch>`；PR 平台 "no checks reported" 先读 mergeability 而非怀疑推送？

---

## Reference（知识侧 · 多关系）

- **方法层知识（Searchable）**：`domains/ai-os/patterns/pre_push_evidence_gate.md` ——
  可迁移方法层、触发/条件/动作 frontmatter、**不携带清单**（pnpm/gh 死引用全列）、与
  `git_safety_net` / `dependent_change_landing` / `testing-tdd` / `code-review` 的互补边界。
  需要边界论证或检索命中时回读本 pattern。
- **原文（Source preservation）**：`evolution/intake/dsh-pre-push-checks/SKILL.md` ——
  若未来真实项目就是 deepseek-harness 类 GitHub 仓库，直接装载原文（含全部 repo 专属命令）。
- **触发关系**：本单位 = 完整工作模式（Assembled / Conditional）；命中 trigger 装载执行完整
  流程；知识检索（experience_push）命中的是 domains pattern（Reference），二者互补不重复。

