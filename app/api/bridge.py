from __future__ import annotations

import logging
import threading
from typing import TYPE_CHECKING

from app import APP_VERSION
from app.services.answer_checker import AnswerChecker

if TYPE_CHECKING:
    from app.application import Application


class ApiBridge:
    def __init__(self, app: "Application"):
        # Keep the application reference private: pywebview recursively exposes
        # public attributes and would otherwise walk into .NET window objects.
        self._app=app

    def bootstrap(self):
        return {"ok":True,"version":APP_VERSION,"libraries":self._app.library_service.summaries(),
                "library_errors":self._app.loader.errors,"settings":self._app.settings.get_all()}

    def get_sequence(self, library_id: str = "", kind: str = "all"):
        items=self._app.library_service.sequence(library_id,kind)
        return {"ok":True,"items":items,"last_item_id":self._app.progress.last_item(library_id) if library_id else None}

    def submit_answer(self, library_id: str, item_id: str, user_answer: str):
        if not self._app.library_service.has_item(library_id,item_id): return {"ok":False,"error":"题目不存在或题库已更新"}
        item=next(x for x in self._app.library_service.libraries[library_id].items if x.id==item_id)
        ignore=bool(self._app.settings.get_all()["ignore_terminal_punctuation"])
        result=AnswerChecker().check(user_answer,item.answers,ignore)
        self._app.progress.record(library_id,item_id,user_answer,result.correct)
        return {"ok":True,"correct":result.correct,"standard_answer":item.en,"matched_answer":result.matched_answer,"notes":item.notes}

    def save_position(self, library_id: str, item_id: str):
        if self._app.library_service.has_item(library_id,item_id): self._app.progress.save_position(library_id,item_id)
        return {"ok":True}

    def toggle_favorite(self, library_id: str, item_id: str):
        if not self._app.library_service.has_item(library_id,item_id): return {"ok":False,"error":"题目不存在"}
        return {"ok":True,"favorite":self._app.progress.toggle_favorite(library_id,item_id)}

    def save_settings(self, values: dict): return {"ok":True,"settings":self._app.settings.save(values)}

    def shutdown(self):
        logging.info("收到页面关闭请求")
        threading.Thread(target=self._app.shutdown, daemon=True).start()
        return {"ok":True}
