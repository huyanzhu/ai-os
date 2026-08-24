---
rule_id: strategy_change_rule
title: 放弃当前策略前先检索既有知识
trigger:
  - 同一问题连续修改 3 次以上仍未解决
  - 准备放弃当前策略/方案
  - 多次尝试变体仍失败
condition: 正在考虑换策略时
action:
  do:
    - 放弃当前策略前，先执行 Pattern Search（experience_push / domains 检索）
    - 检索既有知识，优先复用而非重新发明
    - 若同一方法已重试 3+ 次 → 触发 reset_over_iterative_fix
  dont:
    - 不检索就直接发明新方案
    - 不忽略知识库中已匹配的 pattern
keywords:
  - strategy
  - 策略
  - 换方案
  - pattern search
  - reset
knowledge_position: Standalone
epistemology_tag: OBSERVATION
confidence: HIGH
---

# 换策略先检索（Strategy Change Rule）

> 来源：Core-005（decisions.md），v1 记录"operational in AGENTS.md"但已漂移；本文件从决策原文恢复。

## 规则

**放弃当前策略时，先执行 Pattern Search，再发明新的。**

策略放弃时刻是知识检索价值最高的时刻——Agent 正在主动寻找替代方案。此时把失败连接到知识库，增加既有方案被复用而非重新发明的概率。

## 触发链

```text
同一方法重试 3+ 次
  → reset_over_iterative_fix（重置）
  → Step7A 重触发（B01）
```

## 为什么（operator recall）

> 反复出现：Agent 循环尝试 N 个变体，而一个完全匹配失败场景的 Pattern 闲置在知识库里。缺口不是"Pattern 不存在"，是"没人告诉 Agent 去看"。策略放弃时刻是注入这个"去看"的最高价值点。
