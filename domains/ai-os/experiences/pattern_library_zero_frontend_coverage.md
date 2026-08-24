---
rule_id: pattern_library_zero_frontend_coverage
title: Pattern 库前端覆盖为零（Knowledge）
trigger:
  - 纯前端开发任务
  - Pattern Hook 零匹配
  - 评估知识库覆盖缺口
keywords:
  - pattern
  - frontend
  - 前端
  - 覆盖缺口
  - 知识库
---

# Knowledge: Pattern 库前端覆盖为零

**来源**: Sprint 5 — 纯前端开发（HTML/CSS/JS）
**日期**: 2026-07-13
**类型**: 覆盖缺口

---

## 内容

brain/patterns/ 共 39 个 pattern（13 success + 26 failure），全部来自后端开发经验（Java/Spring/MySQL/微信小程序/编码）。本次 Sprint 是纯前端开发，Pattern Hook 执行后**零匹配**。

**缺口**：缺少前端开发类 pattern。包括但不限于：
- UI 重构策略
- 会话管理（ChatGPT 风格交互）
- 前端状态管理
- 响应式设计

**方向**：随着前端开发继续，自然积累前端 pattern。不需要专门"补前端 pattern"——等真实前端开发中遇到值得复用的经验时，自然写入。

**相关**: [[agent_unreliable_event_detector]] [[bootstrap_as_unified_entry]]
