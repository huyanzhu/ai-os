---
rule_id: tomcat_port_conflict
title: 多 Tomcat 实例共存端口冲突
trigger:
  - 多个 Tomcat 实例共存时启动失败
  - 启动报 BindException: Address already in use
condition: 多 Tomcat 实例共用默认端口(8080 HTTP / 8005 Shutdown)
action:
  do:
    - 用 netstat -ano | Select-String 端口 诊断占用
    - 修改 conf/server.xml 的 HTTP Connector port 与 Server shutdown port 为未占用端口
  dont:
    - 多实例共用默认端口 8080/8005
keywords:
  - tomcat
  - port
  - conflict
  - eclipse
  - server
  - 端口
  - 冲突
  - 8080
  - BindException
  - server.xml
alias:
  - Tomcat端口冲突
  - 端口被占用
---

# 独立 Tomcat 部署端口冲突

## 问题

多个 Tomcat 实例共存时，端口被占用导致启动失败：BindException: Address already in use。

## 冲突端口

| 端口 | 用途 | 默认值 |
|------|------|--------|
| 8080/8081 | HTTP | 8080 |
| 8005 | Shutdown | 8005 |

## 诊断

```powershell
netstat -ano | Select-String "8080|8005"
```

## 修复

修改 `conf/server.xml`：
- HTTP 端口：改 `Connector port="8080"` 为未占用端口（如 8085）
- Shutdown 端口：改 `Server port="8005"` 为未占用端口（如 8007）

改完后用 startup.bat 启动，验证端口已生效：

```powershell
netstat -ano | Select-String "8085"
```

## 来源

- Tomcat
- 端口
- 冲突
- 8080
- 占用

## 【修复注记】2026-08-23 Integrity repair（Knowledge Space Maintenance v2）

- 原正文为已固化的 GBK 错位乱码（提交时即损坏，无法无损反转；约 30 处字符不可恢复）
- 修复方式：frontmatter 保留 HEAD 完整版本（未损坏）；正文依据完整 frontmatter + ASCII 残留（netstat / 8080 / 8005 / server.xml / startup.bat）重建
- 原始损坏版本保留于备份：`D:\AI\scratch\tmp\a4-corrupted-backup-2026-08-23\`
