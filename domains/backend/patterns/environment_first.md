---
rule_id: environment_first
title: 遇到非预期行为时优先排查环境而非怀疑 Brain
trigger:
  - Permission Denied
  - Access Denied
  - 权限不足
  - 权限拒绝
  - 路径不存在
  - File Not Found
  - 命令未找到
  - command not found
  - filesystem write blocked
  - filesystem read blocked
  - Desktop write denied
  - cwd inaccessible
  - network blocked
  - network unreachable
  - proxy blocked
  - sandbox limitation
  - sandbox restricted path
  - write restriction
  - read only
  - file lock
  - approval required
  - 拒绝访问
condition: null
action:
  do:
    - |
      检查错误信息是否包含权限关键词:
          permission denied / access denied / 权限拒绝
          sandbox / sandbox_block / sandbox limitation
          approval required / approval needed
          write restriction / write failure / write blocked
          read only / file lock / file locked
          拒绝访问 / 无权限 / 权限不足
    - |
      若包含上述关键词:
          → 执行 Level 1 Permission First:
            1. 检查 escalation_workflow.md 中是否存在已知 escalate 路径
            2. 有 → 优先请求 escalate (require_escalated)
            3. 无 → 检查 WFI-004 fallback (单 shell 写入等方案)
    - |
      若不包含上述关键词（非权限类错误）:
          → 继续标准环境检查流程:
            - 检查 sandbox 限制（network blocked, GUI限制）
            - 检查文件路径/权限（Desktop, D:\ access）
            - 检查 cwd 是否正确
            - 检查 PATH/环境变量缺失
            - 检查 shell 兼容性（PowerShell vs cmd）
            - 检查文件是否存在或路径拼写错误
            - 检查 proxy/network 配置
    - |
      若 escalate 执行后仍失败:
          → 执行 Level 2 Tool Boundary Analysis:
            - 检查是否为 sandbox 限制类型（Desktop / 网络 / GUI）
            - 检查是否为 GUI 自动化限制（窗口激活、坐标偏移、权限）
            - 检查是否为 provider 限制（stream truncation、token 上限、模型兼容性）
            - 检查是否为 shell 语法差异（PowerShell vs cmd、escape 规则）
            - 检查是否为 filesystem 限制（权限、路径长度、编码）
    - |
      若文件写入后出现乱码 / 编码错误:
          → 执行 Encoding Diagnostic:
            1. 检查 Shell 编码差异
               - PowerShell 5.1 默认: Out-File=UTF-16 LE, Set-Content=ANSI(GBK)
               - PowerShell 7 默认: Out-File=UTF-8 with BOM, Set-Content=UTF-8 without BOM
               - cmd 默认: GBK
               - Python 默认: UTF-8 (但管道到 PowerShell 时可能触发 GBK)
               - 跨 shell 管道传输时编码不一致是已知问题
            2. 检查文件写入方式
               - Set-Content / Out-File 可能加 BOM 或使用错误编码
               - Copy-Item 会重新编码内容 (可能引入 BOM)
               - Add-Content 使用目标文件现有编码 (可能不一致)
               - 推荐: [System.IO.File]::WriteAllBytes + UTF8Encoding(False)
               - 参考: powershell_encoding_cheatsheet.md (tool/)
            3. 写入后验证
               - 读取文件检查 BOM 头 (0xEF 0xBB 0xBF)
               - 检查中文是否可正常读取 (ReadAllText + UTF8)
               - 若文件是 JSON/WXML/WXSS 且报 BOM 错误 → wechat_dev_pitfalls.md
               - 若 PowerShell 管道传 Python 报 GBK 错误 → python_powershell_gbk.md
            dont:
              - 对编码问题盲目切换写入 cmdlet (应先诊断)
              - 将编码问题误判为 governance / architecture 缺陷
              - 使用 Copy-Item 复制文本文件 (会引入 BOM)
    - |
      若环境正常 + 工具正常 + escalate 正常 → 仍失败:
          → 执行 Level 3 Systemic Analysis:
            - 检查 Workflow Drift
            - 检查 Definition Drift
            - 检查 Architecture 缺陷
            - 记录 OBS 后继续排查
  dont:
    - 对已知权限模式进行连续 retry
    - 对已知权限模式进行 Tool Boundary Analysis（应先 escalate）
    - 对权限问题怀疑 Workflow Drift 或 Architecture Defect
    - 未检查环境前怀疑 governance 损坏
    - 未检查环境前怀疑 architecture 缺陷
    - 未检查环境前怀疑 reasoning 错误
    - 未检查环境前怀疑 memory corruption
keywords:
  - permission denied
  - access denied
  - sandbox
  - escalate
  - 权限
  - 拒绝访问
  - environment first
  - tool boundary
  - 环境优先
  - 编码诊断
  - sandbox_block
  - write restriction
knowledge_position: Principle
knowledge_cluster:
  - node: escalation_workflow.md
    type: predecessor_of
  - node: tool_boundary.md
    type: predecessor_of
  - node: io_runtime.ps1
    type: same_capability
epistemology_tag: PATTERN
confidence: HIGH
related_rules:
  - escalation_workflow.md (escalate 执行路径)
  - tool_boundary.md (Level 2 分析路径)
  - WFI-004 (escalate 后 fallback)
---
# Environment-First Principle# 层级: Learned Rule (Runtime)# 版本: v1.1 (WFI-005)# 来源: 多个 session 中反复验证的摩擦模式## 规则遇到问题时，优先判断是否来自环境限制。## 三级决策模型 (WFI-005)```错误信号    │    ▼Level 1 ─── 包含权限关键词? ──→ 优先 escalate    │                               │    否                          escalate 后    │                               │    ▼                               ▼Level 2 ─── 标准环境检查 ──→ escalate 后仍失败 → Tool Boundary Analysis    │    正常    │    ▼Level 3 ─── Systemic Analysis (Workflow / Definition / Architecture)```### Level 1 — Permission First当错误信息包含以下关键词时，**优先 escalate 而非分析**：- permission denied / access denied / 权限拒绝- sandbox / sandbox_block / sandbox limitation- approval required / approval needed- write restriction / write failure / write blocked- read only / file lock / file locked- 拒绝访问 / 无权限 / 权限不足**执行路径：** `escalation_workflow.md`### Level 2 — Tool Boundary仅当 escalate 后仍失败时，执行 Tool Boundary Analysis。**执行路径：** `tool_boundary.md`### Level 3 — Systemic Analysis仅当环境正常 + 工具正常 + escalate 正常仍失败时，才允许怀疑：- Workflow Drift- Definition Drift- Architecture 缺陷## 检查列表- [ ] 错误信息是否包含权限关键词（Level 1）- [ ] 若是 → escalate 是否可行- [ ] 若 escalate 后仍失败 → Tool Boundary Analysis (Level 2)- [ ] 若环境/工具/escalate 均正常仍失败 → Systemic Analysis (Level 3)## 禁止- 对已知权限模式进行连续 retry- 对已知权限模式先执行 Tool Boundary Analysis 再 escalate- 对权限问题怀疑 Workflow Drift 或 Architecture Defect- 在未检查环境前，直接怀疑 governance / architecture / reasoning / memory corruption## 来源- 2026-05-29: Desktop 写入因 sandbox 阻止，非 governance 问题- 2026-05-27: cc-connect 因 HTTP_PROXY 变量阻塞，非架构问题- 2026-06-15: WFI-005 验证 — 10 案例模拟，43% 步骤节省，误判率 20%→0%