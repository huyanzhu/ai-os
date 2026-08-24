---
rule_id: template_var_as_js_identifier
title: Codegen 模板占位符替换后被 Vue/React 当作 JS 标识符求值
trigger:
  - 使用代码生成器(Python/Java/Shell)生成 Vue/React 模板
  - 模板中使用字符串占位符替换且占位符出现在 v-bind/JSX 表达式中
condition: 生成模板时占位符被替换为裸单词，被 Vue :to / JSX 当作 JS 变量名求值得 undefined
action:
  do:
    - 将变量直接嵌入字符串字面量(如 :to="'/food/' + s.id")
    - 在 Python 生成时直接产出完整字符串字面量
  dont:
    - 用 template.replace('API', 'food') 替换为裸单词(JS 变量名)
keywords:
  - template
  - vue
  - javascript
  - identifier
  - codegen
  - 模板
  - 变量
  - 标识符
  - v-bind
  - 代码生成
---
alias:
  - 模板变量命名
  - JS标识符冲突



# Codegen Template Variable Treated as JavaScript Identifier in Vue

## 问题
使用 Python 脚本自动生成 Vue 组件时，模板字符串中的占位符（如 API）被替换为
具体值（如 ood），但 Vue 模板将替换后的单词（如 ood）解析为 JavaScript 变量名而非字符串。

\\\html
<!-- 生成的代码 -->
<router-link :to="'/' + food + '/' + s.id">
<!-- Vue 将 food 解释为 JavaScript 变量，而非字符串 "food" -->
<!-- 实际渲染为 /undefined/1 -->
\\\

## 错误现象
- 页面链接显示为 /undefined/1 而非 /food/1
- 控制台无报错（undefined + 1 = "undefined1" → 路径为 /undefined/1）
- 只有部分路由出问题（硬编码的链接正常，变量替换的异常）

## 原因
Vue 的 :to（v-bind:to）绑定中，值会被当作 JavaScript 表达式求值。
代码生成脚本将占位符 API 替换为 ood，Vue 将 ood 视为变量名。
由于组件中没有定义名为 ood 的变量，表达式求值得 undefined。

类似问题也存在于 react 的 JSX 中（	o={"/" + food + "/" + s.id}）。

## 解决
生成模板时，将变量直接嵌入字符串字面量而不是靠变量名传递：

\\\html
<!-- 错误 -->
:to="'/' + food + '/' + s.id"

<!-- 正确 - 硬编码路径字符串 -->
:to="'/food/' + s.id"
\\\

或者在 Python 生成时：
\\\python
# 错误：API 被替换为 food（JS 变量名）
content = template.replace('API', 'food')

# 正确：直接生成完整字符串字面量
content = template.replace('{PATH}', "'/food/'")
\\\

## 适用条件
- 使用代码生成器（Python/Java/Shell）生成 Vue/React 模板
- 模板中使用字符串占位符替换
- 占位符出现在 v-bind/JSX 表达式中

## 环境
- Vue 3 + Vite
- Python 代码生成
- 日期: 2026-06-26
  - 模板
  - 变量
  - JavaScript
  - 标识符
  - 下划线

