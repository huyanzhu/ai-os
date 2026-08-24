---
rule_id: xml_leading_space_trap
title: apply_patch 创建的 XML 文件前导空格导致 SAXParseException
trigger:
  - apply_patch 工具创建的 XML 文件首字符为 0x20(空格)
  - XML 解析报 SAXParseException 不允许有匹配 [xX][mM][lL] 的处理指令目标
condition: apply_patch 的 + content 格式写入文件时每行前添加一个空格使 <?xml 变成  <?xml
action:
  do:
    - 用 TrimStart() 去除前导空格后 UTF8 重写字节
    - 验证首字节为 3C 3F 78 6D 6C (<?xml)
  dont:
    - 让 <?xml 前出现空格(违反 XML 规范)
keywords:
  - xml
  - space
  - apply-patch
  - sax
  - encoding
  - 前导空格
  - SAXParseException
  - 解析错误
  - 格式
  - TrimStart
---
alias:
  - XML前导空格
  - XML解析错误



 # apply_patch XML 鍓嶅绌烘牸闄烽槺
 
 ## 闂
 apply_patch 宸ュ叿鍒涘缓鐨?XML 鏂囦欢棣栧瓧鑺備负 0x20锛堢┖鏍硷級锛屽鑷?SAXParseException銆? 
 ## 琛ㄧ幇
 閿欒淇℃伅锛歚SAXParseException: 涓嶅厑璁告湁鍖归厤 "[xX][mM][lL]" 鐨勫鐞嗘寚浠ょ洰鏍囥€俙锛宭ine 1 column 7
 
 ## 鍘熷洜
 apply_patch 鐨?`+ content` 鏍煎紡鍦ㄥ啓鍏ユ枃浠舵椂姣忚鍓嶆坊鍔犱簡涓€涓┖鏍硷紝`<?xml` 鍙樻垚浜?` <?xml`銆? 
 ## 淇
 ```powershell
 $bytes = [System.Text.Encoding]::UTF8.GetBytes([System.IO.File]::ReadAllText($file).TrimStart())
 [System.IO.File]::WriteAllBytes($file, $bytes)
 ```
 
 ## 楠岃瘉
 妫€鏌ユ枃浠堕瀛楄妭锛? ```powershell
 [System.IO.File]::ReadAllBytes($file)[0..4] -join '' -eq '3C 3F 78 6D 6C'
 ```
 
 ## 鏉ユ簮
  - XML
  - 空格
  - 解析
  - 前导
  - 格式

