---
rule_id: COT-LEAKAGE-TRIM-001
title: 会话推理转录猎杀（HEAD 视角测试 / 八类泄漏分类 / 保留规则 / 过纠正陷阱）
category: Documentation Standards
trigger:
  - 审计/修复读起来像泄漏的推理转录的散文（死设计会话引用（decision N）/ 审计码（audit C2）/ 未提交
    草稿的 §N / 变更叙述（used to / no longer / this cut）/ 栈与 PR 视角（a later PR in this stack）/
    评审编排（rejected in review / v5 of this note）/ 评审者定向辩护 / 控制流叙述 / 对冲与计划残留 /
    工作语言碎片）
  - "trim the chain-of-thought" / "this reads like a reasoning transcript" / 清理会话视角残留
  - 在评论、JSDoc、文档、Agent Notes 中移除作者会话视角、保留仓库视角
  - 判定某段"是不是泄漏"、某条引用"该保留还是删除"
condition: 语料中的散文其视角是写作会话而非仓库（读者无法在 HEAD 解析引用/核验声明）；修复目标是让每个
  存活事实以 HEAD 视角成立，而不是单向删光
action:
  do:
    - 对每个可疑段落先跑 HEAD 视角测试：无任何会话转录、PR 线程或未提交草稿的读者，能否解析每个引用、
      核验每个声明？不能 → 把存活事实以仓库视角重述、删除其余；能 → 不是泄漏（但可解析只过本 skill 的
      杆；当前状态面（README/文档/JSDoc）上可解析的变更故事仍是变更叙述，按第 3 类送回其许可之家）
    - 按八类分类并分别修复：①死设计会话引用（(decision 7)/(audit C2)/design §4.7/phase 标签 T4 W3 P-I/
      "the design ledger"/"(B ruling)"）——决策有已提交拥有者则按名+路径引用，否则删引用并把事实子句
      重述为独立成立；②栈与 PR 视角（"a later PR in this stack"/"this PR adds"/"the previous commit"）
      ——陈述已交付机制或扩展点，延后工作转 TODO 标记或 issue 引用；③变更叙述与版本戳（"used to"/
      "no longer"/"the old X"/索引戳 "v1"/"this cut"/"today"/"now" 对比过去态）——陈述当前行为，已修复
      回归用现在时反事实（"without X, Y happens"），绝不写仓库历史（"used to Y"）；④评审编排（"Rejected
      in review:"/"the reviewer confirmed"/草稿序号 "v5 of this note"/轮次归属）——保留存活决策与理由为
      平实事实，删谁在何时说的；⑤评审者定向辩护（"the cast is safe — it simply…"/"this is correct
      because…"）——陈述使代码安全的不变式，或代码已显示时删除注释；⑥复述与推导转录（"first we X, then
      we Y"/测试走读/显然分支证明）——删除，只留非显然契约或不变式；⑦对冲与计划残留（"probably fine for
      now"/"should be enough"/无标记的延后）——提升为 TODO/FIXME 或重述为实际边界，删除对冲；⑧写作语言
      碎片（英文散文中残留 端/设计稿/"---- 私有 ----" 分隔符，或中文对应面反向残留）——翻译或删除
    - 应用保留规则（什么不是泄漏）：issue 引用（#1470 / TODO(name): / "issue #N owns the follow-up"）
      在 HEAD 可解析，任何表面都保留（含 README），不移到 Agent Notes；Agent Notes 与 postmortem 内的
      已合并 PR 与 issue 引用是受认可证据（按文档标准的变更故事路由）；抑制理由（lint-disable -- reason /
      coverage-ignore 原因 / 空 catch 解释）是必需散文——修正虚假理由，绝不删除；现在时反事实回归钉
      （"without X, Y happens"/"a naive X would…"）；测量边界（"(measured: 512 nests ≈ 0.15s)"，
      "measured" 出处词承重）；运行时新旧状态（"the old connection drains before the new one accepts"
      是运行时生命周期不是变更史）；变更故事章节内的历史阶段名（"the first cut shipped X" 在该节安全，
      索引戳 "this cut" 处处禁）；设计上在仓库外可解析的外部引用（RFC 9110 §10.1.5 / Figma frame 名——
      §-禁令只覆盖未提交内部草稿，不覆盖外部标准或拥有自己 § 编号的已提交文档）；项目声音与体裁形式
      （"we" 项目声音 / 备选方案章节）
    - 工作流：①按 prose_standard 要求显式 scope 与排除（vendored/第三方、冻结归档、录制的夹具与快照——
      录制模型输出与封存历史保留原声音）②先只读审计：跑检索探针（含 --hidden 覆盖隐藏目录）找候选，
      再对每个命中做语义判断；探针是探针不是定义——还要无模式地读范围内最密的散文（模块 JSDoc/README/
      Agent Notes）③按表面先改拥有者：生成目录→改源 JSDoc 或生成器模板再重新生成；类型等价围栏→改源
      JSDoc 后重贴双语页；双语配对→更新对应面并按双语配对工作流重录；模型可见字符串→措辞即行为，标记
      快照支撑的变更而非静默改写 ④删除前枚举段落的命题（prose-standard）并检查过纠正陷阱：修剪把义务
      翻转成背书、把假说提升成已交付功能、删除真实事实、丢失出处 ⑤验证：重跑探针，预期只剩受认可的
      保留、本 skill 自身目录与拥有注记引用的证据；确认每个剩余引用在 HEAD 可解析；跑触碰表面的既有门禁
  dont:
    - 无显式 scope 就开跑；触碰 vendored/冻结归档/录制夹具与快照
    - 把可解析的历史口吻一律当泄漏（resolvable 只过本 skill 的杆，变更叙述仍按第 3 类处理）
    - 删除 issue 引用 / 承重记录里的已合并 PR 与 issue 证据 / 抑制理由 / 反事实回归钉 / 测量出处 /
      运行时新旧状态 / 外部标准引用 / 项目声音
    - 把死引用之外的事实子句一起删掉（先重述存活事实，再删转录）
    - 修剪把义务翻转成背书、把假说提升成已交付、删除真事实或丢失出处的过纠正
    - 静默改写模型可见字符串（措辞即行为，先标记快照支撑的变更）
keywords:
  - chain-of-thought leakage
  - 推理转录
  - reasoning transcript
  - 会话视角
  - session vantage
  - HEAD 视角
  - at HEAD
  - 死设计会话引用
  - dead design-session citation
  - 变更叙述
  - change narration
  - 版本戳
  - indexical
  - 评审编排
  - review choreography
  - 计划残留
  - planning residue
  - 对冲
  - hedge
  - 过纠正陷阱
  - overcorrection
  - 引用保留
  - 保留规则
alias:
  - dsh-trim-cot-leakage
  - 会话残留分类
  - 推理转录猎杀
  - trim cot leakage
  - CoT leakage

knowledge_position: Cluster
knowledge_cluster: FC-CoT Leakage Trim
epistemology_tag: PROCEDURE
confidence: HIGH
---

# 会话推理转录猎杀（HEAD 视角测试 / 八类泄漏分类 / 保留规则 / 过纠正陷阱）

**来源**：外部 Skill（Human 提供，Evolution Intake #13 / DSH Corpus #10）——deepseek-ai/deepseek-harness
的 `dsh-trim-cot-leakage` SKILL.md（2026-08-24 HTTP 200 逐字下载，原文存
`evolution/intake/dsh-trim-cot-leakage/SKILL.md`）。按 Skill Fusion 先例（D-004 debug-protocol /
D-023 doc_site_projection / D-024 doc_standards / D-025 simplification_audit / D-026
dependent_change_landing / D-027 pre_push_evidence_gate / D-028 prose_standard / D-029
bilingual_doc_pairing：外部 Skill → domains patterns 进 experience_push 检索源；D-008 Human
确认知识/pattern 形态）收编为 V2 pattern。

**解决**：链式思维泄漏（chain-of-thought leakage）= 散文的视角是**写作会话**而非**仓库**：引用只有该
会话能看见的产物、叙述变更而不是状态、或与已离开的评审者争辩。修复从不只是删除——段落带事实子句时，
先把每个子句重述为在 HEAD 成立，再删除周围的转录；不带任何事实子句的段落（审计码、控制流叙述）直接
删除。**单一测试**：对每个可疑段落问——**无任何会话转录、PR 线程或未提交草稿的 HEAD 读者，能否解析
每个引用、核验每个声明？** 不能 → 重述存活事实 + 删除其余；能 → 不是泄漏（但可解析只过本 skill 的杆；
当前状态面（README/文档/JSDoc）上可解析的变更故事仍是变更叙述，按第 3 类送回其许可之家）。本 skill
是 guidance，不是脚本；**完整命题规则由 `prose_standard`（D-028）拥有**，本 skill 应用它。

## 什么时候用 / 不用
- **用**：审计/修复 AI-OS 自身或 workspace 项目语料中读起来像泄漏的推理转录的散文——评论、JSDoc、
  文档、Agent Notes（V2：task card / pattern / SUCCESS_LOG 承重记录）；收到 "trim the chain-of-thought"、
  "this reads like a reasoning transcript"、"清理会话视角残留" 类指令；判定某段"是不是泄漏"、某条
  引用"该保留还是删除"。
- **不用**：一般散文"该写什么/保留什么/删什么"的编辑判断——那是 `prose_standard`（本 skill 的必需
  背景，拥有完整命题规则）；文档"放哪/写多长/语料审计廉价探针"——那是 `doc_standards`（其探针发现
  可疑段落，本 skill 分类与修复）；双语配对同步——那是 `bilingual_doc_pairing`；代码功能本身的实现。

## 协议（AI-OS 上下文映射）
1. **HEAD 视角测试（单一测试）**——对每个可疑段落问：无任何会话转录、PR 线程或未提交草稿的 HEAD
   读者，能否解析每个引用并核验每个声明？不能 → 把存活事实以仓库视角重述，删除其余；能 → 不是泄漏，
   无论多像历史——但可解析只过本 skill 的杆：当前状态面（README/文档/JSDoc）上可解析的变更故事仍是
   变更叙述，按第 3 类送回其许可之家。
2. **八类分类法**——
   ① **死设计会话引用**：`(decision 7)`、`(audit C2)`、`design §4.7`、`plan §1.4`、阶段标签（`T4`/
   `W3`/`P-I`）、"the design ledger"、`(B ruling)`。决策有已提交拥有者 → 按名 + 路径引用；否则删除
   引用并把其事实子句重述为独立成立。
   ② **栈与 PR 视角**：`a later PR in this stack`、`this PR adds`、`the previous commit`。陈述已
   交付机制或扩展点；延后工作移到 `TODO` 标记或 issue 引用。
   ③ **变更叙述与版本戳**：`used to`、`no longer`、`the old X`、索引戳（`v1`、`this cut`、`today`、
   `now` 对比过去态）。陈述当前行为；已修复回归写成现在时反事实（`without X, Y happens`），绝不写仓库
   历史（`used to Y`）。
   ④ **评审编排**：`Rejected in review:`、`the reviewer confirmed`、草稿序号（`v5 of this note`）、
   轮次归属。保留存活决策与理由为平实事实；删除谁在何时说的。
   ⑤ **评审者定向辩护**：`the cast is safe — it simply…`、`this is correct because…`。为自身正确性
   辩护的注释是在对评审者说话，不是对维护者。陈述使代码安全的不变式；代码已显示时删除注释。
   ⑥ **复述与推导转录**：控制流叙述（`first we X, then we Y`）、测试走读、显然分支的证明。删除；
   只留非显然契约或不变式。
   ⑦ **对冲与计划残留**：`probably fine for now`、`should be enough`、无标记的延后。提升为
   `TODO`/`FIXME`，或重述为实际边界；删除对冲。
   ⑧ **写作语言碎片**：英文散文中残留的工作语言碎片（端、设计稿、`---- 私有 ----` 分隔符），或中文
   对应面反向残留。翻译或删除。
3. **保留规则（什么不是泄漏）**——无辅助引用的通过/失败会双向出错：删掉持久引用、留下死引用。按写
   下的规则保留：
   - **Issue 引用**：`#1470`、`TODO(name):`、`issue #N owns the follow-up` 在 HEAD 可解析——任何
     表面都保留（含 README），不把它们移到 Agent Notes。
   - **Agent Notes 与 postmortem 内的已合并 PR 与 issue 引用**：按文档标准的变更故事路由，是受认可
     证据。
   - **抑制理由**：`oxlint-disable … -- reason`、coverage-ignore 原因、空 catch 解释是必需散文——
     修正虚假理由，绝不删除。
   - **现在时反事实回归钉**：`without X, Y happens`、`a naive X would…`。
   - **测量边界**：`(measured: 512 nests ≈ 0.15s)` 校准常量；出处词 "measured" 承重。
   - **运行时新旧状态**：`the old connection drains before the new one accepts` 是运行时生命周期，
     不是变更史。
   - **变更故事章节内的历史阶段名**：`the first cut shipped X` 在该节当前状态安全；索引戳
     （`this cut`）处处禁。
   - **设计上仓库外可解析的外部引用**：标准章节（RFC 9110 §10.1.5）、Figma frame 名——§-禁令覆盖
     未提交内部草稿，不覆盖外部标准或拥有自己 § 编号的已提交文档。
   - **项目声音与体裁形式**：`we` 作为项目声音；note 的备选方案（Alternatives-considered）章节。
4. **工作流**——
   ① 按 `prose_standard` 要求显式 scope 与排除：需要显式 scope；绝不碰 `vendor/`、冻结归档
   （V2：task_cards/archive 等 archived 目录）与录制的夹具/快照——录制模型输出与封存历史保留原声音。
   ② 先只读审计：跑检索探针（含隐藏目录——V2 对应：rg/Select-String 覆盖任务卡/笔记等隐藏面）找候选，
      再对每个命中做语义判断。探针是探针不是定义——原清理的每一轮都发现探针漏掉的案例，所以还要无模式
      地读范围内最密的散文（模块 JSDoc、README、Agent Notes），手里不拿模式。
   ③ 按表面先改拥有者：生成目录 → 改源 JSDoc 或生成器模板，再重新生成；类型等价围栏 → 改源 JSDoc 后
      重贴双语页（V2 无此基建，原则 = 先改源再派生物）；双语配对 → 更新对应面并按 `bilingual_doc_pairing`
      重录；模型可见字符串 → 措辞即行为，标记为快照支撑的变更，不静默改写。
   ④ 删除任何东西前：枚举段落的命题（`prose_standard`）并检查过纠正陷阱——修剪把义务翻转成背书、
      把假说提升成已交付功能、删除真实事实、丢失出处的都要停。
   ⑤ 验证：重跑探针，预期只剩受认可的保留、本 skill 自身目录与拥有注记引用的证据；确认每个剩余引用
      在 HEAD 可解析；跑触碰表面的既有门禁（V2：既有验证入口；无对应物时手工核验并如实汇报）。

## 不携带清单（repo 专属死引用，硬搬会注入）
deepseek-harness 的 `references/recall-batteries.md`（具体探针脚本清单与 `--hidden` 遍历
`.agents/` 约定）、`references/examples.md`（校准示例文件——V2 边界案例沉淀进本 pattern）、
`../../notes/implemented/process/2026-08-09-committed-artifact-citations.md`（引用规则理由注记——
V2 原则由"一个解释一个家"+ 承重记录引用规则承接）、`.agents/notes/` 树（notes/README 契约、
archived 目录机制）、`docs/AGENTS.md` 标准之家、`vendor/` 具体路径约定、JSDoc 类型等价围栏与
`verify-type-equiv`、`doc-sync` / `verify-translation-pairing` 门禁命令、`oxlint-disable` 具体
工具（抑制理由原则保留）、dsh-prose-standard 与 dsh-translate-docs 子 skill 引用（已分别独立
收编 D-028 → `prose_standard`、D-029 → `bilingual_doc_pairing`）在 V2 无对应物；**原样整体不适合
独立装配**。若未来真实项目本身就是 deepseek-harness 类仓库，直接装载原文
`evolution/intake/dsh-trim-cot-leakage/SKILL.md`（本 pattern 只带可迁移方法层）。

## 与既有知识的关系（互补，非重复）
- `prose_standard`（D-028）= **必需背景**：拥有完整命题规则（编辑前识别每个命题、只有每个事实子句
  存活且更清晰才删）——本 skill 应用它到会话视角泄漏类；prose_standard 管"该写/保留/删什么"的一般
  编辑判断（其目标之一即"移除推理转录"），本 pattern 管"哪些是会话视角泄漏 + 八类怎么分类修复 +
  什么必须保留"的专项——原文自述 "REQUIRED BACKGROUND: dsh-prose-standard owns the
  complete-proposition rule this skill applies"——互补不重复。
- `doc_standards`（D-024）= 语料审计的廉价探针：其审计第②项"会话视角残留（死设计会话引用/变更叙述/
  评审编排/控制流叙述/测试走读）——只保留非显然契约与持久理由"负责**发现**可疑段落；本 pattern 提供
  分类、HEAD 判定、保留规则与过纠正陷阱——互补不重复（探针管"找到它"，本 pattern 管"分类并正确修"）。
- `bilingual_doc_pairing`（D-029）= 双语配对更新工作流——本 pattern 的第③步"双语配对 → 更新对应面
  并重录"指向它。
- senior-engineer Review 方法层（D-011 融合 dsh-code-review）= 评审纪律（"注释陈述非显然契约、标记
  实现叙述"——判定该标记什么）；本 pattern 提供会话视角泄漏的具体修复标准（该写/该删什么）——互补。
- `knowledge-space-maintenance` Lifecycle/Archive facet（D-022）= 知识语料的归档封存纪律；本 pattern
  的引用保留规则（issue/已合并 PR 引用在承重记录中是证据）与之衔接——互补。
- `simplification_audit`（D-025）= 代码面简化审计（哪些既有面值得移除），其提案涉及文档/注释时由
  prose_standard + 本 pattern 提供散文编辑判断——互补。

## 检查清单（会话视角泄漏审计中自测）
- [ ] 对每个可疑段落跑了 HEAD 视角测试（无会话转录/PR 线程/未提交草稿的读者能否解析每个引用、核验
      每个声明）？
- [ ] 泄漏按八类分类了吗（死设计引用/栈 PR 视角/变更叙述与版本戳/评审编排/评审者辩护/复述转录/对冲
      计划残留/语言碎片），每类按对应规则修复？
- [ ] 删除前重述了每个事实子句（先重述存活事实，再删转录；不带事实子句的才直接删）？
- [ ] 保留规则应用了吗（issue 引用/承重记录证据/抑制理由/反事实钉/测量出处/运行时新旧/变更故事阶段名/
      外部标准引用/项目声音）？
- [ ] 检查了过纠正陷阱（义务→背书、假说→已交付、删真事实、丢出处）？
- [ ] 先改拥有者再改派生物（生成物先改源再重新生成；模型可见字符串标记快照支撑变更而非静默改写）？
- [ ] 验证过了吗（重跑探针只剩受认可的保留；剩余引用在 HEAD 可解析；跑过触碰表面的既有门禁并如实汇报）？

## 相关对象（2026-08-24 Re-Mapping 物化 · D-035）

- prose_standard（本对象依赖其为背景，双向）；browser_gif_evidence（录制夹具排除项 ↔ 引用保留，双向）；doc_standards / bilingual_doc_pairing（doc 族）；knowledge-space-maintenance Lifecycle facet（引用保留衔接）
- 工作模式单位：`capabilities/cot_leakage_trim.md`（Assembled；本 pattern 为 Reference）
