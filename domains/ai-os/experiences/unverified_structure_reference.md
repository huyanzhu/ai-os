---
rule_id: UNVERIFIED-STRUCTURE-REF-001
title: 规范引用的结构必须先验证存在（读了规范 ≠ 执行了规范）
category: Documentation Discipline
keywords:
  - 规范引用
  - 结构验证
  - 以磁盘为准
  - structure
  - reference
trigger:
  - 文档/规范里引用了目录、文件、能力时（"经验在 patterns/""见 docs/decisions"）
  - 动手前按规范准备时
condition: 规范引用了某个结构，但该结构是否真实存在未经验证
action:
  do:
    - 执行规范引用的动作前，先验证被引用结构真实存在（ls/glob 一下）
    - 引用不存在 → 记录"规范与实际不符"，按磁盘现状调整（以磁盘为准）
    - 把"读了规范"和"执行了规范"分开自检：读了 ≠ 会执行
  dont:
    - 读到"先查已有再动手"就以为自己在执行它（v3 实证：读了没做）
    - 把不存在的引用当正常状态（说明规范已失真，该修的是规范）
---
# 读了规范 ≠ 执行了规范

**来源**: Environment Test v3（去 patterns 变体，2026-08-08）复盘——README/conventions 写"先查已有再动手/经验沉淀在 patterns/"，但 patterns/ 目录不存在；Tester 读了这两条规范，完全没验证目录存在、没查 patterns、没沉淀，事后承认"读了规范，没执行规范"。

**本质**: 声明性文字（README 写"先查已有"）不足以触发行为——行为需要可执行载体（场景化指引如 patterns/reuse_first 的"动手前先看 storage 有没有 add_note"）。这与 W11-Min 行为注入（提示词形态）同构：**塑造需要"在正确时点被送达的可执行指引"，不是放着等人内化的文字**。必达教训首条"文档失真，磁盘为真相"的实操版：引用的结构要先验证存在。
