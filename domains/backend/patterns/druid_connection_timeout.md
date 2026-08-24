---
rule_id: druid_connection_timeout
title: Druid 连接池超时需同时配置 initialSize 和 connectTimeout
trigger:
  - Spring Boot + Druid 数据源初始化时页面卡死
  - 数据库不可达或网络延迟场景下启动卡顿
condition: Druid 连接池初始化创建连接时 TCP 超时导致卡死(maxWait 只对 getConnection 生效不约束 init)
action:
  do:
    - 配置 spring.datasource.druid.initialSize=0
    - 配置 spring.datasource.druid.connectTimeout=2000
  dont:
    - 依赖 maxWait 约束 init()(maxWait 只对 getConnection() 生效)
keywords:
  - druid
  - connection timeout
  - initialSize
  - connectTimeout
  - spring
  - jdbc
  - 连接池
  - 数据库超时
  - DataSource
  - maxWait
---
alias:
  - Druid连接超时
  - 数据库连接池



# Druid 连接池超时需同时配置 initialSize 和 connectTimeout

## 问题
Druid 连接池默认 initialSize=3，Spring 初始化 DataSource 时创建 3 个连接，每个 TCP 超时 30s，导致页面卡死 90s。maxWait 只对 getConnection() 生效，不约束 init()。

## 解决方案
同时配置 `initialSize=0` 和 `connectTimeout=2000`，页面 3s 内报错而非卡死。

## 配置示例
```properties
spring.datasource.druid.initialSize=0
spring.datasource.druid.connectTimeout=2000
```

## 环境
- Spring Boot + Druid 数据源
- 数据库不可达或网络延迟场景
- 日期: 2026-06-29
