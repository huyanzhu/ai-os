# Evolution Decision Log — 裁决记录（append-only）

> 用途：记录**为什么**这个 Capability 被这样处理，让后续 Evolution Instance 继承前一次演化判断。
> 规则：只追加，不修改历史；每条含原因与证据锚点；UNKNOWN 诚实标注。
> 建立：2026-08-23（Evolution V0.1）。

---

## D-001 · A18 experience_push（2026-08-22）

- 处理：内部 reshape —— R1 alias 入打分（P0）/ R2 任务卡递归入索引（P0）/ R3 意图源替代死钩子（P1）/ R4 SUCCESS_LOG 送达样板（P1）/ R5 稀有度加权或 FTS5（P2）
- 不找外部 Skill：无证据表明外部检索库能改变 #1–#6（当时语料无内容，语料成熟后机制自愈）
- 证据：evolution/a18-relevance-diagnosis-2026-08-22.md §3
- 状态：待执行（R1/R2 待 Human 裁决）

## D-003 · NC-001（2026-08-22）

- 处理：保持 Evolution Tool / Evidence Primitive 候选；不重命名 Capability，不扩功能，不塞进 workflow
- 原因：可用 ✅；被 Evolution 使用 1 次；自然复用 UNKNOWN——两次真实 Evolution 任务均无 Cost/Time/Trace 需求触发它
- 状态：待真实"需要 Cost/Time/Trace 证据"的演化任务出现时，再观察 Evolution Instance 是否自然使用
- 证据：evolution/new-capabilities.md；evolution_p2_a18 与 evolution_intake_role_defs 两次 Trace（均未调用 observe_extract）

## D-004 · debug-protocol 外部 Skill（2026-08-23）

- 处理：独立融合 —— 外部 Skill → `domains/ai-os/patterns/debug_protocol.md`（Skill Fusion 先例：2026-08-05 九个外部 Skill 转 domains patterns 进 experience_push 检索源）；登记 `domains/index.md`；不新建工具/机制，不改 README/ONBOARD/TOOL_RUNTIME 入口
- 原因：复现优先 → 单假说证伪 → 证据报告是既有调试族未覆盖的方法层（debug_reconciliation=数据层对账技巧、testing-tdd=修复侧回归、closure_verify 等=验证侧）；外部原文的 tdd-loop 在 V2 无运行时，映射为 testing-tdd Prove-It
- 证据：experience_push 三组真实调试语义查询均置顶命中（27.0 / 27.0 / 31.0 分，含内容摘要送达）；intake README（HTTP 200 逐字下载）
- 状态：已送达（可消费位置）；真实 Work Instance 消费（Q1–Q5）待自然调试任务触发——UNKNOWN 显式标注，不预先宣称已帮助

## D-005 · Capability/Skill 形态三态 + Assembled 通道（2026-08-23）

- 处理：确立三形态判定——知识（检索）/ 能力工具（调用）/ 角色整包（装载 Assembled/Loaded）；外部 Skill 默认先保持完整，不拆解；角色整包类注册进 `capabilities/` 空间，走任务开始时的"能力检索/装配"步骤
- 原因：连续两次 intake 都默认把 Skill 拆成 domains pattern——根因是环境只有知识通道 + Skill Fusion 唯一先例 + 无整包装载路径 + "可消费=可检索"隐含假设（INT-001 / D-004 前因；role-definitions 为反例，已回退）
- 建设（最小）：capabilities/ 空间 + AGENTS.md bootstrap 增加能力检索步骤 + capability-reconstitution 增加形态判定；暂不建 persona runtime、不建评分引擎（等真实单位与摩擦）
- 状态：Evolution V0.2 起点；首个整包单位待 persona intake 注册验证

## D-006 · senior-engineer 外部 Persona Skill（2026-08-23）

- 处理：独立注册 —— 角色整包 → `capabilities/senior-engineer.md`（保持完整，不拆 domains）；注册 `capabilities/INDEX.md` 首行（完成 D-005 预留的"首个整包单位"验证）；V2 引用映射（review-code → code-review pattern / review-security → security-check pattern / review-plan → 外部同插件 skill 无 V2 运行时 → 按原文"计划文本/路径显式传入即权威"执行 / improve-architecture → 无等价、不新建）；不新建工具/机制，不改 README/ONBOARD/TOOL_RUNTIME 入口
- 原因：senior-engineer 是角色定义/工作模式/输出格式的整包单位，命中 D-005 角色整包形态（capabilities/README 原文举例即"Senior Engineer persona"）；拆进 domains 会丢失角色装配语义——与 debug-protocol（方法层、Skill Fusion 拆解）形态不同
- 证据：capabilities/INDEX.md；capabilities/senior-engineer.md；AGENTS.md Bootstrap（能力检索步骤）；intake README（HTTP 200 逐字下载）
- 状态：已注册（可装配位置）；真实 Work Instance 消费（Q1–Q5）待自然评审任务触发——UNKNOWN 显式标注，不预先宣称已帮助

## D-007 · senior-engineer Work 首消费样本（2026-08-23）

- 处理：Work-side Capability Consumption 首样本——LinkVault 代码质量评审任务（纯评审指令，未点名能力）中，Work Instance 经 AGENTS.md bootstrap 能力检索（capabilities/INDEX.md）自然发现 senior-engineer → 判定 trigger 匹配 → 装载全文 → 激活工作模式 → 按 persona 输出结构完成评审（TASK-20260823-003 / Entry #17）
- 结果：Influence observed（40：输出结构 Verdict/Critical/Worth considering/Long-term/What to change + "先研究后判断/分级不都改"纪律）；技术结论来自代码阅读 + 复跑测试 + 探针实测，能力未替 Agent 思考——**反向验证**：评审抓到 Phase 5 benchmark 误测（21x 两轮同 URL），系 Agent 自己的对照实验发现
- Exposure 定级：Task-driven Searchable → Assembled / Activated；**不提升 Global**（由未来使用频率/范围/成本决定）
- 状态：Directionally Supported（单样本）；Value pending repetition；**不制造第二样本**，等自然 PR / 架构 / 高风险变更评审任务出现再验证 persistence
- 证据：workspaces/linkvault/REVIEW_REPORT.md；AI-OS_SUCCESS_LOG Entry #17；work_review_linkvault 会话 Trace

## D-008 · Human 裁决记录（2026-08-23）

- debug-protocol：**不注册** capabilities/ 装配单位（Human：它是角色定义 skill 的一个功能；角色整包已有 senior-engineer 承载）——维持知识/pattern 形态（D-004）
- capability-reconstitution 升级为 Evolution 核心工作 Skill：**暂缓**（Human：多跑跑再说）
- A18 reshape：R1/R2 **暂缓执行**（Human：慢慢来；若要改则倾向大改）；大改方向 = 统一任务开始检索（任务卡/知识/能力/账本 + 每个候选标注来源与消费方式），待方向确认后立项（INT-001 待更新）

## D-009 · Growth Architecture 冻结（2026-08-23）

- 冻结模型（三个正交维度）：
  - Object Semantics：Knowledge / Evidence / Capability / Skill / Facet / Tool / Memory —— 回答"这是什么"
  - Exposure / Activation：Global / Callable / Searchable / Conditional / Assembled —— 回答"Agent 怎么得到/激活它"（使用方式，非对象类型）
  - Growth / Relationship：New / Reuse / Attach / Extend / Specialize / Consolidate / Merge / Promote / Migrate / Retire —— 回答"它与已有对象怎么发展"（Fusion 只是其中一种操作）
- 最高纪律：
  1. Skill 默认保持完整，不默认拆解
  2. Exposure 与 Growth 正交
  3. Consolidation 横切所有对象与所有 Exposure Mode
  4. 默认局部；重复的独立需求才产生 Shared Candidate（Once/Twice 为启发式，非机械规则）
  5. 先判断对象关系，再决定 Exposure
  6. 不为验证制造 Work
- 实现范围（最小）：统一任务开始检索（tools/task_start.py：任务卡=恢复/继续、知识=读/采纳、能力=使用/装配、Skill=装载/激活，来源标注 + 不同消费语义）+ evolution/growth.md（成长裁决承载，不自动化融合）
- 状态：概念讨论收敛，进入实现；实现后以"与现有能力有重叠的新 Skill"做第一轮 Growth Intake 验证（不预设落点，由新架构判定）

## D-010 · Facet 模型冻结 + senior-engineer Facet-ization（2026-08-23）

- 冻结 7 条 Facet 规则：
  1. Facet 是 Role 内的独立工作面，不是章节
  2. Skill 保持完整，不因 Facet 存在而拆包
  3. Facet 边界由"独立工作语义 + 外部能力关系"共同决定（外部能力市场是验证来源，非结构驱动）
  4. 一次需求默认 Facet-local
  5. 第二个独立角色稳定需要时 → Shared Capability Candidate；继续跨角色稳定复用 → Shared Capability
  6. 融合后保留原始 Skill provenance（Runtime consolidation + Source preservation），不让重复对象污染 Runtime
  7. Exposure / Activation 与 Facet / Growth 是不同维度
- 开放点拍板：Communication = 跨面材料（不单列，除非真实 Communication/Writing 类能力出现融合需求）；Review 与 Architecture 分开（工作对象/判断维度/失败代价不同，未来外部 skill 跨面组合时再看）；融合 ≠ 删除来源（原文件进 evolution/ 来源区，目录待定）
- senior-engineer Facet 结构：Review / Architecture / Coding / Debugging（facets 清单 + ## Facets 节，正文六节不动；lens/approach/cares/output format/communication 为跨面材料）
- 下一步：以 Review 类外部 Skill 做 Growth Intake，验证 Facet Fusion

## D-011 · dsh-code-review 外部 Review Skill（2026-08-23）

- 处理：**Facet Fusion** —— 外部 Review Skill（deepseek-ai/deepseek-harness 的 dsh-code-review，PR review
  guidance）的**可迁移方法层**融合进 senior-engineer 的 Review Facet（`capabilities/senior-engineer.md`
  新增 "Review 方法层" 子节：证据优先 / 阻塞闸门 5 条 / 深度手动检查 15 项 / 汇报纪律）；**repo 专属部分
  不携带**（来源链 / `pnpm change-scope` / registrations disposal / `./invariant` / Agent Notes /
  translation rules 等在 V2 无对应物，硬搬注入死引用——原样整体裁决为不适合独立装配）；原文保留在
  `evolution/intake/dsh-code-review/`（Source preservation，D-010 规则 6）
- 原因：D-010 既定下一步 = "以 Review 类外部 Skill 做 Growth Intake，验证 Facet Fusion"；dsh-code-review
  正是 Review 类外部 Skill，其方法层与 senior-engineer Review 面同工作面（独立工作语义 = 评审 PR/代码/计划），
  与 code-review pattern（五轴分级机制）互补不重复——机制在 domains、深度纪律在 Facet，不双写；
  不独立注册 capabilities/ 装配单位（D-008 先例：角色 skill 的功能由 senior-engineer 承载，不另立单位）；
  不拆 domains pattern（方法层归 Facet，避免重复对象污染 Runtime）
- 证据：capabilities/senior-engineer.md（Review Facet 方法层子节）；evolution/growth.md（dsh-code-review
  行 + senior-engineer Review 面裁决更新）；intake README（HTTP 200 逐字下载）；INT-004
- 状态：已送达（Facet 融合完成；消费通道 = senior-engineer 既有 Assembled 装载路径，D-007/Entry #17
  已证明通道可达）；**融合内容本身的真实 Work Instance 消费（Q1–Q5）待自然评审任务触发——UNKNOWN
  显式标注，不预先宣称已帮助**；Human 验收通过（2026-08-23，TASK-20260823-004 已归档）；当前状态 =
  **Fused / Pending Post-Fusion Work Validation**

## D-012 · Post-Fusion Work Validation PASSED（2026-08-23）

- 结果：**第一次 Facet Fusion 回到 Work 且真实影响工作**——ai-consultant 评审（TASK-20260823-006 / Entry #20）中，Work Instance 经统一发现（task_start.py）装载 senior-engineer Review 面（含融合的 dsh-code-review 方法层），**influence true / 80**（证据纪律 / 阻塞闸门 5 条 / 深度检查 15 项 / Verdict-Critical-Worth-Long-term-What to change 汇报结构被实际采用）
- 三样本验证链（同一评审任务，唯一变量 = 入口 + 清理）：
  1. v1：旧入口链无统一发现 → 未检索、能力未进决策空间 → footprint NONE
  2. v2：入口修复后跑通统一发现 + 装载，但撞上既有报告 → 复核模式 → influence false
  3. v3：清理既有报告后从零评审 → 统一发现 + 装载 + **influence 80**
- 结论：① 入口链修复有效（统一发现被自然执行）；② "复核模式"假设成立（清理后才测出真实影响）；③ 融合方法层与 agent 天然行为一致时无可观测差异（同化型），在干净样本中才显现增量
- 状态：**Fused + Validated-1st-sample**；Value directional / pending repetition（等第二个自然评审样本）

## D-014 · Infrastructure Maintenance Skill 空间 + knowledge-maintenance（2026-08-23）

- 处理：建立 `maintenance-skills/`（基础设施维护 Skill 的统一语义归属：Evolution Instance 维护 AI-OS 自身基础设施的能力，与 capabilities/ 区分）；提炼第一个 Maintenance Skill = **knowledge-maintenance**（源自 D-013 真实运行：候选收集 → 全库查重 → 同源/重叠/独立判定 → 抽象 → Evidence 原位挂接 → 新建/归并/关联 → 索引 → 裁决 → 检索验证）
- 原因：Knowledge / Capability / Retrieval / Task Memory 都需要维护，维护 Skill 需要一个稳定归属位置；不把维护 Skill 散放 evolution / domains / capabilities
- 明确不做：capability-maintenance / retrieval-maintenance / task-memory-maintenance **暂不创建**；Health Check / 调用时机 / 体检 **暂不设计**（由真实使用长出来）
- 状态：knowledge-maintenance 已建立；引用：domains/index.md + MAP.md

## D-015 · Maintenance 职责面冻结 + Health Check 入口（2026-08-23）

- 冻结：Work=使用 / Evolution=成长 / **Maintenance=保持 AI-OS 基础设施健康干净可用**——三者不同职责；Maintenance 可被 Evolution 驱动，但**不进普通 Work 的默认任务发现**（task_start 不覆盖；成本保护）
- 校准：① Health Check **暂不等同 NC-001**（可能复用观察能力；重复稳定后才沉淀为 primitive）；② `maintenance-skills/INDEX.md` 是 **discovery surface** 不是完整定义；③ 体检=发现 / Human=裁决 / 维护 Skill=执行
- 实施：INDEX.md（knowledge-maintenance 登记 + health-check 单列）→ 第一次真实体检 → Human 裁决（修/不修/以后修/忽略）→ 维护 Skill 执行 → 复检（Before → Maintenance → After）

## D-016 · Knowledge Space Maintenance v2 升级 + 首次执行（2026-08-23）

- 升级：knowledge-maintenance（v1=Consolidation）→ **Knowledge Space Maintenance（v2）**——真实维护任务证明职责过窄；v2 = Content/Consolidation + Integrity + Structure + Index/Discovery + Provenance；Activation Semantics：duplicate/overlap / malformed / incomplete frontmatter / stale-inconsistent index / orphaned
- 首次执行（Human 裁决后本批次）：
  - **A2（检索盲区）**：experience_push SOURCES 增加顶层 domains/experiences + domains/patterns 扫描；验证 = experience_push "入库审查" 命中 knowledge_admission_rule
  - **A4（两篇 GBK 乱码）**：definition_preservation_check 反转恢复 + 上下文补全 + 修复注记；tomcat_port_conflict 按 HEAD frontmatter + ASCII 残留重建 + 修复注记；原文备份 `D:\AI\scratch\tmp\a4-corrupted-backup-2026-08-23\`
  - **B1（索引）**：domains/index.md 计数对齐（ai-os 23/10/5、总量 92）+ 待办清理
  - **B3（structure）**：3 篇补 keywords（unverified_structure_reference / silent_false_green / stderr_error_channel）
- 边界：A2 只做最小修（检索可达），检索机制深层优化归 retrieval-maintenance 候选；Task Memory / Capability / Git 治理未吞入
- 状态：v2 已建立并首次执行；普通工程修复（A1/A3/A5/B6）与本维护执行分开记录（A1/A3/A5/B6 为直接修复，非 Maintenance Skill 执行）

## D-017 · Line Lifecycle Model（2026-08-23）

- 校准：Evolution **不是**"管理所有线的总控制器"，而是 **AI-OS 的 Growth / Reconstitution 层**——负责让新的职责面被发现、定义、建立、接入、验证和演化；已长出的线自行运行其职责，Evolution 不代替
- 核心原则：AI-OS 的职责面不是预设固定集合；新的职责面只能由真实工作中的持续摩擦与 Human 裁决产生；每个独立职责面拥有自己的最小 Environment、入口、Skill Family 和 Evidence
- Evolution 两个层：**Capability / Skill Growth**（Intake / Onboarding / Facet Fusion / Consolidation / Validation）+ **Line Growth**（发现新职责面 / 判断独立 / 建最小环境 / 注册 / 验证）
- 当前线：Work（operational）/ Evolution（operational, growth）/ Maintenance（operational, emerging）
- 落地：`evolution/lines.md`（线注册 + Line Lifecycle + Candidates 苗头登记）；**不预建** Observation / Retrieval / Learning 线
- Boundary Pass 增补：判断对象归属时增加"它属于哪个职责面？"
- 后续：DSH Skill Corpus 属 Evolution 线 Capability Growth 工作，继续为主线

## D-018 · 收敛：维护与防止死亡 = 演化线的基础设施（2026-08-24）

- 修正 D-015 / D-017 的过度物化：维护与体检、防止死亡**不是独立线/层**，而是**演化线的基础设施**；line / 职责面 ≠ agent 类型
- 核心原则：**Work 是目的，Evolution 是手段**——除了 Work，任何职责面都是为了 Work 而工作；agent 只有两类（Work / Evolution），是同一个 agent 的两种职责面/模式
- Evolution 内部职责：① 成长（intake / fusion / reshape / consolidation）② 维护（health-check 审计 + maintenance-skills 修复）③ 存在性保障（收尾登记 + 体检双向审计 + 接入收口）
- 物理设施保留、归属改标：maintenance-skills/、health-check/、knowledge-space-maintenance 继续存在，所有权 = Evolution 线
- 新职责默认并回演化线；只有 Human 明确判定独立 agent 职责面时才另立

## D-019 · Object / Exposure Unification（2026-08-24）

- 统一：之前几轮"越讨论越长出新线"（维护 → 体检 → 防止死亡 → Survival）的根源 = 把"新对象/行为/基础设施"误当成"新 Line"；实际它们都是**带 Exposure Mode 的对象**
- 冻结 6 条：
  1. Work 与 Evolution 是当前 AI-OS 的两条职责面
  2. 对象不按职责面分类；同一对象可以服务多个职责面
  3. Global / Callable / Searchable / Conditional / Assembled 是 **Exposure / Activation Mode**，不是对象类型
  4. 新增对象不会自动产生新 Line；**只有 Purpose 改变才产生 Line Candidate**
  5. 对象对 Agent 的有效存在要求**至少一个有效 Exposure Path**；失去有效 Path 的对象属于 At Risk / Dead
  6. Registry / INDEX / MAP / TOOL_RUNTIME 等是 **Exposure / Reachability 的实现载体**，不等于 Exposure Mode 本身
- 死亡原因的工程定义：**对象死亡 = 它面向其服务对象的 Exposure Path 不存在或失效**；防止死亡 = Exposure Integrity（保证每个对象至少一个有效 Exposure Path）
- 以后发现新东西的第一问：这是什么对象？服务谁？以什么 Exposure Mode 存在？怎么进入决策空间？怎么成长？——而不是"是不是又一条线"

## D-021 · R1–R7 兑现 + 四态验证（2026-08-24）

- R1：`--auto` 意图源换到 task_cards（`_goal_intent()` 读 active 卡 ## Goal；删 workflows/env 死引用）——验证：intent 含 active 卡意图
- R2：账本 chunk 去重（按 path+title 保留最高分）+ 账本候选"内容"= chunk 文本——验证：Entry #2 不再重复 ×3
- R3：收尾写回链补齐——DevJournal 007/008 移入 `active/DevJournal/`；ai-consultant 建 `active/ai-consultant/PROJECT.md` + 006/007 移入
- R4：MAP 同步（SUCCESS_LOG 行 / workspaces 分类 / experiences 空目录）；卡 001 star_map 死引用加"已删除"注记
- R5：capability-reconstitution 加 **Exposure Path 接入收口**（登记进既有载体 + 验证可达；不新建注册表）
- R6：health-check 升级**双维**（Exposure Integrity + Usage Health）+ **四态**（Dead / At Risk / Unused / Dormant；Unused ≠ Dead）
- R7：`.gitignore` + checkpoint 提交 `6c01f48`（953 文件；安全 checkpoint，非架构）
- 四态小验证：Alive（senior-engineer / knowledge-space-maintenance / health-check / task_start）；Unused（debug-protocol——Exposure 正常无消费，非 Dead）；At Risk（NC-001 缺工具表入口）→ 已补 TOOL_RUNTIME 一行（Exposure Path，不扩功能）
- 后续：DSH Corpus Intake（每 Skill 记录 Object/Growth/Exposure/Path/Discovery/Consumption/Influence/Health/Evidence/Decision）

## D-033 · Knowledge Sink 观察 + 形态判定顺序修正（2026-08-24）

- 观察（Human + DSH 语料）：agent 对外部 Skill 的默认反射是"拆成知识"——D-005 曾因连续两次 intake 默认拆 domains 而建；DSH 11 颗 9 颗落 Knowledge（语料偏方法型，结果大体合理，但**过程顺序偏置**）
- 根因：① D-004 先例链被当模板引用 ② "最小 realization" 天然导向方法层 ③ 反膨胀纪律（不新建对象/已有载体优先）使 domains 成为最便宜落点 ④ Searchable 摩擦最低
- 修正：capability-reconstitution 形态判定加**显式顺序**——① 完整收纳 → ② 融合 → ③ 拆知识 → ④ Reject；拆知识是最后选项；**引用先例 ≠ 默认拆**
- 监视信号（不预建系统）：下一批若出现 Callable / Assembled / Conditional / Shared 候选仍全掉 domains → 才升级为系统性 Knowledge Sink Bias 处理
- 不建工作面索引 / 形态判据表（避免为 11 次 intake 预设计基础设施）

## D-034 · Skill Profile / 关系优先（2026-08-24）

- 修正 D-033：单选顺序（①完整收纳 → ②融合 → ③拆知识 → ④Reject）仍是**单标签盒**；Skill 是**多关系对象**，可跨结构 / 跨领域 / 跨职责面，同时有多个 Exposure 与 Growth 关系
- 模型：Skill → 建立 **Profile**（自身语义 / 工作面 / Facet / 知识 / 能力 / 领域 / 职责面 / Work Context / Exposure 候选 / Growth 关系）→ 判断哪些关系物化 / 引用 / 融合 / 独立 / 拒绝 → 决定 Exposure → 决定物理承载
- 原则：**Physical placement is a realization decision, not the semantic identity of the object**；目录只是承载，不是语义归属
- 下一步：9 个 DSH Skill **Re-Mapping Pass**（只建 Profile 关系图，不迁移、不新建 Capability、不新建 Taxonomy）→ Human 审阅 → 有充分证据才物理调整

## D-036 · 工具 v1 镜像隔离（P0 · 2026-08-24）

- 处理：v1 镜像工具（`D:\AI\tools\experience_push.py` / `wrapup_sync.py` / `resume.py`）移入 `D:\AI\tools\_v1-archived\`；误调 fail-closed；`play_alert.py` 等保留；`D:\AI\tools\README.md` 标注"V2 工具唯一权威在 D:\AI-os\tools"
- 原因：v1 镜像若被误调会**静默读 v1 树**（`D:\AI\domains` + v1 账本）→ Evidence contamination（D-032 发现，Human 裁决隔离）
- 验证：`python D:\AI\tools\experience_push.py "test"` → No such file（fail-closed）；`python D:\AI-os\tools\experience_push.py` 正常
- 补充建议（未执行，待定）：V2 tools 可加 ROOT 断言双保险

## D-038 · DSH 收口：反向引用 + 相关对象网 + Exemplar + 编号说明（2026-08-24）

- 2a 试点：pre_push + prose 物化为 `capabilities/` 工作模式单位（Assembled/Conditional，D-037）
- 2b 补反向引用：5 个 pattern 补"相关对象"节（doc 族双向链 / dependent↔pre_push / cot↔browser / bilingual↔doc_site / prose↔bilingual）
- 2c 相关对象索引：domains/index.md 加"相关对象网"指针（进既有载体，不新建注册表）
- 3 Exemplar：`evolution/exemplars/Corpus-Level-Evolution.md`（语料级 Evolution 案例）
- 4 编号说明：evolution/README 注明 DSH #5 因早期编号错位未分配（以 Evolution intake 编号连续为准）
- 状态：DSH 第一阶段收口完成；真实消费 Q1–Q5 维持 UNKNOWN（等自然任务）；P2 Final Review / GitHub 待 Human 定节奏

## D-013 · Knowledge Space consolidation：两条真实工作 Evidence（2026-08-23）

- 处理：两条 Evidence 各自新建 pattern 并**保持独立**——Evidence A →
  `domains/backend/patterns/startup_dependencies_injectable.md`；Evidence B →
  `domains/backend/patterns/sqlite_backup_include_wal.md`；登记 `domains/index.md`
  （backend 36+ → 40，总 79+ → 81+）；Evidence 原始实例原位保留（REVIEW_REPORT.md /
  FIX_REPORT.md / server.js 启动校验 / scripts/backup.js / tests+CI）；对既有项目经验
  `workspaces/ai-consultant/experiences/storage_is_sqlite_blob.md` 追加修正挂接
  （其"WAL 单文件复制语义"表述被评审证伪，原文保留）
- 原因：A 与 B 的失败模式 / 机制 / 修复均不同——A=测试可复现性（环境接缝 / 注入假 key），
  B=数据持久性（checkpoint / 三件套 / 备份 API）；同源（同一次评审 P1-2/P1-3）≠ 同原则，
  评审本身也把它们列为独立 P1。各自与既有知识关系也不同：A 与项目经验 test_data_isolation
  同主题（测试可复现）不同机制（数据目录隔离 vs 凭证注入），B 与项目经验
  storage_is_sqlite_blob 部分重叠（同一项目备份话题）但该经验依赖了被证伪的备份语义。
  → **"不合并"是正确结论**；共同来源与"文档声明 vs 运行时行为"元教训在 pattern 与决策中
  建立关联，元教训本身已由 verify-before-trust / silent_false_green 覆盖，不新建
- 证据：REVIEW_REPORT.md §3.2/§4.3/§5 P1-2/P1-3；FIX_REPORT.md §二.4/§四；
  server.js 启动校验（process.exit(1)）；scripts/backup.js（copyFileSync(data.db) +
  "单文件复制语义"注释）；磁盘 data.db-wal 4,173,592B vs data.db 200,704B；
  SUCCESS_LOG Entry #19/#20/#21（"待复现再沉淀"触发兑现）
- 状态：已送达（domains/patterns 检索源 + index 登记 + 项目经验修正挂接）；两个 pattern
  的真实消费（Q1–Q5）待自然工作触发——UNKNOWN 显式标注

---

## D-020 · Post-Discovery Architecture Recovery Review（2026-08-24）

- 处理：全量只读恢复/修复评审（TASK-20260824-001），交付
  `evolution/architecture-recovery-2026-08-24.md`；输出 = 8 节（Summary / 结构问题 /
  已修复 / 剩余缺口 / 最小修复计划 / 顺序 / 验收 / 暂缓）。
- 结论（继承前判，不重开）：
  1. 模型层已收敛：D-009/D-019（三维）+ D-018（两线）+ D-019（Exposure Integrity 定义）——
     **不重建**。
  2. 剩余缺口按承重排序：G1 Exposure Integrity 反向审计未实现；G2 `--auto` 意图源死钩子
     （A18 R3）；G3 账本检索噪声（同 Entry 重复 + footprint 自污染 + 内容样板）；G4 收尾写回链
     不一致（SUCCESS_LOG #20/#21 已写而卡 006/007 未更新）；G5 MAP/死引用漂移；G6 Git 安全网
     落后（HEAD 9d35fd1，68 项未提交）；G7 维护 Skill 家族缺口（暂不建）。
  3. 修复顺序：R1–R5 Must Fix Now（全部复用现有工具/文档，零新结构）→ R6 health-check 反向
     审计（Should Fix Next，最高价值结构修复）→ R7 Git 安全网（Human 门）→ 其余 Wait/Do Not Build。
- 纠正（以磁盘为准）：任务表"Health Finding → **Dispatcher** → Skill"无磁盘依据——真实闭环 =
  Finding → Suggested Maintenance Skill → Human 裁决 → Skill（D-015）；不建 Dispatcher。
- 补记：**DSH Skill Corpus 全量吸收正式记为暂停**（D-017 后无动作也无记录；等 R1–R7 完成 +
  真实消费需求再评估）。
- 探针实证（2026-08-24 复跑）：R1（alias）与 A2（顶层检索）已生效；task_start 卡/能力解析
  正常；G2/G3 缺陷复现（--auto 无意图；Entry #2 ×3 重复；"内容"样板一致）。
- 状态：评审交付完成；修复执行待 Human 裁决（R3/R4 数据卫生项可在裁决后直接做）。
- 证据：architecture-recovery-2026-08-24.md；INT-006；TASK-20260824-001；本批探针输出
  （experience_push "problem solving" / "入库审查" / "回收站 软删除…"；task_start 复跑）。

## D-022 · dsh-archive-agent-notes 外部维护 Skill（2026-08-24）

- 处理：**Facet Fusion** —— 外部维护 Skill（deepseek-ai/deepseek-harness 的
  dsh-archive-agent-notes，Agent Notes 归档/修剪/分类/恢复/审查）的**可迁移方法层**融合进
  knowledge-space-maintenance 的 **Lifecycle / Archive facet**
  （`maintenance-skills/knowledge-maintenance/SKILL.md` v3：①添加时 supersession 审计
  ②未来价值分类 keep-archive-reject-delete（词数/年龄非判据）③归档最小改动+封存纪律+入链修复
  ④验证与汇报 ⑤repo 专属不携带清单）；**repo 专属部分不携带**（triplet 结构
  foo.md/foo.zh.md/foo.i18n.yaml、`implemented/<kind>/`+`archived/<kind>/` 路径、sidecar hash、
  `pnpm run verify-archived-agent-notes`/`doc-sync`/`lint`、dsh-pre-push-checks、notes/ 契约、
  PR 内归档工作流在 V2 无对应物，硬搬注入死引用——原样整体裁决为不适合独立装配）；原文保留在
  `evolution/intake/dsh-archive-agent-notes/`（Source preservation，D-010 规则 6）
- 原因：DSH Corpus Intake 恢复（D-020 补记暂停 → Human 送包 = 真实消费需求）；该 Skill 是
  **维护类**外部 Skill，其方法层与 knowledge-space-maintenance（Content/Consolidation +
  Integrity + Structure + Index/Discovery + Provenance，D-016）**同工作面**（维护 AI-OS
  记录/知识语料）且互补——v2 缺的正是**生命周期维度**（保留/归档/拒绝/删除裁决 + 新增时
  supersession 审计 + 归档封存纪律）；不独立注册 capabilities/ 装配单位（D-008/D-011 先例：
  repo 专属 Skill 不另立单位）；不拆 domains pattern（方法层是工作流纪律非原子知识，避免双写）；
  不新建维护 Skill 目录（D-014："其余维护 Skill 由真实维护需求长出来"，融合保持最小足迹）
- 证据：maintenance-skills/knowledge-maintenance/SKILL.md（Lifecycle facet 子节 + 不携带清单）；
  maintenance-skills/INDEX.md + README.md；evolution/growth.md（dsh-archive-agent-notes 行）；
  INT-007；intake README（HTTP 200 逐字下载）
- 状态：已送达（维护 Skill 家 Exposure Path 有效：INDEX.md → TOOL_RUNTIME §1.5；不进 task_start，
  D-015 成本保护）；**融合内容本身的真实维护消费（Q1–Q5）待自然触发——UNKNOWN 显式标注，
  不预先宣称已帮助**；Human 验收待确认（TASK-20260824-002）

## D-023 · dsh-doc-site-sync 外部文档站 Skill（2026-08-24）

- 处理：**Skill Fusion（外部 Skill → domains pattern）**——deepseek-ai/deepseek-harness 的
  dsh-doc-site-sync（文档站页面发布/更新/移动/移除 + docs.ts 映射 + VitePress 诊断 +
  docs:dev/docs:check/doc-sync 工作流）的**可迁移方法层**收编为
  `domains/ai-os/patterns/doc_site_projection.md`（仓库 Markdown 单一源 → 站点是受测投影：
  ①单一可编辑源 + 显式 manifest 白名单 + 可丢弃生成树 ②按变更分类处理 ③manifest 显式白名单、
  不发布内部材料 ④链接保留行为、缺失目标投影失败而非静默坏链 ⑤预览+聚焦检查+完整门禁
  ⑥部署分离、内容同步≠发布）；**repo 专属部分不携带**（website/docs.ts DocsPage 字段集 /
  pairedPages / mirroredPages / project-doc-site.ts 投影器 / raw-Markdown twin + llms.txt /
  VitePress 配置 / 翻译 triplet 契约（foo.md+foo.zh.md+foo.i18n.yaml、禁 zh-CN 目录）/
  pnpm docs:dev/docs:check/doc-sync/lint / dsh-doc-standards / dsh-pre-push-checks /
  verify-doc-site-fragments 在 V2 无对应物，硬搬注入死引用——原样整体裁决为不适合独立装配）；
  原文保留在 `evolution/intake/dsh-doc-site-sync/`（Source preservation，D-010 规则 6）
- 原因：DSH Corpus Intake 继续（D-022 恢复后 Human 送包 = 真实消费需求）；该 Skill 的
  **可迁移方法层**（文档站 = 仓库 Markdown 的受测投影）是 V2 显式缺环——全文检索证伪
  （vitepress / docs.ts / doc-site / 文档站发布在 domains/ + capabilities/ + maintenance-skills/ +
  evolution/ 无既有覆盖；`doc-generation` 是"收尾产出文档文件"，与"把文档发布成站点"不同工作面，
  互补不重复）；**无既有工作面可做 Facet Fusion**（senior-engineer 四面 = Review/Architecture/
  Coding/Debugging；knowledge-space-maintenance = 知识语料维护，均不含文档站发布）；不独立注册
  capabilities/ 装配单位（D-008/D-011/D-022 先例：repo 专属 Skill 不另立单位，原样整体注入死引用）；
  按 D-004 debug-protocol 先例（外部 Skill → domains pattern → experience_push 检索源，
  D-008 Human 确认知识/pattern 形态）收编为 Searchable 知识
- 证据：domains/ai-os/patterns/doc_site_projection.md；domains/index.md（ai-os patterns 23→24，
  总 92→93）；evolution/growth.md（dsh-doc-site-sync 行）；INT-008；intake README（HTTP 200
  逐字下载）；全文检索证伪（vitepress/docs.ts/doc-site 仅 intake 自身命中）
- 状态：已送达（可消费位置：domains/patterns → experience_push 检索源，D-004 同款通道）；
  **pattern 本身的真实 Work Instance 消费（Q1–Q5）待自然文档站任务触发——UNKNOWN 显式标注，
  不预先宣称已帮助**；Human 验收待确认（TASK-20260824-003）

---

## D-024 · dsh-doc-standards 外部文档标准 Skill（2026-08-24）

- 处理：**Skill Fusion（外部 Skill → domains pattern）**——deepseek-ai/deepseek-harness 的
  dsh-doc-standards（文档放置/层次、教程 vs 参考分类、预算纪律、语料审计）的**可迁移方法层**收编为
  `domains/ai-os/patterns/doc_standards.md`（结构先行 / 按用途分类 tutorial-vs-reference / 教程前置
  条件 / 拆分混合形式 / 放置约束（生成目录不手编、移动前 grep 入站引用、原子移动）/ 语料审计廉价探针
  （词数 outlier / 会话残留 / 重复 / 手写清单 / implemented 未来时态）/ 预算 relocate-condense-raise /
  验证汇报）；**repo 专属部分不携带**（docs/AGENTS.md 标准之家、pnpm verify-doc-budgets /
  verify-md-links / verify-doc-refs / change-scope / doc-sync / lint / verify-translation-pairing、
  git ls-files wc 流水线、JSDoc 类型等价围栏、翻译 triplet、.agents/notes implemented/archived 契约
  在 V2 无对应物，硬搬注入死引用——原样整体裁决为不适合独立装配）；原文保留在
  `evolution/intake/dsh-doc-standards/`（Source preservation，D-010 规则 6）
- 原因：DSH Corpus Intake 继续（D-022/D-023 恢复后 Human 送包 = 真实消费需求）；该 Skill 的
  **可迁移方法层**（文档放置/形态/预算/审计）是 V2 显式缺环——全文检索证伪（tutorial / 参考文档 /
  教程 / 文档结构 / 文档分层 / 文档预算 / slop / 文档放置 / hierarchy / 写作规则 在 domains/ +
  capabilities/ + maintenance-skills/ + evolution/ 无既有方法覆盖，命中均为无关语境或 intake 自身）；
  **无既有工作面可做 Facet Fusion**（senior-engineer 四面不含文档标准；knowledge-space-maintenance
  = domains 知识语料维护（frontmatter/索引/去重/生命周期），不含通用文档放置/标准；
  doc_site_projection = 发布投影、doc-generation = 文档产出，均不同工作面）；不独立注册 capabilities/
  装配单位（D-008/D-011/D-022/D-023 先例：repo 专属 Skill 不另立单位，原样整体注入死引用）；
  按 D-004/D-023 先例（外部 Skill → domains pattern → experience_push 检索源，D-008 Human 确认
  知识/pattern 形态）收编为 Searchable 知识
- 证据：domains/ai-os/patterns/doc_standards.md；domains/index.md（ai-os patterns 24→25，总 93→94）；
  evolution/growth.md（dsh-doc-standards 行）；INT-009；intake README（HTTP 200 逐字下载）；
  全文检索证伪（tutorial/教程/文档结构/文档分层/文档预算/slop/hierarchy 仅无关命中或 intake 自身）；
  experience_push 验证探针（"文档放置/教程还是参考/文档太长" 命中 doc_standards）
- 状态：已送达（可消费位置：domains/patterns → experience_push 检索源，D-004/D-023 同款通道）；
  **pattern 本身的真实 Work Instance 消费（Q1–Q5）待自然文档任务触发——UNKNOWN 显式标注，
  不预先宣称已帮助**；Human 验收待确认（TASK-20260824-004）

---

## D-025 · dsh-find-simplifications 外部代码简化审计 Skill（2026-08-24）

- 处理：**Skill Fusion（外部 Skill → domains pattern）**——deepseek-ai/deepseek-harness 的
  dsh-find-simplifications（把宽泛"找简化"变成有证据的简化提案：移除/折叠/降级既有表面积）的
  **可迁移方法层**收编为 `domains/ai-os/patterns/simplification_audit.md`（先读仓库上下文再判断 /
  强候选证据判据（无生产消费者、仅测试文档消费者、双表示镜像、无消费者 seam 方法、投机泛化、
  仅保护未用 API 的防御机制、手写轮子 vs 依赖）/ 广泛 survey 不停第一个候选 / 信任与生命周期边界审计
  （值从哪来、下一步归谁；保护同步发布+回滚、回调封闭、首终局仲裁、worker/进程所有权、
  dispose-to-quiescence 的机制保留）/ 依赖替换按净删除衡量（点名覆盖表面、残余语义计入成本、包健康、
  优先 builtin、先查已记录 seam）/ 证明或拒绝每个候选（生产-非生产-模糊语料分类 + rg 精确符号 +
  读调用点）/ 内联 TODO/FIXME/XXX 稳定标签纪律 / 提案写作（V2 映射 task_cards proposed 卡）/
  记录收编（added-then-removed 完整替代与拒绝归并判据——Lifecycle facet 补充语义）/ 汇报卫生）；
  **repo 专属部分不携带**（`.agents/notes/` 树 + notes/README.md 契约、Agent Note implemented 例子引用、
  dsh-archive-agent-notes 的 triplet 归档机制、pnpm doc-sync/lint 与 pre-push hook 命令链、PR folding
  工作流、knip 特指在 V2 无对应物，硬搬注入死引用——原样整体裁决为不适合独立装配）；原文保留在
  `evolution/intake/dsh-find-simplifications/`（Source preservation，D-010 规则 6）
- 原因：DSH Corpus Intake 继续（D-022/D-023/D-024 恢复后 Human 送包 = 真实消费需求）；该 Skill 的
  **可迁移方法层**（证据驱动的代码简化审计）是 V2 显式缺环——全文检索证伪（simplif/refactor/简化/
  重构/dead code/unused 在 domains/ + capabilities/ + maintenance-skills/ + evolution/ 无既有方法覆盖，
  命中均为无关语境（TDD REFACTOR 步骤、senior-engineer trigger 文案、doc_standards 前向引用）或
  intake 自身）；**无既有工作面可 Facet Fusion**（senior-engineer 四面 = Review/Architecture/Coding/
  Debugging 是评审/实现/诊断视角，不含"证据驱动的简化审计"工作流；knowledge-space-maintenance =
  知识语料维护；doc 族 pattern = 文档放置/投影——均不含代码简化审计工作面）；记录收编部分与
  knowledge-space-maintenance Lifecycle facet（D-022 融合 dsh-archive-agent-notes）重叠，但该 facet
  已承载 supersession 审计——本 skill 只补充 added-then-removed 两条判据作为交叉挂接，不重开 facet；
  不独立注册 capabilities/ 装配单位（D-008/D-011/D-022/D-023/D-024 先例：repo 专属 Skill 不另立单位，
  原样整体注入死引用）；按 D-004/D-023/D-024 先例（外部 Skill → domains pattern → experience_push
  检索源，D-008 Human 确认知识/pattern 形态）收编为 Searchable 知识
- 证据：domains/ai-os/patterns/simplification_audit.md；domains/index.md（ai-os patterns 25→26，
  总 94→95）；evolution/growth.md（dsh-find-simplifications 行）；INT-010；intake README（HTTP 200
  逐字下载）；全文检索证伪；experience_push 验证探针（"找简化候选 死代码 冗余 …"命中
  simplification_audit）
- 状态：已送达（可消费位置：domains/patterns → experience_push 检索源，D-004/D-023/D-024 同款通道）；
  **pattern 本身的真实 Work Instance 消费（Q1–Q5）待自然"找简化/重构/减面"任务触发——UNKNOWN
  显式标注，不预先宣称已帮助**；Human 验收待确认（TASK-20260824-005）

---

## D-026 · dsh-merging-stacked-prs 外部 PR 栈落库 Skill（2026-08-24）

- 处理：**Skill Fusion（外部 Skill → domains pattern）**——deepseek-ai/deepseek-harness 的
  dsh-merging-stacked-prs（用官方 GitHub 原生栈对象 + `gh stack merge` 落地依赖 PR 栈：原生栈
  支持探测与硬停 / 实时精确元数据建链 / 官方栈对象为成员权威 / 缺链成员同作者自动补链 /
  需要时刷新（级联 rebase 或增量 merge-forward）/ 整链预检 / 官方 API 整链落库 /
  落库后验证完成再清理分支）的**可迁移方法层**收编为
  `domains/ai-os/patterns/dependent_change_landing.md`（官方机制优先，不可用即硬停不手工模拟 /
  依赖链以实时状态为准不信任分支名或旧报告 / 补链纪律（同作者加性、冲突与异作者问用户、
  不自动解散重排既有栈）/ 只在需要时刷新且重写后重新审计 / 整链预检（每项独立判定）/
  官方批量 API 整链或显式边界前缀落库（all-or-nothing，阻塞不回退逐项）/ 落库后验证真正完成 +
  剩余链复查 / 分支清理单独最后一步且零依赖才删）；**repo/平台专属部分不携带**（`gh stack` /
  `gh pr merge` / `gh pr edit` 具体命令、GitHub GraphQL `PullRequest.stack` /
  `stackEntry.position` 查询、`gh stack checkout/sync/rebase/push/link` 工作流、官方 stacked-PR
  扩展与 server-side stack 特性、draft/merge-queue 语义在 V2 无对应物——V2 的 git 是本地仓库 +
  既有文件安全网纪律，无 GitHub PR 运行时，硬搬注入死引用——原样整体裁决为不适合独立装配）；
  原文保留在 `evolution/intake/dsh-merging-stacked-prs/`（Source preservation，D-010 规则 6）
- 原因：DSH Corpus Intake 继续（D-022/D-023/D-024/D-025 恢复后 Human 送包 = 真实消费需求）；该 Skill 的
  **可迁移方法层**（依赖变更落库 = 官方机制优先 + 实时状态建链 + 整链预检/落库/验证）是 V2 显式缺环——
  全文检索证伪（stack/pull request/PR merge/retarget/merge commit/依赖链 在 domains/ +
  capabilities/ + maintenance-skills/ + evolution/ 无既有方法覆盖，命中均为无关语境
  （debug_protocol "stack" 词、senior-engineer "PR" 触发文案）或 intake 自身）；
  `git_safety_net` 是"本地 git 文件操作安全带"（status/diff/checkout 恢复），不含"一批相互依赖
  变更的顺序落地与完成验证"维度——互补不重复；**无既有工作面可做 Facet Fusion**（senior-engineer
  四面 = Review/Architecture/Coding/Debugging 是评审/实现/诊断视角，不含"依赖链落地/合并操作"
  工作面；knowledge-space-maintenance = 知识语料维护；doc 族 pattern = 文档放置/投影——均不含
  该工作面）；不独立注册 capabilities/ 装配单位（D-008/D-011/D-022/D-023/D-024/D-025 先例：
  repo/平台专属 Skill 不另立单位，原样整体注入死引用）；按 D-004/D-023/D-024/D-025 先例
  （外部 Skill → domains pattern → experience_push 检索源，D-008 Human 确认知识/pattern 形态）
  收编为 Searchable 知识
- 证据：domains/ai-os/patterns/dependent_change_landing.md；domains/index.md（ai-os patterns 26→27，
  总 95→96）；evolution/growth.md（dsh-merging-stacked-prs 行）；INT-011；intake README（HTTP 200
  逐字下载）；全文检索证伪（stack/pull request/PR merge/retarget/依赖链 仅无关命中或 intake 自身）；
  experience_push 验证探针（"landing a stack of dependent PRs / merge dependent changes in sequence"
  命中 dependent_change_landing 置顶，内容摘要送达；基线探针同查询仅无关低分命中）
- 状态：已送达（可消费位置：domains/patterns → experience_push 检索源，D-004/D-023/D-024/D-025
  同款通道）；**pattern 本身的真实 Work Instance 消费（Q1–Q5）待自然"依赖变更落地/合并 PR 栈"
  任务触发——UNKNOWN 显式标注，不预先宣称已帮助**；Human 验收待确认（TASK-20260824-006）

---

## D-027 · dsh-pre-push-checks 外部推前检查 Skill（2026-08-24）

- 处理：**Skill Fusion（外部 Skill → domains pattern）**——deepseek-ai/deepseek-harness 的
  dsh-pre-push-checks（推送/强制推送/标记 ready/声称检查通过之前，为 outgoing diff 选择最小充分
  证据，不反射式跑全量；hook 管窄检查、CI 管穷尽覆盖；保护历史重写推送——记录远端 OID +
  force-with-lease、绝不 raw --force；重写后重新拉取 live heads 重审评审线程/批准/可合并性/检查；
  批处理发布后逐层验证、未通过不 merge、报告 pending；失败即停不 push 后指望 CI；环境特定失败
  证明（确切命令/失败测试/平台差异 + 非平台证据）；推送后核对远端 ref 与本地 HEAD；PR 平台
  "no checks reported" ≠ 基础设施故障——先读 mergeability，冲突 PR 无 pull_request 运行，
  解决冲突是唯一修复）的**可迁移方法层**收编为 `domains/ai-os/patterns/pre_push_evidence_gate.md`
  （①确认 outgoing 范围——base ref 来自实时远端/栈状态、不猜测，committed paths 与 worktree
  paths 分开 ②按行为变更面选最小充分证据——owning 测试/定向检查，只对 diff 到达的表面积加宽；
  不重复 hook 工作 ③覆盖度量纪律——test selection ≠ coverage selection，命名 owning 测试 +
  源范围，不用 --passWithNoTests/降阈值/收窄 include 隐藏未覆盖文件 ④全量复演仅三种情况：
  用户明确要求 / 诊断 CI 失败 / 变更面广到无更窄集可信 ⑤历史重写保护——记录远端精确 OID、
  --force-with-lease=<branch>:<observed-oid>、绝不 raw --force、重写后重审（旧哈希/锚点不是
  当前证据）⑥发布后验证例外——批处理发布后逐层验证、保持未 merge 并报告 pending、失败保留
  租约保护 heads 修复再发布 ⑦失败即停——push 前相关检查失败=停/修/解释；环境特定失败需证明；
  绕过 hook 仅用户明确要求且精确汇报 ⑧推送后核对——git rev-parse HEAD origin/<branch>；
  PR 场景查 CI、pending 如实报告；"no checks reported" 先读 mergeability，冲突 PR 无
  pull_request 运行，解决冲突是唯一修复）；**repo/平台专属部分不携带**（`pnpm change-scope` /
  vitest / doc-sync / build / test:e2e 命令链、`gh stack` / `gh pr checks` / GitHub GraphQL
  查询、pre-commit/pre-push hook 实现细节在 V2 无对应物，硬搬注入死引用——原样整体裁决为不适合
  独立装配）；原文保留在 `evolution/intake/dsh-pre-push-checks/`（Source preservation，
  D-010 规则 6）
- 原因：DSH Corpus Intake 继续（D-022/D-023/D-024/D-025/D-026 恢复后 Human 送包 = 真实消费需求）；
  该 Skill 的**可迁移方法层**（推前证据选择 / 历史重写推送保护 / 失败处理 / 推送后验证）是 V2
  显式缺环——全文检索证伪（pre-push / push 前 / force-push / 测试选择 / 最小测试 / 全量测试 /
  change-scope / typecheck 在 domains/ + capabilities/ + maintenance-skills/ + evolution/ 无既有
  方法覆盖，命中均为前序 intake 的"dsh-pre-push-checks 在 V2 无对应物"不携带引用、
  testing-tdd 的"提交前测试全绿"（TDD 纪律，不同工作面）或 dependent_change_landing 的 force
  禁令（落库工作面，共享原则不同工作面））；`git_safety_net` 是本地 git 文件操作安全带
  （status/diff/checkout 恢复），不含"推送前证据选择与推送后远端核对"维度——互补不重复；
  **无既有工作面可做 Facet Fusion**（senior-engineer 四面是评审/实现/诊断视角、
  knowledge-space-maintenance = 知识语料维护、doc 族 pattern = 文档放置/投影、
  dependent_change_landing = 依赖变更落库顺序——均不含"outgoing diff 推前证据选择"工作面）；
  不独立注册 capabilities/ 装配单位（D-008/D-011/D-022/D-023/D-024/D-025/D-026 先例：
  repo 专属 Skill 不另立单位，原样整体注入死引用）；按 D-004/D-023/D-024/D-025/D-026 先例
  （外部 Skill → domains pattern → experience_push 检索源，D-008 Human 确认知识/pattern 形态）
  收编为 Searchable 知识
- 证据：domains/ai-os/patterns/pre_push_evidence_gate.md；domains/index.md（ai-os patterns 27→28，
  总 96→97）；evolution/growth.md（dsh-pre-push-checks 行）；INT-012；intake README（HTTP 200
  逐字下载）；全文检索证伪（pre-push/push 前/force-push/测试选择/最小测试/全量测试/change-scope/
  typecheck 仅无关命中或 intake 自身）；experience_push 验证探针（"push 前检查：outgoing diff
  选哪些测试 / force-push 保护 / 推后核对" 命中 pre_push_evidence_gate 置顶，内容摘要送达）
- 状态：已送达（可消费位置：domains/patterns → experience_push 检索源，D-004/D-023/D-024/
  D-025/D-026 同款通道）；**pattern 本身的真实 Work Instance 消费（Q1–Q5）待自然 push /
  force-push / 声称"检查通过"任务触发——UNKNOWN 显式标注，不预先宣称已帮助**；Human 验收待确认
  （TASK-20260824-007）

---

## D-028 · dsh-prose-standard 外部散文与注释编辑 Skill（2026-08-24）

- 处理：**Skill Fusion（外部 Skill → domains pattern）**——deepseek-ai/deepseek-harness 的
  dsh-prose-standard（写/评审/恢复/精简/审计散文：写到足以保留契约为止，再移除推理转录、重复与
  装饰；契约 = 调用方/被调用方/实现方/生产者/消费者依赖的义务、不变式、前置/后置条件或兼容性
  承诺；本 skill 拥有编辑判断与必需散文覆盖）的**可迁移方法层**收编为
  `domains/ai-os/patterns/prose_standard.md`（①输入与范围——显式 scope 缺失即停、mode 默认
  automatic、interactive 仅显式要求、mode 控提问不控写权 ②排除 vendored/第三方依赖与冻结归档
  快照、派生物先改源再重新生成、双语配对无永久作者侧 ③保留完整命题——编辑前识别每个命题
  （actor/action、条件/时序/顺序、模态 must-may-never、负向保证与例外、所有权/副作用/失败模式/
  后果），只有每个事实子句存活且更清晰才删、字少本身不是改进 ④局部契约完整保留 + 架构/理由/
  算法/历史激进链接唯一归属（一个解释只有一个家）⑤非显然理由保留、否则陈述后果并链接理由的家
  ⑥按 12 类位置覆盖必需契约——公开 JSDoc / 内部注释 / 模块注释 / 测试 / cookbook / README /
  Agent Notes / postmortem / skills 与 agent 指令 / 示例与配置注释 / 提示词与可见字符串 / 诊断，
  另含可搜索机制名与模态/时序/负向强调保留 ⑦词检查——contract/boundary/shape/surface/seam/
  gate/vocabulary 用前检查非禁用 ⑧七步工作流——scope 确认（含分支/PR base/AGENTS.md）→ 先读
  标准与拥有代码 → 全范围语义判断（搜索+词数找候选）→ 分类 keep/add/trim/restore/restructure/
  defer → 先改拥有者再派生物、学新规则后复查相似段落 → 窄检查 + 文档门禁 + git diff --check +
  可见字符串行为测试 + diff 无 vendored 路径 → 汇报范围/改动/刻意保留/延后/实际检查 ⑨边界决策——
  borderline 定义（≥2 版本满足完整命题但权衡原则且未解决）、automatic 应用明确编辑并如实报告
  不弱化命题、interactive 分组 + 2-3 版本 + 推荐 + 决定后提炼进 examples 并应用到所有相似段落）；
  **repo 专属部分不携带**（deepseek-harness 的 `vendor/` 具体路径约定与 `.agents/notes/` 树
  （notes/README 契约、archived 机制）、docs/AGENTS.md 标准之家与 lightweight routine path 链、
  package README requirements 仓库表单、references/examples.md、JSDoc 类型等价围栏、翻译 triplet
  契约、dsh-doc-standards 与 dsh-trim-cot-leakage 子 skill 引用（分别独立 intake：doc_standards
  已收编 D-024、trim-cot-leakage 未处理）在 V2 无对应物，硬搬注入死引用——原样整体裁决为不适合
  独立装配）；原文保留在 `evolution/intake/dsh-prose-standard/`（Source preservation，
  D-010 规则 6）
- 原因：DSH Corpus Intake 继续（D-022/D-023/D-024/D-025/D-026/D-027 恢复后 Human 送包 = 真实
  消费需求）；该 Skill 的**可迁移方法层**（散文编辑判断 / 完整命题保留 / 按位置覆盖）是 V2 显式
  缺环——全文检索证伪（prose / proposition / 完整命题 / 编辑判断 / 契约保留 / 注释标准 / JSDoc /
  required coverage / reasoning transcript 在 domains/ + capabilities/ + maintenance-skills/ +
  evolution/ 无既有方法覆盖，命中均为前序 intake 的"dsh-prose-standard 在 V2 无对应物/后续独立
  intake"不携带与前向引用（doc_standards/simplification_audit/senior-engineer）或 intake 自身）；
  `doc_standards` 是"放置/层级/预算/语料审计"（D-024，管放哪/多长），本文是"写什么/保留什么/删
  什么"——原文自述分工（prose-standard 拥有编辑判断与必需散文覆盖；doc-standards 管放置、预算、
  双语配对、文档门禁），互补不重复；senior-engineer Review 方法层（D-011 融合 dsh-code-review）
  含"注释陈述非显然契约、标记实现叙述"纪律（判定该标记什么），本文提供编辑标准（该写/该删什么），
  且 dsh-code-review 融合时已将 dsh-prose-standard 列为不携带的独立 skill——互补不重复；**无既有
  工作面可做 Facet Fusion**（senior-engineer 四面 = Review/Architecture/Coding/Debugging 是
  评审/实现/诊断视角；knowledge-space-maintenance = 知识语料维护；doc 族 pattern =
  doc_standards 放置/预算、doc_site_projection 发布投影、doc-generation 文档产出——均不含
  "散文编辑判断/契约保留"工作面）；不独立注册 capabilities/ 装配单位（D-008/D-011/D-022/D-023/
  D-024/D-025/D-026/D-027 先例：repo 专属 Skill 不另立单位，原样整体注入死引用）；按
  D-004/D-023/D-024/D-025/D-026/D-027 先例（外部 Skill → domains pattern → experience_push
  检索源，D-008 Human 确认知识/pattern 形态）收编为 Searchable 知识
- 证据：domains/ai-os/patterns/prose_standard.md；domains/index.md（ai-os patterns 28→29，
  总 97→98）；evolution/growth.md（dsh-prose-standard 行）；INT-013；intake README（HTTP 200
  逐字下载）；全文检索证伪（prose/proposition/完整命题/编辑判断/契约保留/注释标准/JSDoc/required
  coverage/reasoning transcript 仅无关命中或 intake 自身）；experience_push 验证探针（"写/评审/
  精简散文与注释：保留完整命题与契约、按位置覆盖 JSDoc/内部注释/测试/README/提示词/诊断" 命中
  prose_standard 置顶，内容摘要送达；基线探针同查询仅 SUCCESS_LOG 前序融合摘要低分命中）
- 状态：已送达（可消费位置：domains/patterns → experience_push 检索源，D-004/D-023/D-024/
  D-025/D-026/D-027 同款通道）；**pattern 本身的真实 Work Instance 消费（Q1–Q5）待自然散文 /
  注释 / 提示词 / 可见字符串写评审精简任务触发——UNKNOWN 显式标注，不预先宣称已帮助**；
  Human 验收待确认（TASK-20260824-008）

---

## D-029 · dsh-translate-docs 外部双语配对文档 Skill（2026-08-24）

- 处理：**Skill Fusion（外部 Skill → domains pattern）**——deepseek-ai/deepseek-harness 的
  dsh-translate-docs（保持 `foo.md ↔ foo.zh.md` 双语配对自然一致的扩展工作流：按变更类型分诊 /
  briefing 驱动最小更新 / 整篇翻译委托子 agent / 术语表双向绑定 / 逐句核验 + 结构对齐）的
  **可迁移方法层**收编为 `domains/ai-os/patterns/bilingual_doc_pairing.md`（①分诊先行——
  Update 走 briefing 驱动最小更新路径、New pair 走整篇翻译路径、删除/重命名同步对应面、冻结归档
  不动 ②Briefing = 译者完整工作集——最小可对齐粒度（变化 Markdown 单元 → 整节 → 整文档），
  散文 diff 委托子 agent 时把 briefing 或生成命令整个传过去，不重读语料/不重推 diff，仅 briefing
  留下真正不可回答决策才回权威源 ③最小编辑覆盖 diff——绝不因一次更新重译整篇文档，保留未变部分
  已审措辞 ④整篇翻译——协调者委托子 agent 逐节翻译锁定结构，Pass 1 写不逐字对应（以目标语言母语
  技术作者语域重述）、Pass 2 逐句对照源核验保真（修 = 重写句子不是贴词）、单独读译文改孤立拗口、
  只写最终文本 ⑤术语纪律——翻译前先载入术语表（双向绑定），未列术语须有可引用 OSS/厂商先例否则
  英文 + 「待定术语」，绝不临时自造 ⑥代码块两侧字节一致（含注释）⑦链接保持同一语义目标与精确
  query/fragment 后缀（语料内按语言后缀切换、缺对应面是错误、语料外保持作者路径、switcher 是唯一
  例外）⑧结构对齐手工核验（标题层级/围栏/表格/列表/有序起点/链接语种）⑨收尾——确认一致后才记录
  配对状态，汇报新 vs 更新 + 列出待定术语）；**repo 专属部分不携带**（`pnpm run
  gen-translation-brief` / `gen-translation-brief --apply` / `verify-translation-pairing`
  （`--write`/`--list`/`--all`）命令族、`foo.i18n.yaml` 双侧 blob 哈希一致性记录、语言切换行仓库
  格式、`docs/i18n/README.md` / `translation-rules.md` / `terminology.md` / `translation-prompt.md`
  / `style-samples.md` 具体文件、`scripts/translation-pairing.manifest.json`、`doc-sync` /
  `verify-md-wrap` / `verify-md-links` 门禁、`.agents/notes/archived/` 三元组封存契约与
  dsh-code-review / dsh-prose-standard / dsh-pre-push-checks 子 skill 引用（分别独立 intake，
  见对应 pattern）在 V2 无对应物，硬搬注入死引用——原样整体裁决为不适合独立装配）；原文保留在
  `evolution/intake/dsh-translate-docs/`（Source preservation，D-010 规则 6）
- 原因：DSH Corpus Intake 继续（D-022~D-028 恢复后 Human 送包 = 真实消费需求）；该 Skill 的
  **可迁移方法层**（配对文档一致性维护 = 分诊 / briefing 驱动最小更新 / 术语绑定 / 逐句核验）是
  V2 显式缺环——全文检索证伪（translat/i18n/bilingual/双语/翻译/配对/pairing/zh.md/translation
  在 domains/ + capabilities/ + maintenance-skills/ + evolution/ 无既有方法覆盖，命中均为前序
  intake 的"翻译 triplet 在 V2 无对应物"不携带引用、`doc_standards` 的"双语配对文档每次编辑都欠
  一个对应面更新"放置约束、`prose_standard` 的"双语配对无永久作者侧"原则、senior-engineer 评审
  纪律的"配对哈希绿 ≠ 翻译质量"或 intake 自身——全是**提及/约束/评审侧**，没有**作者侧完整工作流**）；
  `prose_standard` = 单侧散文编辑判断（管"一侧写什么/保留什么/删什么"），本文 = 配对间同步工作流
  （管"两侧怎么保持一致"）——原文自述"guidance, not a translation memory"，互补不重复；
  `doc_standards` = 放置/预算/语料审计（其"双语配对每次编辑欠一个对应面更新"是放置约束，本文提供
  完整工作流）；senior-engineer Review 方法层（D-011）的"双语改动：两侧语义与术语对照"是评审侧
  判定，本文是作者侧——互补不重复；**无既有工作面可做 Facet Fusion**（prose_standard = 编辑判断/
  契约保留、doc_standards = 放置/预算、doc_site_projection = 发布投影、doc-generation = 文档
  产出、knowledge-space-maintenance = 知识语料维护、senior-engineer 四面 = 评审/实现/诊断视角，
  均不含"配对文档同步工作流"工作面）；不独立注册 capabilities/ 装配单位（D-008/D-011/D-022/D-023/
  D-024/D-025/D-026/D-027/D-028 先例：repo 专属 Skill 不另立单位，原样整体注入死引用）；按
  D-004/D-023/D-024/D-025/D-026/D-027/D-028 先例（外部 Skill → domains pattern →
  experience_push 检索源，D-008 Human 确认知识/pattern 形态）收编为 Searchable 知识
- 证据：domains/ai-os/patterns/bilingual_doc_pairing.md；domains/index.md（ai-os patterns 29→30，
  总 98→99）；evolution/growth.md（dsh-translate-docs 行）；INT-014；intake README（HTTP 200
  逐字下载）；全文检索证伪（translat/i18n/bilingual/双语/翻译/配对/pairing/zh.md/translation
  仅无关命中或 intake 自身）；experience_push 验证探针（"维护双语配对文档：更新一侧后同步对应面、
  术语表绑定、逐句核验翻译一致性" 命中 bilingual_doc_pairing 置顶，内容摘要送达；基线探针同查询
  仅 SUCCESS_LOG 前序融合摘要低分命中）
- 状态：已送达（可消费位置：domains/patterns → experience_push 检索源，D-004/D-023/D-024/
  D-025/D-026/D-027/D-028 同款通道）；**pattern 本身的真实 Work Instance 消费（Q1–Q5）待自然
  双语配对/翻译文档/一致性维护任务触发——UNKNOWN 显式标注，不预先宣称已帮助**；Human 验收待确认
  （TASK-20260824-009）

---

## D-030 · dsh-trim-cot-leakage 外部会话推理转录猎杀 Skill（2026-08-24）

- 处理：**Skill Fusion（外部 Skill → domains pattern）**——deepseek-ai/deepseek-harness 的
  dsh-trim-cot-leakage（链式思维泄漏 = 散文视角是写作会话而非仓库：引用只有该会话能看见的产物、
  叙述变更而不是状态、与已离开的评审者争辩；修复从不只是删除——段落带事实子句时先把每个子句重述为
  在 HEAD 成立再删除转录，不带事实子句的直接删除）的**可迁移方法层**收编为
  `domains/ai-os/patterns/cot_leakage_trim.md`（①HEAD 视角测试——无任何会话转录/PR 线程/未提交
  草稿的 HEAD 读者能否解析每个引用、核验每个声明；不能 → 重述存活事实 + 删除其余；能 → 不是泄漏
  （可解析只过本 skill 的杆：当前状态面上可解析的变更故事仍是变更叙述，按第 3 类送回许可之家）
  ②八类泄漏分类——死设计会话引用（(decision 7)/(audit C2)/design §4.7/phase 标签/design ledger/
  (B ruling)：有已提交拥有者按名+路径引用，否则删引用重述事实子句）/ 栈与 PR 视角（a later PR in
  this stack/this PR adds/the previous commit：陈述已交付机制或扩展点、延后转 TODO/issue）/
  变更叙述与版本戳（used to/no longer/the old X/索引戳 v1 this cut today now：陈述当前行为、
  已修复回归用现在时反事实 without X Y happens、绝不写仓库历史）/ 评审编排（Rejected in review/
  the reviewer confirmed/草稿序号 v5 of this note/轮次归属：保留决策与理由删谁在何时说的）/
  评审者定向辩护（the cast is safe — it simply…/this is correct because…：陈述安全不变式或代码
  已显示时删除）/ 复述与推导转录（控制流叙述/测试走读/显然分支证明：删除只留非显然契约/不变式）/
  对冲与计划残留（probably fine for now/should be enough/无标记延后：提升 TODO/FIXME 或重述实际
  边界）/ 写作语言碎片（英文散文残留 端/设计稿/---- 私有 ----，或中文对应面反向：翻译或删除）
  ③保留规则（什么不是泄漏）——issue 引用（#1470/TODO(name):/issue #N owns the follow-up：HEAD
  可解析任何表面都保留含 README 不移到 Agent Notes）/ Agent Notes 与 postmortem 内已合并 PR 与
  issue 引用（受认可证据）/ 抑制理由（lint-disable -- reason/coverage-ignore/空 catch 解释：
  修正虚假理由绝不删除）/ 现在时反事实回归钉（without X Y happens/a naive X would…）/ 测量边界
  （measured 出处词承重）/ 运行时新旧状态（old connection drains before new accepts 是运行时
  生命周期）/ 变更故事章节历史阶段名（first cut shipped X 该节安全、索引戳 this cut 处处禁）/
  外部标准引用（RFC 9110 §10.1.5/Figma frame 名——§-禁令只覆盖未提交内部草稿）/ 项目声音与体裁
  形式（we 项目声音/Alternatives-considered）④工作流——显式 scope + 排除 vendored/冻结归档/录制
  夹具快照 → 先只读审计（检索探针含隐藏目录 + 语义判断 + 无模式读最密散文：探针是探针不是定义）→
  按表面先改拥有者（生成物改源再重新生成/双语配对更新对应面重录/模型可见字符串措辞即行为标记快照
  支撑变更）→ 删除前枚举命题 + 过纠正陷阱检查（义务→背书、假说→已交付、删真事实、丢出处）→ 重跑
  探针预期只剩受认可保留 + 剩余引用 HEAD 可解析 + 跑触碰表面门禁）；**repo 专属部分不携带**
  （`references/recall-batteries.md` 具体探针清单与 --hidden 遍历 .agents/ 约定、
  `references/examples.md`、committed-artifact-citations 注记（../../notes/implemented/process/
  2026-08-09-committed-artifact-citations.md）、`.agents/notes/` 树（notes/README 契约/archived
  机制）、docs/AGENTS.md 标准之家、vendor/ 具体路径约定、JSDoc 类型等价围栏与 verify-type-equiv、
  doc-sync / verify-translation-pairing 门禁命令、oxlint-disable 具体工具（抑制理由原则保留）、
  dsh-prose-standard / dsh-translate-docs 子 skill 引用（分别独立收编 D-028/D-029）在 V2 无对应物，
  硬搬注入死引用——原样整体裁决为不适合独立装配）；原文保留在
  `evolution/intake/dsh-trim-cot-leakage/`（Source preservation，D-010 规则 6）
- 原因：DSH Corpus Intake 继续（D-022~D-029 恢复后 Human 送包 = 真实消费需求）；该 Skill 的
  **可迁移方法层**（会话视角泄漏的 HEAD 判定 + 八类分类 + 保留规则 + 过纠正陷阱）是 V2 显式缺环——
  全文检索证伪（chain-of-thought/leakage/推理转录猎杀/session vantage/dead design-session/
  change narration/review choreography/planning residue/indexical/used to/no longer/this cut/
  design ledger 在 domains/ + capabilities/ + maintenance-skills/ + evolution/ 无既有方法覆盖，
  命中均为前序 pattern 的前向引用——prose_standard "会话推理转录猎杀修复归 dsh-trim-cot-leakage
  （V2 尚未收编）"、doc_standards 语料审计廉价探针"会话视角残留"（发现侧）、bilingual_doc_pairing
  "会话推理转录猎杀——那是 dsh-trim-cot-leakage（V2 未收编）"、INT-013/INT-014 "待独立 intake"——
  全是提及/探针/待办，没有会话视角泄漏的分类与修复方法）；`prose_standard`（D-028）= 一般编辑判断
  与完整命题规则（必需背景，原文自述 "dsh-prose-standard owns the complete-proposition rule this
  skill applies"）——本文应用它到会话视角泄漏专项，互补不重复；`doc_standards`（D-024）语料审计第②
  项"会话视角残留——只保留非显然契约与持久理由"是廉价探针（管发现），本文管分类/判定/修复纪律（管
  正确修）——互补不重复；senior-engineer Review 方法层（D-011）"注释陈述非显然契约、标记实现叙述"
  是评审纪律（判定该标记什么），本文提供专项修复标准（该写/该删什么）——互补不重复；**无既有工作面
  可做 Facet Fusion**（prose_standard=一般编辑判断、doc_standards=放置/预算/审计探针、
  bilingual_doc_pairing=配对同步、knowledge-space-maintenance=知识语料维护/归档封存、
  senior-engineer=评审/实现/诊断视角，均不含"会话视角泄漏分类与修复"工作面）；不独立注册
  capabilities/ 装配单位（D-008/D-011/D-022/D-023/D-024/D-025/D-026/D-027/D-028/D-029 先例：
  repo 专属 Skill 不另立单位，原样整体注入死引用）；按 D-004/D-023/D-024/D-025/D-026/D-027/
  D-028/D-029 先例（外部 Skill → domains pattern → experience_push 检索源，D-008 Human 确认
  知识/pattern 形态）收编为 Searchable 知识
- 证据：domains/ai-os/patterns/cot_leakage_trim.md；domains/index.md（ai-os patterns 30→31，
  总 99→100）；evolution/growth.md（dsh-trim-cot-leakage 行）；INT-015；intake README（HTTP 200
  逐字下载）；全文检索证伪（chain-of-thought/leakage/推理转录猎杀/session vantage/change
  narration/planning residue/indexical/used to/no longer/design ledger 仅前向引用或 intake 自身）；
  experience_push 验证探针（"trim chain-of-thought leakage：清理死设计会话引用、变更叙述、评审
  编排、计划残留等会话视角残留，restate at HEAD" 命中 cot_leakage_trim 置顶，内容摘要送达；
  基线探针同查询仅 doc_standards 廉价探针/SUCCESS_LOG 前序融合摘要/prose_standard 低分命中）
- 状态：已送达（可消费位置：domains/patterns → experience_push 检索源，D-004/D-023/D-024/
  D-025/D-026/D-027/D-028/D-029 同款通道）；**pattern 本身的真实 Work Instance 消费（Q1–Q5）
  待自然"清理会话视角残留/审计推理转录"任务触发——UNKNOWN 显式标注，不预先宣称已帮助**；
  Human 验收待确认（TASK-20260824-010）

---

## D-031 · record-browser-gif 外部浏览器演示录制 Skill（2026-08-24）

- 处理：**Skill Fusion（外部 Skill → domains pattern）**——deepseek-ai/deepseek-harness 的
  record-browser-gif（浏览器/Web UI 交互演示录制为优化 GIF + 附 PR 时走资产分支发布）的
  **可迁移方法层**收编为 `domains/ai-os/patterns/browser_gif_evidence.md`（①录制与发布分离——
  录制只产生帧 + 本地 .gif、从不改动远端状态；发布（推 assets 分支 + 嵌入 PR body）是单独最终
  步骤，只在任务包含"把 GIF 附到 PR"时执行，绝不提交进 PR 分支或长命分支 ②按 PR 分阶段——干净
  worktree + 记录精确 commit（git rev-parse HEAD）+ 从该树构建；一端口一 server + 全新 scratch
  状态根 + 浏览器隔离上下文；一个 storyboard = 一次证据运行，捕获失败丢弃重跑、绝不拼接两次运行
  帧 ③真实条件不替换——真实 server/API 演示不用 fixture 查询/mock transport/合成事件注入/
  test-only hook（用户显式要求 fixture 录制除外），不可用则报告限制；不读不暴露凭证值；只记录
  观察到的 setup 支持的声明 ④状态帧捕获——3–6 个语义状态讲一个故事、单一 viewport/crop、帧字典序
  命名、存 gitignored 目录（先 mkdir 否则 ENOENT）、等具体 UI 条件（唯一 locator / exact:true /
  title 变化 / 响应完成）、完成谓词精确文本匹配（不用 includes 子串——prompt echo 假阳性）、
  工具调用/拒绝/恢复加 detail/trajectory 帧、瞬态用慢前台操作 + 同一浏览器脚本调用内轮询 DOM 并
  截图（跨调用状态因回合 settle 丢失）、设计 prompt 使状态真实发生 + settle 哨兵 ⑤编码纪律——
  缺 python3/ffmpeg/ffprobe 报告依赖不擅自安装；逐帧时长（末帧最长）；大产物先降 max-width 再降
  colors/fps；--force 只精确确认路径后用 ⑥产物验证——读编码器 JSON summary（路径/帧数/尺寸/时长/
  字节）、看编码后 GIF 本身（查看器只渲首帧则 ffmpeg 解码代表帧）、git status 确认只落 ignored
  路径、返回绝对路径 + 陈述 transport ⑦资产分支发布（仅附 PR 时）——专用 orphan `<series>-assets`
  分支（先 ls-remote 列既有）、推送前校验和一致 + 只含 media、既有分支走 shallow single-branch
  scratch clone、新系列 fresh shallow clone + switch --orphan、只 append 绝不删除/重写/force-push
  （merged PR body 永久引用）、推送后认证 GitHub API/raw 验证远端路径/字节/校验和/200/image/gif
  （匿名 404 不证伪私有资产，认证验证）、PR body 编辑前后重读 live head 必须仍在记录 commit +
  Markdown API 渲染确认 img + raw blob URL（?raw=true 必需）⑧provenance——GIF 旁陈述 commit SHA/
  tree 与 origin/mode flags 与浏览器状态例外/是否真实模型轮）；**repo 专属部分不携带**
  （`pnpm run build && pnpm run build:web`、`DSH_HOME`/`DSH_AGENTS_HOME` 与 root `.env` 配置路径、
  browser-control skill（V2 无此运行时——映射仓库声明 Playwright + 隔离 headless）、
  `scripts/encode_gif.py` 与 `GIF_SKILL_DIR` 导出约定（V2 无此脚本——编码原则保留，实现用项目
  既有 ffmpeg/python 流程）、`../../notes/implemented/process/2026-08-08-browser-gif-evidence-chain.md`
  （deepseek-harness 决策注记——V2 的 why 由本 pattern + 决策记录承载）、`.playwright-mcp/` 具体
  目录（V2 用等价 gitignored 目录）在 V2 无对应物，硬搬注入死引用——原样整体裁决为不适合独立装配）；
  原文保留在 `evolution/intake/record-browser-gif/`（Source preservation，D-010 规则 6）
- 原因：DSH Corpus Intake 继续（D-022~D-030 恢复后 Human 送包 = 真实消费需求）；该 Skill 的
  **可迁移方法层**（UI 演示证据的生产侧工作流 = 真实树录制/状态帧捕获/编码验证/资产分支发布纪律）
  是 V2 显式缺环——全文检索证伪（gif/browser/录制/record/playwright/截图/screenshot/演示/demo/
  evidence-chain/assets-branch 在 domains/ + capabilities/ + maintenance-skills/ + evolution/
  无既有方法覆盖，命中均为无关提及：verify-before-trust 的"截图对比"验证例子、closure_verify 的
  Playwright 业界参照、cot_leakage_trim 的"录制的夹具与快照"排除项——全是提及/原则/探针，没有
  **作者侧完整工作流**）；`verify-before-trust` = 验证原则（管"永远给可运行检查"），本文 = 演示
  证据怎么真实地做出来（管"何时截/截什么/如何证明状态到达/如何验证编码产物"）——互补不重复；
  `closure_verify` = 端到端对账正确性（扮演链路上下家 + 数据层不变式断言），本文 = 面向人的演示
  artifact 生产与真实性（证明"这个树在这个条件下表现出 X"）——互补不重复；`pre_push_evidence_gate`
  = 推前证据选择与核对（管 outgoing 范围/最小充分证据/远端核对），本文 = GUI PR 证据的生产侧 +
  资产分支发布纪律——互补不重复；`git_safety_net` = 本地文件安全网，本文的 scratch clone/只 append
  不 force 是其 PR 发布场景延伸——互补不重复；**无既有工作面可做 Facet Fusion**（verify-before-trust
  是原则、closure_verify 是验证方法、pre_push_evidence_gate 是推前证据选择、git_safety_net 是本地
  安全网，均不含"UI 演示录制/资产分支发布"工作面）；不独立注册 capabilities/ 装配单位
  （D-008/D-011/D-022/D-023/D-024/D-025/D-026/D-027/D-028/D-029/D-030 先例：repo 专属 Skill
  不另立单位，原样整体注入死引用）；按 D-004/D-023/D-024/D-025/D-026/D-027/D-028/D-029/D-030
  先例（外部 Skill → domains pattern → experience_push 检索源，D-008 Human 确认知识/pattern
  形态）收编为 Searchable 知识
- 证据：domains/ai-os/patterns/browser_gif_evidence.md；domains/index.md（ai-os patterns 31→32，
  总 100→101）；evolution/growth.md（record-browser-gif 行）；INT-016；intake README（HTTP 200
  逐字下载）；全文检索证伪（gif/browser/录制/record/playwright/截图/screenshot/演示/demo/
  evidence-chain/assets-branch 仅无关命中或 intake 自身）；experience_push 验证探针（"录制浏览器
  工作流演示 GIF：按真实 PR 树 staging、状态帧捕获、精确完成谓词、编码后验证、专用 assets 分支发布"
  命中 browser_gif_evidence 置顶，内容摘要送达；基线探针同查询仅 SUCCESS_LOG 前序融合摘要低分命中）
- 状态：已送达（可消费位置：domains/patterns → experience_push 检索源，D-004/D-023/D-024/
  D-025/D-026/D-027/D-028/D-029/D-030 同款通道）；**pattern 本身的真实 Work Instance 消费
  （Q1–Q5）待自然"录制浏览器演示/为 GUI PR 附演示 GIF"任务触发——UNKNOWN 显式标注，不预先宣称
  已帮助**；Human 验收待确认（TASK-20260824-011）

---

## D-032 · DSH Corpus-Level Review（2026-08-24）

- 处理：Corpus 汇总评审（11 个 deepseek-harness Skill：dsh-code-review + DSH Corpus #1~#4/#6~#11）
  → 交付 `evolution/dsh-corpus-review-2026-08-24.md`；裁决汇总 + 记录 INT-017 + SUCCESS_LOG Entry #34
- 裁决（corpus-level）：
  - 已融合（Facet Fusion）：dsh-code-review（senior-engineer Review 面，**唯一真实 Work 验证**
    Entry #20 influence 80，pending repetition）；dsh-archive-agent-notes（knowledge-space-
    maintenance Lifecycle 面）
  - 已转知识（Skill Fusion → Searchable pattern）：其余 9 个（doc_site_projection / doc_standards /
    simplification_audit / dependent_change_landing / pre_push_evidence_gate / prose_standard /
    bilingual_doc_pairing / cot_leakage_trim / browser_gif_evidence）
  - 已拒绝（原样整体）：11/11（repo 专属死引用，无独立装配）；已保留（Source preservation）：
    11/11 原文存 evolution/intake/
  - 待真实 Work 验证（Q1–Q5）：10/11；dsh-code-review 待第二自然样本
  - **DSH 作为 Evolution Line 第一套外部能力吸收实证：Intake/融合/登记/暴露验证流程层面足够；
    "能力帮助 Agent"层面不足（10/11 零消费足迹）；"下批不再需人工解释"层面不足**
- 新发现（架构 Gap）：tools/ 全部工具的 ROOT 按 `__file__` 相对位置解析——只在 D:\AI-os 根目录
  相对调用时正确；从其他工作目录调用时 experience_push 静默读 v1（D:\AI）语料、task_start/task_card
  直接报错（本次复现）。建议下批处理：显式工作目录校验或按环境变量解析根
- 另记：DSH Corpus 编号 #5 跳号无说明；growth 统计 2 Facet Fusion + 9 pattern、0 Reject/0 Shared
  Candidate；Human Predictions 对照 7/11 方向命中、6/11 价值分歧（磁盘裁决系统性更乐观但全部诚实标
  UNKNOWN）
- 证据：evolution/dsh-corpus-review-2026-08-24.md；INT-017；decisions D-011/D-022~D-031；
  growth.md；INT-004/007~016；SUCCESS_LOG #17/#20/#24~#33；复跑 experience_push 探针（双语配对
  160.0 / 推前检查 77.0 置顶，记录数字可复现）
- 状态：评审交付完成；Gap（工具工作目录护栏）待 Human 裁决是否立项修复；10 个 pattern 的真实消费
  仍 UNKNOWN（不因评审而升级）

---

## D-035 · DSH Re-Mapping Pass（2026-08-24）

- 处理：执行 D-034 的下一步——9 个已接入 DSH Skill（doc_site_projection / doc_standards /
  simplification_audit / dependent_change_landing / pre_push_evidence_gate / prose_standard /
  bilingual_doc_pairing / cot_leakage_trim / browser_gif_evidence）的 **Re-Mapping Pass**，
  每个 Skill 一份 Profile（Skill/Source/Core Semantic/Work Contexts/Facet Relations/Knowledge
  Relations/Capability-Skill Relations/Domain Relations/Cross-line Relations/Exposure
  Candidates/Growth Relations/Current Physical Realization/Candidate Changes/
  Confidence-UNKNOWN），交付 `evolution/dsh-remapping-2026-08-24.md`；**只建关系图，
  不做任何物理迁移**（三不动：不动 9 个对象 / 不新建 Capability / 不新建 Taxonomy）
- 结论（关系映射）：
  - 9/9 均验证为**多关系对象**——同时是 Reference Knowledge（domains pattern, Searchable）+
    Evolution 演化对象 + 多数带 senior-engineer Review 相邻面 / knowledge-space-maintenance
    衔接面 / 同族 DSH 拆分链；Physical placement（domains/patterns）只是承载，不是语义身份
    （D-034 模型实证）
  - **Facet 关系 ≠ 知识引用关系**：9/9 判定"无既有工作面可 Facet Fusion"（0 Facet 成员），
    但 5 个 pattern 正文显式引用 senior-engineer Review 面作评审侧互补——非成员却可作 Facet 输入
  - doc 族五对象（doc_site_projection / doc_standards / prose_standard / bilingual_doc_pairing /
    cot_leakage_trim）形成"发现→编辑判断→配对同步→泄漏修复→发布投影"分工链但**非全连通**
    （doc_site_projection 无同族命名链；prose↔bilingual、bilingual→doc_site、cot↔browser、
    dependent↔pre_push 存在单向往缺失）——未物化反向链均为关系候选，非既有关系
  - 9/9 真实 Work 消费 Q1–Q5 维持 UNKNOWN（本映射不升级任何对象状态；presence ≠ use ≠ influence）
- 不执行项：所有 Candidate Changes（补反向引用 / 相关对象索引）**未物化**——待 Human 审阅 +
  充分证据才物理调整（D-034 纪律）；不建工作面索引 / 形态判据表（D-033 纪律）
- 证据：evolution/dsh-remapping-2026-08-24.md（9 份 Profile + 汇总关系图 + 诚实标注）；
  9 个 pattern 全文 + 9 份 intake 原文；D-023~D-031 + D-032/D-034；INT-008~017；growth.md；
  domains/index.md；capabilities/INDEX + senior-engineer.md；maintenance-skills/；
  SUCCESS_LOG #24~#34；复跑全文检索确认引用方向（单向/双向逐文件核对）
- 状态：映射交付完成；待 Human 审阅（关系图）→ 裁决是否物化候选；未 git commit / push
  （任务纪律）；收尾补记 INT-018 + SUCCESS_LOG Entry #35 + task card TASK-20260824-013

---

## D-037 · DSH 试点物化：pre_push_evidence_gate + prose_standard 升级为 Assembled / Conditional 工作模式单位（2026-08-24）

- 处理：执行 D-035 之后的 Human 裁决——从 9 个已接入 DSH 多关系对象中**试点物化 2 个**
  （`pre_push_evidence_gate` / `prose_standard`）：从"纯 domains 知识"升级为"**剔除死引用后的
  完整工作模式单位**（可激活）"。对每个对象执行：
  ① **剔除式整包保留**——以原 `evolution/intake/dsh-*-checks|standard/SKILL.md` 为主体重建
  完整工作模式单位：剔除 pnpm/gh 等 V2 无对应物的死引用（pre_push：`pnpm change-scope` /
  `pnpm exec vitest` / `pnpm run doc-sync|build|test:e2e` / `gh stack push|sync` / `gh pr
  checks|view` / GitHub GraphQL / hook 实现细节；prose：`vendor/` 与 `.agents/notes/archived/`
  具体路径、docs/AGENTS.md 与 cookbook 表单链、`references/examples.md`、dsh-doc-standards /
  dsh-trim-cot-leakage 子 skill 引用），**保留流程整体**（pre_push 七节：inspect outgoing →
  选最小充分证据 → 覆盖度量 → 全量复演三情况 → 历史重写保护 → 发布后验证 → 失败处理 → 推后核对；
  prose 全部编辑标准节：输入与排除 → 保留完整命题 → 12 类位置覆盖 → 工作流 → 边界决策）；
  **"剔除"不是"拆解"**——单位保持完整结构，不是抽方法层当知识（D-033/D-034 纪律）。
  ② **注册为 Assembled / Conditional**——两单位各带 `trigger`（push / force-push / 声称
  "检查通过"之前、历史重写后推送、批处理发布后验证、测试选择困惑；prose：写/评审/恢复/精简/
  审计散文与注释、决定该不该有注释、编辑提示词/可见字符串/诊断）+ `activation`（任务命中 →
  capabilities/INDEX 能力检索 → 读单位全文 → 装载为工作模式 → 执行完整流程 → 检查清单自测），
  注册进 `capabilities/INDEX.md`（既有载体，不新建注册表 / Taxonomy）。
  ③ **domains 原 pattern 保留为 Reference**——domains pattern 不动其方法层内容，只加方向
  引用（指向单位）；单位文件内 `knowledge_ref` 反向指向 pattern 与原文——双向链建立
  （多关系：单位主体 + 知识引用 + 触发，D-034 模型物化）。
  ④ **进既有载体**——capabilities/（Assembled 空间，README 定义"工作模式、整包行为协议"）；
  不新建注册表 / 不新建 Taxonomy / 不新建 Line。
  ⑤ **记录**——growth.md 两行更新（Skill Fusion → domains pattern + 物化 Assembled /
  Conditional 单位）、INT-019（pre_push）/ INT-020（prose）、evolution/README 第六节补条目、
  task card TASK-20260824-014、SUCCESS_LOG Entry #36。
- 原因：D-035 Re-Mapping 实证 9 个对象均为**多关系对象**（Physical placement 只是承载不是
  语义身份）；其中 `pre_push_evidence_gate` 与 `prose_standard` 的原文是**完整工作流**
  （不是方法层摘要），其 domains pattern 已把可迁移方法层蒸馏为知识，但**完整工作模式（可装载
  执行）缺少 Assembled 承载**——"任务命中时装载为工作模式、执行完整流程"这一消费语义此前只有
  senior-engineer（D-006/D-007）实现过；试点这 2 个（Human 裁决）验证"多关系对象 → 多承载"
  的物化路径，不动其他 7 个（纪律）。**不升级消费状态**：物化 = Exposure/承载变化，不是价值
  证明——两单位真实消费 Q1–Q5 维持 UNKNOWN（V2 无远端/CI、无自然编辑任务，显式不宣称已帮助）。
- 证据：capabilities/pre_push_evidence_gate.md + prose_standard.md（新建单位）；
  capabilities/INDEX.md（行 2/3 注册）；domains/ai-os/patterns/pre_push_evidence_gate.md +
  prose_standard.md（方向引用）；原文 evolution/intake/dsh-pre-push-checks/SKILL.md +
  dsh-prose-standard/SKILL.md（整包保留主体）；D-027/D-028（方法层知识来源）；D-034（多关系
  对象模型）；D-033（剔除 ≠ 拆解：不抽方法层）；D-006/D-007（Assembled 装载先例）；
  INT-012/INT-013（前序工作记忆）+ 本任务 INT-019/INT-020；growth.md 两行；experience_push /
  task_start 验证探针（Exposure Path 复跑命中，见 INT-019/020 与 SUCCESS_LOG Entry #36）
- 状态：物化交付完成（2/9 试点）；其余 7 个 DSH 对象未动；未 git commit / push（任务纪律）；
  真实消费验证待自然任务触发（Q1–Q5 UNKNOWN 显式标注）；Human 验收待确认（TASK-20260824-014）

---

## D-039 · DSH 试点物化续：cot_leakage_trim 升级为 Assembled / Conditional 工作模式单位（2026-08-24）

- 处理：执行 D-037 试点路径的延续（Human 派单本任务）——把 `cot_leakage_trim`
  （dsh-trim-cot-leakage，会话推理转录猎杀）从"纯 domains 知识"升级为"**剔除死引用后的
  完整工作模式单位**"（Assembled / Conditional，可激活）。对对象执行：
  ① **剔除式整包保留**——以原 `evolution/intake/dsh-trim-cot-leakage/SKILL.md` 为主体重建
  完整工作模式单位：剔除 `references/recall-batteries.md`（具体探针清单与 `--hidden` 遍历
  `.agents/` 约定）、`references/examples.md`（校准示例文件）、committed-artifact-citations
  注记、`.agents/notes/` 树、`docs/AGENTS.md` 标准之家、`vendor/` 具体路径约定、JSDoc 类型
  等价围栏与 `verify-type-equiv`、`doc-sync` / `verify-translation-pairing` 门禁命令、
  `oxlint-disable` 具体工具（抑制理由原则保留）、dsh-prose-standard / dsh-translate-docs
  子 skill 引用（映射 `prose_standard` / `bilingual_doc_pairing`）等 V2 无对应物的死引用；
  **保留流程整体**（The one test → Taxonomy 八类 → What is not leakage 保留规则 →
  Workflow 五步 + 中文检查清单）；**"剔除"不是"拆解"**——单位保持完整结构（D-033/D-034 纪律）。
  ② **注册为 Assembled / Conditional**——单位带完整 `trigger`（审计/修复读起来像泄漏的推理
  转录的散文、八类泄漏模式、"trim the chain-of-thought" 类指令、判定某段是不是泄漏/某条引用
  该保留还是删除）+ `activation`（任务命中 → capabilities/INDEX 能力检索 → 读单位全文 →
  装载为工作模式 → 执行完整流程 → 检查清单自测），注册进 `capabilities/INDEX.md`（行 4，
  既有载体，不新建注册表 / Taxonomy）。
  ③ **domains 原 pattern 保留为 Reference**——domains pattern 不动其方法层内容，只加方向
  引用（指向单位）；单位文件内 `knowledge_ref` 反向指向 pattern 与原文——双向链建立。
  ④ **进既有载体**——capabilities/（Assembled 空间，README 定义"工作模式、整包行为协议"）。
  ⑤ **记录**——growth.md 行更新（Skill Fusion → domains pattern + 物化 Assembled /
  Conditional 单位）、INT-021、evolution/README 第六节补条目、task card TASK-20260824-015、
  SUCCESS_LOG Entry #37。
- 原因：D-037 试点已实证"多关系对象 → 多承载"物化路径有效（pre_push / prose 两单位 +
  Exposure Path 探针命中；task_start 能力检索 trigger 命中 + experience_push pattern 置顶），
  Human 继续派单验证其余 DSH 对象的同款物化；`cot_leakage_trim` 的原文是**完整工作流**（不是
  方法层摘要），其 domains pattern 已把可迁移方法层蒸馏为知识，但**完整工作模式（可装载执行）
  缺少 Assembled 承载**——与 D-037 两对象同判据（D-034 多关系对象模型物化延续）。
  **不升级消费状态**：物化 = Exposure/承载变化，不是价值证明——单位真实消费 Q1–Q5 维持
  UNKNOWN（无自然会话视角泄漏猎杀任务，显式不宣称已帮助）。
- 证据：capabilities/cot_leakage_trim.md（新建单位）；capabilities/INDEX.md（行 4 注册）；
  domains/ai-os/patterns/cot_leakage_trim.md（方向引用）；原文
  evolution/intake/dsh-trim-cot-leakage/SKILL.md（整包保留主体）；D-030（方法层知识来源 +
  不携带清单）；D-034（多关系对象模型）；D-033（剔除 ≠ 拆解：不抽方法层）；D-037（试点物化
  先例）；INT-015（前序工作记忆）+ 本任务 INT-021；growth.md 行；experience_push / task_start
  验证探针（Exposure Path 复跑命中，见 INT-021 与 SUCCESS_LOG Entry #37）
- 状态：物化交付完成（3/9 已物化：pre_push / prose / cot；其余 6 个 DSH 对象未动）；未 git
  commit / push（任务纪律）；真实消费验证待自然任务触发（Q1–Q5 UNKNOWN 显式标注）；Human
  验收待确认（TASK-20260824-015）

---

## D-040 · DSH 试点物化续：doc_site_projection 升级为 Assembled / Conditional 工作模式单位（2026-08-24）

- 处理：执行 D-037/D-039 试点路径的延续（Human 派单本任务）——把 `doc_site_projection`
  （dsh-doc-site-sync，文档站受测投影）从"纯 domains 知识"升级为"**剔除死引用后的
  完整工作模式单位**"（Assembled / Conditional，可激活）。对对象执行：
  ① **剔除式整包保留**——以原 `evolution/intake/dsh-doc-site-sync/SKILL.md` 为主体重建
  完整工作模式单位：剔除 `website/docs.ts`（DocsPage 字段集与 `pairedPages()` /
  `mirroredPages()` 实现）、`website/.vitepress/config.ts` 具体配置、
  `scripts/project-doc-site.ts` 投影器、raw-Markdown twin + `llms.txt` 具体实现、翻译
  triplet 契约（foo.md / foo.zh.md / foo.i18n.yaml 与禁 `zh-CN/` 语言目录）、`pnpm
  docs:dev` / `docs:check` / `doc-sync` / `lint` 命令、`verify-doc-site-fragments`、
  `docs/AGENTS.md` 与 `docs/i18n/README.md` 具体文件、`website/` 具体路径约定、
  dsh-doc-standards / dsh-pre-push-checks 子 skill 引用（映射 `doc_standards` /
  `pre_push_evidence_gate`）等 V2 无对应物的死引用；**保留流程整体**（读拥有契约 →
  变更分类 → manifest 白名单条目维护（字段显式设定）→ 链接保留（缺失目标即投影失败）→
  预览与验证门 → 部署分离 + 中文检查清单）；**"剔除"不是"拆解"**——单位保持完整结构
  （D-033/D-034 纪律）。
  ② **注册为 Assembled / Conditional**——单位带完整 `trigger`（发布/更新/移动/删除文档站
  页面、编辑站点 manifest 映射或导航、诊断页面缺失/投影链接失效、修复投影链接、站点内容
  变更后跑预览/聚焦检查/同步工作流、建立或改造项目文档站）+ `activation`（任务命中 →
  capabilities/INDEX 能力检索 → 读单位全文 → 装载为工作模式 → 执行完整流程 → 检查清单
  自测），注册进 `capabilities/INDEX.md`（行 5，既有载体，不新建注册表 / Taxonomy）。
  ③ **domains 原 pattern 保留为 Reference**——domains pattern 不动其方法层内容，只加方向
  引用（指向单位）；单位文件内 `knowledge_ref` 反向指向 pattern 与原文——双向链建立。
  ④ **进既有载体**——capabilities/（Assembled 空间，README 定义"工作模式、整包行为协议"）。
  ⑤ **记录**——growth.md 行更新（Skill Fusion → domains pattern + 物化 Assembled /
  Conditional 单位）、INT-022、evolution/README 第六节补条目、task card
  TASK-20260824-016、SUCCESS_LOG Entry #38。
- 原因：D-037/D-039 试点已实证"多关系对象 → 多承载"物化路径有效（pre_push / prose / cot
  三单位 + Exposure Path 探针命中；task_start 能力检索 trigger 命中 + experience_push
  pattern 置顶），Human 继续派单验证其余 DSH 对象的同款物化；`doc_site_projection` 的原文
  是**完整工作流**（不是方法层摘要），其 domains pattern 已把可迁移方法层蒸馏为知识，但
  **完整工作模式（可装载执行）缺少 Assembled 承载**——与 D-037/D-039 同判据（D-034 多关系
  对象模型物化延续）。**不升级消费状态**：物化 = Exposure/承载变化，不是价值证明——单位
  真实消费 Q1–Q5 维持 UNKNOWN（V2 无文档站基建、无自然文档站任务，显式不宣称已帮助）。
- 证据：capabilities/doc_site_projection.md（新建单位）；capabilities/INDEX.md（行 5 注册）；
  domains/ai-os/patterns/doc_site_projection.md（方向引用）；原文
  evolution/intake/dsh-doc-site-sync/SKILL.md（整包保留主体）；D-023（方法层知识来源 +
  不携带清单）；D-034（多关系对象模型）；D-033（剔除 ≠ 拆解：不抽方法层）；D-037/D-039
  （试点物化先例）；INT-008（前序工作记忆）+ 本任务 INT-022；growth.md 行；experience_push /
  task_start 验证探针（Exposure Path 复跑命中，见 INT-022 与 SUCCESS_LOG Entry #38）
- 状态：物化交付完成（4/9 已物化：pre_push / prose / cot / doc_site；其余 5 个 DSH 对象未动）；
  未 git commit / push（任务纪律）；真实消费验证待自然任务触发（Q1–Q5 UNKNOWN 显式标注）；
  Human 验收待确认（TASK-20260824-016）

---

## D-041 · DSH 试点物化续：doc_standards 升级为 Assembled / Conditional 工作模式单位（2026-08-24）

- 处理：执行 D-037/D-039/D-040 试点路径的延续（Human 派单本任务）——把 `doc_standards`
  （dsh-doc-standards，文档放置与预算标准）从"纯 domains 知识"升级为"**剔除死引用后的
  完整工作模式单位**"（Assembled / Conditional，可激活）。对对象执行：
  ① **剔除式整包保留**——以原 `evolution/intake/dsh-doc-standards/SKILL.md` 为主体重建
  完整工作模式单位：剔除 `docs/AGENTS.md`（标准之家）、`.agents/notes/README.md`
  （Agent Notes 契约与 verify-agent-note-format）、`docs/postmortem/README.md`、
  `docs/i18n/README.md`、根 `AGENTS.md` 具体文件、Archived Agent Notes 具体树、
  `pnpm run verify-doc-budgets` / `verify-md-links` / `verify-doc-refs` / `change-scope` /
  `doc-sync` / `lint` / `verify-translation-pairing` 命令族、`git ls-files '*.md' |
  xargs wc -w` 流水线、JSDoc 类型等价围栏、翻译 triplet 契约、`.agents/notes/` implemented /
  archived 目录契约、dsh-prose-standard / dsh-trim-cot-leakage / dsh-find-simplifications
  子 skill 引用（映射 `prose_standard` / `cot_leakage_trim` / `simplification_audit`）等
  V2 无对应物的死引用；**保留流程整体**（Sources of truth → Review structure before prose
  （五步 + 放置约束）→ Audit the corpus（最廉价探针先行六步）→ 承重规则保留 → 预算
  relocate-condense-raise → 验证汇报 + 中文检查清单）；**"剔除"不是"拆解"**——单位保持
  完整结构（D-033/D-034 纪律）。
  ② **注册为 Assembled / Conditional**——单位带完整 `trigger`（写/移动/评审/审计仓库文档、
  决定文档层级/教程-vs-参考/长度、文档太长/重复/会话残留、"improve / audit the docs" 类
  指令、文档预算失败信号）+ `activation`（任务命中 → capabilities/INDEX 能力检索 → 读单位
  全文 → 装载为工作模式 → 执行完整流程 → 检查清单自测），注册进 `capabilities/INDEX.md`
  （行 6，既有载体，不新建注册表 / Taxonomy）。
  ③ **domains 原 pattern 保留为 Reference**——domains pattern 不动其方法层内容，只加方向
  引用（指向单位）；单位文件内 `knowledge_ref` 反向指向 pattern 与原文——双向链建立。
  ④ **进既有载体**——capabilities/（Assembled 空间，README 定义"工作模式、整包行为协议"）。
  ⑤ **记录**——growth.md 行更新（Skill Fusion → domains pattern + 物化 Assembled /
  Conditional 单位）、INT-023、evolution/README 第六节补条目、task card
  TASK-20260824-017、SUCCESS_LOG Entry #39。
- 原因：D-037/D-039/D-040 试点已实证"多关系对象 → 多承载"物化路径有效（pre_push / prose /
  cot / doc_site 四单位 + Exposure Path 探针命中；task_start 能力检索 trigger 命中 +
  experience_push pattern 置顶），Human 继续派单验证其余 DSH 对象的同款物化；`doc_standards`
  的原文是**完整工作流**（不是方法层摘要），其 domains pattern 已把可迁移方法层蒸馏为知识，
  但**完整工作模式（可装载执行）缺少 Assembled 承载**——与 D-037/D-039/D-040 同判据
  （D-034 多关系对象模型物化延续；D-035 Re-Mapping Profile §2 已列多关系对象 +
  Conditional 候选）。**不升级消费状态**：物化 = Exposure/承载变化，不是价值证明——单位
  真实消费 Q1–Q5 维持 UNKNOWN（无自然"文档编写/移动/审计"任务，显式不宣称已帮助）。
- 证据：capabilities/doc_standards.md（新建单位）；capabilities/INDEX.md（行 6 注册）；
  domains/ai-os/patterns/doc_standards.md（方向引用）；原文
  evolution/intake/dsh-doc-standards/SKILL.md（整包保留主体）；D-024（方法层知识来源 +
  不携带清单）；D-034（多关系对象模型）；D-033（剔除 ≠ 拆解：不抽方法层）；D-037/D-039/
  D-040（试点物化先例）；INT-009（前序工作记忆）+ 本任务 INT-023；growth.md 行；
  experience_push / task_start 验证探针（Exposure Path 复跑命中，见 INT-023 与
  SUCCESS_LOG Entry #39）
- 状态：物化交付完成（5/9 已物化：pre_push / prose / cot / doc_site / doc_standards；
  其余 4 个 DSH 对象未动）；未 git commit / push（任务纪律）；真实消费验证待自然任务触发
  （Q1–Q5 UNKNOWN 显式标注）；Human 验收待确认（TASK-20260824-017）

---

## D-042 · DSH 试点物化续：simplification_audit 升级为 Assembled / Conditional 工作模式单位（2026-08-24）

- 处理：执行 D-037/D-039/D-040/D-041 试点路径的延续（Human 派单本任务）——把
  `simplification_audit`（dsh-find-simplifications，证据驱动的代码简化审计）从"纯 domains
  知识"升级为"**剔除死引用后的完整工作模式单位**"（Assembled / Conditional，可激活）。
  对对象执行：
  ① **剔除式整包保留**——以原 `evolution/intake/dsh-find-simplifications/SKILL.md` 为
  主体重建完整工作模式单位：剔除 `AGENTS.md` 与 `docs/defensive-patterns.md` /
  `docs/testing.md` / `docs/architecture.md` 具体文件、`.agents/notes/` 树（README 规则与
  implemented 具体例子）、`docs/development.md` urgency 语义、`notes/implemented/process/
  2026-07-26-dependencies-over-hand-rolling.md` 具体记录、`pnpm run doc-sync` / `lint` /
  `git diff --check` 具体命令链与 pre-push hook、PR folding 工作流（sibling branch vs
  origin/master、PR body 更新、draft → ready）、knip 特指、dsh-archive-agent-notes 子 skill
  引用（映射 `knowledge-space-maintenance` Lifecycle / Archive facet）等 V2 无对应物的死
  引用；**保留流程整体**（Start With Repo Context → What Counts As A Strong Candidate →
  Survey Broadly → Audit Trust And Lifecycle Boundaries → Hand-Rolled Code Versus A
  Dependency → Prove Or Reject Each Candidate → Coalesce Superseded Notes → Write The
  Proposal → Inline TODO Notes → When Folding Another PR Or Branch → Validation And Reporting
  Hygiene + 中文检查清单）；**"剔除"不是"拆解"**——单位保持完整结构（D-033/D-034 纪律）。
  ② **注册为 Assembled / Conditional**——单位带完整 `trigger`（"find things to simplify" /
  "找简化候选" / "简化这个代码库" / 减面 / 去冗余 / 删死代码、重构前全量简化候选审计、评审中
  需证据支撑的移除提案、审计/归并已被取代的记录、折叠另一分支的简化想法、写内联
  TODO/FIXME/XXX）+ `activation`（任务命中 → capabilities/INDEX 能力检索 → 读单位全文 →
  装载为工作模式 → 执行完整流程 → 检查清单自测），注册进 `capabilities/INDEX.md`（行 7，
  既有载体，不新建注册表 / Taxonomy）。
  ③ **domains 原 pattern 保留为 Reference**——domains pattern 不动其方法层内容，只加方向
  引用（指向单位）；单位文件内 `knowledge_ref` 反向指向 pattern 与原文——双向链建立。
  ④ **进既有载体**——capabilities/（Assembled 空间，README 定义"工作模式、整包行为协议"）。
  ⑤ **记录**——growth.md 行更新（Skill Fusion → domains pattern + 物化 Assembled /
  Conditional 单位）、INT-024、evolution/README 第六节补条目、task card
  TASK-20260824-018、SUCCESS_LOG Entry #40。
- 原因：D-037/D-039/D-040/D-041 试点已实证"多关系对象 → 多承载"物化路径有效（pre_push /
  prose / cot / doc_site / doc_standards 五单位 + Exposure Path 探针命中；task_start 能力
  检索 trigger 命中 + experience_push pattern 置顶），Human 继续派单验证其余 DSH 对象的
  同款物化；`simplification_audit` 的原文是**完整工作流**（不是方法层摘要），其 domains
  pattern 已把可迁移方法层蒸馏为知识，但**完整工作模式（可装载执行）缺少 Assembled 承载**
  ——与 D-037/D-039/D-040/D-041 同判据（D-034 多关系对象模型物化延续；D-035 Re-Mapping
  Profile §3 已列多关系对象 + Conditional 候选）。**不升级消费状态**：物化 = Exposure/
  承载变化，不是价值证明——单位真实消费 Q1–Q5 维持 UNKNOWN（无自然"找简化候选/减面/删死代码"
  任务，显式不宣称已帮助）。
- 证据：capabilities/simplification_audit.md（新建单位）；capabilities/INDEX.md（行 7 注册）；
  domains/ai-os/patterns/simplification_audit.md（方向引用）；原文
  evolution/intake/dsh-find-simplifications/SKILL.md（整包保留主体）；D-025（方法层知识
  来源 + 不携带清单）；D-034（多关系对象模型）；D-033（剔除 ≠ 拆解：不抽方法层）；
  D-037/D-039/D-040/D-041（试点物化先例）；INT-010（前序工作记忆）+ 本任务 INT-024；
  growth.md 行；experience_push / task_start 验证探针（Exposure Path 复跑命中，见
  INT-024 与 SUCCESS_LOG Entry #40）
- 状态：物化交付完成（6/9 已物化：pre_push / prose / cot / doc_site / doc_standards /
  simplification_audit；其余 3 个 DSH 对象未动）；未 git commit / push（任务纪律）；
  真实消费验证待自然任务触发（Q1–Q5 UNKNOWN 显式标注）；Human 验收待确认
  （TASK-20260824-018）

---

## D-043 · test-driven-development 外部 Skill 接入（2026-08-24）

- 处理：**独立接入为 Assembled / Conditional 完整工作模式单位**——外部 Skill
  （obra/superpowers `skills/test-driven-development/SKILL.md`，Evolution Intake
  "test-driven-development"）按整包保持完整接入 `capabilities/test-driven-development.md`
  （Iron Law → RED → Verify RED → GREEN → Verify GREEN → REFACTOR → 合理化拦截表 →
  Red Flags → 检查清单；原文逐字主体 + 【V2 注】命令/工具映射，不删除原流程任何一步）；
  注册 `capabilities/INDEX.md` 行 8（trigger + activation 完整）；
  **既有 domains pattern `testing-tdd` 保留为知识侧 Reference**（RED-GREEN-REFACTOR 核心
  循环 / 适用边界 / 既有外部标杆映射），只加方向引用（指向单位），单位 `knowledge_ref`
  反向指向 pattern 与原文——双向链建立；不进新注册表 / Taxonomy。
- 原因：① 形态判定（capability-reconstitution + D-005/D-034）——该 Skill 是**完整工作模式
  整包**（测试先行纪律 / Verify RED-GREEN 强制 / 例外裁决 / 合理化拦截 / Red Flags /
  检查清单），不是原子方法层；默认保持完整不拆解。② 关系判定（D-034 多关系对象）——
  V2 已存在 `testing-tdd` pattern（知识侧：核心循环 + 适用边界，Searchable via
  experience_push，既有外部标杆映射），但**完整可装载工作模式（Assembled 承载）此前在 V2
  缺失**；知识侧已有 ≠ 工作模式已有（D-037 系列先例同判据）。③ 该 Skill 的 trigger 是
  实现类任务普适触发（新功能 / 修 bug / 重构 / 行为变更）——与 DSH 各工作面的条件触发不同，
  TDD 是**默认应装载的实现工作模式**，但仍按保守 Exposure 定级为 Conditional →
  Assembled / Activated（不提升 Global；由未来真实使用频率与范围决定，D-007 同款逻辑）。
  ④ `writing-good-tests.md` 配套文件不在 intake 内——不虚构其内容，只以【V2 注】标注缺失
  并映射既有知识侧等价原则。
- 证据：capabilities/test-driven-development.md（新建单位）；capabilities/INDEX.md（行 8
  注册）；domains/ai-os/patterns/testing-tdd.md（方向引用，双向链）；原文
  evolution/intake/test-driven-development/SKILL.md（整包保留主体）；intake README
  （HTTP 200 逐字下载）；D-005/D-033/D-034/D-037 系列（形态判定 / 剔除≠拆解 / 多关系 /
  物化先例）；task_start 探针（trigger 命中，见 INT-025 与 SUCCESS_LOG Entry #41）；
  experience_push 探针（testing-tdd pattern 命中，知识侧通道可核）
- 状态：接入交付完成（单位落位 + INDEX 注册 + 双向引用 + 记录四件套）；未 git commit /
  push（任务纪律）；真实 TDD 完整装载消费 Q1–Q5 维持 UNKNOWN（V2 自然实现任务尚未按本
  工作模式完整装载执行，显式不宣称已帮助）；Human 验收待确认（TASK-20260824-019）

## D-044 · V2 tools ROOT 断言双保险（D-036 补充兑现 · 2026-08-24）

- 处理：新增 `tools/_root_guard.py`——断言 guard 模块真实路径必须等于唯一权威
  `D:\AI-os\tools`；五个 V2 工具（experience_push / task_card / task_start /
  wrapup_sync / observe_extract）启动时在解析 ROOT 前调用 `guard(__file__)`；任何
  拷贝/移动到其他位置运行 → fail-closed（exit 1），不再可能静默读 v1 树。
- 原因：D-036 已把 v1 镜像工具移入 `D:\AI\tools\_v1-archived\` 并 fail-closed；
  本项是 D-036 原"补充建议（未执行，待定）"，Human 裁决"做"后兑现——第二道保险，
  防未来错误副本出现（拷贝副本即使连同 guard 一起拷走，也会因不在权威目录而失败）。
- 验证：`python D:\AI-os\tools\task_start.py --help` / `experience_push.py --help`
  正常；把 experience_push.py + _root_guard.py 一起拷到
  `D:\AI\scratch\tmp\guard_test_*` 运行 → `[root-guard] FAIL-CLOSED`，exit 1。
- 状态：已执行（2026-08-24）；D-036 补充建议行同步更新；INT-017 Next ① 关闭。

  **v2 修正（2026-08-24 · 发布验证驱动）**：发布后 clone 实测发现，硬编码
  `D:\AI-os\tools` 使发布版在任何非 D:\AI-os 路径全部 fail-closed——违背
  "下载下来能正常使用"。改为**结构断言**：tools 脚本必须在自身 tools 目录内，
  且父目录具备 V2 结构标志（AGENTS.md + capabilities/INDEX.md + domains/patterns），
  否则 fail-closed。v1 树无 capabilities/INDEX.md，防污染能力保留；发布 clone
  （结构完整）任意路径可用。验证：D:\AI-os 正常 / v1 模拟树 FAIL-CLOSED /
  发布 clone task_start + experience_push 正常。
