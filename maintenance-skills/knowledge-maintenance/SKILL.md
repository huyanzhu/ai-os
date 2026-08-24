# Knowledge Space Maintenance（Knowledge Maintenance v2 → v3 · 2026-08-24）

> v1（D-013 真实运行：知识归并 / Consolidation）→ **v2**（D-016：真实维护任务证明职责过窄，扩展为 Knowledge Space 完整性维护）→ **v3**（D-022：Lifecycle / Archive facet——Intake #5 dsh-archive-agent-notes 外部 Skill 可迁移方法层融合，补记录生命周期维度）。
> 归属：Evolution Instance 维护 AI-OS 基础设施的能力（`maintenance-skills/`）；与 capabilities/（Work 可装载的工作能力）区分。
> 入口：**不进入普通 task_start**；由 Health Check Finding 驱动（Finding → Suggested Maintenance Skill → Human 裁决 → 本 Skill）。

## 职责（均有真实证据）

- **Content / Consolidation** —— 查重/抽象/挂 Evidence/新建/归并/关联（D-013：启动依赖注入 + WAL 备份）
- **Integrity** —— 乱码/损坏修复、来源恢复（D-016 A4：两篇 GBK 乱码 pattern 反转恢复 + 重建）
- **Structure** —— frontmatter 完整性（D-016 B3：3 篇补 keywords）
- **Index / Discovery** —— 索引统计与检索可达性（D-016 B1：index 与实际对齐；A2：顶层元规则检索盲区修复）
- **Provenance** —— Evidence 原位保留、修复保留备份与注记（D-013 / D-016）
- **Lifecycle / Archive** —— 记录生命周期裁决：新增先做 supersession 审计；按未来决策价值分类 keep / archive / reject / delete；归档最小改动 + 封存纪律 + 入链修复（v3 · 2026-08-24 · Intake #5 dsh-archive-agent-notes 融合 · D-022）

## 触发条件（Activation Semantics · 本轮真实确认）

- duplicate / overlap finding（知识重复/重叠）
- malformed knowledge（乱码/损坏）
- incomplete frontmatter（结构不完整）
- stale / inconsistent index（索引过期/不一致）
- orphaned knowledge（孤儿条目）
- supersession（新记录覆盖同一决策/机制/被否替代案，需审计既有记录）
- archive / prune（记录收尾归档或语料瘦身，需未来价值裁决）
- obsolete rejection（被否提案已过时/不再防错，需删除并修链）

## 主流程

Inspect → Classify Finding（五类）→ Decide → Repair / Consolidate / Preserve / Archive / Delete → Re-index → Verify

## 过程（v1 真实运行 + v2 首次执行的稳定行为）

1. 收集候选：真实工作 Evidence（Learning Closure / 评审修复教训 / Health Check Finding）
2. 全库查重/核查：列 domains/、读 index.md、主题词+机制词检索、对照 git HEAD 与磁盘
3. 判定关系：真新增 / 重复（并入或挂接）/ 部分重叠（修正挂接）/ 兄弟（关联不合并）——**相似 ≠ 同源**
4. 抽象或修复：可执行 pattern（frontmatter 五键）；损坏可恢复则反转恢复、不可恢复则依据证据重建并标注
5. Evidence 挂接：原始实例原位保留（报告/源码/测试/备份路径），不删除原文
6. 更新索引：domains/index.md（数量 + 登记 + 待办清理）
7. 记录裁决：evolution/decisions.md + growth.md + INT（为什么新建/归并/不合并/重建）
8. 验证：experience_push 检索命中（置顶）；内容可读性/结构校验

## Lifecycle / Archive facet（v3 · 2026-08-24 · Intake #5 融合）

> 来源：外部 Skill `evolution/intake/dsh-archive-agent-notes/SKILL.md`（deepseek-ai/deepseek-harness · 2026-08-24 HTTP 200 逐字下载 · D-022）。
> 语义：v2 的五个职责管"知识/记录健不健康"；本 facet 管"哪些该留、哪些该归档、哪些该删"——按**未来决策价值**裁决；词数/年龄只是发现辅助，不是归档判据。

适用对象（AI-OS 记录/知识语料）：`domains/` 知识、`task_cards/` 工作记忆、evolution 候选（`lines.md` Candidates / `new-capabilities.md`）。
不适用：`decisions.md` / `growth.md` / `AI-OS_SUCCESS_LOG.md` —— 裁决继承账本与承重证据账本**只追加，不修剪**。

### ① 添加时的 Supersession 审计（先于落笔）

每新增一条覆盖同一决策/机制/被否替代案的记录，先做 scoped 审计：
- 完整替代 → 同批归档被替代项（或显式标记被替代）；
- 部分替代 → 保留原记录并交叉链接；
- 被否提案 → reject（诚实原因，满足 rejected 生命周期格式）；
- 已知匹配不得推迟到以后的语料审计。

### ② 未来价值分类（word count / 年龄 ≠ 判据）

- **已实现 · 保留 active**：rationale / alternatives / 负面保证 / durable·wire 语义 / 所有权边界 / 安全规则 / 重入条件 仍可能指导未来变更。长度无关。
- **已实现 · 归档**：决策已闭环且正文不太可能指导未来（一次性 UI、窄适配、已关闭的小 bug、被替代的实现细节、行为已在别处显而易见的流程史）。
- **提案 · 永不归档**：活提案保持 active；不再值得追求 → 用诚实原因 reject。
- **被否 · 仅作护栏保留**：失败方案仍是诱人的有意义错误，且正文解释了它为何失败。
- **被否 · 删除**：过时 / 被替代 / 不再可能 / 不会阻止重新诉讼该错误 → 删除整个记录，并修复或删除入链。
- **不为配额归档**：逐条语义判断；真正 borderline 案例记录给 Human 交接。

### ③ 归档机制纪律

- 正文零改动；只允许最小元数据（如 `Archived: YYYY-MM-DD`）；机械性重验（`git diff` 确认仅元数据改动）。
- 扫描 active 正文的入链：重定向到当前权威 / 仅当有意引用历史快照才保留指向归档路径 / 删除。**归档记录向外的链不验证、不修复**。
- 封存后永不编辑/移动/翻译/改格式/删除；归档记录仍是合法入链目标，但是**历史快照，不是当前行为权威**。

### ④ 验证与汇报

聚焦验证（diff / 入链扫描）+ 常规检查；汇报：active 保留数 / 归档数 / 被否保留数 / 被否删除数 / 提案 reject 数 + 每个真正 borderline 案例（词数 + 裁决）。
**不声称没跑过的检查**（如外链校验——归档验证本就不查外链）。

### ⑤ 不携带清单（repo 专属死引用，硬搬会注入）

deepseek-harness 的 triplet 结构（foo.md / foo.zh.md / foo.i18n.yaml）、`implemented/<kind>/` + `archived/<kind>/` 路径、`Status: implemented` frontmatter、sidecar hash、`pnpm run verify-archived-agent-notes` / `doc-sync` / `lint`、`dsh-pre-push-checks`、`notes/README.md` + `notes/archived/AGENTS.md` 契约、PR 内归档工作流。

## 纪律

- Evidence 不能消失（抽象/合并/重建 ≠ 丢历史；损坏原文进备份）
- "不合并"是有效结论（不为合并而合并）
- **修复不编造**：不可恢复处显式标注（修复注记），不静默补全
- 只做必要最小改动；不重构无关内容；**不吞 Task Memory / Capability / Git Governance / Retrieval 深层优化**
- 诚实：没有证据就说没有
- 归档/删除是 Human 裁决动作：维护 Skill 提供方法与执行，不自动删历史（Finding → Human 裁决 → Skill）
