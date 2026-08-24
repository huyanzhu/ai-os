---
rule_id: knowledge_admission_rule
title: 经验入库前轻量审查（Knowledge Admission Gate）
trigger:
  - 准备往 domains/experiences 或 domains/patterns 写入新经验时
  - 收工复盘发现值得沉淀的经验时
keywords:
  - 经验
  - 入库
  - 审查
  - pattern
  - gate
---

# 经验入库前轻量审查

> 来源：A04/A05（v1 审查 Gate，REDUCE-008 错误删除后缺口至今）；V2 恢复最小形态——不建系统，只加审查动作。

## 规则（入库前四问）

1. **类型**：这是经验（可复用）还是事实（一次性）？经验才入库，事实留任务卡/账本。
2. **可执行性**：能不能写出"遇到 X → 做 Y"？写不出就不是经验。
3. **去重**：domains 里是否已有覆盖？（有 → 合并/引用，不新建）
4. **证据**：这条经验有真实来源吗？（磁盘/git/失败/任务记录；无 → 标"未核实/待验证"）

## 触发点

- 收工复盘（wrapup 时）判断"是否值得沉淀"后；
- 四问通过 → 写入 domains/experiences 或 domains/patterns；
- 不通过 → 不写，或标"未核实"。

> 这是【建议方向（未核实）】级规则：思想来自 v1 考古（RECOVER），价值待真实使用检验。
