---
rule_id: agently_mail_token_mismatch
title: agently-cli 发送邮件 — confirmation_token 要求 body 逐字符一致
trigger:
  - agently-cli
  - 发邮件
  - confirmation_token
  - 发送失败
  - token 失效
  - 邮件 API
condition: 使用 agently-cli message +send 发送邮件需要两步确认时
action:
  do:
    - 第一次发送获取 confirmation_token
    - 第二次发送 —body/--subject/--to 必须与第一次完全一致
    - 不能缩短、不能换行调整、不能改任何字符
    - 建议：把 body 存为变量，两次复用同一个变量
  dont:
    - 不要在第二步修改任何请求内容
    - 不要缩短 body（即使意思一样也不行）
    - 不要重新格式化文本
keywords:
  - agently-cli
  - 邮件
  - token
  - confirmation
  - 发送
  - 确认
---

# agently-cli 发邮件 token 校验失败

## 问题

使用 `agently-cli message +send` 发邮件时，第一步返回 `confirmation_token`，第二步带上 `--confirmation-token` 重发，但报错：

```
Request content modified since confirmation
```

token 失效，必须重新发起。

## 原因

confirmation_token 绑定的是第一次请求的完整内容（`--to`、`--subject`、`--body` 的逐字符 hash）。第二步如果对正文做了任何修改——包括缩短、换行调整、加标点——hash 不匹配，token 立即失效。

## 解决

两步的 body 必须逐字符一致。最简单的方式：把正文存为变量，两次传同一个变量。

```bash
BODY="完整邮件正文，不做任何改动"
agently-cli message +send --to xxx --subject xxx --body "$BODY"
# 得到 token 后
agently-cli message +send --to xxx --subject xxx --body "$BODY" --confirmation-token ctk_xxx
```
