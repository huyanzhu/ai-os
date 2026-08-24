---
rule_id: PROBLEM-SOLVE-001
title: 解决问题六步（外部调研 → 收编 domains）——开发者专用
category: Evolution Execution
trigger:
  - Skill 声明/需要出现（"我希望自己会 X"）
  - 用户派调研任务
  - 发现"需要"但 AI-OS 无对应资产
condition: 需要把"需要"变成 AI-OS 的土壤（domains 资产）
action:
  do:
    - 造前遍历：先查 domains/地图/账本——已有就不调研（输出"已遍历 X/Y/Z"证据）
    - 外部调研：WebSearch/WebFetch/读 GitHub/读文档，找业界成熟做法（哪个项目/公司/标准怎么解决）；只读联网默认允许
    - 拆解：提炼 触发条件 + 做法步骤 + 边界（能/不能）+ 来源标注（外部标杆）
    - 收编：写成 domains/{域}/patterns|experiences|guidelines/ 文件（统一 frontmatter）
    - 验证：experience_push 检索能命中（"以后需要时搜得到"）
    - 登记：domains/index.md + 地图更新
  dont:
    - 未遍历就调研（重复发明）
    - 让非开发者 Agent 执行收编（声明谁都行，执行只有开发者）
    - 收编无来源/无边界的内容
keywords:
  - skill
  - 调研
  - 解决问题
  - 收编
  - 外部
  - 土壤
alias:
  - 解决问题提示词
  - 调研收编
  - problem solving
  - 外部调研

knowledge_position: Cluster
knowledge_cluster: FC-Evolution Execution
epistemology_tag: PROCEDURE
confidence: HIGH
---

# 解决问题六步（外部调研 → 收编土壤）

**2026-08-06 用户设计**：双篇分工——找问题篇（SKILL-COLLECT-001，所有 Agent 通用）= 发现需要；解决问题篇（本文件，开发者专用）= 执行补齐。两篇合起来 = **Skill 链全流程：声明 → 调研 → 拆解 → 收编 → 送达**。

**流程**：
```
1. 造前遍历   先查 domains/地图/账本——已有就不调研（防重复发明）
2. 外部调研   WebSearch / WebFetch / 读 GitHub / 读文档——找业界成熟做法；只读联网默认允许
3. 拆解       提炼：触发条件 + 做法步骤 + 边界（能/不能）+ 来源标注
4. 收编       写成 domains/{域}/patterns|experiences|guidelines/ 文件（统一 frontmatter）
5. 验证       experience_push 检索能命中
6. 登记       domains/index.md + 地图更新
```

**产出标准**：一个"需要" → 一篇可检索的 domains 资产 + 来源可追溯。

**实践先例**：Skill Fusion 收编 9 个融合能力（code-review/security/testing-tdd/doc-generation/web-research/notify-wechat/ui 系列，2026-08-05 commit 26c26ba）。
