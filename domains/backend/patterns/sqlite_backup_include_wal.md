---
rule_id: sqlite_backup_include_wal
title: SQLite WAL 模式备份必须包含 WAL——只复制主库会丢未 checkpoint 写入
trigger:
  - SQLite 开启 journal_mode=WAL 的项目写备份逻辑
  - 备份脚本只 copy 主 .db 文件
  - 磁盘出现 data.db-wal / -shm 且备份体积远小于主库+WAL
  - README / 脚本注释声称"单文件备份 = 复制即安全"
  - 备份还原演练前发现备份不完整
condition: SQLite 处于 WAL 模式，备份只复制主库文件
action:
  do:
    - 备份前 PRAGMA wal_checkpoint(TRUNCATE)，检查返回结果（busy 则重试/降级），再复制主库
    - 或同步复制三件套（.db + -wal + -shm），且保证无写竞争/进程静止
    - 或使用 SQLite 在线备份 API（sqlite3_backup / node:sqlite backup API）
    - 备份后验证：数据行数/内容与源库一致，确认 WAL 内容已落盘
  dont:
    - 不在 WAL 模式下只复制主库当备份（未 checkpoint 写入会丢；热拷贝可能得到非一致快照）
    - 不把"备份体积≈主库"当成正确信号（WAL 可能比主库还大）
keywords:
  - sqlite
  - WAL
  - wal
  - 备份
  - backup
  - checkpoint
  - -wal
  - -shm
  - 数据丢失
  - data loss
  - journal_mode
alias:
  - 备份丢数据
  - WAL 备份
  - wal_checkpoint
  - sqlite backup
---

# SQLite WAL 模式备份必须包含 WAL

**来源**：ai-consultant 真实评审（2026-08-23）——REVIEW_REPORT.md §5 P1-3；
Evidence B（Knowledge Space consolidation，2026-08-23）。

## 问题

存储是 WAL 模式（`PRAGMA journal_mode=WAL`），但备份（`scripts/backup.js` 与
server.js 启动自动备份）只 `copyFileSync(data.db)`：不 checkpoint、不复制
`-wal`/`-shm`。实测磁盘：`data.db-wal` **4,173,592B**（≈1000 页，恰在自动 checkpoint
边界）vs `data.db` 200,704B；`backups/` 下备份均 ≤200KB——**WAL 里存着未落主库的
写入，当前备份策略会丢它们**；热拷贝还可能得到非一致快照。

## 为什么

SQLite WAL 模式下，提交的写入先进 `-wal`，主库文件在 checkpoint 前不包含这些写入。
备份"只复制主库"等于把 checkpoint 之前的所有新数据当成不存在。备份脚本注释里的
"SQLite 单文件，备份 = 复制（文档已定义该语义）"把**实现缺陷包装成了设计语义**——
文档承诺了不存在的安全性，这是最危险的一层（使用者会因此跳过验证）。

## 修复（几行）

```sql
PRAGMA wal_checkpoint(TRUNCATE);  -- 先让 WAL 落主库，检查返回结果
```

再复制主库；或复制三件套（.db + -wal + -shm，需无写竞争）；或直接用 SQLite 在线备份
API。备份后应验证：备份文件行数/内容与源库一致。

## 与其他知识的关系

- `storage_is_sqlite_blob`（workspaces/ai-consultant/experiences）：同项目 SQLite 话题，
  但其"WAL 单文件复制语义"表述被本次评审证伪——已在该经验文件追加修正挂接；
  "改库前先备份"仍成立，但备份动作本身必须先含 WAL。
- `protected_artifact_write`：那是"改受保护文件前确认 git 可恢复"，与数据库备份语义无关，
  不混淆。

## 检查清单

- [ ] 备份路径是否在 WAL 模式下仍能恢复 checkpoint 前提交的全部数据？
- [ ] 备份脚本/文档是否声称了未经证实的"复制即安全"语义？
- [ ] 最近一次备份是否做过还原验证（数据行数/内容一致）？
