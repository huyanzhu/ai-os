---
rule_id: knowledge_frontmatter_rule
title: 知识文件 frontmatter 合规规范（rule_id/title/trigger/keywords）
trigger:
  - 新建 domains 知识文件时
  - 修复既有知识文件时
  - 校验 experience_push 检索质量时
keywords:
  - frontmatter
  - 知识库
  - 检索
  - experience_push
---

# 知识文件 frontmatter 合规规范

> 证据：v1 census（domains 84 篇，21 篇缺 frontmatter；scan_patterns 只查 frontmatter，查不出正文乱码）；v1 世界 A 经验 3 篇自然落盘均带 frontmatter。

## 规则
- 每个 domains 知识文件必须以 `---` 开头，含 `rule_id` / `title` / `trigger` / `keywords` 四键（trigger 为列表，keywords 供检索命中）。
- 正文编码必须 UTF-8 无 BOM；出现 U+FFFD 或 GBK 错位乱码即视为损坏。
- 这是【已核实事实】级规则（方向性；为检索质量兜底必须执行）。
