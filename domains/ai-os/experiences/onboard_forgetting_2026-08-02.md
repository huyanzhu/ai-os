---
rule_id: onboard_forgetting_2026_08_02
title: Agent 会话重启时遗忘 ONBOARD 流程（2026-08-02 Observation）
trigger:
  - 新会话或新 turn 开始
  - Agent 漂移到工具层知识
  - 讨论是否新建审核 skill
keywords:
  - onboard
  - resume
  - 会话重启
  - 遗忘
  - observation
  - review
---

# Observation: Agent 会话重启时遗忘 ONBOARD 流程，用户三次纠正

- Timestamp: 2026-08-02 19:40
- Trigger Source: 用户在多轮对话中连续纠正（"你应该已经忘记了" / "还是不对 走一遍 onboard"）
- Raw Signal: 我在 2026-08-02 讨论"审核是否要建 skill"时，直接去查 WorkBuddy 的 SkillManage 市场，声称"没有现成 review skill、要新建"，却没先走 AI-OS 的 ONBOARD 流程。用户三次提示后才读 AI-OS 根目录的 ONBOARD.md / AGENTS.md / CURRENT_GOAL.md。

## 结论
1. **AI-OS 的"审核闸门"早已存在，不是待建 skill：**
   - `AGENTS.md` 的 Review 五问（Q1–Q5，Existence Questions）是最高验收层。
   - `workflows/new-feature.md` 等每一步都有 Review 步骤（"Review 五问 + Adversarial review"）。
   - 我们的"出方案→审核→执行"中，审核 = 把 Review 五问套在方案上，无需新建 WorkBuddy skill。
2. **AI-OS 的 "Skill sandbox" 在 `AGENTS.md:246` 明确标为 "not built"（Value-Not-Proven）。** 在 Review 五问实践稳定前就把它做成自动化 skill，违反 "Capture before Automation"（同一 Proposal 反复验证 ≥3 次才自动化）。
3. **混淆了两个 skill 系统：** WorkBuddy 的 `SkillManage`（工具层）vs AI-OS 的 capability/workflow（轻量、五问验收）。用户指的路是后者。

## 它帮到 Agent 了吗（Q1–Q5 预填）
- **Q1 价值提供**：是。本轮 ONBOARD（`resume.py` 恢复 CURRENT_GOAL + 推送经验）在我漂移到"用 WorkBuddy 工具知识替代 AI-OS 自身机制"时，把我重新锚定回 AI-OS 真实路径（`domains/` + `experience_push` + Review 五问）。
- **Q2 减少负担**：是。`resume.py` 一行恢复目标态，省去从日志尾重建"做到哪"。
- **Q5 承重（无/有对照）**：本轮即证据——没走 ONBOARD 时我答错（说要新建 skill），走完后答对了（用现有五问）。差异可观测。

## 下一步建议（非强制）
- 任何新会话/新 turn 开头，先 `python tools/resume.py`（或读 CURRENT_GOAL.md）+ 需要时重读 AGENTS.md，再回答"AI-OS 有没有 X / 要不要建 skill"类问题。
- "审核"类需求优先复用 Review 五问，不新建 skill，直到五问实践被 ≥3 次验证指向同一方向。
