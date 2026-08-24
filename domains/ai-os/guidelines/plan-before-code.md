---
rule_id: plan_before_code
title: Plan Before Code（不确定时先出 Plan）
trigger:
  - 改动涉及多个文件
  - 实现方式不确定
  - 不熟悉被修改的代码
keywords:
  - plan
  - 先计划
  - guideline
  - workflow
  - 验证
---

# Plan Before Code

> 来源: Claude Code, Linear Method, GitHub Flow, Figma, Cursor — 五个 Workflow 共同的第一步
> 类型: Guideline
> 域: ai-os

## 原则

不确定时先出 Plan，同意后再实现。一句话能描述 diff → 跳过 Plan。

## 为什么

让 Agent 直接写代码会产生解决错误问题的代码。Plan 是"先想清楚再动手"——它回答三个问题：改哪些文件、怎么改、怎么验证。

## 什么时候做 Plan

| 场景 | 做 Plan？ |
|------|:--:|
| 改动涉及多个文件 | ✅ |
| 不确定实现方式 | ✅ |
| 不熟悉被修改的代码 | ✅ |
| 一句话能描述 diff | ❌ 跳过 |
| 修 typo、加 log、改名 | ❌ 跳过 |

## Plan 包含什么

1. 改哪些文件
2. 每个文件改什么
3. Scope（做什么）和 Out-of-scope（不做什么）
4. 验证步骤（测试、构建、截图对比）

## 什么时候用

TaskStarted → Bootstrap Assembly → Resolver 自动装配此 Guideline。
