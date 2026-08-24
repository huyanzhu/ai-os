---
rule_id: design_token_first
title: Design Token First（设计从 Token 开始）
trigger:
  - design 任务类型
  - 新建页面或组件
  - UI 一致性设计
keywords:
  - design token
  - frontend
  - UI
  - 一致性
  - guideline
---

# Design Token First

> 来源: Figma Design System
> 类型: Guideline
> 域: frontend

## 原则

设计从 Token 开始（颜色、字体、间距），不是从页面开始。Token 保证一致性。

## 怎么做

1. 定义 Token: 颜色、字体、间距、圆角
2. 定义 Primitive: Button, Input, Icon
3. 定义 Composite: Form, Card, Modal
4. 组合 Template: Page Layout

## 什么时候用

design 任务类型 → Bootstrap Assembly 自动注入。
