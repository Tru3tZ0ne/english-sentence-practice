# 题库格式

UTF-8 JSON 根对象需要 `schema_version: 1`、唯一稳定 `id`、`title`、非空 `items`。id 只能用小写字母、数字、`_`、`-`。item 必须有唯一稳定 `id`、`zh`、标准英文 `en`；可选 `answers`（允许答案数组，标准 en 自动加入）、`notes`、字符串 `tags`、1~5 `difficulty`。题库可有 `description`、`language`（默认 en-US）、`tags`。

新增文件后重启自动扫描；坏文件跳过并记录错误。使用 `tools/validate_libraries.py` 校验。不要以数组下标作为进度 ID；修改已有题目尽量保留 item id，新增字段须向后兼容。

内容质量要求见 [CONTENT_QUALITY.md](CONTENT_QUALITY.md)。`tags` 可继续使用现有字符串数组存放主题、句式、交际任务和子场景，不新增 schema 字段；`notes` 填写逐题用法，`difficulty` 按实际学习负担标注。缩写和完整形式等可接受变体放入同一题的 `answers`。

题库标题应展示实际题量。旧文件名和 ID 中的 `1000`、`5000` 只作为稳定标识保留，不表示当前题数。2026-10-04 精选版仍兼容 schema v1，原始题库归档在 `reviews/2026-10-04/original-libraries.zip`，不会被题库加载器扫描。
