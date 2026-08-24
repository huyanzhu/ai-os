---
rule_id: tomcat_jsp_hot_deploy
title: Tomcat JSP 热部署配置（Eclipse 发布模式同步）
trigger:
  - 修改 JSP 后刷新不生效
  - Tomcat 需要手动重启
  - Eclipse + Tomcat 开发环境
keywords:
  - tomcat
  - jsp
  - 热部署
  - eclipse
  - wtpwebapps
  - backend
---

# Tomcat JSP 热部署配置

## 问题

修改 JSP 文件后，刷新浏览器不生效，必须手动重启 Tomcat 服务器。

## 原因

Eclipse 中 Tomcat 默认以「发布」模式运行，修改文件后不会自动同步到 Tomcat 的工作目录。

## 解决方案

### 方案一：修改 Eclipse Server 配置（推荐）

1. Eclipse Servers 视图中双击 Tomcat 服务器
2. 在 Server Options 中勾选：
   - `Serve modules without publishing`
   - `Automatically publish when resources change`
   - `Publishing interval: 1 second`
3. 保存配置，重启 Tomcat

效果：修改 JSP 后，Eclipse 自动同步到 Tomcat 工作目录，浏览器刷新即可看到变化。

### 方案二：直接修改 Tomcat 工作目录

JSP 文件修改后，手动复制到：
`{Tomcat 工作目录}\wtpwebapps\{项目名}\`

但此方案每次修改都要手动复制，不推荐。

## 环境

- Eclipse + Tomcat 10.1
- Tomcat 工作目录由 Eclipse WTP 管理
