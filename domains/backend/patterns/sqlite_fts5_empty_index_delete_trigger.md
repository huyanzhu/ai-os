---
rule_id: sqlite_fts5_empty_index_delete_trigger
title: SQLite FTS5 外部内容表在索引为空时执行 DELETE 触发器报 database disk image is malformed
trigger:
  - 存量库（无 FTS 表）首次打开：建 FTS 表/触发器后、回填索引前删除或修改存量行
  - 迁移/清理逻辑中 DELETE 触发 FTS 删除触发器，随后报 "database disk image is malformed"
condition: FTS5 外部内容表（content='links'）在索引为空（未 rebuild）时，删除内容表行会触发
  FTS 删除触发器，SQLite 报 malformed；先 rebuild 再删/改则正常
action:
  do:
    - 打开存量库时先 INSERT INTO fts(fts) VALUES('rebuild') 回填索引，再做任何行删除/迁移
    - 以「FTS 表是否存在」判断是否需要 rebuild（外部内容表 count(*) 读的是内容表行数，不能用于判断索引是否为空）
    - 若在调试中见到 malformed 且 quick_check 正常，优先怀疑空 FTS 索引上的删除/更新触发器
  dont:
    - 在回填前依赖 DELETE/UPDATE 触发器维护 FTS 索引（空索引上会报 malformed）
    - 用 COUNT(*) 判断外部内容 FTS 索引是否为空
keywords:
  - sqlite
  - fts5
  - trigram
  - external content
  - trigger
  - malformed
  - rebuild
  - 迁移
alias:
  - SQLite FTS 损坏
  - database disk image is malformed
  - FTS5 触发器报错
---

# SQLite FTS5 空索引 DELETE 触发器坑

> 来源: LinkVault Phase 5 真实开发（2026-08-22，`D:\AI-os\workspaces\linkvault`）实测诊断

## 表现

存量库（Phase 1 老 schema，无 FTS 表）首次打开时：建 `links_fts` 外部内容表与
`AFTER DELETE` 触发器 → 迁移逻辑 DELETE 一条内容表行 → `sqlite3.DatabaseError:
database disk image is malformed`。而 `PRAGMA quick_check` 返回 ok，库文件本身没有损坏。

## 根因

FTS5 外部内容表（`content='links', content_rowid='id'`）在索引**为空**（尚未
`rebuild`）时，对内容表执行 DELETE 会触发 FTS 删除触发器，SQLite 尝试从空索引
删除段 → 报 "database disk image is malformed"。先把存量数据 `rebuild` 进索引，
再删/改内容表行则一切正常（触发器能正确匹配待删除条目）。

## 修复

顺序必须是：**建表/触发器 → rebuild 回填 → 再删/改存量行**：

```python
fts_existed = self._fts_table_exists()          # sqlite_master 判断表是否存在
self._conn.executescript(SCHEMA)                # 建 links 表/触发器/FTS 表
if not fts_existed:
    self._conn.execute("INSERT INTO links_fts(links_fts) VALUES('rebuild')")
    self._conn.commit()
self._normalize_legacy_rows()                   # 此后的 DELETE/UPDATE 才安全
```

## 判断要点

- 外部内容表 `SELECT COUNT(*) FROM links_fts` 返回的是**内容表行数**（SQLite 对
  外部内容表 count 的优化），不能用来判断索引是否为空——用 `sqlite_master` 里
  FTS 表是否存在即可（新建空库 rebuild 是无害空操作）。
- 遇到 "malformed" 且 quick_check 正常时，不要直奔「库损坏」修复路径；先检查
  是否在空 FTS 索引上触发了删除/更新触发器。

## 适用范围

- SQLite FTS5 + external content 表 + 触发器自动同步索引的项目
- 任何「旧库打开时迁移存量行」的启动逻辑
