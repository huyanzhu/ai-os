# AI-OS 地图

> 以磁盘为准；任何结构变化 → 同步更新本图。
> 请阅读 `README.md` 并按照规范执行；正在执行或执行过不管。

| 文件/目录 | 作用 |
|---|---|
| `AGENTS.md` | 宪法（身份/L1/硬约束/设计规则） |
| `README.md` | 启动顺序（唯一必读入口：ONBOARD → TOOL_RUNTIME → 开工） |
| `ONBOARD.md` | 身份 / 宪法 / 原则 |
| `TOOL_RUNTIME.md` | 工具一行式（是什么/什么时候用）+ 故障语义 + WFI-005 |
| `AI-OS_SUCCESS_LOG.md` | 承重证据账本（append-only；消费足迹 matched/read/referenced/influence） |
| `task_cards/` | **工作记忆**（active/archive + 模板；active 支持项目文件夹，运行时创建） |
| `任务文件模板_v1.3.md` | 正式任务文件模板（R7 兑现） |
| `domains/` | 领域知识（experience_push 检索源：patterns/experiences） |
| `tools/` | task_card.py / experience_push.py / wrapup_sync.py / observe_extract.py / **task_start.py（统一开工发现，2026-08-23）** |
| `capabilities/` | **可装配能力空间**（角色/整包 Skill 单位：INDEX.md 注册表 + 单位文件；Work 开工统一发现步骤装载） |
| `evolution/` | **演化工作台**（capability-reconstitution 核心 Skill + 五个真实 Exemplars + intake/ 输入包 + workspace/INT-xxx 工作记忆 + decisions.md 裁决日志 + growth.md 成长裁决记录 + **lines.md 线注册 · Line Lifecycle**，2026-08-23） |
| `maintenance-skills/` | **演化线维护基础设施**（health-check 审计 + 维护 Skill 家：knowledge-space-maintenance；归属 Evolution） |
