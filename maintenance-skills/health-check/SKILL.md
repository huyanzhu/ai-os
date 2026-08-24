# Health Check（AI-OS 基础设施体检 · 观察入口）

> 2026-08-23 建立（D-015 冻结）。职责面：Maintenance（AI-OS 基础设施）——**不是普通 Work Task 的默认上下文**，不进 task_start 统一发现。
> 定位：观察/发现入口。**暂不等同 NC-001**（可能复用观察能力，但只有体检流程重复稳定后才考虑沉淀为 Observation/Health primitive）。

## 职责

只读扫描 AI-OS 基础设施 → 输出维护需求清单（findings）。**不自动修；不直接决定修什么——裁决权在 Human。**

## 扫描范围（只读）

- `domains/`：重复 / 碎片 / 孤儿条目 / 索引一致性
- `capabilities/`：覆盖重叠 / 触发冲突 / 状态过期
- `task_cards/`：过期 / 未归档残留 / 项目归属
- 检索：index 与磁盘一致 / 脏数据 / 死引用
- 账本：SUCCESS_LOG / decisions / growth 完整性
- `MAP.md`：与磁盘实际一致
- **对象 → 有效 Exposure Path**（反向审计）：逐对象空间核验是否已登记 + 入口可达（INDEX / MAP / TOOL_RUNTIME / README / 启动链之一）

## 两个维度（D-020 R6）

- **Exposure Integrity**：registered? → reachable? → activation path alive?
- **Usage Health**：discovered? → consumed? → influenced?（来源：SUCCESS_LOG footprint / task_start 消费 / 任务卡）

## 对象状态（四态，不混为一谈）

- **Dead**：没有有效 Exposure，Agent 已无法正常获得
- **At Risk**：注册存在，但入口 / 目标 / 激活路径可能失效
- **Unused**：Exposure 正常，但长期没有真实消费（**Unused ≠ Dead**——不得因"没人用"就清理）
- **Dormant**：有意保持未使用，等待自然条件（正常，不属于故障）

## 输出格式（每条 Finding 五字段）

```text
Finding | Severity | Infrastructure | Suggested Maintenance Skill | Evidence
```

## 纪律

- **只读**：不修改任何文件
- **不自动修**：发现问题只报告，交 Human 裁决（修 / 不修 / 以后修 / 忽略）
- 诚实：没有证据就说没有
- 体检输出同时是"维护 Skill 需求"的来源：重复/覆盖 → knowledge / capability maintenance 需求
- 反向审计只报告"无有效 Exposure Path"（Dead / At Risk），不把 Unused / Dormant 当故障
