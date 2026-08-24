---
rule_id: domains_index
title: domains 知识库索引（4 域 × 3 类导航入口）
trigger:
  - 经验检索
  - 造前遍历
  - 新经验入库
  - 知识底账核对
keywords:
  - domains
  - 知识库
  - 索引
  - 检索
  - experience_push
  - 导航
---

# domains 知识库索引

> 导航入口（2026-08-05 补建，原缺 index.md 导致 61 篇知识无入口）。
> 用途：经验检索/造前遍历的知识侧底账。⚠️ 以磁盘为准：本索引可能失真，查具体内容以文件为准。

## 结构

4 域 × 3 类 + 顶层元规则 = 101 篇（非 README md；frontmatter 统一：rule_id/title/trigger/condition/action/keywords/alias）

| 域 | patterns（可复用经验） | experiences（失败复盘） | guidelines（设计原则） | 主题 |
|----|----------------------|------------------------|----------------------|------|
| `ai-os/` | 32 | 10 | 5 | Bootstrap 四根/Discovery 锚点/small-steps/AER/OBS 健康检查/plan-before-code/verify-before-trust/context-as-constraint + **Skill Fusion 收编（2026-08-05）：code-review 五轴/security-check/testing-tdd/doc-generation/web-research** + **双篇提示词（2026-08-06）：skill_collection_prompt（Skill 采集·纯 Skill 链·所有 Agent 通用）/problem_solving_prompt（解决问题·开发者专用）** + **双问收编三方法论（2026-08-06）：debug_reconciliation（端到端对账读数据层）/assert_recalc（断言独立核算）/realpath_test（真实用户行为路径）** + **技能包（2026-08-06）：skill_pack_direction（找方向——69 分命中）/skill_pack_self_verification（Self-Verification 自我验证——无复核者生存技能，68 分命中）** + **闭环收口验证（2026-08-06）：closure_verify（扮演链路上下家+数据层不变式断言，48 分命中）** + **科学调试协议（2026-08-23 Intake #2）：debug_protocol（复现优先→单假说证伪→证据报告；与 debug_reconciliation/testing-tdd 同簇互补）** + **文档站投影（2026-08-24 Intake #6）：doc_site_projection（仓库 Markdown 单一源 → 站点是受测投影；与 doc-generation 互补不重复，D-023）** + **文档放置与预算标准（2026-08-24 Intake #7）：doc_standards（结构先行/用途分类 tutorial-vs-reference/预算纪律/语料审计廉价探针；与 doc-generation/doc_site_projection 互补不重复，D-024）** + **证据驱动代码简化审计（2026-08-24 Intake #8）：simplification_audit（候选强度/消费方分类/信任与生命周期边界/证明或拒绝；与 code-review、senior-engineer Coding 面、knowledge-space-maintenance Lifecycle facet 互补不重复，D-025）** + **依赖变更落库（2026-08-24 Intake #9）：dependent_change_landing（官方机制优先/依赖链以实时状态为准/整链预检与整链落库/落库后验证再清理；与 git_safety_net 互补不重复，D-026）** + **推送前证据闸门（2026-08-24 Intake #10 / DSH Corpus #7）：pre_push_evidence_gate（outgoing 范围确认/按行为变更面选最小充分证据/历史重写推送保护/失败即停/推送后远端核对；与 git_safety_net、dependent_change_landing 互补不重复，D-027）** + **散文与注释编辑标准（2026-08-24 Intake #11 / DSH Corpus #8）：prose_standard（保留完整命题/按 12 类位置覆盖必需契约/编辑判断与边界决策；与 doc_standards 管放置/预算、senior-engineer 管评审纪律互补不重复，D-028）** + **双语配对文档工作流（2026-08-24 Intake #12 / DSH Corpus #9）：bilingual_doc_pairing（按变更类型分诊/ briefing 驱动最小更新（绝不因一次更新重译整篇）/ 术语表双向绑定 + 待定术语 / 逐句核验 + 结构对齐；与 prose_standard 管单侧编辑质量、doc_standards 管放置预算互补不重复，D-029）** + **会话推理转录猎杀（2026-08-24 Intake #13 / DSH Corpus #10）：cot_leakage_trim（HEAD 视角测试/八类泄漏分类（死设计会话引用/栈 PR 视角/变更叙述与版本戳/评审编排/评审者辩护/复述转录/对冲计划残留/语言碎片）/保留规则/过纠正陷阱；prose_standard=一般编辑判断、doc_standards=廉价探针，本 pattern=会话视角泄漏专项分类与修复纪律，D-030）** + **浏览器 UI 演示录制证据纪律（2026-08-24 Intake #14 / DSH Corpus #11）：browser_gif_evidence（真实树录制/一个 storyboard=一次隔离运行/状态帧捕获+精确完成谓词/编码产物验证/录制与发布分离+专用 assets 分支发布；与 verify-before-trust=验证原则、closure_verify=正确性对账、pre_push_evidence_gate=推前证据选择互补不重复，D-031）** |
| `backend/` | 40 | — | — | Java/Spring/Tomcat/MySQL/微信小程序/PowerShell/Flask 踩坑（编码 BOM/版本兼容/路径归一化/进程启动）+ notify-wechat + **Knowledge Space consolidation（2026-08-23）：startup_dependencies_injectable（启动硬依赖必须可注入/测试可复现）/sqlite_backup_include_wal（WAL 模式备份必须含 WAL）** |
| `frontend/` | 5 | — | 1 | shadcn/tailwind 思维/design-token-first + **Skill Fusion 收编：frontend-design/ui-beautification(≥80 门禁)/ui-composition(friendly-precise)** |
| `product/` | — | — | 4 | CLAUDE/VISION/ARCHITECTURE/USER_JOURNEY（产品宪法） |

> Skill Fusion 收编（2026-08-05）：9 个外部 Skill 融合能力（曾设计为 Lifecycle Hook 触发，Hook 系统已死）→ 转成 domains patterns 进 experience_push 检索源（复用活着的血管，被真实摩擦 pull）。来源标注见各文件正文"参考来源"节（addyosmani/anthropics/trailofbits/styleseed 等）。

## 用法

- **检索**：`python tools/experience_push.py "描述当前任务"`——按 trigger/keywords/alias 打分推候选。
- **alias 同义词**：2026-08-05 从 archive/brain 找回 7 个文件 alias（+flask 迁入），中文同义词可命中（"git回滚"→git_safety_net 等）。
- **造前遍历**：动手前把 domains 当作"已有什么"底账之一（见 AI-OS_MAP §三）。
- **入库**：新经验写入对应域/类，遵守 frontmatter 格式；不确定归哪→ai-os/experiences 或带观察回讨论。

## 待办

- frontend 域已覆盖（5 pattern + 1 guideline；历史缺口已闭合）
- 08-02 experiences 已全部被 git 跟踪（10/10）
- 知识入库 Gate（审查"是 pattern 还是噪音"）在工程计划阶段 4 候选

> Knowledge 空间维护由 `maintenance-skills/knowledge-maintenance` 承担（Evolution 侧 · 2026-08-23）。
> 相关对象网（2026-08-24 D-035）：跨 pattern 关系（doc 族 / git 族 / 维护面 / Facet 评审输入）见 `evolution/dsh-remapping-2026-08-24.md` §10；pattern 内以"相关对象"节双向导航。
