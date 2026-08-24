---
rule_id: project_persistence
title: Project Persistence Workflow（PROJECT.md 轻量运行时连续性工具）
trigger:
  - 长期项目建立目录
  - 决定项目状态快照的存放位置
  - PROJECT.md 用途边界讨论
keywords:
  - project
  - persistence
  - PROJECT.md
  - 状态快照
  - workflow
---

# Project Persistence Workflow
# 层级: Knowledge
# 来源: AI-OS 项目实践验证

## 规则

每个长期项目目录中允许存在 PROJECT.md。
作为项目状态快照，非永久知识系统。

## PROJECT.md 可包含

- 当前目标
- 已完成部分
- 当前 blocker
- 关键路径
- 已验证方案
- 注意事项

## 禁止

PROJECT.md 演化为：
- 长期 memory system
- autonomous planner
- governance layer

## 原则

PROJECT.md 只是轻量 runtime continuity 工具。
项目结束时 PROJECT.md 归档到 brain/ 或 docs/。
