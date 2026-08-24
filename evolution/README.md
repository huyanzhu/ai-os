# Evolution Mode — 怎么让 AI-OS 获得 / 重塑一个 Capability

> **入口**：Work Mode（怎么使用 AI-OS）在根 `README.md`；本目录回答"我怎么让一个 Capability 进入 AI-OS，或改变一个已有 Capability"。
> **核心资产**：Capability Reconstitution Skill + 五个真实 Exemplars（不是研究文档）。

---

## 一、核心 Skill

[capability-reconstitution.md](capability-reconstitution.md) —— 把任意 Capability 一步步带到真实可消费状态的过程（可复用的是**过程**，不是某次答案）。

## 二、五个真实 Exemplars（照做样本）

| Exemplar | 学到的东西 | 结果 |
|---|---|---|
| [A16 Working Memory](exemplars/A16.md) | 如何让 Capability 进入正常工作闭环，并跨轮消费 | 独立重塑 |
| [A11/A18 Searchable](exemplars/A11-A18.md) | 如何把候选从"存在"推到"进入决策空间" | Delivery Reshape |
| [D07 → A22](exemplars/D07-A22.md) | 如何发现 Capability 已被其他 Capability 吸收 | 融合 |
| [A19 SUCCESS_LOG](exemplars/A19.md) | 从 Conceptual Gap → 最小 Reshape → Persistence | 重新进入决策空间 |
| [Learning Closure](exemplars/Learning-Closure.md) | 把完全没进入 Agent 模型的概念最小化带入决策空间，形成 Learning Loop | 闭环首验 |

## 三、输入来源（Capability 可以是）

```text
V1 Heritage（历史能力）
外部 Skill（Human 发现并引入）
Human Want
Runtime 观察暴露的新缺口
已有 Capability 的新问题
```

## 四、双实例运行

```text
Work Instance      —— 正常真实工作，产生 Knowledge/Evidence/Gap/Want
Evolution Instance —— 消化这些 + Human Want + 外部 Skill，用本 Skill 重塑 Capability，送回 Work
```

> 本目录 = Evolution Instance 的工作台。

---

## 五、Evolution 工作记忆与裁决记录（V0.1 · 2026-08-23）

- `workspace/INT-xxx.md` —— 演化工作项：正在把哪个 Capability 带到哪里（当前阶段 / 状态 / 发现 / 下一步 / 证据 / 裁决）。开工与收尾时更新。
- `decisions.md` —— 裁决日志（append-only）：为什么这个 Capability 被这样处理；后续演化工作先读，继承前一次判断。

> 语义对应 Work 线的 task_cards（工作记忆）与 SUCCESS_LOG（承重账本），但只记录演化维度。

---

## 六、Capability Space（可装配能力 · V0.2 · 2026-08-23）

- `capabilities/` —— 完整 Skill / 角色整包单位（不默认拆解）；Work 任务开始时经 bootstrap 能力检索步骤装载。
- 语义：第三种消费形态——知识=检索（experience_push）、工具=调用（tools/）、角色/整包=装载（capabilities/）。

> DSH Corpus 编号 #1–#4、#6–#11（**#5 因早期编号错位未分配**；以 Evolution intake 编号 #5–#14 连续为准，2026-08-24 说明）。
- 首个整包单位已注册：senior-engineer（Evolution Intake #3 → INT-003 / D-006）。
- Review Facet 方法层融合完成：dsh-code-review（Evolution Intake #4 → INT-004 / D-011）——D-010
  "以 Review 类外部 Skill 验证 Facet Fusion"落地：可迁移方法层归 senior-engineer Review 面，
  repo 专属机制不携带（原样整体不适合独立装配）。
- 维护方法层融合完成：dsh-archive-agent-notes（Evolution Intake #5 → INT-007 / D-022）——可迁移
  方法层归 knowledge-space-maintenance 的 Lifecycle / Archive facet（v3：supersession 审计 /
  未来价值分类 / 归档封存纪律 / 验证汇报），repo 专属机制不携带（triplet 归档 / pnpm 验证器 /
  dsh-pre-push-checks 在 V2 无对应物，原样整体不适合独立装配）。
- 文档站方法层收编完成：dsh-doc-site-sync（Evolution Intake #6 / DSH Corpus #2 → INT-008 /
  D-023）——可迁移方法层归 domains pattern `doc_site_projection`（仓库 Markdown 单一源 → 站点
  受测投影：变更分类 / manifest 白名单 / 链接保留 / 验证门 / 部署分离；Searchable via
  experience_push，D-004 同款通道），repo 专属机制不携带（docs.ts / 投影器 / VitePress / pnpm /
  翻译 triplet 在 V2 无对应物，原样整体不适合独立装配；无既有工作面可 Facet Fusion）。
- 文档标准方法层收编完成：dsh-doc-standards（Evolution Intake #7 / DSH Corpus #3 → INT-009 /
  D-024）——可迁移方法层归 domains pattern `doc_standards`（结构先行 / 教程 vs 参考用途分类 /
  预算纪律 / 语料审计廉价探针；Searchable via experience_push，D-004 同款通道），repo 专属机制
  不携带（pnpm 验证器 / docs/AGENTS.md 标准之家 / 翻译 triplet / .agents/notes 契约在 V2 无对应物，
  原样整体不适合独立装配；无既有工作面可 Facet Fusion——doc_site_projection=发布投影 /
  doc-generation=文档产出 / knowledge-space-maintenance=知识语料维护，均不含"文档放置/标准"工作面）。
- 代码简化审计方法层收编完成：dsh-find-simplifications（Evolution Intake #8 / DSH Corpus #4 →
  INT-010 / D-025）——可迁移方法层归 domains pattern `simplification_audit`（强候选证据判据 /
  消费方分类（生产-非生产-模糊语料）/ 信任与生命周期边界审计 / 依赖替换净删除衡量 / 证明或拒绝 /
  内联 TODO 稳定标签 / 提案写作 V2 映射 / added-then-removed 记录收编判据；Searchable via
  experience_push，D-004/D-023/D-024 同款通道），repo 专属机制不携带（.agents/notes 树 / pnpm
  验证器与 pre-push hook / PR folding / knip 特指在 V2 无对应物，原样整体不适合独立装配；无既有
  工作面可 Facet Fusion——senior-engineer 四面 / knowledge-space-maintenance / doc 族 pattern 均
   不含"代码简化审计"工作面；记录收编部分由 Lifecycle facet（D-022）承接，本 skill 仅补充判据）。
- 依赖变更落库方法层收编完成：dsh-merging-stacked-prs（Evolution Intake #9 / DSH Corpus #6 →
  INT-011 / D-026）——可迁移方法层归 domains pattern `dependent_change_landing`（官方机制优先
  不可用即硬停 / 依赖链以实时状态为准 / 补链纪律 / 只在需要时刷新且重写后重新审计 / 整链预检 /
  官方批量 API 整链或显式边界前缀落库（all-or-nothing）/ 落库后验证真正完成 + 剩余链复查 /
  分支清理单独最后一步且零依赖才删；Searchable via experience_push，D-004/D-023/D-024/D-025
  同款通道），repo/平台专属机制不携带（`gh stack` 命令族 / GitHub GraphQL 栈查询 / 官方
  stacked-PR 扩展与 merge-queue 语义在 V2 无对应物——V2 的 git 是本地仓库 + 文件安全网纪律，
  原样整体不适合独立装配；无既有工作面可 Facet Fusion——senior-engineer 四面 /
  knowledge-space-maintenance / doc 族 pattern / git_safety_net 均不含"依赖变更落地"工作面，
  git_safety_net 是本地文件安全带，互补不重复）。
- 推送前证据闸门方法层收编完成：dsh-pre-push-checks（Evolution Intake #10 / DSH Corpus #7 →
  INT-012 / D-027）——可迁移方法层归 domains pattern `pre_push_evidence_gate`（outgoing 范围
  确认（base ref 实时远端/栈状态）/ 按行为变更面选最小充分证据不反射跑全量 / 覆盖度量纪律 /
  全量复演仅三情况 / 历史重写保护（远端 OID + force-with-lease，绝不 raw --force，重写后重审）/
  发布后验证例外 / 失败即停 + 环境特定失败证明 / 推送后远端核对 + "no checks reported" 先读
  mergeability；Searchable via experience_push，D-004/D-023/D-024/D-025/D-026 同款通道），
  repo 专属机制不携带（pnpm change-scope/vitest/doc-sync/build/test:e2e、`gh stack`/`gh pr
  checks` 与 GitHub GraphQL、hook 实现细节在 V2 无对应物，原样整体不适合独立装配；无既有工作面
  可 Facet Fusion——senior-engineer 四面 / knowledge-space-maintenance / doc 族 pattern /
  dependent_change_landing（共享 force 禁令与重写重审原则，工作面不同）/ git_safety_net
  （本地文件安全带，互补不重复）均不含"outgoing diff 推前证据选择"工作面）。
- 散文与注释编辑判断方法层收编完成：dsh-prose-standard（Evolution Intake #11 / DSH Corpus #8 →
  INT-013 / D-028）——可迁移方法层归 domains pattern `prose_standard`（显式 scope 与 mode 纪律
  （automatic 默认 / interactive 仅显式要求；mode 控提问不控写权）/ 排除 vendored 与冻结归档、
  派生物先改源再重新生成 / 编辑前识别并保留完整命题（actor-action、条件-时序、模态 must-may-never、
  负向保证与例外、所有权-副作用-失败-后果；字少本身不是改进）/ 局部契约完整 + 架构理由激进链接
  唯一归属（一个解释一个家）/ 非显然理由保留 / 按 12 类位置覆盖必需契约（公开 JSDoc、内部注释、
  模块注释、测试、cookbook、README、Agent Notes、postmortem、skills 与 agent 指令、示例与配置
  注释、提示词与可见字符串、诊断）/ 词检查（contract/boundary/shape/surface/seam/gate/vocabulary
  用前检查非禁用）/ 七步工作流（scope 确认 → 先读标准与拥有代码 → 全范围语义判断 → 分类 keep-add-
  trim-restore-restructure-defer → 先改拥有者再派生物 → 窄检查 + git diff --check + 可见字符串
  行为测试 → 汇报）/ 边界决策（borderline 定义、automatic 应用明确编辑并如实报告不弱化命题、
  interactive 分组 + 2-3 版本 + 推荐、决定后提炼进 examples 并应用到所有相似段落；Searchable via
  experience_push，D-004/D-023/D-024/D-025/D-026/D-027 同款通道），repo 专属机制不携带
  （vendor/ 具体路径与 .agents/notes 树、docs/AGENTS.md 标准之家、package README requirements
  仓库表单、references/examples.md、JSDoc 类型等价围栏、翻译 triplet、dsh-doc-standards /
  dsh-trim-cot-leakage 子 skill 引用在 V2 无对应物或分别独立 intake——doc_standards 已收编
  D-024，trim-cot-leakage 已收编 D-030（2026-08-24），原样整体不适合独立装配；无既有工作面可 Facet Fusion——
  doc_standards=放置/预算/审计、senior-engineer=评审/实现/诊断视角（评审纪律判定"该标记什么"、
  本文提供"该写/该删什么"的编辑标准）、knowledge-space-maintenance=知识语料维护，均不含
  "散文编辑判断/契约保留"工作面）。
- 双语配对文档工作流方法层收编完成：dsh-translate-docs（Evolution Intake #12 / DSH Corpus #9 →
  INT-014 / D-029）——可迁移方法层归 domains pattern `bilingual_doc_pairing`（按变更类型分诊
  （Update 走 briefing 驱动最小更新 / New pair 走整篇翻译 / 删除重命名同步对应面 / 冻结归档不动）/
  briefing = 译者完整工作集（最小可对齐粒度：变化 Markdown 单元 → 整节 → 整文档；委托子 agent 不
  重读语料/不重推 diff）/ 最小编辑覆盖 diff（绝不因一次更新重译整篇——保留已审措辞）/ 整篇翻译两遍
  法（Pass 1 写不逐字对应 → Pass 2 逐句对照源核验保真 → 单独读译文改孤立拗口）/ 术语表双向绑定先
  载入（未列术语须有可引用 OSS/厂商先例，否则英文 + 待定术语，绝不临时自造）/ 代码块两侧字节一致 /
  链接保持语义目标与精确 query/fragment（语料内按语言后缀切换、缺对应面是错误）/ 结构对齐手工核验
  （标题层级/围栏/表格/列表/有序起点/链接语种）/ 确认一致后才记录配对状态 + 汇报新 vs 更新 + 列出
  待定术语；Searchable via experience_push，D-004/D-023/D-024/D-025/D-026/D-027/D-028 同款
  通道），repo 专属机制不携带（pnpm gen-translation-brief / verify-translation-pairing 命令族、
  foo.i18n.yaml 双侧 blob 哈希一致性记录、语言切换行仓库格式、docs/i18n 具体文件、
  scripts/translation-pairing.manifest.json、doc-sync / verify-md-wrap / verify-md-links 门禁、
  .agents/notes/archived 三元组封存契约与 dsh-code-review / dsh-prose-standard / dsh-pre-push-
  checks 子 skill 引用在 V2 无对应物或分别独立 intake，原样整体不适合独立装配；无既有工作面可
  Facet Fusion——prose_standard=单侧散文编辑判断、doc_standards=放置/预算/审计、doc_site_
  projection=发布投影、doc-generation=文档产出、knowledge-space-maintenance=知识语料维护、
  senior-engineer=评审视角，均不含"配对文档同步工作流"工作面）。
- 会话推理转录猎杀方法层收编完成：dsh-trim-cot-leakage（Evolution Intake #13 / DSH Corpus #10 →
  INT-015 / D-030）——可迁移方法层归 domains pattern `cot_leakage_trim`（HEAD 视角测试（无任何
  会话转录/PR 线程/未提交草稿的读者能否解析每个引用、核验每个声明——不能 → 重述存活事实 + 删除
  其余；能 → 不是泄漏，但可解析只过本 skill 的杆，当前状态面上可解析的变更故事仍是变更叙述按第 3
  类送回许可之家）/ 八类泄漏分类（①死设计会话引用——(decision 7)/(audit C2)/design §4.7/phase
  标签/design ledger/(B ruling)：有已提交拥有者按名+路径引用否则删引用重述事实子句 ②栈与 PR 视角
  ——a later PR in this stack/this PR adds/the previous commit：陈述已交付机制或扩展点、延后转
  TODO/issue ③变更叙述与版本戳——used to/no longer/the old X/索引戳 v1 this cut today now：
  陈述当前行为、已修复回归用现在时反事实 without X Y happens、绝不写仓库历史 ④评审编排——
  Rejected in review/the reviewer confirmed/草稿序号 v5 of this note/轮次归属：保留决策与理由删
  谁在何时说的 ⑤评审者定向辩护——the cast is safe — it simply…/this is correct because…：
  陈述安全不变式或代码已显示时删除 ⑥复述与推导转录——控制流叙述/测试走读/显然分支证明：删除只留
  非显然契约/不变式 ⑦对冲与计划残留——probably fine for now/should be enough/无标记延后：提升
  TODO/FIXME 或重述实际边界 ⑧写作语言碎片——英文散文残留 端/设计稿/---- 私有 ----，或中文对应面
  反向：翻译或删除）/ 保留规则（issue 引用 / 承重记录内已合并 PR 与 issue 证据 / 抑制理由（修正
  虚假理由绝不删除）/ 现在时反事实回归钉 / 测量出处词承重 / 运行时新旧状态 / 变更故事章节历史阶段名
  （索引戳处处禁）/ 外部标准引用 / 项目声音与体裁形式）/ 过纠正陷阱（义务→背书、假说→已交付、删
  真事实、丢出处）/ 工作流（显式 scope + 排除 vendored/冻结归档/录制夹具快照 → 先只读审计（探针 +
  无模式读最密散文）→ 先改拥有者再派生物 → 删除前枚举命题 + 过纠正检查 → 重跑探针 + 剩余引用 HEAD
  可解析 + 触碰表面门禁）；Searchable via experience_push，D-004/D-023/D-024/D-025/D-026/
  D-027/D-028/D-029 同款通道），repo 专属机制不携带（references/recall-batteries.md 具体探针
  清单与 --hidden 遍历 .agents/ 约定、references/examples.md、committed-artifact-citations 注记、
  .agents/notes 树、docs/AGENTS.md 标准之家、vendor/ 具体路径约定、JSDoc 类型等价围栏与
  verify-type-equiv、doc-sync / verify-translation-pairing 门禁命令、oxlint-disable 具体工具
  （抑制理由原则保留）、dsh-prose-standard / dsh-translate-docs 子 skill 引用（已分别独立收编
  D-028/D-029）在 V2 无对应物，原样整体不适合独立装配；无既有工作面可 Facet Fusion——
  prose_standard=一般编辑判断/完整命题规则（必需背景）、doc_standards=语料审计廉价探针（发现可疑
  段落）、bilingual_doc_pairing=配对同步、knowledge-space-maintenance=知识语料维护/归档封存、
  senior-engineer=评审视角，均不含"会话视角泄漏分类与修复"工作面）。
- 浏览器演示录制方法层收编完成：record-browser-gif（Evolution Intake #14 / DSH Corpus #11 →
  INT-016 / D-031）——可迁移方法层归 domains pattern `browser_gif_evidence`（录制与发布分离
  （录制只产生帧 + 本地 .gif、不改远端；发布=推专用 assets 分支 + 嵌入 PR body，仅任务包含"附到
  PR"时执行，绝不提交进 PR 分支/长命分支）/ 按 PR 分阶段（干净 worktree + 精确 commit + 从该树
  构建 + 全新状态根 + 浏览器隔离上下文；一个 storyboard = 一次证据运行，绝不拼接两次运行帧）/
  真实条件不替换（真实 server/API 不用 fixture/mock/合成事件/test hook，不可用报告限制；不读不
  暴露凭证值）/ 状态帧捕获（3–6 语义状态、单 viewport/crop、字典序帧名、gitignored 目录、具体
  UI 条件等待 + 精确文本完成谓词（非子串）、瞬态同一浏览器调用内轮询截图）/ 编码纪律（缺依赖报告
  不擅自装、逐帧时长末帧最长、先降宽再降色/fps、force 精确确认路径）/ 产物验证（编码器 JSON
  summary + 看编码后 GIF 本身 + git status 只 ignored 路径 + 返回绝对路径陈述 transport）/
  资产分支发布（专用 orphan <series>-assets、scratch clone、只 append 不 force、推送后认证验证
  （匿名 404 不证伪私有资产）、PR body 编辑前后 live head 核验 + Markdown API 渲染确认 img +
  raw blob URL ?raw=true）/ provenance（commit SHA/tree 与 origin/mode flags/是否真实模型轮）；
  Searchable via experience_push，D-004/D-023/D-024/D-025/D-026/D-027/D-028/D-029/D-030
  同款通道），repo 专属机制不携带（`pnpm run build && pnpm run build:web`、`DSH_HOME`/
  `DSH_AGENTS_HOME` 与 root `.env` 配置路径、browser-control skill（V2 无此运行时——映射仓库
  声明 Playwright + 隔离 headless）、`scripts/encode_gif.py` 与 `GIF_SKILL_DIR` 导出约定（编码
  原则保留，实现用项目既有 ffmpeg/python 流程）、evidence-chain 决策注记
  （2026-08-08-browser-gif-evidence-chain.md）、`.playwright-mcp/` 具体目录在 V2 无对应物，原样
  整体不适合独立装配；无既有工作面可 Facet Fusion——verify-before-trust=验证原则、closure_verify=
  端到端正确性对账、pre_push_evidence_gate=推前证据选择与核对、git_safety_net=本地文件安全网，
  均不含"UI 演示录制/资产分支发布"工作面）。
- **DSH 试点物化（2026-08-24 · D-037）**：从 9 个多关系对象中试点 2 个升级为
  **Assembled / Conditional 完整工作模式单位**（可装载激活，剔除死引用后的整包）——
  `pre_push_evidence_gate`（推送前证据闸门 · 完整流程：outgoing 范围 → 最小充分证据 →
  历史重写保护 → 发布后验证 → 失败即停 → 推后核对，INT-019）与 `prose_standard`
  （散文与注释编辑标准 · 完整流程：scope/mode → 完整命题 → 12 类位置覆盖 → 七步工作流 →
  边界决策，INT-020）；注册 `capabilities/INDEX.md`（行 2/3，trigger + activation）；
  domains pattern 保留为 Reference 并加双向引用（多关系：单位主体 + 知识引用 + 触发，
  D-034 模型物化）；真实消费 Q1–Q5 维持 UNKNOWN（不因物化升级）。
- **DSH 试点物化续（2026-08-24 · D-039）**：`cot_leakage_trim`（会话推理转录猎杀）升级为
  **Assembled / Conditional 完整工作模式单位**（可装载激活，剔除死引用后的整包）——
  `capabilities/cot_leakage_trim.md`（完整流程：HEAD 视角测试 → 八类泄漏分类 → 保留规则 →
  五步工作流 + 检查清单，INT-021）；注册 `capabilities/INDEX.md`（行 4，trigger + activation）；
  domains pattern 保留为 Reference 并加双向引用；真实消费 Q1–Q5 维持 UNKNOWN（不因物化升级）。
- **DSH 试点物化续（2026-08-24 · D-040）**：`doc_site_projection`（文档站受测投影）升级为
  **Assembled / Conditional 完整工作模式单位**（可装载激活，剔除死引用后的整包）——
  `capabilities/doc_site_projection.md`（完整流程：读拥有契约 → 变更分类 → manifest 白名单
  条目维护 → 链接保留与缺失即失败 → 预览验证门 → 部署分离 + 检查清单，INT-022）；注册
  `capabilities/INDEX.md`（行 5，trigger + activation）；domains pattern 保留为 Reference 并
  加双向引用；真实消费 Q1–Q5 维持 UNKNOWN（不因物化升级）。
- **DSH 试点物化续（2026-08-24 · D-041）**：`doc_standards`（文档放置与预算标准）升级为
  **Assembled / Conditional 完整工作模式单位**（可装载激活，剔除死引用后的整包）——
  `capabilities/doc_standards.md`（完整流程：结构先行 → 用途分类（教程 vs 参考）→ 教程前置
  条件 → 拆分混合形式 → 放置约束 → 语料审计廉价探针 → 预算 relocate-condense-raise →
  验证汇报 + 检查清单，INT-023）；注册 `capabilities/INDEX.md`（行 6，trigger + activation）；
  domains pattern 保留为 Reference 并加双向引用；真实消费 Q1–Q5 维持 UNKNOWN（不因物化升级）。
- **DSH 试点物化续（2026-08-24 · D-042）**：`simplification_audit`（证据驱动的代码简化审计）
  升级为 **Assembled / Conditional 完整工作模式单位**（可装载激活，剔除死引用后的整包）——
  `capabilities/simplification_audit.md`（完整流程：先读仓库上下文 → 强候选判据 → 广泛
  survey → 信任与生命周期边界审计 → 依赖替换净删除衡量 → 证明或拒绝每个候选 → 记录收编 →
  提案写作 → 内联 TODO 纪律 → 验证汇报 + 检查清单，INT-024）；注册
  `capabilities/INDEX.md`（行 7，trigger + activation）；domains pattern 保留为 Reference
  并加双向引用；真实消费 Q1–Q5 维持 UNKNOWN（不因物化升级）。
- **外部 Skill 接入（2026-08-24 · D-043）**：`test-driven-development`（TDD 完整工作模式 ·
  obra/superpowers）接入为 **Assembled / Conditional 完整工作模式单位**（可装载激活，整包
  保持完整）——`capabilities/test-driven-development.md`（完整流程：Overview → When to
  Use → Iron Law（无失败测试则无生产代码）→ Red-Green-Refactor（RED → Verify RED → GREEN →
  Verify GREEN → REFACTOR）→ Good Tests → Common Rationalizations → Red Flags → Example →
  Verification Checklist → When Stuck → Debugging Integration → Final Rule + 中文检查清单，
  INT-025）；注册 `capabilities/INDEX.md`（行 8，trigger + activation）；既有 domains
  pattern `testing-tdd` 保留为知识侧 Reference 并加双向引用（核心循环 + 适用边界 +
  既有外部标杆映射）；真实 TDD 完整装载消费 Q1–Q5 维持 UNKNOWN（不因接入升级）。

> 关联：decisions.md D-005；capability-reconstitution.md 形态判定。

---

## 七、Growth / Consolidation（V0.2 · 2026-08-23 · D-009）

- 三个正交维度：Object Semantics（是什么）/ Exposure（怎么得到与激活）/ Growth（与已有对象怎么发展）。
- `evolution/growth.md` —— 成长裁决记录（append-only）：每个对象的成长关系判定（独立 / 复用 / 融合 / 共享候选 / 合并 / 迁移 / 淘汰）有地方存在；不自动化融合。
- 统一开工发现：`tools/task_start.py`（任务卡=恢复/继续、知识=读/采纳、能力=使用/装配、Skill=装载/激活，来源标注 + 不同消费语义）。

> 纪律：Skill 默认保持完整；先判断对象关系，再决定 Exposure；默认局部，重复独立需求才产生 Shared Candidate。

---

## 八、近期工作文档（非导航入口 · 2026-08-24 增补）

| 文档 | 是什么 |
|---|---|
| `a18-relevance-diagnosis-2026-08-22.md` | A18 检索相关性诊断（Work Package 01 · P2） |
| `architecture-recovery-2026-08-24.md` | Post-Discovery 架构恢复 / 修复（TASK-20260824-001） |
| `dsh-corpus-review-2026-08-24.md` | DSH Corpus 汇总评审（TASK-20260824-012） |
| `dsh-remapping-2026-08-24.md` | DSH Skill 关系映射（TASK-20260824-013） |

> 这些是按日期落盘的演化工作记录；导航与裁决仍以 `workspace/INT-xxx` + `decisions.md` + `growth.md` 为准。

---

*关联：Task-Centered Capability Observation Protocol；V2 Reconstitution Exemplars；Star Map。*
