---
rule_id: wechat_dev_pitfalls
title: 微信小程序开发高频踩坑 — 权限/BOM/WXML/Skyline
trigger:
  - "Access to the path ... is denied"
  - "Unexpected token ﻿"
  - "unexpected character `\"`"
  - "WXML 文件编译错误"
  - "unexpected current frame status timedout"
  - BOM 相关解析错误
  - 微信开发工具崩溃
  - DevTools Crash
  - WeChat DevTools Crash
condition: 开发环境为微信开发者工具 + PowerShell + Codex CLI 交叉环境
action:
  do:
    - 文件写入拒绝 → 用 %TEMP% 中转再 Copy-Item 到目标
    - JSON/WXSS BOM 错误 → 用 [System.IO.File]::WriteAllBytes + UTF8Encoding($false) 写入
    - WXML 引号/三元表达式 → 移到 JS 预处理，WXML 只引用 data 字段
    - Skyline 超时 → 移除 renderer/skyline/componentFramework/lazyCodeLoading 配置，切回 WebView
  dont:
    - 直接用 Set-Content 写入目标路径
    - 用 Copy-Item 复制文本文件（会引入 BOM）
    - 在 WXML 中使用三元表达式或引号字符字面量
    - 保留 Skyline 配置
keywords:
  - wechat
  - miniapp
  - wxml
  - wxss
  - encoding

knowledge_position: Cluster
knowledge_cluster: FC-004 WeChat Miniapp
epistemology_tag: OBSERVATION
confidence: HIGH
---
alias:
  - 微信开发踩坑
  - 小程序开发错误
  - 微信开发者工具



# 微信小程序开发高频踩坑模式

## 问题类型
开发环境兼容性 — 微信开发者工具 + PowerShell + Codex CLI 交叉问题

## 模式 1：文件写入权限拒绝

### 表现
Set-Content / Copy-Item 报 `Access to the path ... is denied`

### 根因
PowerShell 在沙箱/受限模式下直接写入 D 盘部分目录时触发了 UAC 或权限检查。

### 修复方案
```powershell
# 不行：
Set-Content -Path $path -Value $content

# 可行：
$tmp = [System.IO.Path]::GetTempFileName() + ".ext"
Set-Content -Path $tmp -Value $content -Encoding UTF8
Copy-Item -Path $tmp -Destination $path -Force
Remove-Item $tmp -Force
```
利用系统临时目录（`%TEMP%`）中转，再 `Copy-Item` 到目标路径。

---

## 模式 2：Copy-Item 引入 UTF-8 BOM

### 表现
JSON 解析报 `Unexpected token ﻿`，WXSS 报 `unexpected '﻿'`
微信开发者工具中持续报 BOM 错误，即使已清除过。

### 根因
`Copy-Item` 在复制文件到目标路径时，PowerShell 会重新编码内容并添加 UTF-8 BOM（0xEF 0xBB 0xBF）。每次复写都会重新引入。

### 修复方案
```powershell
# 不行（会加 BOM）：
Copy-Item -Path $tmp -Destination $path -Force

# 可行（直接写字节流，无 BOM）：
$utf8NoBom = New-Object System.Text.UTF8Encoding $false
[System.IO.File]::WriteAllBytes($path, $utf8NoBom.GetBytes($content))
```
所有 .json / .js / .wxml / .wxss 文件必须用 `WriteAllBytes` + `UTF8Encoding($false)` 写入。

### 检测
```powershell
$bytes = [System.IO.File]::ReadAllBytes($path)
if ($bytes[0] -eq 0xEF -and $bytes[1] -eq 0xBB -and $bytes[2] -eq 0xBF) {
    "有 BOM，需清除"
}
```

### 批量修复
```powershell
$utf8NoBom = New-Object System.Text.UTF8Encoding $false
Get-ChildItem -Path $root -Recurse -Include *.json,*.js,*.wxml,*.wxss | ForEach-Object {
    $b = [System.IO.File]::ReadAllBytes($_.FullName)
    if ($b[0] -eq 0xEF) {
        $t = [System.Text.Encoding]::UTF8.GetString($b, 3, $b.Length - 3)
        [System.IO.File]::WriteAllBytes($_.FullName, $utf8NoBom.GetBytes($t))
    }
}
```

---

## 模式 3：WXML 中禁止使用引号和三元表达式

### 表现
```
[ WXML 文件编译错误] unexpected character `"`
  or: unexpected end
  at line X: {{condition ? ''a'' : ''b''}}
```

### 根因
微信小程序 WXML 中：
- 属性值内不能包含 `"` 双引号（会被解析为属性结束）
- `{{}}` 内不能包含 `'` 单引号字符字面量
- 不能使用三元表达式 `{{cond ? ''a'' : ''b''}}`

### 修复方案
把所有条件逻辑移到 JS 中预处理，WXML 只引用 data 字段：

```js
// JS: 预处理
Page({
  data: {
    btnText: "立即报名",
    btnType: "primary",
    msgClass: "message-item self"
  },
  onLoad() {
    // 预计算好再 setData
    this.setData({ btnText: "加入圈子", btnType: "primary" })
  },
  toggleJoin() {
    var now = !this.data.joined
    this.setData({
      joined: now,
      btnText: now ? "已加入" : "加入圈子",
      btnType: now ? "default" : "primary"
    })
  }
})
```

```xml
<!-- WXML: 只引用预计算字段 -->
<button type="{{btnType}}">{{btnText}}</button>
```

---

## 模式 4：Skyline 渲染引擎与自定义导航栏不兼容

### 表现
```
Error: [loader] unexpected current frame status timedout
    at l.getCurrentInstanceFrame (index.js:1)
```

### 根因
微信小程序 Skyline 渲染引擎（v3.15）下，`navigation-bar` 自定义组件和 `glass-easel` 组件框架存在兼容问题，`getCurrentInstanceFrame` 超时。

### 修复方案
```json
// app.json 中移除 Skyline 相关配置
// 删掉这些字段：
"renderer": "skyline",
"rendererOptions": { "skyline": { ... } },
"componentFramework": "glass-easel",
"lazyCodeLoading": "requiredComponents"
```
切回默认 WebView 渲染引擎即可。

---

## 经验分类
- 标签：wechat-miniapp, wxml, encoding, bom, permissions, skyline
- 严重程度：高（每个都会阻塞编译/预览）

## 沉淀日期
2026-05-29
  - 微信
  - 小程序
  - 开发
  - BOM
  - 权限
  - Skyline

