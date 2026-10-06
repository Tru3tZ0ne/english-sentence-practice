# 英语句子练习

在线版通过 GitHub Pages 发布。网页端包含与桌面版相同的 66 个题库、4,320 道题；学习进度、收藏和设置只保存在当前浏览器的本地存储中。网页入口提供客户端登录门槛，但 GitHub Pages 不支持服务器端身份验证，因此它不适合保护敏感数据。

Python + pywebview + 原生 HTML/CSS/JS + SQLite 的本地英语学习工具。题库正文只在 `content/libraries/*.json`，数据库只保存用户数据。

首次和日常均双击 `start.bat`；脚本会定位自身目录、创建 `.venv`、安装依赖一次后启动。数据在 `data/app.db`，日志在 `logs/app.log`。运行测试：`.venv\Scripts\python.exe -m pytest`；校验题库：`.venv\Scripts\python.exe tools\validate_libraries.py`；打包双击 `build_release.bat`。`reset_env.bat` 只删除虚拟环境。

新增题库只需放入 JSON 并重启，格式见 CONTENT_FORMAT.md。无 Python 时请安装 3.11+ 并勾选 PATH；无桌面环境无法显示窗口，但可运行核心测试。

题库现已扩充到 66 个库、4,320 题，包含小学、初中、高中、四级、六级分级训练，以及介词、从句、非谓语、冠词、指代、比较、否定和语序等专项。题目包含逐题讲解、结构和场景标签。

静态站点由 `tools/build_static_site.py` 从 `web/` 与 `content/libraries/` 构建，并发布到 GitHub Pages 的 `gh-pages` 分支。题库仍只在 `content/libraries/` 维护。

内容维护请阅读 [题库质量标准](CONTENT_QUALITY.md)。完整问题清单、改进计划、验证结果和原库恢复说明见 [项目审查报告](reviews/2026-10-04/REVIEW.md)。`tools/generate_*.py` 是会覆盖正式题库的旧生成脚本，不再用于日常扩题，详见 [工具说明](tools/README.md)。
