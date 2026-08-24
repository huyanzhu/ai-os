---
rule_id: flask_templates_pitfall
title: Flask templates/ 不提供静态文件服务 + Windows Python 别名冲突
trigger:
  - JS 文件放在 templates/ 目录下，HTML 引用后浏览器返回 404
  - python 命令解析到 Windows App Exec Alias 而非实际安装路径，import flask 失败
condition: Flask templates/ 专为 render_template（Jinja2）设计，不作为静态文件目录；Windows 11 默认 Python App Exec Alias 优先级高于 PATH
action:
  do:
    - 加显式路由 send_from_directory 服务 templates/ 下的 js
    - 或将 JS 放入 static/ 目录引用 /static/xxx.js
    - 小文件直接内联 JS 到 HTML
    - 用全路径运行 python（如 D:\python\python.exe app.py）
  dont:
    - 依赖 templates/ 提供静态文件服务（Flask 不会）
    - 依赖 python 命令解析到真实安装（Windows App Exec Alias 会截胡）
keywords:
  - flask
  - template
  - static
  - js
  - python
  - 404
  - serve
  - alias
  - 渲染
alias:
  - Flask模板错误
  - Jinja2问题
  - Python别名冲突
---

# Flask Templates 静态文件 & Windows Python 别名

> 来源: brain/patterns/failure/flask_templates_pitfall.md（2026-06-17 迁移漏网，2026-08-05 考古找回）

## Observation 1: Flask templates/ 不提供静态文件服务

### 表现
JS 文件放在 `templates/` 目录下，HTML `<script src="parallelChart.js">` 引用后，浏览器请求返回 404，导致 `is not defined` 错误。

### 根因
Flask 的 `templates/` 目录专为 `render_template` 设计（Jinja2 模板渲染），不作为静态文件服务目录。浏览器请求 `/parallelChart.js` 时，Flask 无匹配路由返回 404。

### 修复
添加显式路由：
```python
from flask import send_from_directory

@app.route("/<filename>.js")
def serve_js(filename):
    return send_from_directory("templates", f"{filename}.js")
```

### 备选方案
- 将 JS 放入 `static/` 目录引用 `/static/parallelChart.js`
- 直接内联 JS 到 HTML 中（小文件适用）

## Observation 2: Windows Python 别名冲突

### 表现
`python` 命令解析到 `C:\Users\123\AppData\Local\Microsoft\WindowsApps\python.exe`（Windows App Exec Alias），而非实际安装的 `D:\python\python.exe`，导致 `import flask` 失败。

### 根因
Windows 11 默认安装 Python App Exec Alias，优先级高于 PATH 中的实际 Python 路径。

### 修复
使用全路径运行：`D:\python\python.exe app.py`；或修改 PATH 优先级/禁用 Windows Apps 别名。

## 适用范围
- Windows 环境下的 Flask 项目
- templates/ 含 JS/CSS 文件的场景
- Windows Python 多版本管理
