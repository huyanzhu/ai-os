---
rule_id: shadcn_ui_thinking
title: shadcn/ui Thinking (组件作为源码而非依赖)
trigger:
  - React 项目的 UI 开发
  - 需要复杂交互组件(表格、下拉菜单、模态框)
  - AI 辅助的前端开发
condition: 从零构建复杂 UI 组件效率低，组件库作为依赖难以定制，AI 生成组件质量不稳定
action:
  do:
    - 组件作为源码而非依赖(复制进项目可修改)
    - 使用 Radix UI 原语保证可访问性
    - 结合 Tailwind CSS 定制样式
  dont:
    - 用于非 React 项目(纯静态多页 HTML、JSP/Spring MVC)
    - 仅需简单静态页面时使用
keywords:
  - ui
  - shadcn
  - component
  - design
  - thinking
  - 前端
  - 组件
  - Radix UI
  - Tailwind
alias:
  - shadcn组件
  - UI设计模式
  - React
---

# Pattern: shadcn/ui Thinking

## 问题

从零构建复杂 UI 组件（表格、对话框、表单）效率低。
组件库作为依赖难以定制；AI 生成的组件质量不稳定，可访问性容易被忽略。

## 解决方案

基于 shadcn/ui 组件库的思路进行前端开发：
- 组件作为源码而非依赖（复制进项目，可修改）
- 使用 Radix UI 原语保证可访问性
- 结合 Tailwind CSS 定制样式
- 组件结构可预测，适合 AI 生成

## 适用场景

- React 项目的 UI 开发
- 需要复杂交互组件（表格、下拉菜单、模态框）
- AI 辅助的前端开发

## 不适用

- 非 React 项目（如纯静态多页 HTML、JSP/Spring MVC）
- 仅需简单静态页面
