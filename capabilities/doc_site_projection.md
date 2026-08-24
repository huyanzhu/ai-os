---
name: doc_site_projection
type: Assembled / Conditional（工作模式整包单位 · 可激活）
source: 外部 Skill dsh-doc-site-sync（deepseek-ai/deepseek-harness · Human 提供）；原文见 evolution/intake/dsh-doc-site-sync/SKILL.md
trigger:
  - 发布 / 更新 / 移动 / 删除文档站页面
  - 编辑站点 manifest（docs.ts 类映射文件）或导航 / 侧边栏 / 多语言结构
  - 诊断页面从站点缺失 / 投影链接失效
  - 修复投影链接（仓库相对链接在站点上的路由 / 源链接解析）
  - 站点内容变更后跑预览 / 聚焦检查 / 同步（docs:dev / docs:check / doc-sync 类）工作流
  - 建立或改造项目文档站点（VitePress / Docusaurus 等静态文档站）
activation: 开工 bootstrap 能力检索（task_start.py 查 capabilities/INDEX.md）命中本 trigger →
  读本文件全文 → 把"文档站受测投影"完整流程装载为当前任务工作模式：读拥有契约（AGENTS.md /
  doc_standards / bilingual_doc_pairing）→ 变更分类（改页 / 新页 / 移动删除 / 生成目录 /
  结构）→ manifest 白名单条目维护 → 链接保留（缺失目标即投影失败）→ 预览与验证门 → 部署分离；
  按最后"检查清单"自测后汇报
status: Assembled + Delivered（可激活）；真实文档站消费 Q1–Q5 UNKNOWN
  （V2 无文档站基建、无自然任务触发，显式不宣称已帮助）
decision_ref: D-023 / D-040
knowledge_ref:
  - domains/ai-os/patterns/doc_site_projection.md（方法层知识 · Searchable ·
    边界论证 / 不携带清单 / 与既有知识互补关系 / 边界案例沉淀区）
  - evolution/intake/dsh-doc-site-sync/SKILL.md（原文 · 若真实项目即 deepseek-harness
    类仓库直接装载原文）
---

# 文档站受测投影 — 完整工作模式（Documentation Site Projection · Assembled / Conditional）

> 本文件 = **可激活的完整工作模式单位**（剔除死引用后的整包，不是方法层摘录）。
> 装载条件与激活方式见 frontmatter `trigger` / `activation`；命中后按下面完整流程执行。
> 方法层知识（可检索、含边界论证与不携带清单）保留在
> `domains/ai-os/patterns/doc_site_projection.md`（Reference）——本文件与它互为同一对象的不同
> 承载（D-034：Physical placement 是承载，不是语义身份）。
> 原文：deepseek-ai/deepseek-harness `.agents/skills/dsh-doc-site-sync/SKILL.md`
> 。**剔除**：deepseek-harness 专属路径/文件/命令
> （死引用）；**保留**：完整文档站同步流程（剔除 ≠ 拆解）。

---

name: doc_site_projection
description: Use when publishing, updating, moving, or removing documentation website pages; editing site manifest mappings or navigation; diagnosing a page missing from the static site; fixing projected documentation links; or running the preview, check, and sync workflow after website-content changes.
tools: ["Read", "Grep", "Glob", "Bash", "Git"]

【V2 注】tools 映射：Read/Grep/Glob/Bash/Git = carrier 工具层文件 I/O、搜索与 git 执行。

## When to load this working mode

Keep repository Markdown as the only editable content source. Treat the website as a tested
projection: the manifest selects public pages, the projector rewrites them into a disposable
generated tree, and the static-site framework builds that tree. The build additionally emits
derived artifacts (a raw-Markdown twin of every route and a root index); both derive from the
same manifest and projector, so publishing, moving, or removing a page updates them
automatically and the build fails when one is missing.

【V2 注】原文 `website/docs.ts`（DocsPage 字段集 + `pairedPages()` / `mirroredPages()`）、
`scripts/project-doc-site.ts` 投影器、raw-Markdown twin + `llms.txt` 索引、VitePress 构建是
deepseek-harness 专属实现（死引用已剔除）——V2 对应：仓库实际 manifest 文件（字段集以当前
manifest 为准，不依赖记忆）、实际投影脚本/构建链、站点框架配置（VitePress / Docusaurus 类）；
"投影自动派生索引、构建缺一即失败"机制保留。

Repository translations follow the sibling pairing contract: English `foo.md`, Chinese
`foo.zh.md`, and `foo.i18n.yaml` live together. Never create `zh-CN/` or other locale
directories for website content. The site route trees are independent of that source layout:
`foo.zh.md` projects to the root route and `foo.md` projects to the matching `/en/` route.

【V2 注】翻译 triplet 契约（foo.md / foo.zh.md / foo.i18n.yaml 相邻配对、禁语言目录）是
deepseek-harness 专属文件布局（死引用已剔除）——V2 双语配对纪律已由 `bilingual_doc_pairing`
（D-029）独立收编：源文件相邻配对、不建语言目录的原则可借鉴，具体 triplet / i18n 实现以
项目实际契约为准。

## Read the owning contracts

- Read the applicable `AGENTS.md` and use the documentation-standards knowledge when deciding
  where content belongs or changing product documentation prose.
  【V2 注】原文 `docs/AGENTS.md` 与 `dsh-doc-standards` 子 skill 引用是 repo 专属（死引用已
  剔除）——V2 对应：适用 AGENTS.md（项目/文档拥有契约）+ `doc_standards`（D-024，
  domains/ai-os/patterns/doc_standards.md）。
- For an edited bilingual source, follow the lightweight routine path in the applicable
  `AGENTS.md` and the pairing contract; never invoke the extended translation workflow
  automatically.
  【V2 注】原文 `docs/AGENTS.md#writing-rules` 与 `docs/i18n/README.md` 是 repo 专属（死引用
  已剔除）——V2 对应：`bilingual_doc_pairing`（D-029）轻量例程；绝不自动调用扩展翻译工作流。
- Read the current manifest type and entries before changing the manifest; do not rely on a
  remembered field set.
  【V2 注】原文 `website/docs.ts` DocsPage 类型是 repo 专属（死引用已剔除）——V2 对应：仓库
  实际 manifest 文件的字段定义与条目，改前必读。
- Read the site-framework configuration before adding a new section, sidebar collection,
  locale, or top-level navigation item.
  【V2 注】原文 `website/.vitepress/config.ts` 是 repo 专属（死引用已剔除）——V2 对应：实际
  站点框架配置（VitePress / Docusaurus 类）。

## Classify the change

- **Edit an already published page:** change only its canonical Markdown source. Do not touch
  the manifest unless its route or navigation metadata changes.
- **Publish a new page:** create it in its owning documentation tier, then add one manifest entry.
- **Rename, move, or remove a page:** update the canonical file, manifest entry, and inbound
  repository links atomically. Remove stale manifest entries; the check rejects missing sources.
- **Publish a generated catalog:** map the generated documentation file, but change its generator
  or source metadata rather than editing the catalog by hand.
- **Change site structure:** update the manifest for ordinary pages; update site-framework
  configuration only when the existing sidebar, section, or locale model cannot express the
  change.

Never edit or commit the generated tree, cache, or build output. Except for the site's own
contract file, never add Markdown under the site directory; locale and route directories such as
`zh-CN/`, `en/`, and `api/` are invalid source layouts. Keep generated catalogs under their
owning documentation tier, freshness-gate them there, and publish them through the manifest.

【V2 注】原文 `website/.generated/` / `website/.cache/` / `website/.dist/` / `website/AGENTS.md`
是 repo 专属具体路径（死引用已剔除）——V2 对应：项目实际的生成树 / 缓存 / 构建产物目录（永不
手编或提交）；"站点目录下只放站点契约、语言/路由目录是无效源布局"原则保留，具体目录名以项目
实际布局为准。

## Add or update a manifest entry

Set every manifest field deliberately:

- `source`: repository-relative canonical Markdown path. For a complete bilingual pair, add the
  English `.md` path through the pairing helper; it derives the sibling localized file, the
  content locales, and counterpart aliases.
- `route`: public site path including the `.md` suffix.
- `label`: sidebar label, not necessarily the document H1.
- `sidebar`: reuse an existing collection unless the information architecture genuinely needs
  another one.
- `section`: reuse an existing section when possible. If adding one, also place it in the
  section order in the site-framework configuration.
- `order`: stable order within the section.
- `sourceAliases`: optional additional repository paths that should resolve to this page when
  links are projected. It does not create another public route.

【V2 注】原文 DocsPage 字段集（source / route / label / sidebar / section / order /
sourceAliases）与 `pairedPages()` / `mirroredPages()` 辅助函数是 deepseek-harness 专属实现
（死引用已剔除）——V2 对应：仓库实际 manifest 的字段与配对/回退语义（"每个字段显式设定"、"配对
辅助函数派生对应面与反向别名"、"回退辅助函数只用于单一源在两路由树回退到同一可用语言、对应面
出现后转配对"原则保留，具体字段名/函数名以项目实际 manifest 为准）。

Use the fallback helper only for a source that intentionally falls back to the same available
language in both route trees. Convert that entry to the pairing helper when its counterpart is
added. Keep the manifest an explicit public allowlist. Do not publish RFCs, postmortems, testing
guides, `AGENTS.md`, or maintainer workflows merely because they exist under the documentation
tier; add internal material only when the user explicitly expands what the site publishes.

## Preserve link behavior

Write normal repository-relative Markdown links in canonical docs. The projector applies these
rules:

- A target present in the manifest becomes a site-relative route.
- An existing target outside the manifest becomes a repository source link, including supported
  line suffixes.
- An image is the exception: its file is copied into the generated tree and referenced from
  there, so the site serves it regardless of repository visibility. It must be a regular file
  inside the repository.
- External URLs, site-absolute URLs, email links, and fragment-only links remain unchanged.
- A missing repository-relative target fails projection instead of silently producing a broken
  link.
- Cross-page fragments use the canonical repository heading id. If an authored heading emits a
  different site-framework id, place an explicit `<a id="..."></a>` immediately before it; add
  generated aliases in the owning generator.

Do not write website-specific routes into canonical Markdown just to satisfy the site framework.
Use source aliases for directory-style repository links that should resolve to a mapped index
page.

## Preview and validate

Run local preview while editing:

```sh
<项目实际预览命令>
```

The dev server watches mapped source files and reprojects them. Restart it after changing the
manifest if the new source is not picked up automatically.

【V2 注】原文 `pnpm docs:dev` 是 deepseek-harness 专属命令（死引用已剔除）——V2 对应：项目
实际预览命令（机制 = dev 服务盯源文件 + 重新投影；manifest 变更后新源未自动拾取则重启）。

Run the focused site gate before treating the mapping as valid:

```sh
<项目实际聚焦检查命令>
```

If Markdown link checks pass but the site build reports a missing fragment, follow the source
and target paths of the fragment verification.

【V2 注】原文 `pnpm docs:check` 与 `verify-doc-site-fragments` 是 repo 专属命令（死引用已
剔除）——V2 对应：项目实际聚焦检查（链接 / 源存在性）；缺失片段诊断用既有验证入口，无对应物
时手工核验并如实汇报。

Before committing a documentation-site change, run:

```sh
<项目实际同步/投影门禁命令>
<项目实际 lint 命令>
git diff --check
```

【V2 注】原文 `pnpm run doc-sync` / `pnpm run lint` 是 deepseek-harness 专属命令（死引用已
剔除）——V2 对应：项目实际的同步 / lint 命令（机制 = 提交前跑同步门禁 + lint + `git diff
--check`；`git diff --check` 本身通用保留）。

Use the pre-push evidence gate before pushing.

【V2 注】原文 `dsh-pre-push-checks` 子 skill 引用已独立收编为 `pre_push_evidence_gate`
（D-027 方法层 + D-037 物化，capabilities/pre_push_evidence_gate.md + domains pattern）——
推送前装载该单位执行完整推前验证流程。

Report the canonical files changed, manifest entries added or removed, public routes affected,
and the exact checks run.

## Keep deployment separate

Synchronizing content into the static-site build does not publish it to the internet. Do not add
hosting permissions, deployment workflows, custom domains, or public hosting unless the user
explicitly requests deployment and confirms the hosting policy.

## 检查清单（文档站同步工作中自测）

- [ ] 我只编辑了规范 Markdown 源（没有手编生成树 / 缓存 / 构建产物）？
- [ ] 变更按分类处理了吗（改已发布页 / 新页 / 重命名移动删除 / 生成目录 / 站点结构）？
- [ ] 重命名 / 移动 / 删除时源文件 + manifest 条目 + 仓库内入站链接是原子改的吗？
- [ ] 改 manifest 前读了当前 manifest 的字段与条目（没有依赖记忆的字段集）？
- [ ] manifest 是显式公共白名单，只发布了用户要公开的内容（没有把 RFC / 复盘 / 测试指南 /
      AGENTS.md / 维护工作流顺手发出去）？
- [ ] 规范源里只写了仓库相对链接，缺失目标在投影/构建期失败了（没有静默坏链）？
- [ ] 双语配对纪律遵守了吗（源文件相邻配对、不建语言目录；改双语源按轻量例程、不自动调用
      扩展翻译工作流）？
- [ ] 我实际跑过预览 + 聚焦检查 + 完整门禁，并在汇报里列了跑过的检查与受影响公共路由？
- [ ] 内容同步没有顺手加了部署配置 / 公网发布（部署分离）？

---

## Reference（知识侧 · 多关系）

- **方法层知识（Searchable）**：`domains/ai-os/patterns/doc_site_projection.md` ——
  可迁移方法层、触发/条件/动作 frontmatter、**不携带清单**（repo 专属死引用全列）、与
  `doc_standards` / `bilingual_doc_pairing` / `prose_standard` / `cot_leakage_trim` /
  `doc-generation` 的互补边界、边界案例沉淀区。需要边界论证或检索命中时回读本 pattern。
- **原文（Source preservation）**：`evolution/intake/dsh-doc-site-sync/SKILL.md` ——
  若未来真实项目就是 deepseek-harness 类仓库，直接装载原文（含全部 repo 专属约定）。
- **触发关系**：本单位 = 完整工作模式（Assembled / Conditional）；命中 trigger 装载执行完整
  流程；知识检索（experience_push）命中的是 domains pattern（Reference），二者互补不重复。
