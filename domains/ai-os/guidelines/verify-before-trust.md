---
rule_id: verify_before_trust
title: Verify Before Trust（可运行检查优先）
trigger:
  - 实现前定义验收条件
  - 实现后运行检查
  - 判断任务是否完成
keywords:
  - verify
  - 验证
  - 检查
  - 验收
  - guideline
---

# Verify Before Trust

> 来源: Claude Code Best Practices
> 类型: Guideline
> 域: ai-os

## 原则

永远给 Agent 一个可运行的检查——测试、构建、截图对比。不是"看起来对"，是"检查通过了"。

## 为什么

Agent 停止工作的条件是"看起来做完了"。没有可运行检查，"看起来"是唯一信号，每一个错误都需要 Human 发现。

## 怎么做

- 实现前：定义验收条件（什么算"完成"）
- 实现后：运行检查，读结果，迭代直到检查通过
- 检查可以是：测试套件、构建退出码、linter、截图对比

## 什么时候用

TaskStarted → Bootstrap Assembly 自动注入此 Guideline。
