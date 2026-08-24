---
rule_id: failure_observation_rule
title: 失败观察记录格式（并入 E6 空结果即信号家族）
trigger:
  - 任务失败/异常时
  - 复盘是否值得沉淀 pattern 时
keywords:
  - 失败
  - observation
  - pattern
  - E6
---

# 失败观察记录格式

> 来源：v1 planner_failures（只定义格式、从未收集，2026-08-17 收编评估：不新建采集器，格式并入 E6 家族）。

## 规则
- 失败是 Observation 不是 Bug Report：记录"发生了什么 / 为什么失败（Belief 盲区？措辞？顺序？）/ 怎么修 / 是否值得成为 Pattern"。
- 触发点：任务失败或异常时，在收尾（wrapup）顺带判断是否值得沉淀；不新建专门采集器（与 E6"空结果即信号"同源）。
- 这是【建议方向（未核实）】级规则：格式来自 v1 未验证资产，价值待真实使用检验。
