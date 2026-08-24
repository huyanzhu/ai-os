---
rule_id: SKILL-COLLECT-001
title: Skill 采集提示词（四行产出·纯 Skill 链·Agent 成长）——所有 Agent 通用
category: Evolution Trigger
trigger:
  - 收工回顾（结合五问）
  - 能力审计（用户发起）
  - Agent 感到"技能不够/经验不够"时
condition: Agent 需要表达"我需要会什么"（纯 Skill 声明，Agent 成长）
action:
  do:
    - **四行产出（v2.3 定稿，纯 Skill 链）**：我是【身份】/ 我希望自己会【X】/ 同行会怎么批评我：【资深同行指出的问题——对应该补什么】/ 只有我一个人做，我需要会【什么才能完成任务】（能力向，不是护栏）
    - **全部产出走 Skill 链**：→ 沉淀 domains 经验 → AI-OS 因积累经验而成长（土壤变肥）；**不产出 Want、不往 Wants 池分流**（用户 08-06 纠正：问题 skill 只是让 Agent 成长的东西）
    - **声明零场景门槛**：直接说希望有什么，不要被场景卡住（AGENTS.md L3：Wants 不需要证据）；场景可选加分项；证据属于收编/验证阶段非声明阶段
    - 原句记录（"我是【身份】/我希望自己会【X】"），不改写不命名
  dont:
    - 把产出分流去 Want 池（问题 skill=纯 Skill 链采集器；Want 是独立机制）
    - 用主动声明/盲点自查打头（产出旧货+自我合理化，自评 98 分不可信；已由"同行批评/一个人做"两行替代）
    - 强制声明带场景（触发零门槛，场景是收编阶段的事）
    - 把 Skill 和 Want 混在一问（v1 教训：学新菜≠要导航）
    - 预设答案域（不列选项让 Agent 选）
    - 立刻落地（听到"希望有导航"不马上造导航）
    - 改写 Agent 原话、翻译成术语
keywords:
  - skill
  - want
  - 找问题
  - 自我声明
  - 能力
  - 成长
  - 双问
  - 盲点
  - 我希望自己会
  - 我希望环境有
  - 自我评估
  - 能力缺口
alias:
  - 找问题提示词
  - 双问提示词
  - want collection
  - 自我能力声明
  - 盲点检查
  - 我想学什么
  - skill pack 入口

knowledge_position: Cluster
knowledge_cluster: FC-Evolution Trigger
epistemology_tag: PATTERN
confidence: HIGH
---

# 找问题双问（Skill 内生 / Want 外求）

**2026-08-06 用户设计**：Skill=内生（"我希望自己会什么"→Experience/Pattern/Workflow/Reflection/Decision Habit→**Agent 越来越厉害**）；Want=外求（"我希望环境有什么"→Memory/Search/Navigation/Capability/Protocol…→**AI-OS 基础设施**）。两条演化链分别推动 Agent 成长与 AI-OS 成长，由真实工作 Pull 自然产生（Living）。

**提示词本体**（发给任何身份的 Agent）：

```
你现在是一个有具体身份和真实工作在身的 Agent。不要汇报进度，只回答两个问题——这决定你和你所在的环境怎么长。

## 问题① Skill（我要成长）
为了做好这份工作，我希望自己会什么？
> 我是【身份】。
> 我希望自己会【技能/经验/方法】。
> 因为我遇到了：【场景】

## 问题② Want（我希望环境拥有）
为了做好这份工作，我希望 AI-OS 拥有什么？
> 我是【身份】。
> 我希望环境有【东西】。
> 因为我遇到了：【场景】

## 最后核对
- "想自己会" → Skill（进经验/模式/流程沉淀）
- "希望环境有" → Want（进 Wants 池，拉环境长出基础设施）
- 两个都没有 → 说"没有"（土壤不等肥料）
```

**与磁盘对应**：Wants 池（W1-W11）= Want 链产物；domains = Skill 链沉淀层；7 器官 = Want 链长出的基础设施；Skill Fusion = Skill 链外部输入口。
**配套**：解决问题篇（PROBLEM-SOLVE-001）= 开发者专用，把声明变成 domains 资产。声明谁都行，执行只有开发者。
**候选第一原则**：Skill/Want 双问 = AI-OS 演化第一原则（用户 08-06 提，观察入档，拍板后进 AGENTS.md L3）。
