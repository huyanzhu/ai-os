---
rule_id: skill_fusion_doc_generation
title: Doc Generation 文档产出
trigger:
  - 收尾需要产出 AD/报告/正式交付物
  - 架构决策要落文档
keywords:
  - doc
  - 文档
  - adr
  - 报告
  - pptx
  - docx
action:
  do:
    - 架构决策→AD；阶段总结→报告/PPTX；数据→XLSX；正式交付→DOCX/PDF
---

# Doc Generation

## 是什么
在任务收尾（TaskClosed）时，生成结构化文档产物的能力：提案、AD（架构决策）、报告，以及 office 文档（DOCX / PPTX / XLSX / PDF）。

参考外部标杆：anthropics/skills 的 `docx` / `pdf` / `pptx` / `xlsx` + `doc-coauthoring` / `internal-comms`；addyosmani/agent-skills 的 `documentation-and-adrs`。

## 什么时候用
TaskClosed 事件 → Doc Generation Hook 在收尾时提示生成对应的交付文档。
（当前 Lifecycle Hook 运行时未落地，开发前夕由 Agent 在收尾时手动触发。）

## 适用场景
- 架构决策 → AD 文档
- 阶段总结 → 报告 / PPTX
- 数据导出 → XLSX
- 正式交付物 → DOCX / PDF

## 输出格式
结构化文档（按模板 templates/doc-generation.md）；文档结构范式被复用时可沉淀为 Pattern / Observation。

## 参考来源（外部 Skill 融合）
- anthropics/skills (161.4k)：docx / pdf / pptx / xlsx / doc-coauthoring / internal-comms
- addyosmani/agent-skills (78.5k)：documentation-and-adrs

## 融合映射（来自 proposal 2026-07-16）
- 能力定义 → 本 Capability
- 触发条件 → Lifecycle Hook: TaskClosed
- 输出格式 → Observation / Pattern
