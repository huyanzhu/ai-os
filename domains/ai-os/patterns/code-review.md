---
rule_id: skill_fusion_code_review
title: Code Review 五轴审查（工程级）
trigger:
  - 代码完成/commit 前需要工程级质量审查
  - 合并前自查代码质量
keywords:
  - code-review
  - 审查
  - 质量
  - 五轴
  - correctness
  - readability
action:
  do:
    - 五轴审查：正确性/可读性/架构/安全/性能，分级 Critical/Important/Suggestion 含 file:line
---

# Code Review（工程级）

## 是什么
在「代码完成」时，对本次改动做工程级代码质量审查的能力。独立于 AI-OS 的进化 Review（`review` #36 五问，服务于进化数据）——本能力聚焦**代码本身的质量**，产出五轴分级 findings。

参考外部标杆：addyosmani/agent-skills 的 `code-review-and-quality` skill + `commands/review.toml`（五轴审查）。

## 什么时候用
TaskCompleted 事件 → Code Review Hook 自动触发。
（当前 Lifecycle Hook 运行时未落地，开发前夕由 Agent 在 commit / 完成前手动模拟触发。）

## 五轴审查
1. **正确性 Correctness** — 符合规格？边界处理？测试充分？
2. **可读性 Readability** — 命名清晰？逻辑直白？组织得当？
3. **架构 Architecture** — 遵循既有模式？边界清晰？抽象层级正确？
4. **安全 Security** — 输入校验？密钥安全？鉴权到位？（可委派 `security-check` 能力）
5. **性能 Performance** — 无 N+1 查询？无无界操作？（可委派性能相关能力）

## 输出格式
分级：Critical / Important / Suggestion。结构化，含 `file:line` 引用与修复建议。
模板：templates/code-review.md
可沉淀：重复出现的问题 → Pattern；一次性发现 → Observation（经 knowledge-capture）。

## 参考来源（外部 Skill 融合）
- addyosmani/agent-skills (78.5k star)：`code-review-and-quality` skill + `commands/review.toml`

## 融合映射（来自 proposal 2026-07-16）
- 能力定义 → 本 Capability
- 触发条件 → Lifecycle Hook: TaskCompleted
- 输出格式 → Observation / Pattern
