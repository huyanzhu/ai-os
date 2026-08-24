---
rule_id: springmvc_setup
title: Spring MVC 文件上传配置的两个高频错误
trigger:
  - Spring MVC 返回 404
  - Spring MVC 返回 500
  - multipart 文件上传失败
  - JSP 使用 JSTL taglib 报编译错误
condition: Spring 6 + Jakarta Servlet 6 + Tomcat 10.1
action:
  do:
    - 404 排查：检查 multipartResolver 配置文件是否被 web.xml 引用
    - 将 multipartResolver 和 view-controller 合并到 springmvc-servlet.xml
    - 500 排查：检查 JSP 是否引用了 JSTL taglib 但项目无依赖
    - JSTL 错误 → 去掉 taglib，改用纯 JSP 脚本表达式
  dont:
    - 将上传配置写在独立配置文件中而不在 web.xml 中引用
    - 在无 JSTL 依赖时使用 <c:forEach> 等 JSTL 标签
keywords:
  - spring-mvc
  - config
  - mybatis
  - interceptor
  - setup

knowledge_position: Cluster
knowledge_cluster: FC-005 Spring/Java
epistemology_tag: OBSERVATION
confidence: MEDIUM
---
alias:
  - SpringMVC配置错误
  - MVC 404
  - 文件上传500



# Spring MVC 文件上传配置失败记录

## 问题 1：404 — 配置文件未加载 multipartResolver 和 view-controller

**原因**：`web.xml` 只引用了 `springmvc-servlet.xml`，而上传相关配置写在了独立的 `fileoperation.xml` 中，未被加载。

**解决**：将 multipartResolver 和 view-controller 合并到 `springmvc-servlet.xml`，删除独立配置文件。

## 问题 2：500 — JSP 引用了 JSTL taglib 但项目无依赖

**原因**：JSP 中使用 `<%@ taglib uri="jakarta.tags.core" prefix="c" %>` 和 `<c:forEach>`，但 pom.xml 未引入 `jakarta.servlet.jsp.jstl` 依赖，JSP 编译失败。

**解决**：去掉 JSTL taglib，改用纯 JSP 脚本表达式输出结果。

## 环境

- Spring 6.0.13 + Jakarta Servlet 6.0 + Tomcat 10.1.50
- 文件上传解析器使用 `StandardServletMultipartResolver`（Spring 6 内置，无需 commons-fileupload）
- DispatcherServlet 需配置 `<multipart-config>`（在 web.xml 中）
  - Spring MVC
  - 配置
  - 404
  - 500
  - 文件上传

