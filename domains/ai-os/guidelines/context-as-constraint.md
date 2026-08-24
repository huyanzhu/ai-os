---
rule_id: context_as_constraint
title: Context As Constraint（上下文窗口是最稀缺资源）
trigger:
  - 上下文窗口膨胀
  - 无关历史填满上下文
  - Bootstrap 装配范围设计
keywords:
  - context
  - 上下文
  - constraint
  - bootstrap
  - 资源
  - guideline
---

# Context As Constraint

> 来源: Claude Code Best Practices
> 类型: Guideline
> 域: ai-os

## 原则

上下文窗口是最稀缺的资源。Agent 性能随上下文增长而下降。

## 为什么

无关的对话历史、文件内容、命令输出会填满上下文。Agent 开始"忘记"早期指令、犯更多错误。

## 怎么做

- 无关任务间 `/clear` 重置上下文
- 探索代码库用子 Agent，不污染主 Agent 上下文
- 纠正两次以上 → 开新会话，带上更精确的 prompt

## 什么时候用

TaskStarted → Bootstrap Assembly 自动注入。Bootstrap 装配时应只装配当前任务相关的内容，不装配与任务无关的 Capability。
