from __future__ import annotations

from app.database import Database


class ProgressService:
    def __init__(self, db: Database): self.db = db

    def record(self, library_id: str, item_id: str, answer: str, correct: bool) -> None:
        self.db.execute("INSERT INTO attempts(library_id,item_id,user_answer,is_correct) VALUES(?,?,?,?)", (library_id,item_id,answer,int(correct)))
        column = "correct_count" if correct else "wrong_count"
        self.db.execute(f"INSERT INTO progress(library_id,item_id,{column},last_answer,last_practiced_at) VALUES(?,?,1,?,CURRENT_TIMESTAMP) ON CONFLICT(library_id,item_id) DO UPDATE SET {column}={column}+1,last_answer=excluded.last_answer,last_practiced_at=CURRENT_TIMESTAMP", (library_id,item_id,answer))
        self.save_position(library_id, item_id)

    def save_position(self, library_id: str, item_id: str) -> None:
        self.db.execute("INSERT INTO library_state(library_id,last_item_id) VALUES(?,?) ON CONFLICT(library_id) DO UPDATE SET last_item_id=excluded.last_item_id,updated_at=CURRENT_TIMESTAMP", (library_id,item_id))

    def last_item(self, library_id: str) -> str | None:
        rows = self.db.query("SELECT last_item_id FROM library_state WHERE library_id=?", (library_id,))
        return rows[0]["last_item_id"] if rows else None

    def toggle_favorite(self, library_id: str, item_id: str) -> bool:
        rows = self.db.query("SELECT 1 FROM favorites WHERE library_id=? AND item_id=?", (library_id,item_id))
        if rows:
            self.db.execute("DELETE FROM favorites WHERE library_id=? AND item_id=?", (library_id,item_id)); return False
        self.db.execute("INSERT INTO favorites(library_id,item_id) VALUES(?,?)", (library_id,item_id)); return True

    def is_favorite(self, library_id: str, item_id: str) -> bool:
        return bool(self.db.query("SELECT 1 FROM favorites WHERE library_id=? AND item_id=?", (library_id,item_id)))

    def item_ids(self, kind: str) -> list[tuple[str,str]]:
        if kind == "favorites": return [(r["library_id"],r["item_id"]) for r in self.db.query("SELECT library_id,item_id FROM favorites ORDER BY created_at DESC")]
        if kind == "wrong": return [(r["library_id"],r["item_id"]) for r in self.db.query("SELECT library_id,item_id FROM progress WHERE wrong_count>0 ORDER BY last_practiced_at DESC")]
        return []

    def stats(self, library_id: str) -> dict:
        rows = self.db.query("SELECT COUNT(*) practiced,COALESCE(SUM(correct_count),0) correct,COALESCE(SUM(wrong_count),0) wrong FROM progress WHERE library_id=?", (library_id,))
        fav = self.db.query("SELECT COUNT(*) count FROM favorites WHERE library_id=?", (library_id,))[0]["count"]
        row=rows[0]; total=row["correct"]+row["wrong"]
        return {"practiced":row["practiced"],"correct":row["correct"],"wrong":row["wrong"],"accuracy":round(row["correct"]*100/total) if total else 0,"favorites":fav,"last_item_id":self.last_item(library_id)}
