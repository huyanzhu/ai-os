---
rule_id: SIMPLIFICATION-AUDIT-001
title: 证据驱动的代码简化审计（候选强度 / 消费方分类 / 信任与生命周期边界 / 证明或拒绝）
category: Code Simplification Audit
trigger:
  - "find things to simplify" / "找简化候选" / "简化这个代码库" / 减面 / 去冗余 / 删死代码
  - 重构前先做全量简化候选审计（dead / duplicated / speculative / over-built / added-then-removed / hand-rolled-where-dependency-exists）
  - 评审中发现复杂度 / 投机泛化 / 重复表示，但需要证据支撑的移除提案
  - 写内联 TODO/FIXME/XXX 简化注记
condition: 任务要求"找可简化面"并把候选变成有证据的提案（判断简化是否值得、是否有生产消费者、是否破坏已记录设计）
action:
  do:
    - 先读仓库上下文（AGENTS.md / README / 架构与约定文档）再判断；简化与已记录设计冲突时需要额外证据
    - 强候选证据驱动：无生产消费者 / 仅测试文档消费者 / 双表示镜像同一事实 / 无消费者的 seam 方法 /
      投机泛化 / 仅保护未用 API 的防御机制 / 手写轮子有维护良好的依赖或 builtin 等价 / 简化后行为仍合理且更好解释
    - 广泛 survey：并行子代理分域或自模拟广度；先看最大生产代码 delta；不停在第一个明显候选
    - 信任与生命周期边界审计：为每个防御拷贝 / 冻结 / 校验器 / 回调捕获命名"值从哪来、下一步归谁"；
      同进程借用只读 vs 解析器/队列/线数据自有权；保护同步发布+回滚 / 回调封闭 / 首终局仲裁 /
      worker-进程所有权 / dispose-to-quiescence 的机制保留
    - 依赖替换候选按同等标准证明：点名包覆盖的确切表面、残余语义计入成本、检查包健康、优先 builtin、
      先查已记录 seam、按净删除（实现+测试+文档 − 剩余胶水）衡量
    - 每个候选先分类消费者（生产语料 / 非生产语料 / 模糊语料）再判：rg 精确符号/事件名/配置键/线字符串 +
      读调用点；生产调用者 / 已记录理由 / 无关 churn / 太小→TODO 时拒绝或降级
    - 内联 TODO/FIXME/XXX：稳定标签（如 TODO(double-default)）+ 说明为何安全 revisit 与什么动作会简化；
      不写投机抱怨
    - 提案写作（V2：任务卡 proposed / 任务文件模板）：Problem（指名 API + 消费证据，区分生产/测试/文档）/
      Proposal（精确移除面 + 测试/文档/索引清理）/ Why not keep it 或 What we give up / Acceptance criteria /
      Risks
    - 记录收编（V2：knowledge-space-maintenance Lifecycle facet——D-022 已承载 supersession 审计）：
      added-then-removed 完整替代判据——生产代码/配置/schema/线格式/迁移/兼容/文档/测试均无该特性且无文档
      宣称可用时，删除记录拥有历史（保留存在原因/动机为何不再成立/替代方案/让渡能力/重入条件/移除完整证据）；
      仅一个运输/默认/实现/展示形态的移除、持久数据或兼容处理存活、移除记录证据不足时拒绝归并
    - 汇报卫生：新增/合并/保留/删除数、survey 范围、显式排除、实际跑过的检查；不声称没跑过的门禁
  dont:
    - 不把"看起来复杂"当候选——没有调用点证据
    - 不删除被记录理由保护的设计（已实现提案 / 硬赢防御模式），除非新证据击败该理由
    - 不因"无人用"就清 Unused（Unused ≠ Dead；Exposure 正常无消费不是故障）
    - 不把仅测试/演示/支持代码打包当作低风险清除而不查其是否承重
    - 不为简化引入依赖包装同一复杂度（净删除才是胜利）
    - 不把每个简化 survey 扩成全库记录审计
keywords:
  - 简化
  - simplification
  - 重构
  - refactor
  - 减面
  - surface reduction
  - dead code
  - 死代码
  - 冗余
  - duplicated
  - 投机泛化
  - speculative generality
  - over-built
  - 手写轮子
  - hand-rolled
  - 依赖替换
  - dependency swap
  - unused
  - 消费方分类
  - consumer classification
  - TODO
  - FIXME
  - XXX
alias:
  - dsh-find-simplifications
  - 简化审计
  - simplification audit
  - 找简化候选
  - 减面审计
knowledge_position: Cluster
knowledge_cluster: FC-Simplification Audit
epistemology_tag: PROCEDURE
confidence: HIGH
---

# 证据驱动的代码简化审计（候选强度 / 消费方分类 / 信任与生命周期边界 / 证明或拒绝）

**来源**：外部 Skill（Human 提供，Evolution Intake #8 / DSH Corpus #4）——deepseek-ai/deepseek-harness
的 `dsh-find-simplifications` SKILL.md（2026-08-24 HTTP 200 逐字下载，原文存
`evolution/intake/dsh-find-simplifications/SKILL.md`）。按 Skill Fusion 先例（D-004 debug-protocol /
D-023 doc_site_projection / D-024 doc_standards：外部 Skill → domains patterns 进 experience_push
检索源；D-008 Human 确认知识/pattern 形态）收编为 V2 pattern。

**解决**：把宽泛的"找简化"请求变成有证据的简化提案——移除 / 折叠 / 降级真实的既有表面积，而不是堆一摞
薄猜测。核心纪律：**强候选必须证据驱动；先读上下文再判断；广泛 survey 不停在第一个候选；信任与生命周期
边界（谁拥有值、下一步归谁）决定防御机制去留；每个候选先分类消费者再证明或拒绝；太小走内联 TODO，
值得决定才写提案。**

## 什么时候用 / 不用
- **用**：收到 "find things to simplify" / "找简化候选" / "简化这个代码库" / "减面 / 去冗余 / 删死代码"；
  重构前做简化候选审计；评审中遇到复杂度 / 投机泛化 / 重复表示但需要证据支撑的移除提案；写内联
  TODO/FIXME/XXX 简化注记。
- **不用**：评审 PR/代码质量并输出分级问题——那是 `code-review`（五轴）+ senior-engineer Review 面
  （深度纪律）；实现 / 改进建议（数据访问 / 错误处理 / 测试性）——那是 senior-engineer Coding 面；
  对知识语料做生命周期 / 归档裁决——那是 knowledge-space-maintenance（本 pattern 只在涉及"记录收编"
  时交叉引用）；TDD 的 REFACTOR 步骤——那是 `testing-tdd`。

## 协议（AI-OS 上下文映射）
1. **先读仓库上下文再判断**——读 AGENTS.md / README 与相关约定、架构、测试文档；简化与已记录设计
   （已实现提案 / 硬赢防御模式 / 既有 seam）冲突时需要**额外证据**击败记录理由。受保护 seam 内部的
   未用方法/钩子仍可合法移除，只要不折叠受保护设计本身。
2. **强候选判据（证据驱动）**——移除 / 折叠 / 降级某个真实的东西，且有清晰证据证明"当前设计成本 > 收益"：
   - 公共方法 / 事件 / 配置旋钮 / 注册通知 / helper / 包 / 持久事件 / 测试工件**无生产消费者**；
   - 只有测试或文档是消费者，且它们钉住的行为不承重；
   - **双表示镜像同一事实**（尤其是持久会话事件与瞬态 agent 事件各存一份）；
   - seam 存在每个实现都必须支持、却无消费者使用的方法；
   - 独立包仅为测试/演示/支持代码而存在，徒增发布或依赖开销；
   - **投机泛化**：多会话/会话加载、后台任务名册、live 注册失效、回合中转向、工具自有 UI 渲染等
     无产品归属的通用性设计；
   - 不变式 / 回滚路径 / 预期输出集 / 特例测试仅用于保护一个未用 API；
   - **手写轮子**重造了维护良好的外部包或引擎 floor builtin 已提供的能力，且替换会删掉实现 + 专属测试；
   - 简化后行为可能略有不同，但新行为仍合理且**更容易解释**。
   薄候选（删一个 typo、跑一次 knip、"这里看起来复杂"）通常不足以成为提案。
3. **广泛 survey**——需要广度时并行子代理分域，每个子代理要证据不要猜测；若子代理不可用，自己模拟
   同样广度。**先看最大生产代码 delta**——只扫明显未用符号会漏掉重复生命周期 / 防御机制占大头的文件。
4. **信任与生命周期边界审计**——对每个防御拷贝 / 冻结 / 校验器 / 回调捕获，命名"值从哪来、谁拥有下一步"：
   同进程类型化服务/插件调用通常借用只读值；解析器、配置加载器、队列、模型/工具 JSON、持久文件、
   worker、进程、线解码器**拥有或校验**自己的数据。围绕敌意 getter / 假 typed 对象 / 回调替换 /
   同进程交接后变更的测试，是潜在投机契约的证据，不是自动保留理由。复杂异步代码画所有权图：每个
   sentinel / readiness promise / 取消路径 / disposer / 状态旗标映射到唯一 owner 或转移；多个机制镜像
   同一 liveness / settlement 事实时，提议一个事务或生命周期控制器。**保留**保护同步发布+回滚、回调封闭、
   首终局仲裁、worker/进程所有权、dispose-to-quiescence 的独立机制。
5. **手写轮子 vs 依赖**——引入依赖是合法的简化动作，不是政策例外：问协议解析器、framing、重试/退避、
   glob 匹配、diff 引擎等基础设施——"维护良好的 npm 包或引擎 floor builtin 是否已做这个？" 证明依赖替换
   与任何候选同等严格：读手写实现并点名包覆盖的**确切表面**；包不覆盖的残余语义计入反对；诚实检查包健康
   （维护 / 采用 / 传递足迹），引擎 floor 有 builtin 时优先 builtin；先查已记录 seam（已裁决的机制是定案，
   推翻需击败记录理由）；按**净删除**衡量——实现 + 专属测试 + 文档 − 剩余胶水；只是把同一复杂度搬进
   wrapper 不是胜利。
6. **证明或拒绝每个候选**——先分类消费者再判断：生产语料（src / 运行时脚本 / 加载器配置路径）、
   非生产语料（测试 / README / 文档 / 快照 / 生成预期输出 / 注释）、模糊语料（examples/scripts 可能是
   产品冒烟路径——先用后判）。**rg 先行**：精确符号、事件名、包名、配置键、`.name(` 与 `name(` 两种
   写法、线字符串；然后读调用点。拒绝或降级：存在生产调用者且简化会是功能决策而非清理；API 被已实现
   提案或硬赢防御模式显式合理化且新证据未击败它；移除会迫使无关 churn 而不真正缩小公共 API / 必需行为；
   想法正确但太小 → 内联 TODO/FIXME/XXX。
7. **内联 TODO/FIXME/XXX 纪律**——只用于小而清晰、明显有用但**不是持久设计决策**的本地清理：命名
   smell 用稳定标签（`TODO(double-default)` / `XXX(unused-default)`）；解释为何安全 revisit 与什么动作
   会简化它；不为投机抱怨或需要提案级决策的行为添加 TODO。
8. **提案写作（V2 映射）**——每个持久提案写一份文件：V2 对应 `task_cards/` proposed 卡或
   `任务文件模板_v1.3.md` 形态；结构：`Problem`（指名当前 API、引用相关文件、消费证据——生产调用者与
   测试/文档分开）、`Proposal`（精确移除/折叠/降级/搬家的内容，含测试、文档、README、JSDoc、事件分类、
   快照、生成文件清理）、`Why not keep it` 或 `What we give up`（让最强反方意见可读）、`Acceptance
   criteria`（可观察终态与门禁）、`Risks`（公共 API / 行为变化 / 未来产品 Want，以及为何权衡仍合理）。
   具体到实现 PR 能跟的粒度；不写"简化这个包"式的模糊提案；与既有提案重叠时把有用细节并入既有者，
   不建重复。
9. **记录收编（coalescing，V2 映射）**——当用户要求收编/减少记录，或实现的简化使持有记录过时时才做
   全库审计；**不把每个简化 survey 扩成记录审计**。V2 的保留/归档/删除裁决由 knowledge-space-maintenance
   Lifecycle / Archive facet 承担（已融合 dsh-archive-agent-notes · D-022）。本 skill 补充两条
   added-then-removed 判据：**完整替代**——特性在生产代码/配置/schema/线或持久格式/迁移/兼容行为全部
   缺席、无文档宣称可用、无测试把它当受支持行为时，删除记录拥有历史（存在原因、动机为何不再成立、
   替代方案、让渡能力、重入条件、移除完整证据）；**拒绝归并**——移除只是某一运输/默认/实现/展示形态、
   持久数据或兼容处理存活、或移除记录证据不足（防意外重新引入的 rationale 未到位）时。
10. **汇报卫生**——汇报：新增 / 合并 / 保留为部分替代 / 删除的提案数与内联注记数；survey 的主域；
    显式排除项；实际跑过的检查（V2：git diff --check / 项目自身验证器）；不声称没跑过的门禁。合并组
    逐个点名旧 owner 与新 owner、完整替代证据、删除为何安全；added-then-removed 扫描无合格记录时如实
    报告该结果与保留的代表性部分案例。

## 不携带清单（repo 专属死引用，硬搬会注入）
deepseek-harness 的 `.agents/notes/<lifecycle>/<class>/yyyy-mm-dd-topic.md` 树 + `notes/README.md` 规则
（含 Agent Note 生命周期 / `Status: proposed` 契约、implemented 例子引用）、`dsh-archive-agent-notes`
子 skill 的 triplet 归档机制（V2 已由 knowledge-space-maintenance Lifecycle facet 承接裁决语义）、
`pnpm run doc-sync` / `lint` / `git diff --check` 的具体命令链与 pre-push hook（V2 无对应 CI 门禁，
只保留"实际跑过才汇报"原则）、PR folding 工作流（sibling branch vs origin/master 对比、PR body 更新、
draft → ready）与 knip 特指（V2 无 npm 工程约定；保留"rg 精确符号 + 读调用点"原则）在 V2 无对应物；
**原样整体不适合独立装配**。若未来真实项目本身就是 deepseek-harness 类仓库，直接装载原文
`evolution/intake/dsh-find-simplifications/SKILL.md`（本 pattern 只带可迁移方法层）。

## 与既有知识的关系（互补，非重复）
- `code-review`（五轴分级机制）+ senior-engineer Review 面（深度纪律：证据优先 / 阻塞闸门 / 深度检查）：
  评审回答"这次改动对不对 / 好不好"；本 pattern 回答"哪些既有面值得移除 / 折叠"，产出是提案不是分级报告
  ——评审中遇到的复杂度观察可以借用本 pattern 的证据纪律升级为移除提案。
- senior-engineer Coding 面（实现 / 改进建议：数据访问 / 错误处理 / 测试性）：是"怎么改得更好"的实现侧；
  本 pattern 是"哪些可以删 / 减"的审计侧——互补。
- `knowledge-space-maintenance` Lifecycle / Archive facet（D-022 融合 dsh-archive-agent-notes）：
  记录保留/归档/删除的**执行者**；本 pattern 只补充 added-then-removed 完整替代/拒绝归并两条判据，
  不重开 facet、不抢裁决。
- `testing-tdd` 的 REFACTOR 步骤：是"保持绿下清理"的局部实践；本 pattern 是"全库找简化候选"的审计工作流。
- 同族 DSH Skill（dsh-prose-standard / dsh-translate-docs / dsh-trim-cot-leakage /
  dsh-archive-agent-notes / dsh-pre-push-checks / dsh-code-review）是既有/后续独立 intake，与本 pattern
  的成长关系已在各自裁决中记录，不在此重开。

## 检查清单（简化审计任务中自测）
- [ ] 先读了仓库上下文（AGENTS / README / 架构与约定）再判断？
- [ ] 每个候选都有消费证据（rg 精确符号 + 调用点）而不是"看起来复杂"？
- [ ] 生产调用者 / 已记录理由 / 无关 churn 的拒绝理由都写了吗？
- [ ] 双表示、投机泛化、仅测试消费、手写轮子这些面都覆盖了吗；survey 停了第一个候选吗？
- [ ] 防御机制审计命名了"值从哪来、下一步归谁"；保护性机制（发布+回滚 / 回调封闭 / 仲裁 / 所有权 /
      quiescence）保留了吗？
- [ ] 依赖替换按净删除衡量、包健康与残余语义都查了吗？
- [ ] 小清理走的是带稳定标签的内联 TODO，而不是提案文件？
- [ ] 提案有 Problem / Proposal / Why not 或 What we give up / Acceptance / Risks 吗？
- [ ] 记录收编（如涉及）走了 knowledge-space-maintenance Lifecycle facet 判据，没有把简化 survey
      扩成全库审计？
- [ ] 汇报列了新增/合并/保留/删除数、survey 范围、显式排除与实际跑过的检查？

## 可装配工作模式（Assembled / Conditional · D-042）

完整工作模式单位（剔除 .agents/notes 树 / pnpm 验证器与 pre-push hook / PR folding / knip
死引用后的整包，可装载激活）在 `capabilities/simplification_audit.md`——命中 trigger
（"find things to simplify" / "找简化候选" / "简化这个代码库" / 减面 / 去冗余 / 删死代码、
重构前全量简化候选审计、评审中需证据支撑的移除提案、审计/归并已被取代的记录、折叠另一分支的
简化想法、写内联 TODO/FIXME/XXX）时装载该单位、执行完整流程（先读仓库上下文 → 强候选判据 →
广泛 survey → 信任与生命周期边界审计 → 依赖替换净删除衡量 → 证明或拒绝每个候选 → 记录收编 →
提案写作 → 内联 TODO 纪律 → 验证汇报）；需要边界论证、不携带清单或与既有知识互补关系时回读
本 pattern（多关系：单位主体 + 知识引用 + 触发，D-034/D-042）。本 pattern 仍为方法层
Reference（Searchable，experience_push 检索源）。
