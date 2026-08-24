---
rule_id: bulk_fix_use_codegen
title: 同类 bug 跨多个文件时用代码批量生成修复
trigger:
  - 同类 bug 跨多个代码文件
  - 批量修改文件头部 / 格式 / 注释
  - 批量生成模板代码
condition: 手动逐个修改耗时（如 9 文件 30+ 分钟）
action:
  do:
    - 写脚本批量生成修复代码（遍历实体 → 生成正确内容 → 写文件）
    - 用 codegen 替代手工逐个改，把 30+ 分钟压到 2 分钟量级
  dont:
    - 手动逐个修改同类 bug（耗时且易漏改 / 改错）
keywords:
  - batch
  - codegen
  - 批量
  - 修复
  - mapper
  - 脚本
  - 代码生成
  - 同类bug
---

# Pattern: 同类 bug 跨多个文件时用代码批量生成修复

> pattern_id: PS-20260622-003
> type: success / confidence: HIGH / verified: true
> source_task: tourism 项目 9 个 Mapper XML 修复 (2026-06-22)

## 问题

9 个 Mapper.xml 的 SQL 全部复制粘贴了错误列名。手动逐个修改需 30+ 分钟。

## 解决方案

写脚本批量生成修复代码：

```python
for name, info in entities.items():
    sql = generate_correct_sql(name, info)
    write_file(f'{name}Mapper.xml', sql)
```

2 分钟完成 9 个文件的修复。

## 适用场景

- 同类 bug 跨多个代码文件
- 批量修改文件头部 / 格式 / 注释
- 批量生成模板代码
