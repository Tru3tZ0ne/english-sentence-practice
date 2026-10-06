from __future__ import annotations

import logging
import threading

from app.api.bridge import ApiBridge
from app.config import DB_PATH, LIBRARIES_DIR, WEB_DIR
from app.content.library_loader import LibraryLoader
from app.database import Database
from app.services.library_service import LibraryService
from app.services.progress_service import ProgressService
from app.services.settings_service import SettingsService


class Application:
    def __init__(self):
        self._shutdown_lock=threading.Lock(); self._closed=False; self.window=None
        self.db=Database(DB_PATH)
        self.progress=ProgressService(self.db); self.settings=SettingsService(self.db)
        self.loader=LibraryLoader(LIBRARIES_DIR); self.library_service=LibraryService(self.loader,self.progress)
        self.api=ApiBridge(self)

    def run(self):
        import webview
        self.window=webview.create_window("英语句子练习", str(WEB_DIR / "index.html"), js_api=self.api,
                                          width=1280,height=800,min_size=(1000,650),text_select=True)
        self.window.events.closed += self._on_window_closed
        webview.start(debug=False)
        self.shutdown(destroy_window=False)

    def _on_window_closed(self): self.shutdown(destroy_window=False)

    def shutdown(self, destroy_window=True):
        with self._shutdown_lock:
            if self._closed: return
            self._closed=True
            try: self.db.close()
            except Exception: logging.exception("关闭数据库失败")
            if destroy_window and self.window:
                try: self.window.destroy()
                except Exception: logging.exception("销毁窗口失败")
            logging.info("应用已关闭")
