---
rule_id: human_centric_design
title: Human-Centric Design 原则（自然意图映射标准流程）
trigger:
  - 设计用户交互入口
  - 新增快捷指令
  - 讨论自然语言到标准流程的映射
keywords:
  - human-centric
  - 自然语言
  - alias
  - 快捷指令
  - UX
  - 交互设计
---

# Human-Centric Design 原则

## 核心

用户无需记忆系统内部编号（Skill / Stage / AIS 编号）。
用户只需表达自然意图。
系统负责自然语言 → 标准流程的映射。

## 原则

```text
一个流程可以对应多个说法
多个说法不要对应多个流程
```

## 示例

| 用户说 | 系统理解 |
|--------|---------|
| 现在做到哪了 / 当前状态 / status | AIS-001 Stage 2 Task Acquisition |
| 下一步干啥 / TODO / 待办事项 | AIS-001 Stage 2 读取 TO_DO_LIST |
| 查一下 / 搜索经验 / 之前做过吗 | AIS-001 Stage 7 Knowledge Discovery |
| 收工 / 我走了 / 今天到这 | AIS-001 Stage 9 Graceful Shutdown |
| 接着干 / 回来继续 | AIS-001 Stage 1 → Skill-002 Context Recovery |
| 健康检查 | AIS-001 Stage 3 → Skill-001 Environment Diagnosis |

## 扩展规则（Shortcut Alias Rule）

新增快捷指令时：
```text
优先增加 Alias（别名）
避免新增新的执行流程
```

## 适用范围

所有 AI-OS Agent 实例与用户的交互界面。

## 关联

- SHORTCUT_COMMANDS.md：D:\AI\docs\SHORTCUT_COMMANDS.md
- AIS-001：D:\AI\docs\AIS-001_Instance_Lifecycle_Standard.md
