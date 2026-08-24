---
rule_id: tailwind_thinking
title: Tailwind Thinking (Utility-First CSS 替代手写 CSS)
trigger:
  - 任何前端页面或组件开发
  - AI 生成 UI 时优先用 Tailwind 类名
  - 项目初始化时设置 Tailwind 配置
condition: 手写 CSS 导致代码膨胀/维护困难，AI 生成自定义 CSS 易冲突
action:
  do:
    - 所有样式直接在 HTML 中用 utility classes 表达
    - 利用设计令牌保证一致性
  dont:
    - 在 CSS 文件中写自定义样式
keywords:
  - tailwind
  - css
  - design
  - thinking
  - ui
  - frontend
  - 设计
  - 样式
  - 前端
  - 布局
  - utility-first
alias:
  - Tailwind设计
  - CSS设计模式
  - Tailwind思维
---# Pattern: Tailwind Thinking## 问题手写 CSS 导致代码膨胀、维护困难。AI 生成自定义 CSS 容易产生冲突。CSS 级联问题难以调试，样式不一致。## 解决方案使用 Utility-First CSS（Tailwind）替代手写 CSS：- 所有样式直接在 HTML 中用 utility classes 表达- 不在 CSS 文件中写自定义样式- 利用设计令牌保证一致性## 适用场景- 任何前端页面或组件开发- AI 生成 UI 时，优先用 Tailwind 类名- 项目初始化时设置 Tailwind 配置