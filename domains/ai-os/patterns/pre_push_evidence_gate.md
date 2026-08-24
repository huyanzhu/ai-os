---
rule_id: PRE-PUSH-EVIDENCE-GATE-001
title: 推送前证据闸门（outgoing diff 最小充分证据 / 历史重写推送保护 / 失败即停 / 推送后远端核对）
category: Pre-Push Evidence Gate
trigger:
  - push / force-push / 推送到远端之前
  - 历史重写后推送（rebase / amend / 改写已发布分支）
  - 标记 ready for review 或声称"检查通过 / 准备就绪"之前
  - 批处理刚刚发布重写分支（级联 rebase / sync 类），需要立即验证
  - 面对"该跑哪些测试/检查"的选择，或有反射式跑全量套件的冲动
condition: 有 outgoing diff 需要推送到远端（或刚被发布、需要验证），且需要决定本地跑哪些证据
action:
  do:
    - 用实时远端/栈状态确认 base ref，检查完整 outgoing 范围（committed paths 相对 merge base + worktree paths 分开）
    - 为 outgoing diff 选最小充分证据：该行为回归会失败的 owning 测试/定向检查；只对 diff 真正到达的表面积加宽检查
    - 文档/输出/清单/构建类变更跑 owning 检查；真实 provider/agent 行为有凭证时跑 e2e（不打印秘密）
    - 历史重写前记录远端精确 OID，用 --force-with-lease=<branch>:<observed-oid> 发布；绝不 raw --force
    - 重写推送后重新拉取远端 live heads，重新审计评审线程/批准/可合并性/检查（旧 commit 哈希与内联锚点不是当前证据）
    - 相关检查失败即停：修复或解释，不 push 后指望 CI 不同；环境特定失败记录确切命令/失败测试/平台差异并证明非平台证据
    - push 后验证远端 ref 与本地 HEAD 一致；PR 场景查 CI 并如实报告 pending
  dont:
    - 不反射式跑全量套件（hook 管窄检查、CI 管穷尽覆盖；除非用户明确要求/诊断 CI 失败/变更面广到无更窄集可信）
    - 不因 commit/push 跟随而重复已通过的检查；不重复 hook 已做的工作
    - 不用 --passWithNoTests / 降低阈值 / 收窄 include 隐藏未覆盖的受影响文件
    - 不用猜测的 base；不信任旧报告/旧哈希作为当前证据
    - 不 raw --force；不在批处理发布前假装能插入本地验证（发布后立即逐层验证，未通过不 merge、报告 pending）
keywords:
  - 推送前
  - pre-push
  - push
  - force-push
  - force-with-lease
  - 历史重写
  - history rewrite
  - rebase
  - 证据选择
  - evidence selection
  - 最小充分证据
  - 测试选择
  - test selection
  - outgoing diff
  - 变更范围
  - change scope
  - 全量测试
  - full suite
  - 回归
  - regression
  - 失败即停
  - 环境特定失败
  - CI
  - 远端核对
  - mergeability
  - 冲突
  - conflict
alias:
  - dsh-pre-push-checks
  - 推前检查
  - 推送前检查
  - pre-push checks
  - 推前证据
  - 最小测试选择
  - 历史重写保护
  - force push 保护
knowledge_position: Cluster
knowledge_cluster: FC-Pre-Push Evidence Gate
epistemology_tag: PROCEDURE
confidence: HIGH
---

# 推送前证据闸门（outgoing diff 最小充分证据 / 历史重写推送保护 / 失败即停 / 推送后远端核对）

**来源**：外部 Skill（Human 提供，Evolution Intake #10 / DSH Corpus #7）——deepseek-ai/deepseek-harness
的 `dsh-pre-push-checks` SKILL.md（2026-08-24 HTTP 200 逐字下载，原文存
`evolution/intake/dsh-pre-push-checks/SKILL.md`）。按 Skill Fusion 先例（D-004 debug-protocol /
D-023 doc_site_projection / D-024 doc_standards / D-025 simplification_audit / D-026
dependent_change_landing：外部 Skill → domains patterns 进 experience_push 检索源；D-008 Human
确认知识/pattern 形态）收编为 V2 pattern。

**解决**：推送 / 强制推送 / 标记 ready / 声称"检查通过"之前，为 **outgoing diff**（本次要推出去
的变更范围）选择**最小而充分的本地证据**——不反射式跑全量套件；hook 管窄检查、CI 管穷尽覆盖；
历史重写推送必须有租约保护且重写后重新审计；相关检查失败即停，不 push 后指望 CI 不同；推送后
核对远端 ref 与本地 HEAD。

**可装配工作模式（Assembled / Conditional · D-037）**：本 pattern = 方法层知识（Searchable，
experience_push 检索源）。完整工作模式单位（剔除 pnpm/gh 死引用后的整包，可装载激活）在
`capabilities/pre_push_evidence_gate.md`——命中 trigger（push / force-push / 声称"检查通过"
之前 / 历史重写后推送 / 批处理发布后验证）时装载该单位、执行完整流程；需要边界论证、不携带
清单或与既有知识互补关系时回读本 pattern（多关系：单位主体 + 知识引用 + 触发，D-034/D-037）。

## 什么时候用 / 不用
- **用**：push / force-push 之前；历史重写（rebase / amend / 改写已发布分支）后推送之前；
  标记 ready for review 或声称"检查通过/准备就绪"之前；批处理刚发布重写分支后立即验证；
  面对"该跑哪些测试/检查"的选择（尤其有"跑一遍全量"冲动时）。
- **不用**：本地工作区文件操作安全（改前 status / 改后 diff / 恢复）——那是 `git_safety_net`；
  一批相互依赖变更的落库顺序与完成验证——那是 `dependent_change_landing`；评审"这次改动对不对"——
  那是 `code-review` / senior-engineer Review 面；写测试的 RED-GREEN-REFACTOR 纪律——
  那是 `testing-tdd`。

## 协议（AI-OS 上下文映射）
1. **先确认 outgoing 范围**——确认 checkout 与分支；base ref 必须来自**实时远端或栈状态**
   （不猜测、不自动 fetch 猜测）；用变更范围工具（类 `change-scope`）检查完整 outgoing 范围：
   **已提交路径相对 resolved merge base + 暂存/未暂存/未跟踪路径描述当前 worktree**，两类分开。
   base 被合并/变化后：重跑报告、重新评估合并后范围影响的行为、只重跑被该合并失效的检查。
2. **按行为变更面选最小充分证据**——没有超出现有 hook 的"通用本地基线"。每个行为变更都需要
   **该回归会失败的最窄测试或定向检查**；只对 diff 真正到达的表面积增加更宽检查：
   - 包/脚本行为 → owning 测试文件或聚焦测试名；共享契约变化才加相邻包测试；仓库级覆盖留给 CI
     （除非真正跨切面或用户要求）。
   - 文档/Agent Notes/目录/文档链接注释 → 文档同步检查（类 doc-sync）；工作流要求时跑全量 lint。
   - 模型/编辑器/CLI/终端可见输出 → 拥有该输出的聚焦快照或真实可运行示例。
   - 包清单/公开导出/构建配置/worker/bin 条目/构建产物路径 → 构建 + 相关 hygiene 检查 +
     owning 构建产物冒烟。
   - 真实 provider/agent 行为 → 有凭证时跑相关 e2e；**绝不打印秘密**。
   - **不因 commit/push 跟随而重复已通过的检查**；尤其不 push 前单跑 typecheck 重复 pre-push
     hook 的工作。
3. **覆盖度量纪律**——测试选择与覆盖选择是两件事：选哪些测试跑 vs 测哪些源文件的覆盖。
   涉及覆盖时**同时点名 owning 测试与源文件/包范围**：`--coverage.include` 指源范围、owning
   测试指执行范围；行为真限于单模块时用精确源文件；多文件/多包重复 include；配置的按文件 100%
   阈值仍适用。owning 测试不清楚时先用依赖图发现候选集（类 `vitest related`），**检查选中测试
   后才当证据**；依赖图发现不了配置/动态加载/子进程/worker/构建产物/外部 provider 触达的行为，
   显式选 owning 测试。**不用 `--passWithNoTests`、不降低阈值、不收窄 include 来隐藏未覆盖的
   受影响文件**——选中范围失败只因一个聚焦测试没覆盖它时，补其他相关 owning 测试，或只在被排除
   模块确实不可能受影响时收窄源范围。
4. **全量复演仅三种情况**——用户明确要求 / 诊断 CI 失败 / 变更横跨仓库到无更窄集可信。用当前
   工作流与包脚本做清单，不重建已删除的聚合检查。
5. **保护历史重写推送**——rebase 允许（独立与栈式 PR 分支、含评审后）。独立重写前：fetch 当前
   远端分支并记录**确切 OID**；用 `--force-with-lease=<branch>:<observed-oid>` 发布，让并发更新
   中止推送；**raw `--force` 永不使用**。任何重写推送后：重新 fetch live heads，重新审计
   **未解决评审线程 / 批准 / 可合并性 / 检查**——重写前的 commit 哈希与内联评论锚点不是当前证据。
6. **发布后验证例外**——某些批处理操作（类 `gh stack sync`）fetch + 级联 rebase + 发布是一步，
   无法把本地验证插在重写与发布之间：运行前要求干净 worktree、记录官方栈顺序与精确远端 heads；
   返回后①重查每个分支 head 与官方顺序 ②检查每个被重写层相对其 live PR base 的变更范围 ③对每个
   受影响层跑本 Skill 选择的证据 ④**保持每个 PR 未合并、验证作为 pending 报告直到全部通过**。
   证据失败：保留租约保护下已发布的 heads，修复、验证修复、发布修正；**不因命令成功就声称栈已就绪**。
7. **失败处理**——普通 push 前相关检查失败：**停，修复或解释阻塞**；不 push 后指望 CI 不同。
   发布后验证例外：阻塞合并并按上条修复程序。环境特定失败要**证明**：记录确切命令 / 失败测试 /
   平台特定不匹配；确认相关非平台证据；检查是必需时优先修跨平台不确定性；绕过本地 hook 仅当
   用户明确要求/同意，并精确报告什么失败、为何预期 CI 不同。
8. **推送程序与推送后核对**——①跑选定证据一次 ②正常 commit，检查 pre-commit fixer 改动的文件
   ③正常 push（或授权重写分支用确切 lease）让增量 typecheck hook 运行 ④验证远端 ref 与本地
   HEAD 一致（`git rev-parse HEAD origin/$(git branch --show-current)`）。PR 场景推送后查远端 CI
   （类 `gh pr checks`）：**pending 如实报告为 pending**；检查失败先归因再判环境。平台报
   "no checks reported" 且 head 事件 `total_count: 0`：**先读 mergeability 再怀疑推送或丢事件**——
   冲突/脏 PR 根本不会产生 pull_request 运行，缺失信号=冲突而非基础设施；**解决冲突是唯一修复**
   （空 commit / `--allow-empty` / draft-ready 反复 / revert-restore 弹跳都让 `total_count` 停在
   0 且加垃圾历史）；本地无法合时用 `git merge-tree --write-tree HEAD origin/<base>` 确认冲突路径。

## 不携带清单（repo/平台专属死引用，硬搬会注入）
`pnpm change-scope` / `pnpm run doc-sync` / `pnpm run build` / `pnpm run test:e2e` /
`pnpm exec vitest` 命令链、deepseek-harness 的 pre-commit/pre-push hook 实现（staged lint /
whitespace / vendored-source metadata / 增量仓库 typecheck）、`gh stack push/sync` 工作流、
`gh pr checks` / `/actions/runs?head_sha=` / `gh pr view` 具体查询、GitHub GraphQL 在 V2 无对应物
（V2 的 git 是本地仓库 + 文件安全网纪律，当前 `D:\AI-os` 本身无远端——本 pattern 是面向任何真实
项目的推前验证知识，未来项目有远端/CI/PR 平台时按"机制"落地，不绑定 deepseek-harness 命令）。
具体工具名只作为**机制示例**保留；**原样整体不适合独立装配**。若未来真实项目就是
deepseek-harness 类 GitHub 仓库，直接装载原文 `evolution/intake/dsh-pre-push-checks/SKILL.md`
（本 pattern 只带可迁移方法层）。

## 与既有知识的关系（互补，非重复）
- `git_safety_net`：本地 git 文件操作安全带（改前 status / 改后 diff / checkout 恢复）——覆盖
  "单仓库本地文件"维度；本 pattern 覆盖"推送前的证据选择与推送后远端核对"维度——互补不重复。
- `dependent_change_landing`：一批相互依赖变更的落库顺序与完成验证（官方机制 / 实时状态建链 /
  整链预检/落库 / 落库后验证再清理）——共享"绝不 raw --force、重写后重新拉取并重审、验证完成
  才推进"原则，但工作面不同（落库顺序 vs outgoing diff 证据选择）——互补不重复。
- `testing-tdd`：写测试的 RED-GREEN-REFACTOR 与提交前测试全绿；本 pattern 回答"这次要推的
  diff 该跑哪些既有证据"，不是如何写测试。
- `code-review` / senior-engineer Review 面：评审改动质量；本 pattern 是发布前的验证闸门，
  评审门禁（approval / checks）作为预检输入引用，不重开评审机制。

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
