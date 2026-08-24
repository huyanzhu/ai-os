---
rule_id: session_cookie_path_proxy
title: Session Cookie Path 与开发代理不匹配导致登录状态丢失
trigger:
  - 后端有上下文路径(context path)且前端使用代理访问后端
  - 使用 Session 进行用户认证
  - 登录 API 返回 200 但后续请求返回"请先登录"
condition: Spring/Tomcat 默认 Session Cookie Path 等于应用上下文路径，与代理请求路径不匹配
action:
  do:
    - 在 web.xml 添加 session-config 将 Cookie Path 改为 /
  dont:
    - 依赖 curl 测试验证登录(curl 不检查 cookie path 会误判正常)
keywords:
  - cookie
  - session
  - proxy
  - vite
  - login
  - path
  - 路径
  - 代理
  - context path
  - 登录丢失
---
alias:
  - Cookie路径问题
  - Session丢失
  - 代理Cookie



# Session Cookie Path Mismatch with Dev Proxy

## 问题
Vite 开发服务器将 /api 代理到 http://localhost:8085/tourism，但后端设置的 Session Cookie Path 为 /tourism。
浏览器请求路径为 /api/user/info，Cookie 路径 /tourism 不匹配请求路径 /api/user/info，
导致浏览器不发送 Cookie，登录状态丢失。

## 错误现象
- 登录 API 返回 200，但后续请求（如 /api/user/info）返回 {"code":400,"msg":"请先登录"}
- curl 带 cookie 测试正常（curl 不检查 cookie path）
- 浏览器中 Navbar 始终显示"登录"而非用户名

## 原因
Spring/Tomcat 默认的 Session Cookie Path 等于应用上下文路径（如 /tourism）。
浏览器只会在请求路径以 Cookie Path 为前缀时发送 Cookie。
/api/user/info 不以 /tourism 开头 → 不发送 Cookie → 后端创建新 Session → 用户未登录。

## 解决
在 web.xml 中添加 <session-config> 将 Cookie Path 改为 /：

\\\xml
<session-config>
    <cookie-config>
        <path>/</path>
    </cookie-config>
</session-config>
\\\

## 适用条件
- 后端有上下文路径（context path）
- 前端使用代理访问后端
- 使用 Session 进行用户认证

## 环境
- Spring 6 + Tomcat 10
- Vite dev server with proxy
- 日期: 2026-06-26
  - Cookie
  - Session
  - 路径
  - 代理
  - Nginx

