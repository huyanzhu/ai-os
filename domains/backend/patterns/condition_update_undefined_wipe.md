---
rule_id: condition_update_undefined_wipe
title: 可选字段合并更新时用 !== undefined 而非 in 判断
trigger:
  - merge 风格更新函数(updateStatus/updateProfile/patchX)接收可选字段并写回存储
  - 前端只发部分字段、后端用同一个 extra 对象合并
condition: 接收可选字段并合并进持久化对象的更新函数判断字段是否提供时
action:
  do:
    - 用 extra.field !== undefined 判断字段是否真正传值
    - 未提供字段原样保留
  dont:
    - 用 'field' in extra 判断(值为 undefined 时 in 仍为 true 会清空已有值)
    - 用 obj.field || default 直接赋值(undefined/null/""都被当成未提供)
keywords:
  - condition update
  - undefined
  - in 操作符
  - merge 更新
  - 字段合并
  - partial update
  - 可选字段
  - 清空
  - patch
  - updateStatus
---

# Condition Update: 用 `!== undefined` 而非 `in`

> 来源: TASK-20260714-004 Workspace 交付物捕获（data.js updateStatus 修复）
> 类型: Pattern（失败→纠正）
> 域: backend
> 日期: 2026-07-15

## 模式

接收可选 `extra` 字段并合并进持久化对象的更新函数，判断"是否提供了某字段"时必须用 `extra.field !== undefined`，不能用 `'field' in extra`。

```js
// 正确
if (extra.delivery !== undefined) {
  t.delivery = extra.delivery || null;
}

// 错误（会清空已有值）
if ('delivery' in extra) {
  t.delivery = extra.delivery || null;
}
```

## 为什么

- 调用方经常只传部分字段，例如只更新 `status` 时写成 `{ status: 'completed' }`，但服务端拆包后 `extra = { status, provider_id: undefined, delivery: undefined }`。
- 一旦 `extra.delivery` 存在（值为 `undefined`），`'delivery' in extra` 为 **true**，于是 `t.delivery = undefined || null` → 把之前存好的交付内容**清空**。
- `!== undefined` 只对"真正传了值"的情况生效，未提供的字段原样保留。

## 触发条件

- 任何 merge 风格的更新函数（`updateStatus`、`updateProfile`、`patchX` 等）接收可选字段并写回存储。
- 前端只发部分字段、后端用同一个 `extra` 对象合并时尤其高发。

## 反模式

- `if ('field' in obj)` 当 obj 来自 `body = { ...defaults, ...partial }` 的解构。
- 用 `obj.field || default` 直接赋值（undefined 和 null 和 "" 都被当成"未提供"）。
