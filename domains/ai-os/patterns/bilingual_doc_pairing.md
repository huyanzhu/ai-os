---
rule_id: BILINGUAL-DOC-PAIRING-001
title: 双语配对文档工作流（按变更类型分诊 / briefing 驱动最小更新 / 术语表绑定 / 逐句核验）
category: Documentation Standards
trigger:
  - 维护双语/多语言配对文档（foo.md ↔ foo.zh.md 或任意语言对应面）
  - 一方已编辑、需要更新对应语言的副本（minimal counterpart update）
  - 为尚无对应面的文档补写整篇翻译（new pair）
  - 删除/重命名文档时同步处理对应语言面
  - 校对双语一致性 / 术语是否统一 / 翻译是否忠实
  - "translate this doc" / "keep the two languages in sync" / "update the zh counterpart"
condition: 文档语料存在多语言配对，两侧权威相等、任何一侧都可作为作者侧；工作目标是让配对在两种语言中都
  自然一致，而不是单侧"翻译"另一侧
action:
  do:
    - 先按变更类型分诊，再决定路径：Update（配对已存在、一侧被编辑）走 briefing 驱动的最小更新路径；
      New pair（无对应面）走整篇翻译路径；删除/重命名则同步处理对应面（否则配对完整性校验报错）
    - 任何一侧被编辑后都欠一个对应面更新（无永久作者侧：双语配对每次编辑都产生配对工作，不是一次性任务）
    - 更新路径：先生成/核对变更 briefing（最小可安全对齐的粒度：变化的 Markdown 单元（段落/表格行/
      列表项/标题）→ 整节 → 整文档），拿到作者侧的 diff、每个变化单元的最近确认源/当前源/当前对应面
      文本、涉及的术语行与约束摘要，再做最小对应面编辑——绝不因一次更新重译整篇文档（保留未变部分的
      已审措辞）
    - 机械性变更（仅代码围栏内容变化且两侧共享）→ 直接按对应围栏拼接并做结构校验；散文变更 →
      把 briefing 作为译者完整工作集委托子 agent 执行，不要求其重读语料/重推 diff，仅当 briefing
      留下真正不可回答的决策（未列术语且上下文无先例、或整文档 briefing）才回到整篇翻译的权威源
    - 最小编辑覆盖 diff：不动未变部分；逐句核验变化块——不增、不漏、术语按行、代码 span 逐字保留
    - 整篇翻译：Pass 1 写不逐字对应（读语义单元后以目标语言母语技术作者口吻重述，保持结构框架）；
      Pass 2 逐句对照源核验保真（可在此修正，用重写句子而非往句子里贴词）；完成后单独读译文（脱离源），
      改写只在孤立阅读中才显出的拗口
    - 术语纪律：翻译前先载入术语表（绑定双向）；目标中文用中文列 + 首次出现列；未列术语须有可引用的
      OSS/厂商先例，否则保留英文并列入「待定术语」，绝不临时自造
    - 代码块两侧字节一致（含注释）；文档内相对链接保持同一语义目标与精确 query/fragment 后缀（语料内
      目标按语言后缀切换、语料外保持原路径）
    - 结构对齐：标题层级/围栏块/表格行列数/列表类型与项数/有序列表起点/链接语言后缀逐项手工核对
    - 收尾：记录配对状态（哪个配对被确认一致）+ 汇报哪些是新配对、哪些是最小更新、列出「待定术语」
  dont:
    - 不因一次更新重译整篇文档（丢弃已审措辞）
    - 不让译者无 briefing 重读整个语料/重推 diff（briefing 是其完整工作集）
    - 不临时自造术语渲染（未列术语须有先例或留英文 + 待定术语）
    - 不让代码块/注释在两侧出现差异；不改变链接语义目标或丢失 query/fragment
    - 不在确认一致前记录"已验证"；不对未实际检查的配对声称绿色
    - 不把冻结归档（archived）的双语配对当作翻译工作处理（封存即不动）
keywords:
  - 双语配对
  - bilingual pairing
  - 翻译
  - translation
  - translate
  - 术语表
  - terminology
  - 待定术语
  - 配对文档
  - paired docs
  - 多语言文档
  - multilingual docs
  - 一致性核验
  - consistency check
  - 最小更新
  - minimal update
  - 对应面
  - counterpart
  - 逐句核验
  - clause-by-clause
  - i18n
  - 双语文档工作流
alias:
  - dsh-translate-docs
  - 翻译配对工作流
  - 双语翻译工作流
  - 文档翻译
  - 翻译文档
  - doc translation

knowledge_position: Cluster
knowledge_cluster: FC-Bilingual Doc Pairing
epistemology_tag: PROCEDURE
confidence: HIGH
---

# 双语配对文档工作流（按变更类型分诊 / briefing 驱动最小更新 / 术语表绑定 / 逐句核验）

**来源**：外部 Skill（Human 提供，Evolution Intake #12 / DSH Corpus #9）——deepseek-ai/deepseek-harness
的 `dsh-translate-docs` SKILL.md（2026-08-24 HTTP 200 逐字下载，原文存
`evolution/intake/dsh-translate-docs/SKILL.md`）。按 Skill Fusion 先例（D-004 debug-protocol /
D-023 doc_site_projection / D-024 doc_standards / D-025 simplification_audit / D-026
dependent_change_landing / D-027 pre_push_evidence_gate / D-028 prose_standard：外部 Skill →
domains patterns 进 experience_push 检索源；D-008 Human 确认知识/pattern 形态）收编为 V2 pattern。

**解决**：多语言配对文档（`foo.md ↔ foo.zh.md` 或任意语言对应面）的**一致性维护工作流**——如何让两侧
在两种语言中都自然一致。**本 skill 是工作流地图，不是翻译记忆**：它规定"必须成立什么"（分诊、最小更新、
术语绑定、逐句核验、结构对齐），不规定具体句子怎么译——措辞判断属于译者，术语不属于。

## 什么时候用 / 不用
- **用**：维护双语/多语言配对文档；一侧被编辑后需要更新对应面；为无对应面的文档补写整篇翻译；
  删除/重命名文档需同步处理配对；校对双语一致性 / 术语统一 / 翻译忠实度。
- **不用**：单份交付文档产出——那是 `doc-generation`；文档放哪/多长/审计——那是 `doc_standards`；
  散文写什么/保留什么/删什么——那是 `prose_standard`（其"双语配对无永久作者侧"原则与本 pattern
  的分诊/最小更新/术语纪律互补：prose_standard 管两侧各自的编辑质量，本文管配对间的同步工作流）；
  把文档发布成站点——那是 `doc_site_projection`；会话推理转录猎杀——那是 dsh-trim-cot-leakage
  ——那是 `cot_leakage_trim`（D-030）。

## 协议（AI-OS 上下文映射）
1. **分诊先行（决定一切后续）**——按变更类型走不同路径：
   - **Update**（配对已存在、一侧被编辑）→ briefing 驱动的最小更新路径：不重读语料、不做 git 考古、
     只做最小对应面编辑；**绝不因一次更新重译整篇文档**——最小更新保留未变部分已审措辞，重译等于
     把已审措辞扔进回收站。
   - **New pair**（尚无对应面）→ 整篇翻译路径（见第 4 条）。
   - **删除/重命名** → 同步删除/重命名对应面与配对状态记录，否则配对完整性校验会报"不完整配对"。
   - 冻结归档下的双语配对不是翻译工作：封存即不动，任何一侧都不再更新/重录/修复。
2. **Briefing = 译者完整工作集**——更新的最小可对齐粒度：变化 Markdown 单元（段落/表格行/列表项/
   标题）→ 整节 → 整文档；briefing 内含作者侧 diff、每个变化单元的最近确认源/当前源/当前对应面文本
   （带行号）、涉及的术语行、首次出现位置变化与约束摘要。散文 diff 委托子 agent 时**把 briefing 或
   生成它的命令整个传过去**——子 agent 不重读语料（规则摘要/术语行/三向上下文都在内联）、不重推 diff；
   只有当 briefing 留下真正不可回答的决策（未列术语且周围文本无先例、或整文档 briefing——两侧都变/
   单元与节都不对齐）才回到整篇翻译路径的权威源手工调和。
3. **最小编辑覆盖 diff**——只动 diff 触及的部分，其余保持已审措辞；逐句核验变化块：不增、不漏、
   术语按内联行、代码 span 逐字保留。
4. **整篇翻译（新配对）**——**协调者不亲自逐句翻译，委托子 agent 执行**；译者先读权威源（配对契约/
   翻译规则/术语表），再整篇译入目标语言；长文档逐节推进，每节结构即时锁定源，不最后统一修结构。
   - **Pass 1 写，不逐字对应**：读语义单元，以目标语言母语技术作者在最近风格样本中的语域重述；保留
     必需框架，不强迫逐句对应。
   - **Pass 2 对照源逐句核验**：保真在这里检查而非写出来——确认不增不漏、术语全按表、代码 span 逐字
     存活；修法 = 用母语重写句子，不是往句子里贴词。
   - **单独读译文**：脱离源读一遍，改写只在孤立阅读中才显出的拗口。
   - 只把最终文本写进文件，不留草稿/注记。
5. **术语纪律（双向绑定）**——翻译前**先载入术语表**，不是遇到不确定的词才翻（注意不到的词才是漂移
   的）。目标中文用中文列 + 首次出现列；未列术语须有可引用的中文 OSS/厂商先例，否则保留英文并列入
   「待定术语」。目标英文用英文列 + 既定英文技术词；歧义源词保留并加短 gloss、列待定。**绝不临时
   自造渲染。**
6. **代码与链接纪律**——代码块两侧字节一致（注释也一致）；仓库内相对文档链接保持同一语义目标与精确
   query/fragment 后缀：语料内目标按语言后缀切换（英文侧 `.md` / 中文侧 `.zh.md`）、语料内缺对应面
   是错误、语料外目标保持作者路径。语言切换链接（switcher）是跨语种的唯一例外。
7. **结构对齐（Pass 2 手工核验）**——标题层级、围栏块、表格行数与列数、列表类型、有序列表起点、
   列表项数、链接语种、语义目标逐项核对。
8. **收尾与记录**——确认一致后再记录配对状态（记录是"我确认这两侧说同一件事"的可审阅陈述，只在
   真正确认后运行）；汇报哪些配对是新 vs 最小更新；「待定术语」显式列出。普通文档无需额外登记
   （每个语料内源都要求配对）；仅当政策文档证明存在真正的生成/教学/双语构造成例外时才改 manifest。

## 不携带清单（repo 专属死引用，硬搬会注入）
deepseek-harness 的 `pnpm run gen-translation-brief` / `gen-translation-brief --apply` /
`verify-translation-pairing`（含 `--write` / `--list` / `--all`）命令族、`foo.i18n.yaml` 双侧
blob 哈希一致性记录文件、语言切换行（`[English](foo.md) | 中文`）的仓库格式、`docs/i18n/README.md`
/ `translation-rules.md` / `terminology.md` / `translation-prompt.md` / `style-samples.md` 具体文件、
`scripts/translation-pairing.manifest.json`、`doc-sync` / `verify-md-wrap` / `verify-md-links` 门禁、
`.agents/notes/archived/` 三元组封存契约与 dsh-code-review / dsh-prose-standard / dsh-pre-push-checks
子 skill 引用（分别独立 intake，见对应 pattern）在 V2 无对应物；**原样整体不适合独立装配**。若未来
真实项目本身就是 deepseek-harness 类仓库，直接装载原文
`evolution/intake/dsh-translate-docs/SKILL.md`（本 pattern 只带可迁移方法层）。V2 当前无配对基建：
未来真实项目需要双语文档时，配对状态可用既有文件纪律记录（如项目内 `*.i18n.yaml` 或等价的配对
清单），本 pattern 提供方法层，不新建注册表/工具。

## 与既有知识的关系（互补，非重复）
- `prose_standard`（D-028）= 单侧散文编辑判断/契约保留/按位置覆盖（管"一侧写什么/保留什么/删什么"；
  其"双语配对无永久作者侧"原则与本 pattern 的分诊/最小更新/术语纪律互补）；本文 = 配对间同步工作流
  （管"两侧怎么保持一致"）。
- `doc_standards`（D-024）= 文档放置/层级/预算/语料审计（其放置约束"双语配对文档每次编辑都欠一个
  对应面更新"由本文提供完整工作流）；互补不重复。
- `doc_site_projection`（D-023）= 发布投影（链接完整性/单一源/受测投影）；本文的链接语种纪律是其
  多语种场景的配对侧补充。
- `doc-generation` = 单份交付文档产出；senior-engineer Review 方法层（D-011 融合 dsh-code-review）
  的"双语改动：两侧语义与术语对照（配对哈希绿 ≠ 翻译质量）"是评审侧判定，本文提供作者侧工作流——
  互补。
- 同族 `cot_leakage_trim`（D-030，会话推理转录猎杀）已独立收编——本 pattern 第③步"双语配对 →
  更新对应面并重录"与第④步的对应面修复纪律衔接：配对侧的会话视角泄漏修复由该 pattern 承载。

## 检查清单（双语配对工作中自测）
- [ ] 先分诊了吗（Update / New pair / 删除重命名 / 归档不动）？
- [ ] 更新走 briefing 驱动的最小编辑了吗（没有因一次更新重译整篇）？
- [ ] 散文 diff 委托时把 briefing 作为完整工作集传了吗（子 agent 不重读语料/重推 diff）？
- [ ] 翻译前载入术语表了吗；未列术语有先例或留英文 + 待定术语，没有自造？
- [ ] Pass 2 逐句核验保真了吗（不增不漏、术语按表、代码 span 逐字）？
- [ ] 单独读译文改写过孤立阅读才显出的拗口吗？
- [ ] 代码块/注释两侧字节一致；链接语义目标与 query/fragment 精确保留？
- [ ] 结构对齐核验了吗（标题层级/围栏/表格/列表/有序起点/链接语种）？
- [ ] 只在真正确认一致后记录配对状态；「待定术语」列出来了吗？

## 相关对象（2026-08-24 Re-Mapping 物化 · D-035）

- prose_standard（作者侧编辑标准，双向）；doc_standards（双向）；doc_site_projection（配对同步 → 发布投影校验，双向）；senior-engineer Review 面（作者侧 vs 评审侧，非成员）
