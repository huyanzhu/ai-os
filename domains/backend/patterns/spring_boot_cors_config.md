---
keywords:
  - cors
  - spring-boot
  - config
  - cross-origin
---

---
rule_id: spring_boot_cors_config
title: Spring Boot 3.x CORS 閰嶇疆鏂规硶
trigger:
  - CORS 璺ㄥ煙璇锋眰琚嫆缁?  - Access-Control-Allow-Origin 閿欒
  - 鍓嶅悗绔垎绂婚」鐩法鍩熼棶棰?  - 鍓嶇鏃犳硶璋冨悗绔?API
alias:
  - CORS 閰嶇疆
  - 璺ㄥ煙
  - 鍓嶅悗绔垎绂?condition: Spring Boot 3.x + Spring Security 6.x
action:
  do:
    - 鍦?SecurityConfig 涓坊鍔?.cors(cors -> cors.configurationSource(corsConfig()))
    - 鍒涘缓 corsConfig() 鏂规硶锛宎ddAllowedOriginPattern("*")
    - addAllowedMethod("*") + addAllowedHeader("*") + setAllowCredentials(true)
    - 娉ㄥ唽鍒?UrlBasedCorsConfigurationSource
  dont:
    - 涓嶈鐢?WebMvcConfigurer + addCorsMappings锛堜細琚?Security 瑕嗙洊锛?    - 涓嶈 allowCredentials(true) + allowedOrigin("*") 娣风敤锛堟祻瑙堝櫒鎷掔粷锛?
  - CORS
  - 跨域
  - Spring Boot
  - 配置
  - 前端

