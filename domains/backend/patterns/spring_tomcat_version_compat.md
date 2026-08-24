---
rule_id: spring_tomcat_version_compat
title: Spring + Tomcat + MyBatis-Spring 版本兼容搭配
trigger:
  - Spring + Tomcat + MyBatis-Spring 版本搭配部署
  - 应用部署后 DispatcherServlet 无法匹配 URL 返回 404
condition: Spring/Tomcat/MyBatis-Spring 跨大版本搭配
action:
  do:
    - Tomcat 10 配 Jakarta Servlet 5+ / Spring 6+ / MyBatis-Spring 3+
    - Tomcat 9 配 javax.servlet 4 / Spring 5 / MyBatis-Spring 2
  dont:
    - 跨大版本混搭(如 Tomcat 10 + Spring 5)导致 DispatcherServlet 无法匹配 URL
keywords:
  - tomcat
  - spring
  - version
  - compatibility
  - jakarta
  - javax.servlet
  - MyBatis-Spring
  - 版本
  - 兼容
  - 部署
---
alias:
  - Tomcat版本不兼容
  - Spring版本匹配



 # Spring + Tomcat + MyBatis-Spring 閻楀牊婀伴崗鐓庮啇
 
 ## 閸︾儤娅? 閺備即銆嶉惄顔肩磻閸欐垶妞傞柅澶嬪閸氬牓鈧倻娈?Spring閵嗕箑omcat閵嗕府yBatis-Spring 閻楀牊婀扮紒鍕値閵? 
 ## 閻楀牊婀扮€靛湱鍙? 
 | Spring | Tomcat | Servlet API | MyBatis-Spring |
 |--------|--------|-------------|----------------|
 | 5.3.x | 9.x | javax.servlet | 2.x |
 | **6.0.x** | **10.x** | **jakarta.servlet** | **3.x** |
 
 ## 鐟欏嫬鍨? - Tomcat 10 = Jakarta Servlet 5+ = Spring 6+ = MyBatis-Spring 3+
 - Tomcat 9 = javax.servlet 4 = Spring 5 = MyBatis-Spring 2
 - 濞ｉ攱鎯屾导姘辨纯閹恒儱顕遍懛?DispatcherServlet 閺冪姵纭跺▔銊ュ斀閿涘牊澧嶉張?URL 鏉╂柨娲?404閿? 
 ## 妤犲矁鐦? 闁劎璁查崥搴ゎ問闂傤喕鎹㈤幇?URL閿?00 鐞涖劎銇氶悧鍫熸拱閸忕厧顔愰敍?04 娑撴梹妫╄箛妤佹￥閸氼垰濮╅柨娆掝嚖鐞涖劎銇?API 娑撳秴灏柊宥冣偓? 
  - Tomcat
  - 版本
  - Spring
  - 兼容
  - 部署

