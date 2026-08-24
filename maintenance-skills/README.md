# maintenance-skills/ — AI-OS 基础设施维护层

> **维护与体检是演化线的基础设施**——health-check（审计）+ maintenance-skills（修复 Skill 家）+ 登记纪律（存在性保障）均为 Evolution agent 的资产；不进普通 Work 的默认任务发现（task_start 不覆盖，成本保护）。
> 结构：**体检（观察/发现）** + **维修（维护 Skill 的家）**。

## 一、体检（观察入口 · 单列）

- `health-check/` —— 只读扫描基础设施 → Finding/Severity/Infrastructure/Suggested Maintenance Skill/Evidence；**不自动修，交 Human 裁决**。
- 定位：观察方向，暂不等同 NC-001（可能复用观察能力；只有重复稳定后才考虑沉淀为 primitive）。

## 二、维修（维护 Skill 注册表）

- `INDEX.md` —— **discovery surface**：让我知道"有什么维护能力"，不是完整定义；需要时打开 Skill 本体。
- 当前：`knowledge-maintenance`（knowledge-space-maintenance · Lifecycle / Archive facet，含 dsh-archive-agent-notes 可迁移方法层）；其余维护 Skill 由真实维护需求长出来，不预先创建。
