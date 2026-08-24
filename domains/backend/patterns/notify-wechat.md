---
rule_id: skill_fusion_notify_wechat
title: Notify WeChat 任务完成通知（企业微信）
trigger:
  - 任务完成需要通知用户
  - 用户离开终端时要收到完成信号
keywords:
  - notify
  - wechat
  - 通知
  - 企业微信
  - 完成
action:
  do:
    - TaskClosed 时经 wecom 连接器发消息（格式：任务ID+一句话结论+产出路径）；未连接降级为会话内文字告知
---

# Notify WeChat

## 是什么
任务完成（TaskClosed）时，向用户发送微信（企业微信）通知的能力。让用户在离开终端时也能收到「做完了」的信号。

## 什么时候用
TaskClosed 事件 → Notify Hook 自动触发，调用企业微信（wecom）连接器发送消息。

## 前置依赖（重要）
- 企业微信连接器（wecom）必须已连接并 Trust。当前状态：**disconnected** —— 需在连接器管理页启用后方可实际发送。
- 未连接时降级：在会话内文字告知用户「任务完成」，不阻塞流程，也不报错。

## 消息格式
```
【AI-OS 任务完成】{task_id}
{一句话结论}
{产出物路径（如有）}
```

## 融合映射（来自 proposal 2026-07-16「收口」扩展）
- 能力定义 → 本 Capability
- 触发条件 → Lifecycle Hook: TaskClosed
- 输出格式 → 企业微信消息（降级为会话内文字）
