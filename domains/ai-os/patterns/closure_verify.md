---
rule_id: CLOSURE-VERIFY-001
title: 闭环收口验证（扮演链路上下家 + 数据层不变式断言）
category: Testing Methodology
trigger:
  - 我这侧动作（交付/认领/验收）成功后宣告 done 之前
  - 涉及跨角色状态流转的功能（钱/里程碑/托管）
condition: 无复核者、无 QA 旁观（solo 环境），"我宣布完成"需要变成"我已证明完成"
action:
  do:
    - 我这侧成功后不立刻 declare done，切到对方侧把下一个动作真实走一遍（交付→切需求方点验收）
    - 读权威数据层（data.db/SQLite 整行）核对不变式：如"completed 时三里程碑必 accepted、托管必已结算"
    - 不变式写成属性断言（property-based testing：fast-check/Hypothesis 随机生成数据验证），机器随机测而非手写几条
    - 用一手数据（数据行）而非界面判断闭环是否真收口
  dont:
    - 只在自己这侧"成功"就收工（下游副作用未被验证）
    - 用界面表现判定收口（会被渲染层掩盖真相反差）
    - 手写断言只测正常路径（不变式要靠随机属性验证防旁路）
keywords:
  - 闭环
  - 收口
  - 上下家
  - 不变式
  - 数据层
  - 属性断言
  - 结算
alias:
  - 闭环收口验证
  - 扮演上下家
  - 链路收口
  - closure verify
  - 不变式断言
  - property-based

knowledge_position: Cluster
knowledge_cluster: FC-Test Methodology
epistemology_tag: PATTERN
confidence: HIGH
---

# 闭环收口验证（无复核者环境的下游验证）

**解决**："我这侧动作成功后不立刻 declare done，而是切到对方侧把下一个动作真实走一遍，确认整条链路真的收口——钱到账、状态自洽、里程碑翻转。"

**对应角色**：QA/测试（provider 测试账号 2026-08-06 声明）。

**核心洞察**：solo 环境没有旁观者拦你——"成功"的定义必须从"我做完我这侧"扩到"整条链路收口"。P0（验收完成但 ¥100 没结算、接单方实收 ¥0）就是"我这侧成功但下游没收口"的典型：界面显示 completed，数据层没结算。

## 三步闭环（对应角色声明 + 业界参照）

### ① 扮演下家（换身份走下一步）
- 我这侧交付/认领成功后，切到对方身份（需求方/接单方）把下一个动作真实点一遍
- 目的：验证我的动作真的产生了正确的下游副作用（不是只在我这侧"成功"）
- **业界参照**：Playwright（86k⭐）端到端浏览器自动化——把"切到对方侧走一遍"从手动变自动

### ② 数据层不变式断言（读一手数据）
- 直接读权威数据层整行，核对状态不变式：`completed ⇒ 三里程碑 accepted ∧ 托管已结算`
- 用一手数据而非界面判断——界面会被渲染层/缓存掩盖真相（debug_reconciliation 同源）
- **业界参照**：fast-check（~4.5k⭐）/ Hypothesis（~7k⭐）property-based testing——把不变式写成属性，随机生成输入验证，比手写几条断言硬一个量级（机器测旁路，不是人找旁路）

### ③ 宣告 done 的闸门
- 只有 ①② 都过，才允许 declare done
- "我宣布完成" = "我已证明完成"（Self-Verification 技能包的落地动作之一）

## 检查清单（宣告 done 前自测）
- [ ] 我切到对方侧把下一个动作真实走了一遍吗（不是只在我这侧成功）？
- [ ] 我读了数据层核对不变式吗（不是只看界面）？
- [ ] 不变式是属性断言（随机验证）还是手写几条（只测正常路径）？

## 来源
- **声明**：provider 测试账号 2026-08-06（"我这侧动作成功后不立刻 declare done，切到对方侧把下一个动作真实走一遍"）
- **外部调研（2026-08-06，GitHub 高 star）**：Playwright（86k⭐，E2E 路径自动化）/ fast-check（~4.5k⭐）、Hypothesis（~7k⭐）property-based testing（不变式属性断言）
- **关联**：debug_reconciliation（读数据层还原路径）、realpath_test（走最顺手的路）、assert_recalc（断言独立核算）、skill_pack_self_verification（整合技能包）
