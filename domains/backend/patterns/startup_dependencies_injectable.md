---
rule_id: startup_dependencies_injectable
title: 启动硬依赖必须可注入——外部凭证不得阻塞启动/测试复现
trigger:
  - 服务启动路径硬校验 API key / 外部凭证 / 外部服务可用性
  - 测试或 CI 需要真实外部凭证才能拉起被测服务
  - README 声称"零依赖 / 开箱即测"但干净环境跑不满
  - 编写会 spawn 被测服务的集成测试 / CI 工作流
  - 测试套件在本地全绿、换干净环境却失败
condition: 被测服务的启动路径强制要求外部凭证（如 API key），缺省即退出
action:
  do:
    - 外部凭证走环境变量/配置注入；启动只校验"有值"，缺省允许启动，调用侧按需 503/报错
    - 测试与 CI 注入假值（如 DEEPSEEK_API_KEY=test-key）：只影响启动校验，不触发真实外部调用
    - 用"无任何预置环境变量的干净环境"跑完整测试套件，作为可复现断言
    - README 的测试/运行声明先实跑再写数字，与实现一致
  dont:
    - 不在启动路径 process.exit 硬卡外部凭证（会连带拖死测试 / CI / 文档承诺）
    - 不把"我本地能跑"当成"可复现"——换干净环境验证
    - 不把假 key 注入与真实调用混淆（假值只用于启动/存根；真实调用仍需隔离、限额与密钥管理）
keywords:
  - 启动依赖
  - 可注入
  - api key
  - API_KEY
  - 环境变量
  - 测试复现
  - CI
  - 零依赖
  - injectable
  - startup
  - credential
  - 假 key
alias:
  - 测试不可复现
  - DEEPSEEK_API_KEY
  - 启动硬依赖
  - startup dependency
  - injectable dependency
---

# 启动硬依赖必须可注入

**来源**：ai-consultant 真实评审 + 修复（2026-08-23）——REVIEW_REPORT.md §4.3/P1-2、
FIX_REPORT.md §二.4；Evidence A（Knowledge Space consolidation，2026-08-23）。

## 问题

README 声称 `npm test` "10/10 suites passed in 1.2s"、零依赖开箱即测，但干净环境实测
**9/10**：server.js 启动路径对缺失的 `DEEPSEEK_API_KEY` 直接 `process.exit(1)`，
`lifecycle_contract`（HTTP 集成套件）要 spawn 服务器，缺 key 拉不起服务器 → 套件失败。
CI 两个 job 同样不注入 key → 公开 PR 必红。**"零依赖可复现"的承诺在运行时被启动硬校验击穿。**

## 为什么

启动路径把"外部凭证存在"当成进程级前置条件，而测试/CI/本地预览并不需要真实凭证——
它们只需要进程能起来。启动校验一旦升级为硬退出，就变成所有下游（测试、CI、冒烟、
Docker 启动）的公共依赖，任何一处没有该凭证都会连锁失败，且失败模式与产品逻辑无关，
纯粹是环境缺值。文档声明"可复现"与实际"需要秘密才能跑"的矛盾由此产生。

## 修复（本项目已落地，三层）

1. **启动降级**：外部凭证缺省允许启动，AI 端点按需 503/明确报错（更彻底；本项目为最小改动
   保留启动校验，改用注入）。
2. **测试/CI 注入假值**：`tests/run-all.js`、`scripts/http_smoke.js` 与
   `.github/workflows/test.yml` spawn 服务器时注入 `DEEPSEEK_API_KEY=test-key`——
   只满足启动校验，不触发真实外部调用。
3. **声明与实测一致**：README 测试声明改为实跑后的真实数字（10 套 → 12 套）。

修复后干净环境（无预置 key）`npm test` **12/12 全绿**。

## 与其他知识的关系

- `test_data_isolation`（workspaces/ai-consultant/experiences）：同主题（测试可复现性）不同机制
  ——那条管**数据目录隔离**（`AI_CONSULTANT_DATA_DIR`），本条管**凭证注入/启动接缝**；
  同一项目的两条兄弟经验，不合并。
- `testing-tdd`：TDD 是"先写失败测试再实现"的节奏；本条是"让测试环境可复现"的前置条件，
  两者叠加使用（先能复现，再谈红绿）。
- `environment_first`：WFI-005 是遇到错误时的排查顺序；本条是**预防**（设计时让环境差异
  不成为失败源），不是诊断路径。

## 检查清单

- [ ] 测试/CI 是否在无任何外部凭证预置的环境下完整通过？
- [ ] 启动路径是否允许"有配置才用、缺配置不炸"？
- [ ] 注入的假值是否只触碰启动/存根，不进入真实外部调用？
- [ ] README 声明的测试数字是否来自刚跑过的干净环境实测？
