# 工具使用说明

日常维护使用：

```powershell
.venv\Scripts\python.exe tools\validate_libraries.py
.venv\Scripts\python.exe -m pytest -q
```

`validate_libraries.py` 检查 JSON 和 schema，不检查语法、翻译或重复句。编辑前请阅读 [题库质量标准](../CONTENT_QUALITY.md)。

以下脚本是历史批量生成工具，保留用于追溯旧题库的来源，已退出正式内容生产流程：

- `generate_1000.py`
- `generate_ielts_3000.py`
- `generate_comprehensive_5000.py`
- `generate_topic_libraries.py`
- `generate_more_topics.py`
- `split_ielts_topics.py`

这些脚本直接写入 `content/libraries/`，部分在导入时就会执行；运行会覆盖已经审校的内容。`split_ielts_topics.py` 还会删除其输入文件。不要为了补题量重新运行或导入它们。

旧生成方式存在跨主题复用、笛卡尔组合、硬截断和语法搭配问题。未来如需恢复辅助工具，应先改为只输出独立草稿目录，进行逐题审校和质量检查后再发布，不能把随机组合直接作为正式题库。

2026-10-04 原始题库备份与审查结果见 [审查报告](../reviews/2026-10-04/REVIEW.md)。
