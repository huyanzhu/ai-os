---
rule_id: DEPENDENT-CHANGE-LANDING-001
title: 依赖变更落库（官方机制优先 / 依赖链以实时状态为准 / 整链预检与整链落库 / 落库后验证再清理）
category: Dependent Change Landing
trigger:
  - 落地一批相互依赖的变更（PR 栈 / 依赖 PR / 顺序合并 / 一批必须按序落地的改动）
  - 合并一个 base 是另一个在途变更分支的变更
  - 收到 "stacked PRs" / "PR stack" / "dependent PRs" / "依赖 PR" / "PR 栈" / "按序合并多个关联改动"
  - 在"用官方批量机制落库"与"逐项手工合并/重定向"之间做选择
  - 落库前/后需要确认一批变更的依赖顺序、完成状态或可清理性
condition: 有多个依赖关系真实存在的变更需要落地（每个变更的 base 是另一个在途变更），而不是单个独立变更
action:
  do:
    - 先确认官方原生机制可用（运行其版本/支持探测），不可用则硬停并报告，不手工逐项模拟官方语义
    - 用实时状态（实际 base/head OID、状态、作者、草稿/评审/检查）建立依赖链，不信任分支名或旧报告
    - 链外成员按作者一致性自动补链（自底向上顺序）；作者不一致/顺序冲突/多栈/意外成员需用户裁决后再动
    - 补链或任何历史重写后，重新拉取精确 head 并重新审计评审线程/批准/可合并性/检查
    - 只在实时状态或仓库规则要求时刷新（官方级联 rebase 或增量 merge-forward 二选一），不为了"有刷新机制"而刷新
    - 落库前对整链预检：每个被选变更都 open、非 draft、顺序正确、满足评审与检查要求；就绪的顶层不代表依赖层就绪
    - 通过官方批量 API 整链（或显式边界前缀）落库，不做逐项合并/手工重定向；直接落库是 all-or-nothing
    - 等待每个被选变更报告真正完成（queued ≠ 完成），部分落库后复查剩余链仍成官方栈且顺序正确
    - 分支清理单独作为最后一步，且每个分支在其 PR 完成且无 open 变更仍以它为 base 之后才删
  dont:
    - 不手工逐项合并 + 逐个 retarget 来复刻栈语义（官方原生对象拥有顺序/CI/重定向/合并状态）
    - 不用分支名或旧报告代替精确 head OID / 实时状态
    - 不自动解散/重排/重建既有官方栈；link 只做加性补链，已入队条目不可出栈
    - 不使用 raw --force 或覆盖并发推进的远端 head
    - 不在合并被官方机制阻塞时回退到逐项 `merge`
    - 不在 PR 未完成/仍有依赖它的 open 变更时删分支
keywords:
  - 依赖变更
  - dependent changes
  - 落库
  - landing
  - PR 栈
  - stacked PRs
  - PR stack
  - 依赖 PR
  - dependent PRs
  - 顺序合并
  - merge in sequence
  - 官方机制
  - native mechanism
  - all-or-nothing
  - 整链
  - chain
  - 自底向上
  - bottom-to-top
  - 重定向
  - retarget
  - 合并
  - merge
alias:
  - dsh-merging-stacked-prs
  - stacked PR merge
  - PR 栈合并
  - 依赖 PR 合并
  - 顺序落地多个关联改动
knowledge_position: Cluster
knowledge_cluster: FC-Dependent Change Landing
epistemology_tag: PROCEDURE
confidence: HIGH
---

# 依赖变更落库（官方机制优先 / 依赖链以实时状态为准 / 整链预检与整链落库 / 落库后验证再清理）

**来源**：外部 Skill（Human 提供，Evolution Intake #9 / DSH Corpus #6）——deepseek-ai/deepseek-harness
的 `dsh-merging-stacked-prs` SKILL.md（2026-08-24 HTTP 200 逐字下载，原文存
`evolution/intake/dsh-merging-stacked-prs/SKILL.md`）。按 Skill Fusion 先例（D-004 debug-protocol /
D-023 doc_site_projection / D-024 doc_standards / D-025 simplification_audit：外部 Skill →
domains patterns 进 experience_push 检索源；D-008 Human 确认知识/pattern 形态）收编为 V2 pattern。

**解决**：一批相互依赖的变更（每个的 base 是另一个在途变更）需要落地时，用**官方原生机制**拥有栈级
语义（顺序 / CI / 重定向 / 合并状态），而不是靠手工逐项合并 + 逐个 retarget 复刻。核心纪律：
**依赖链以实时状态为准，不信任分支名或旧报告；整链预检、整链落库（all-or-nothing）；落库后验证
完成状态再清理；官方机制不可用时硬停，不手工模拟。**

## 什么时候用 / 不用
- **用**：合并一批依赖变更（PR 栈 / 依赖 PR / 顺序合并）；合并一个 base 是另一个在途变更分支的变更；
  收到 "stacked PRs / PR stack / dependent PRs / 依赖 PR / PR 栈 / 按序合并多个关联改动"；
  在"官方批量机制 vs 逐项手工合并"之间做选择；落库前后核对依赖顺序 / 完成状态 / 可清理性。
- **不用**：单个独立变更的普通合并（无依赖链）——那是常规 git 工作流；本地文件安全网/回滚——
  那是 `git_safety_net`；评审一批 PR 的代码质量——那是 `code-review` / senior-engineer Review 面。

## 协议（AI-OS 上下文映射）
1. **官方机制优先，不可用即硬停**——先探测平台的原生栈/批量合并能力（`gh stack --version` 类探测；
  V2 对应：任何官方 API/CLI/合并队列）。官方栈要求全部 head 分支在同一仓库，跨 fork 链硬停。
  官方机制不可用时**硬停并报告**，不手工逐项合并 + 逐个 retarget 复刻栈语义（顺序 / CI / 重定向 /
  合并状态由官方对象拥有，复刻必失真）。
2. **依赖链以实时状态为准**——用干净专用 worktree；重新拉取每个变更的精确元数据
  （number / author / baseRef / baseOid / headRef / headOid / cross-repo / state / draft /
  review / mergeState / checks），不用分支名或旧报告。查询官方栈对象及其成员位置（GraphQL
  `PullRequest.stack` + `stackEntry.position`），**官方对象是栈成员归属的权威**，不是 base 推断。
  按实时 base 自底向上建立期望顺序：最底变更指向主干，每个上层变更指向其下一层 head。
3. **补链有纪律**——对比既有栈条目与期望链：一个既有栈可能含请求链的有序子集；多个栈号 /
  意外成员 / 冲突顺序 → **用户裁决后再动**。缺链成员时：逐项精确比较作者；全部作者一致才自动
  自底向上补链（`gh stack link --base <trunk> <bottom> <next> ... <top>`）；作者不一致或作者不可用
   → 先问用户。补链后重新查询并要求：一个栈号 / 期望主干 / 完整变更集 / 期望位置与 base 链。
   **不自动解散、重排、重建既有栈**；link 只做加性补链；已合并或已入队的条目不可出栈。
4. **只在需要时刷新**——不因为"有刷新机制"就重写分支。当实时合并状态或仓库规则要求更新主干时，
  二选一：**官方级联 rebase**（检出远端栈 → sync；会级联 rebase 与租约保护 force-push，之后立即
  检查每层重写范围、跑相关检查、不通过不合并）或**增量 merge-forward**（主干先并入最底受影响分支，
  再自底向上把每个更新后的父分支并入其子分支，正常 push）。任何历史重写都会使 OID 假设失效：
  重新拉取精确 head，重新审计未解决评审线程 / 批准 / 可合并性 / 检查。**绝不用 raw `--force`，
  绝不覆盖并发推进的远端 head**；sync 报分歧（本地/远端栈组成不一致）→ 取消并询问，不自动删除重建。
5. **整链预检**——落库前重新查询官方栈。要求每个被选变更：open、非 draft、顺序正确、满足仓库评审与
  检查要求。**每个变更独立判定**——顶层就绪不代表依赖层就绪。"land the stack" = 整链；
  部分落库 = 显式边界变更，且包含从底部到该边界的所有层。
6. **官方 API 整链落库**——按官方栈号整链合并（`gh stack merge <stack> --yes --merge`）或按显式
  边界变更部分合并；**不传删分支标志、不手工重定向依赖、不逐项发合并命令**。官方按自底向上合并所选
  范围并重定向/重排剩余上层。直接栈合并是 all-or-nothing；合并队列下官方会整链入队但可能分组合并。
   **不绕过合并要求**：官方报阻塞 → 通过所属变更解决该阻塞或停止并报告；**永不回退到逐项 merge**。
7. **落库后验证再清理**——等待每个被选变更报告**真正完成**（queued ≠ 完成）。部分落库时重新查询官方栈，
  验证剩余变更仍按期望顺序成链、指向栈主干或下一层；重新检查 head / 评审状态 / CI（官方可能已 rebase
  剩余层）。分支删除**单独作为最后一步**，且每个分支在其对应变更完成且平台报告**无 open 变更仍以它为
  base**（`gh pr list --state open --base <branch>` 长度 0）之后才删；非 0 即阻塞删除。

## 不携带清单（repo/平台专属死引用，硬搬会注入）
`gh stack` / `gh pr merge` / `gh pr edit` 具体命令、GitHub GraphQL `PullRequest.stack` /
`stackEntry.position` 查询、`gh stack checkout/sync/rebase/push/link` 工作流、GitHub 官方
stacked-PR 扩展与 server-side stack 特性、PR draft/merge-queue 语义在 V2 无对应物（V2 的 git 是
本地仓库 + 既有文件安全网纪律，无 GitHub PR 运行时）；具体工具名只作为**机制探测示例**保留，
不绑定任何平台；**原样整体不适合独立装配**。若未来真实项目就是 deepseek-harness 类 GitHub 仓库，
直接装载原文 `evolution/intake/dsh-merging-stacked-prs/SKILL.md`（本 pattern 只带可迁移方法层）。

## 与既有知识的关系（互补，非重复）
- `git_safety_net`：本地 git 文件操作安全带（改前 status / 改后 diff / checkout 恢复）——覆盖
  "单仓库本地文件"维度；本 pattern 覆盖"一批相互依赖变更的落库顺序与完成验证"维度——互补不重复。
- `code-review` / senior-engineer Review 面：评审"这次改动对不对 / 好不好"；本 pattern 回答
  "这批依赖变更怎么落地"——评审门禁（approval / checks）被本 pattern 作为**预检输入**引用，
  不重开评审机制。
- `plan-before-code` / `small-steps`：单任务/单变更粒度纪律；本 pattern 处理的是"多个变更已存在、
  必须按依赖顺序落地"的**合并/落地阶段**，不是开发阶段的步骤划分。

## 检查清单（依赖变更落库任务中自测）
- [ ] 先探测了官方原生栈/批量合并机制可用；不可用时硬停并报告，没有手工逐项模拟？
- [ ] 依赖链来自实时精确元数据（base/head OID + 状态 + 作者 + 评审/检查），不是分支名或旧报告？
- [ ] 官方栈对象确认了一个栈号 / 期望主干 / 完整成员 / 期望顺序；补链只做了同作者自底向上加性操作？
- [ ] 任何历史重写（级联 rebase / merge-forward）后重新拉取 head 并重审了评审线程/批准/检查？
- [ ] 落库前整链预检：每个被选变更独立满足 open / 非 draft / 顺序 / 评审与检查要求？
- [ ] 通过官方批量 API 整链（或显式边界前缀）落库，没有逐项合并/手工 retarget/删分支标志？
- [ ] 每个被选变更都报告真正完成（queued ≠ 完成）；部分落库后剩余链仍成官方栈且顺序正确？
- [ ] 分支删除在完成验证 + 零依赖该分支的 open 变更之后单独进行？

## 相关对象（2026-08-24 Re-Mapping 物化 · D-035）

- pre_push_evidence_gate（共享 force 禁令 / 重写后重审原则，双向）；git_safety_net / code-review / plan-before-code / small-steps（既有）
