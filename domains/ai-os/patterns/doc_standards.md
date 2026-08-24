---
rule_id: DOC-STANDARDS-001
title: 文档放置与预算标准（结构先行 / 用途分类 / 预算纪律 / 语料审计）
category: Documentation Standards
trigger:
  - 写 / 移动 / 评审 / 审计仓库文档（README / 导航 / 报告 / 项目文档）
  - 决定一篇文档放哪个层级 / 写成教程还是参考 / 写多长
  - 文档太长 / 重复 / 含会话视角残留（reasoning transcript leakage）
  - "improve the docs" / "audit the docs" / "where should this be documented" / "this doc is too long"
condition: 面向人的文档进入 AI-OS 或 workspace 项目语料时（教程要有序通向可观察产出；参考要可查找；
  篇幅本身不是缺陷）
action:
  do:
    - 先定结构再写正文：在导航树中定位文档，陈述自身主题并识别直接子文档；主题细节留在本层，子文档
      按用途/职责/高层行为概括并链接，更深解释移到拥有它的子文档
    - 按预期用途分类而非路径/标题：教程=有序工作导向可观察产出；参考=显式范围内可查找、不要求顺序阅读
    - 教程先私有判定起始读者（初/中/高），把每个概念追到前置条件，前移过早材料，可选高级细节移到
      后续教程或参考
    - 明显混合形式拆开；小次要形式放清晰标注章节
    - 移动/重命名前 grep 入站引用（链接 + 锚点）；移动是原子的——旧移除 + 新加入 + 同一改动修全部
      入站链接
    - 审计语料用最廉价探针先行：词数找越界 outlier → 会话视角残留（死设计引用/变更叙述/评审编排/
      控制流叙述/测试走读）→ 重复（grep 特色短语）→ 手写目录/清单/状态盘点 → implemented 记录里
      未来时态与验收清单
    - 保留每条承重规则：1-3 行 + 指向理由的链接；删故事/重复/状态注记/推导路径；超长按
      relocate（移归属）→ condense（压缩）→ raise（提预算并说明理由）顺序处理
    - 汇报实际跑过的检查与词数增量；不声称没跑过的门禁
  dont:
    - 不按路径/标题推断文档类型；不把篇幅当缺陷
    - 不手编生成目录/清单（改生成器或源）
    - 移动不修入站链接；删除不查引用
    - 不删会改变承诺行为（而非解释）的措辞——先用 proposed 记录（任务卡/决策草案），不静默改
    - 不审计/修改冻结归档快照（archived）
    - 不新建解释仅为了搬运可丢弃的推理
keywords:
  - 文档标准
  - doc standards
  - 文档放置
  - 文档分层
  - placement
  - hierarchy
  - tutorial
  - 教程
  - reference
  - 参考文档
  - 文档预算
  - doc budget
  - slop
  - 文档审计
  - corpus audit
  - 文档太长
  - 结构先行
  - 用途分类
alias:
  - dsh-doc-standards
  - 文档放置标准
  - 文档结构标准
  - 文档预算标准

knowledge_position: Cluster
knowledge_cluster: FC-Doc Standards
epistemology_tag: PROCEDURE
confidence: HIGH
---

# 文档放置与预算标准（结构先行 / 用途分类 / 预算纪律 / 语料审计）

**来源**：外部 Skill（Human 提供，Evolution Intake #7 / DSH Corpus #3）——deepseek-ai/deepseek-harness
的 `dsh-doc-standards` SKILL.md（2026-08-24 HTTP 200 逐字下载，原文存
`evolution/intake/dsh-doc-standards/SKILL.md`）。按 Skill Fusion 先例（D-004 debug-protocol / D-023
doc_site_projection：外部 Skill → domains patterns 进 experience_push 检索源；D-008 Human 确认
知识/pattern 形态）收编为 V2 pattern。

**解决**：仓库/语料里的文档"放哪、写成什么形态、写多长、怎么审计"。核心纪律：
**先定结构再写正文——每篇文档有自己的主题与直接子文档；细节留在所属层，子文档按用途概括并链接；
按预期用途（教程 vs 参考）分类而非按路径/标题；预算纪律防文档膨胀；语料审计用最廉价探针先行。**

## 什么时候用 / 不用
- **用**：写/移动/评审/审计 AI-OS 自身文档（README / ONBOARD / TOOL_RUNTIME / MAP / AGENTS +
  evolution/ + capabilities/ + maintenance-skills/ 文档）或 workspace 项目文档；决定一篇文档放哪个
  层级、是教程还是参考、写多长；收到 "improve / audit the docs"、"文档太长"、文档预算类失败信号。
- **不用**：只是产出单份交付文档（AD / 报告 / DOCX / PPTX）——那是 `doc-generation`；把文档发布成
  站点——那是 `doc_site_projection`；对 domains 知识语料做入库/索引/生命周期维护——那是
  knowledge-space-maintenance；篇幅未超、结构清晰时的日常小改。

## 协议（AI-OS 上下文映射）
1. **结构先行（先于正文）**——对范围内每篇面向人文档：在导航树中定位，陈述自身主题并识别直接子文档；
   允许的细节层级 = 自身主题全细节、子文档按用途/职责/高层行为概括、更深解释移到拥有它的子文档并链接。
2. **按用途分类（不是路径/标题）**——教程 = 有序工作导向可观察产出；参考 = 显式范围内可查找、不要求
   顺序读。教程先私有判定起始读者（初/中/高），把每个概念追到前置条件，前移过早材料，可选高级细节
   移到后续教程或参考。
3. **拆分混合形式**——明显混合形态拆开；小次要形态放清晰标注章节。
4. **放置约束**——生成目录/清单永不手编（改生成器或源）；移动/重命名前 grep 入站引用（链接 + 锚点）；
   移动是原子的：旧移除 + 新加入 + 同一改动修全部入站链接；双语配对文档每次编辑都欠一个对应面更新
   （V2 当前无翻译配对基建，原则是"先知道安置成本再选家"）。
5. **语料审计（最廉价探针先行）**——
   ① 词数找未预算 outlier；
   ② 会话视角残留（死设计会话引用 / 变更叙述 / 评审编排 / 控制流叙述 / 测试走读）——只保留非显然契约
   与持久理由，同一理由在一处有家、他处链接；
   ③ grep 特色短语找重复——保留一处，其余改链接；
   ④ 手写目录 / 测试清单 / 状态盘点 → 权威树 / 脚本 / 生成物；
   ⑤ implemented 记录（V2：归档 task card / pattern / SUCCESS_LOG）里移除迁移计划 / 验收清单 /
   未来时态规范，保留精简验证契约（行为 + 层级 + 指名覆盖缺口）；
   ⑥ 若删措辞会改变承诺行为（而非解释）→ 先走 proposed 记录（任务卡 / 决策草案），不静默改。
   排除 archived 冻结快照，不跟随归档清理进入冻结目标。
6. **预算纪律**——超长按 relocate（移到更合适归属）→ condense（压缩）→ raise（提预算并说明理由）
   顺序处理；承重规则保留为 1-3 行 + 指向理由的链接；删故事/重复/状态注记/推导路径；不新建解释仅为
   搬运可丢弃的推理；篇幅本身不是缺陷。
7. **验证与汇报**——跑范围内最便宜的既有检查；汇报词数增量、刻意长例外、实际跑过的检查清单；
   不声称没跑过的门禁。

## 不携带清单（repo 专属死引用，硬搬会注入）
deepseek-harness 的 `docs/AGENTS.md`（标准之家）、`pnpm run verify-doc-budgets` / `verify-md-links` /
`verify-doc-refs` / `change-scope` / `doc-sync` / `lint` / `verify-translation-pairing`、`git ls-files
'*.md' ':(exclude)vendor/**' | xargs wc -w` 流水线、JSDoc 类型等价围栏、翻译 triplet（foo.md +
foo.zh.md + foo.i18n.yaml）与 `.agents/notes/` implemented / archived 目录契约在 V2 无对应物；
**原样整体不适合独立装配**。若未来真实项目本身就是 deepseek-harness 类仓库，直接装载原文
`evolution/intake/dsh-doc-standards/SKILL.md`（本 pattern 只带可迁移方法层）。

## 与既有知识的关系（互补，非重复）
- `doc_site_projection`（D-023）= 文档"发布成站点"的受测投影（单一源 / manifest / 链接完整性 /
  部署分离）；本文 = 文档"怎么写 / 放哪 / 多长 / 审计"的作者侧标准——互补：先有结构标准，再谈投影发布。
- `doc-generation` = 收尾产出单份交付文档（AD / 报告 / DOCX / PPTX）——不同工作面。
- `knowledge-space-maintenance`（D-016/D-022）= domains 知识语料的维护（frontmatter / 索引 / 去重 /
  生命周期）——本文的语料审计是"对文档语料的通用审计方法"，两者互补：知识语料的具体维护动作由维护
  Skill 执行。
- 宪法 Writing 规则（环境事实→env/、可复用经验→patterns/、项目专属→projects/、任务记录→task_cards/）
  是一行式放置规则的具体实例；本文补上通用方法（层级 / 形态 / 预算 / 审计）。
- 同族 DSH 文档 Skill 已分别独立收编：dsh-pre-push-checks 推前检查 → `pre_push_evidence_gate`
  （D-027）、dsh-prose-standard 编辑判断 → `prose_standard`（D-028）、dsh-translate-docs 双语配对
  → `bilingual_doc_pairing`（D-029）、dsh-trim-cot-leakage 会话残留分类 → `cot_leakage_trim`
  （D-030）；dsh-find-simplifications（简化提案）已独立收编为 `simplification_audit` pattern
  （D-025，2026-08-24）——与本文互补：本文管"文档怎么写/放哪/多长"，各 pattern 管各自工作面。

## 检查清单（文档工作中自测）
- [ ] 写之前定位了吗：主题 + 直接子文档 + 允许的细节层级？
- [ ] 是按用途（教程/参考）分类的，不是按路径/标题？
- [ ] 教程的前置条件 / 起始读者判定过了吗；过早材料移走了吗？
- [ ] 移动/重命名时入站链接在同一改动里修完了吗？
- [ ] 手编过生成目录/清单吗（应该改源/生成器）？
- [ ] 保留的是承重规则（1-3 行 + 链接），删掉的是故事/重复/状态注记/推导？
- [ ] 删措辞没有改变承诺行为吗（改变则先走 proposed 记录）？
- [ ] 汇报里列了实际跑过的检查与词数增量吗？

## 可装配工作模式（Assembled / Conditional · D-041）

完整工作模式单位（剔除 docs/AGENTS.md / pnpm 验证器 / 翻译 triplet / .agents/notes 死引用后
的整包，可装载激活）在 `capabilities/doc_standards.md`——命中 trigger（写/移动/评审/审计仓库
文档、决定文档层级/形态/长度、"improve / audit the docs" 类指令、文档预算与语料审计信号）时
装载该单位、执行完整流程（结构先行 → 用途分类 → 教程前置条件 → 拆分混合形式 → 放置约束 →
语料审计廉价探针 → 预算 relocate-condense-raise → 验证汇报）；需要边界论证、不携带清单或与
既有知识互补关系时回读本 pattern（多关系：单位主体 + 知识引用 + 触发，D-034/D-041）。本
pattern 仍为方法层 Reference（Searchable，experience_push 检索源）。
