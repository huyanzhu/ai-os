# AI-OS 工具运行时（Agent 实际使用的）

> 本文档 = 工具入口：每个工具一句话（是什么 / 什么时候用）。
> 请阅读 `README.md` 并按照规范执行；正在执行或执行过不管。

## 1. 工具一行式

| 工具 | 是什么 | 什么时候用 |
|---|---|---|
| `tools/task_card.py` | 任务卡管理：`list`（看进行中卡片，含项目文件夹）· `create <标题>`（建卡）· `archive TASK-ID --confirm`（归档：任务完成 + 用户确认） | 开工建卡记目标；任务中更新状态；任务完成且用户确认后归档；项目级状态用 `PROJECT.md`（项目文件夹内） |
| `tools/experience_push.py` | 经验推送：按当前任务描述检索相关经验并**直接展示内容摘要（命中请采纳）**（Don't Pay Twice）。**外部记忆默认关闭**：仅检索当前环境（SUCCESS_LOG + domains + 项目内 `.workbuddy`）；设置 `AIOS_EXTERNAL_MEMORY` 环境变量才接入外部记忆（显式 opt-in） | 任务开始或卡住时运行；命中即采纳 |
| `tools/task_start.py` | 统一开工发现：一键列出任务卡（恢复/继续）、相关经验（读/采纳）、可装配能力/Skill（使用/装配/装载），均标注来源 | 每轮开工时运行（`--auto` 或带任务描述）；统一发现 = 任务卡 + 知识 + 能力三个来源的合体入口 |
| `tools/observe_extract.py` | 观察提取（NC-001）：从 session JSONL 提取结构化观察（能力使用 Trace / token 成本 / 时间 / 推理片段 / Artifact） | Evolution 侧需要 Cost/Time/Trace 证据时运行（Evidence Primitive 候选，等自然需求） |
| `tools/wrapup_sync.py` | 收尾写回：把收尾事件（git 提交 + 改动 + 未提交提醒）追加到任务卡 Event Log（`wrapup_sync TASK-ID`；不传则取 active 最近更新卡） | 任务结束收尾 |

## 1.5 维护层（AI-OS 基础设施 · 非普通任务上下文）

| 入口 | 是什么 | 什么时候用 |
|---|---|---|
| `maintenance-skills/health-check/` | 只读体检：扫描基础设施 → Finding/Severity/Infrastructure/Suggested Maintenance Skill/Evidence | 需要体检时；输出交 Human 裁决，不自动修 |
| `maintenance-skills/INDEX.md` | 维护能力发现入口（discovery surface） | 需要找/执行维护 Skill 时（如 knowledge-maintenance） |

## 2. 工具调用约定

- 允许串行与并行 tool 调用；并行建议单批不超过 80 并发（已验证安全值）。
- 任何时候只允许一个活跃 tool stream；前一工具完全结束后再启动下一个。
- Provider 侧错误（`invalid_request_error` 等）不影响 Agent 状态，处理方法：停止当前 stream，等待下一条用户消息。
- Framework 侧错误（`insufficient_tool_messages` 等）属框架层，停止、不 replay。
- 超时允许一次有限重试；再次失败报告 timeout。
- 未知错误码分类为 unknown，不追溯映射到 tool lifecycle error。

## 3. 不要做的事

- 不要假设存在 v1 的 phantom "自动 Bootstrap Assembly"（已归档）；统一开工发现由真实工具 `tools/task_start.py` 承担（见工具表）。
- 不要为"让 AI-OS 看起来完整"而新建 Runtime / Telemetry / State Enforcer——动机锁。
- 不要把 provider error 当成 Agent 状态损坏（架构层解耦）。

## 4. 优先级

本文件 < `AGENTS.md`（宪法）< 当前任务指令。它是工具层约定，不是治理栈。

## 5. 故障语义（免疫器官，2026-08-05 从 BOOT.md 找回）

> 故障隔离判据（源自 BOOT.md）。判据用途：**这些错误是运行层故障，不是知识库/宪法损坏**——看到它们不要启动"查 domains/改宪法"的修复路径，那是错误归因。

**Runtime Layer Failure（默认解释为运行层故障，不代表 Brain/Constitution/Memory 损坏）**：
- `insufficient tool messages`
- `invalid_request_error`
- `stream disconnect`
- `metadata fallback`

**对应行动**：
- 停止当前 stream，等待下一条用户消息（provider 侧）；框架侧停止、不 replay。
- **禁止**因此怀疑 domains/AGENTS.md/MEMORY 损坏而去重写它们（错误归因——WFI-005 C7/C8 判据："工具限制被误判为架构缺陷"是可复用失败模式）。
- 超时允许一次有限重试；再次失败报告 timeout。
- 未知错误码分类为 unknown，不追溯映射。

## 6. 决策质量（WFI-005 三级诊断，2026-08-05 从 archive 找回）

> 第一纪元 WFI-005 三级决策模型（验证报告 WFI-005-VAL 2026-06-15：10 个真实 Runtime/Tool/Sandbox 案例回放，**省步骤 43%、0 误判、0 漏诊**）。遇错时的诊断顺序——**从最可能的层开始，不跳过、不跳到最严重的**：

**Level 1 · Permission First（权限优先）**：
- 信号：`Access Denied` / 权限错误
- 动作：优先 escalate（require_escalated / 换权限路径），不要先查 ACL/怀疑数据损坏
- C1/C2 实证：原 4-7 步 → 2 步（escalate 即成功）

**Level 2 · Tool Boundary（工具边界）**：
- 信号：`insufficient_tool_messages` / 工具/沙箱/Provider 异常 / 并发限制
- 动作：检查 sandbox/shell/工具/Provider 限制——**不要**直接怀疑架构缺陷/知识损坏
- C7/C8 实证：并发读取触发 insufficient_tool_messages 被误判为 Brain corruption；并行工具调用异常被误判为架构缺陷（实测 168 次调用零异常=并行不是根因）→ **"工具限制被误判为架构缺陷"是本项目最贵的误判模式**

**Level 3 · Systemic（系统性）**：
- 信号：上述两层排除后仍异常
- 动作：才进入系统层（架构/数据/知识库）排查

**纪律**：三级是**顺序闸门**不是菜单——Level 1 信号没排除前不进 Level 2，Level 2 没排除前不进 Level 3。误判的代价 > 漏诊的代价（误判=错误归因+污染诊断路径）。
