# Changelog

## 2026-08-25 · First evidence-driven post-release improvement

`task_start` empty-state guidance — 首次由独立使用观察直接驱动的发布后改进。

- 触发：两个独立 fresh Agent 先后撞到同一摩擦——空结果（无 active 任务卡 / 知识未命中 / 能力 trigger 未命中）没有下一步引导。
- 修复：三个空态分支输出明确下一步（建卡命令 / 重跑或沉淀 / 换描述或手动装配）。
- 验证：六类场景（全空 / 无能力注册表 / 知识未命中 / 能力命中 / 无查询 / `--auto`）。
