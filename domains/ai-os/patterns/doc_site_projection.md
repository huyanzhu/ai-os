---
rule_id: DOC-SITE-PROJECTION-001
title: 文档站受测投影（仓库 Markdown 单一源 → 站点是可验证投影）
category: Documentation Site Publishing
trigger:
  - 发布 / 更新 / 移动 / 删除文档站页面
  - 建立或改造项目文档站点（VitePress / Docusaurus 等静态文档站）
  - 文档站页面缺失 / 投影链接失效诊断
  - 网站导航 / 侧边栏 / 多语言结构变更
condition: 项目需要把仓库内 Markdown 发布成站点（当前 V2 无文档站基建——本 pattern 是方法知识；无站点时是"预置方法"，不主动制造站点）
action:
  do:
    - 保持仓库 Markdown 为唯一可编辑内容源；站点是"显式 manifest 白名单 → 投影 → 可丢弃生成树 → 站点构建"的受测投影，构建对缺失页面/缺失源失败
    - 按变更分类处理：改已发布页只改源 / 发布新页=建源 + 一个 manifest 条目 / 重命名-移动-删除=源 + manifest + 入站链接原子改 / 生成目录改生成器而非手编 / 站点结构先 manifest、现有模型表达不了才改站点配置
    - manifest 每个条目字段显式设定；manifest 是显式公共白名单，不发布 RFC / 复盘 / 测试指南 / AGENTS.md / 维护工作流，除非用户显式扩界
    - 规范源内写仓库相对链接，由投影规则解析（白名单内→站内路由 / 白名单外→源链接 / 图片拷贝 / 外部 URL 不变）；缺失目标必须投影失败而非静默坏链
    - 发布前跑预览 + 聚焦检查 + 完整门禁（构建缺页即失败）；不声称没跑过的检查
    - 内容同步 ≠ 发布：不加部署权限 / 部署工作流 / 自定义域名 / 公网托管，除非用户显式请求并确认托管政策
  dont:
    - 手编生成树 / 缓存 / 构建产物
    - 在规范 Markdown 里写网站专属路由以满足站点框架（用 manifest 别名承接目录式链接）
    - 仅因站点模型表达不了就改站点配置（先试 manifest）
    - 把内部材料（RFC / 复盘 / 测试指南 / AGENTS.md / 维护工作流）发布出去
    - 静默放过缺失链接 / 缺失源文件（构建必须失败）
    - 为文档站新增公网部署配置，除非用户显式请求
keywords:
  - 文档站
  - 文档网站
  - doc site
  - vitepress
  - docusaurus
  - 投影
  - projection
  - manifest
  - 白名单
  - 单一源
  - single source
  - 链接完整性
  - 发布
  - 部署分离
  - 双语
  - 文档站同步
alias:
  - 文档站投影
  - 站点投影
  - doc site sync
  - dsh-doc-site-sync
  - 文档站同步
  - 文档发布

knowledge_position: Cluster
knowledge_cluster: FC-Doc Publishing
epistemology_tag: PROCEDURE
confidence: HIGH
---

# 文档站受测投影（仓库 Markdown 单一源 → 站点是可验证投影）

**来源**：外部 Skill（Human 提供，Evolution Intake #6 / DSH Corpus #2）——deepseek-ai/deepseek-harness
的 `dsh-doc-site-sync` SKILL.md（2026-08-24 HTTP 200 逐字下载，原文存
`evolution/intake/dsh-doc-site-sync/SKILL.md`）。按 Skill Fusion 先例（D-004 debug-protocol：外部 Skill
→ domains patterns 进 experience_push 检索源；D-008 Human 确认知识/pattern 形态）收编为 V2 pattern。

**解决**：把"仓库里的文档"变成"可访问的文档网站"而不产生第二份可编辑真相。核心纪律：
**仓库 Markdown 是唯一可编辑内容源，网站只是它的一份可验证投影（tested projection）**——任何页面
缺失、源缺失、链接断裂都在构建期失败，而不是静默上线一个坏站点。

## 什么时候用 / 不用
- **用**：项目要建立或维护文档站（VitePress / Docusaurus 等静态站）；文档站页面缺失 /
  投影链接失效需要诊断；导航 / 侧边栏 / 多语言结构变更。
- **不用**：只是生成单份交付文档（AD / 报告 / DOCX / PPTX）——那是 `doc-generation` 的领域；
  当前 AI-OS V2 没有文档站基建，本 pattern 是方法知识，真实消费待自然文档站任务触发。

## 协议（AI-OS 上下文映射）
1. **单一可编辑源**——仓库 Markdown 是唯一可编辑源；站点由"显式 manifest 白名单 → 投影脚本 →
   可丢弃生成树 → 站点构建"生成。生成树 / 缓存 / 构建产物**永不手编**。
2. **按变更分类处理**——
   - 改已发布页：只改规范 Markdown 源，不动 manifest（除非路由 / 导航元数据变了）；
   - 发布新页：在所属 docs 层建源，然后加一个 manifest 条目；
   - 重命名 / 移动 / 删除：源 + manifest 条目 + 仓库内入站链接**原子改**；陈旧条目必须移除
     （检查拒绝缺失源）；
   - 生成目录：映射生成的 docs 文件，但改其生成器 / 源元数据，不手编目录；
   - 改站点结构：普通页面走 manifest；只有现有侧边栏 / 分区 / 语言模型表达不了时才改站点配置。
3. **manifest 显式白名单**——每个条目的字段（源 / 路由 / 标签 / 侧边栏 / 分区 / 排序 / 别名）显式设定；
   配对 / 回退语义显式声明。**不发布内部材料**（RFC / 复盘 / 测试指南 / AGENTS.md / 维护工作流），
   除非用户显式扩展发布范围。
4. **链接保留行为**——规范源内写仓库相对链接，由投影规则统一解析：白名单内 → 站内路由；
   白名单外但存在 → 源链接；图片 → 拷入生成树由站点服务；外部 URL / 站内绝对 URL / 邮件 /
   纯锚点 → 原样保留；**缺失仓库目标 → 投影失败，不静默坏链**。跨页锚点用规范 heading id；
   站点框架生成不同 id 时在源内显式放 `<a id>` 别名。
5. **发布前验证门**——预览（dev 服务盯源文件 + 重新投影）+ 聚焦检查（链接 / 源存在性）+
   完整门禁（构建缺页即失败）→ 才可提交。报告：改了哪些规范源 / manifest 条目增减 /
   受影响公共路由 / 实际跑过的检查清单。
6. **部署分离**——把内容同步进站点构建**不等于发布到互联网**。不加部署权限 / 部署工作流 /
   自定义域名 / 公网托管，除非用户显式请求部署并确认托管政策。

## 不携带清单（repo 专属死引用，硬搬会注入）
deepseek-harness 的 `website/docs.ts` DocsPage 字段集（source / route / label / sidebar / section /
order / sourceAliases）、`pairedPages()` / `mirroredPages()` 实现、`scripts/project-doc-site.ts`
投影器、raw-Markdown twin + `llms.txt` 衍生、VitePress 配置细节、翻译 triplet 契约
（foo.md / foo.zh.md / foo.i18n.yaml 相邻配对、禁 `zh-CN/` 语言目录）、`pnpm docs:dev` /
`docs:check` / `doc-sync` / `lint`、`dsh-doc-standards` / `dsh-pre-push-checks` /
`verify-doc-site-fragments` 等仓库机制在 V2 无对应物；**原样整体不适合独立装配**。
若未来真实项目本身就是 deepseek-harness 类仓库，直接装载原文
`evolution/intake/dsh-doc-site-sync/SKILL.md`（本 pattern 只带可迁移方法层）。

## 与既有知识的关系（互补，非重复）
- `doc-generation`（文档文件产出）= "任务收尾产出 AD / 报告 / 办公文档"；本 pattern =
  "把已有文档发布成站点"——不同工作面，互补不重复。
- 双语纪律：AI-OS 以中文为主但会产出双语交付物；"双语源文件相邻配对、不建语言目录"的方法可借鉴，
  triplet / i18n 具体实现不携带。

## 检查清单（文档站工作中自测）
- [ ] 我只编辑了规范 Markdown 源（没有手编生成树 / 缓存 / 产物）？
- [ ] 变更按分类处理了吗（改页 / 新页 / 移动删除 / 生成目录 / 结构）？
- [ ] 移动 / 删除时源 + manifest + 入站链接是原子改的吗？
- [ ] manifest 只发布了用户要公开的内容（没有把内部材料顺手发出去）？
- [ ] 缺失源 / 缺失链接在构建期失败了（没有静默坏链）？
- [ ] 我实际跑过预览 + 检查 + 门禁，并在汇报里列了跑过的检查？
- [ ] 我没有为内容同步顺手加了部署配置 / 公网发布？

## 相关对象（2026-08-24 Re-Mapping 物化 · D-035）

- doc-generation（发布侧边界，既有）；doc_standards / bilingual_doc_pairing / prose_standard / cot_leakage_trim（doc 族：发现 → 编辑判断 → 配对同步 → 泄漏修复 → 发布投影）
- 反向：bilingual_doc_pairing → 本对象（配对同步需发布投影校验）

## 可装配工作模式（Assembled / Conditional · D-040）

完整工作模式单位（剔除 docs.ts / VitePress / pnpm 死引用后的整包，可装载激活）在
`capabilities/doc_site_projection.md`——命中 trigger（发布/更新/移动/删除文档站页面、编辑站点
manifest 或导航、诊断页面缺失/投影链接失效、修复投影链接、站点内容变更后跑预览/聚焦检查/同步
工作流、建立或改造项目文档站）时装载该单位、执行完整流程；需要边界论证、不携带清单或与既有
知识互补关系时回读本 pattern（多关系：单位主体 + 知识引用 + 触发，D-034/D-040）。本 pattern
仍为方法层 Reference（Searchable，experience_push 检索源）。
