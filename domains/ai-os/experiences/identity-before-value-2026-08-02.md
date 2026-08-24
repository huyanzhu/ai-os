---
rule_id: identity_before_value_2026_08_02
title: 身份先于价值，是 AI-OS 反复死掉的根因（2026-08-02 Observation）
trigger:
  - Agent 不使用 AI-OS
  - 讨论 AI-OS 能力形态
  - 设计 Runtime 或 Living Pool
keywords:
  - identity
  - value
  - AI-OS
  - 身份
  - 价值
  - observation
---

# Observation: 身份先于价值，是 AI-OS 反复死掉的根因（2026-08-02）

> ONBOARD Step 4 产物：每轮至少一条 Observation。本条目记录 2026-08-02 晚用户推翻 v1 问题提纲时揭示的更底层诊断。

## 现象（v1 抓到的，但只是症状）
"Agent 不在 AI-OS 上跑"——Agent 的 substrate 是 WorkBuddy，AI-OS 只是被提醒才翻阅的外部参考。

## 真正的问题（用户 20:10 重述）
问题不是"Agent 为什么不用 AI-OS"，而是 **"AI-OS 有没有资格要求 Agent 去使用它？"**
- AI-OS 目前没有任何能力让 Agent 主动产生"我想用它"的冲动；其存在只靠 Human 提醒 / 文档 / Prompt 注入 / Workflow 规定，不靠 Agent 自身工作需求。
- 对照：Git / Docker / VSCode 能要求使用，因它们解决不可替代问题。AI-OS 对 Agent 说"来因为这是 AI-OS"，Agent 可回"为什么？"

## 历史证据（分野）
- 死掉的（Living Pool / Capability Seed / Runtime）：先决定 AI-OS 该长什么样，再求 Agent 用 → 全死。
- 活下来的（ADR / Methodology / Protocol / Memory）：根本没想成为 AI-OS，只解决真实问题，后来才被认出是 AI-OS。
- standup（今天新认识）：不是新东西，只是把 Memory 显形。

规律：活下来的都不是"为 AI-OS 建的"，是"为解决真实问题建的"。AI-OS 不是被设计出来的平台，是被"解决真实问题"一次次**认出来的副产品**。

## 核心张力
真正打架的是 **AI-OS 的"身份" vs "价值"**，且顺序错了：**身份先于价值**。这等于几件事全死的共同根因，也是"agent 不在平台上"的唯一真正解释。

## 最大发现：那句话不是 Agent 的 Want，是 AI-OS 的
昨天 Agent 说"地方牢了，可我自己的东西还是没个地方放"——当时当作用户的 Want 记下了（见 working memory 2026-07-25）。今日回看，这句话可能**是 AI-OS 自己的 Want**：AI-OS 一直没找到位置，不断问 Runtime?/Living Pool?/Protocol?/Workflow?/Standup? 该以什么形式存在。活下来的东西给的答案是反的：别问"我该以什么形式存在"，先去解决真实问题，形式自己长出来。

## 接近答案（用户今日指出）
"不是设计机制让 agent 更频繁用 AI-OS，而是让 AI-OS 成为 agent 会想用的工具。"重点在"agent 会想用"。AI-OS 无资格要求使用，只能靠价值被一次次选择。

## 待验证（不立法）
- 这个重述对不对，需 GPT（外部独立 AI）独立判断——见 `docs/ai-os-gap-problem-brief-2026-08-02.md` §7。
- 最小验证信号：下次真实产品工作时，能否观测到"Agent 自己想用 AI-OS"vs"被提醒才用"的差异。
