from __future__ import annotations

import logging
import sys

from app import APP_VERSION
from app.application import Application
from app.config import LOG_DIR


def configure_logging():
    LOG_DIR.mkdir(parents=True,exist_ok=True)
    logging.basicConfig(filename=LOG_DIR/"app.log",level=logging.INFO,encoding="utf-8",
                        format="%(asctime)s %(levelname)s %(message)s")


def main() -> int:
    configure_logging(); logging.info("启动英语学习应用 v%s",APP_VERSION)
    app=None
    try:
        app=Application(); app.run(); return 0
    except Exception:
        logging.exception("应用启动或运行失败")
        print("应用启动失败，详情请查看 logs\\app.log。",file=sys.stderr); return 1
    finally:
        if app: app.shutdown(destroy_window=False)


if __name__ == "__main__": raise SystemExit(main())
