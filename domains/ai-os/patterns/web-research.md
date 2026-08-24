---
rule_id: skill_fusion_web_research
title: Web Research 版本特定文档拉取（Context7 模式）
trigger:
  - 用到不熟悉的第三方库/框架
  - 库有大版本差异(API 易过时)
  - 需要最新官方示例/配置
keywords:
  - web-research
  - context7
  - 文档
  - 版本
  - 外部库
action:
  do:
    - 按库名+版本拉取官方文档入上下文，避免用过时训练知识；可靠用法沉淀为 pattern
---

# Web Research

## 是什么
在任务开始（TaskStarted）时，拉取「版本特定」的外部库文档 / 最新资料入上下文的能力。补齐 Knowledge Runtime 仅本地、无外部文档的**新鲜度缺口**。

参考外部标杆：Context7 模式（intellectronica/agent-skills / upstash context7）—— 按库名 + 版本拉取官方文档，避免用过时的训练知识写代码。

## 什么时候用
TaskStarted 事件 → Web Research Hook 在涉及不熟悉 / 有版本的外部依赖时提示拉取对应文档。
（当前 Lifecycle Hook 运行时未落地，开发前夕由 Agent 手动触发。）

## 适用场景
- 用到不熟悉的第三方库 / 框架
- 库有大版本差异（API 易过时）
- 需要最新官方示例 / 配置

## 输出格式
被注入上下文的文档片段 + 来源链接；可靠用法可沉淀为 Pattern（某库的推荐用法）。

## 参考来源（外部 Skill 融合）
- Context7 模式：intellectronica/agent-skills / upstash/context7

## 融合映射（来自 proposal 2026-07-16）
- 能力定义 → 本 Capability
- 触发条件 → Lifecycle Hook: TaskStarted
- 输出格式 → Observation / Pattern
