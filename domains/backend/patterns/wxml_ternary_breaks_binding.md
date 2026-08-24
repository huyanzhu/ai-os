---
rule_id: wxml_ternary_breaks_binding
title: WXML涓夊厓琛ㄨ揪寮忛樆璧涙暟鎹粦瀹?
trigger:
  - WXML class="{{cond ? 'a' : 'b'}}"
  - setData涓嶇敓鏁堜絾鏃犳姤閿?
  - 椤甸潰閮ㄥ垎娓叉煋浣嗕笉瀹屾暣
condition: 寰俊灏忕▼搴廤XML涓寘鍚? :涓夊厓琛ㄨ揪寮?
action:
  do:
    - 灏哤XML涓墍鏈変笁鍏冭〃杈惧紡绉昏嚦JS棰勫鐞?
    - 鐢╯etData浼犻€掕绠楀ソ鐨勭被鍚嶅瓧娈?
  dont:
    - 鍦╓XML灞炴€т腑浣跨敤? :涓夊厓
keywords:
  - wxml
  - ternary
  - binding
  - wechat
  - miniapp

knowledge_position: Cluster
knowledge_cluster: FC-004 WeChat Miniapp
epistemology_tag: OBSERVATION
confidence: HIGH
---

# WXML涓笁鍏冭〃杈惧紡瀵艰嚧鏁版嵁缁戝畾澶辨晥

## 闂
鍦ㄥ井淇″皬绋嬪簭鐨刉XML涓紝class="{{cond ? 'class-a' : 'class-b'}}" 杩欐牱鐨勪笁鍏冭〃杈惧紡浼氬鑷碬XML缂栬瘧鍣ㄩ潤榛樺け璐ワ紝椤甸潰铏界劧鑳介儴鍒嗘覆鏌擄紝浣嗘墍鏈夋暟鎹粦瀹?setData)瀹屽叏涓嶇敓鏁堬紝涓旀帶鍒跺彴鏃犳姤閿欍€?

## 鏍瑰洜
WXML鐨凪ustache璇硶{{}}鍐呬笉鍏佽浣跨敤寮曞彿瀛楃瀛楅潰閲?'鎴?)锛屼笁鍏冭〃杈惧紡涓殑寮曞彿瀵艰嚧缂栬瘧鍣ㄨВ鏋愬紓甯革紝闈欓粯澶辫触銆?

## 淇
鎶婃墍鏈夋潯浠堕€昏緫绉诲埌JS涓紝閫氳繃setData浼犻€掕绠楀ソ鐨勭被鍚嶏細
`javascript
this.setData({ catBarClass: count > 0 ? "bar-active" : "bar" })
`
WXML涓洿鎺ヤ娇鐢細class="{{catBarClass}}"

## 鍒ゅ畾鎸囨爣
- partial render + setData涓嶇敓鏁?= 90% WXML缂栬瘧鏈夐棶棰?
- [[wxml_partial_render_trap]]锛堝叧鑱旀ā寮忥級
  - WXML
  - 三元
  - 模板
  - 绑定
  - 微信
alias:
  - WXML三元表达式
  - 模板绑定错误



