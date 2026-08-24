---
rule_id: vue_template_unicode_escape
title: Vue HTML 模板中 \uXXXX 转义不会被解释
trigger:
  - Vue html 模板中使用 \uXXXX(如 \u00a5 表示¥)显示为文字而非字符
  - 确认 \uXXXX 出现在 template 中而非 script 中
condition: Vue template 编译 HTML 时 \uXXXX 不是 HTML 实体也不是 Vue 语法原样输出
action:
  do:
    - template 中直接使用实际字符
    - 在 JS 中定义变量再绑定
  dont:
    - 在 Vue template 中使用 \uXXXX 期望被解释(仅在 script 标签 JS 中有效)
keywords:
  - vue
  - template
  - unicode
  - escape
  - html
  - frontend
  - 模板
  - 编码
  - 转义
  - 前端
---
alias:
  - Vue模板Unicode
  - 转义不生效
  - Vue HTML转义


# Vue HTML Template 中 \uXXXX 转义不会被解释

## 问题
Vue html 模板中使用 \uXXXX（如 \u00a5 表示¥），页面显示为文字而不是字符。

## 原因
Vue template 编译 HTML 时，\uXXXX 不是 HTML 实体也不是 Vue 语法，原样输出。script 标签中的 JS 代码中 \uXXXX 才有效。

## 解决方案
template 中直接使用实际字符，或在 JS 中定义变量再绑定。

## 诊断
1. 检查 Vue template 中的 \uXXXX
2. 确认是否在 template 中而非 script 中
3. 替换为直接字符或 JS 变量
