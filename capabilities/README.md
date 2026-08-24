# capabilities/ — Capability Space（可装配能力空间）

> 2026-08-23 建立（Evolution V0.2 起点）。与 domains/（知识）并列的第二种消费空间。

## 这里放什么

- **完整 Capability / Skill 单位**：角色定义、工作模式、整包行为协议（如 Senior Engineer persona、PR Review 工作方式）。
- 不默认拆解。只有真实证据证明需要拆成原子方法时，才拆进 domains/（知识/pattern）。

## 与 domains/ 的区别

| | domains/（知识） | capabilities/（可装配能力） |
|---|---|---|
| 消费语义 | 检索 → 读 → 采纳（信息） | 检索 → 装配 → 激活工作模式（装载） |
| 单位 | pattern / experience / guideline（可拆分） | 整包 Skill / 角色（保持完整） |
| 通道 | experience_push（任务开始知识检索） | capabilities/INDEX.md（任务开始能力检索） |

## 单位元数据（每单位一个文件 + INDEX 注册）

`name` / `source` / `trigger`（何时发挥作用）/ `activation`（如何装载）/ `status` / `decision ref`

## 规则

- 角色整包类 → 注册进 INDEX，不拆进 domains。
- Global / Callable / Searchable / Conditional / Assembled 是 Exposure/Activation 模式，不是 Capability 的类型。
- 裁决引 evolution/decisions.md。
