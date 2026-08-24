---
rule_id: wechat_dataid_type_mismatch
title: 微信小程序 data-id 类型匹配陷阱
trigger:
  - 微信小程序 click 事件中 data-id 匹配失败
  - data-id="1" 与数字 1 用 === 比较返回 false
condition: data-id 属性存储为字符串，与后端/JS 数字类型用 === 比较时类型不匹配
action:
  do:
    - 改用 == 比较
    - 显式 toString() 后再比较
  dont:
    - 用 === 比较 data-id 字符串与数字(类型不匹配永远为 false)
keywords:
  - wechat
  - miniapp
  - data-id
  - type
  - match
  - javascript
  - 微信
  - 小程序
  - 类型
  - 匹配
alias:
  - 微信data-id
  - 类型不匹配
  - 小程序数据类型
---

## 问题
微信小程序中 data-id 属性存储的是字符串，但后端或 JS 逻辑中获取的数据是数字类型。
使用 === 比较时类型不匹配导致条件永远为 false。

## 错误现象
- 小程序 click 事件中匹配失败
- data-id="1" 与数字 1 的 === 比较返回 false

## 解决
改用 == 或显式 toString() 后再比较。

## 环境
- 微信小程序基础库 3.x+
- 日期: 2026-06-28