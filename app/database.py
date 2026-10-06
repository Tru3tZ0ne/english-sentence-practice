from __future__ import annotations

import sqlite3
import threading
from pathlib import Path
from typing import Any

MIGRATIONS = [
    """CREATE TABLE IF NOT EXISTS schema_migrations (version INTEGER PRIMARY KEY, applied_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP);
    CREATE TABLE IF NOT EXISTS progress (library_id TEXT NOT NULL, item_id TEXT NOT NULL, correct_count INTEGER NOT NULL DEFAULT 0, wrong_count INTEGER NOT NULL DEFAULT 0, last_answer TEXT, last_practiced_at TEXT, PRIMARY KEY(library_id,item_id));
    CREATE TABLE IF NOT EXISTS attempts (id INTEGER PRIMARY KEY AUTOINCREMENT, library_id TEXT NOT NULL, item_id TEXT NOT NULL, user_answer TEXT NOT NULL, is_correct INTEGER NOT NULL, created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP);
    CREATE INDEX IF NOT EXISTS idx_attempts_library_item ON attempts(library_id,item_id);
    CREATE TABLE IF NOT EXISTS favorites (library_id TEXT NOT NULL, item_id TEXT NOT NULL, created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY(library_id,item_id));
    CREATE TABLE IF NOT EXISTS settings (key TEXT PRIMARY KEY, value TEXT NOT NULL);
    CREATE TABLE IF NOT EXISTS library_state (library_id TEXT PRIMARY KEY, last_item_id TEXT, updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP);"""
]


class Database:
    def __init__(self, path: Path):
        path.parent.mkdir(parents=True, exist_ok=True)
        self.connection = sqlite3.connect(path, check_same_thread=False)
        self.connection.row_factory = sqlite3.Row
        self.lock = threading.RLock()
        self._migrate()

    def _migrate(self) -> None:
        with self.lock:
            self.connection.execute("CREATE TABLE IF NOT EXISTS schema_migrations (version INTEGER PRIMARY KEY, applied_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP)")
            applied = {row[0] for row in self.connection.execute("SELECT version FROM schema_migrations")}
            for version, script in enumerate(MIGRATIONS, 1):
                if version not in applied:
                    self.connection.executescript(script)
                    self.connection.execute("INSERT INTO schema_migrations(version) VALUES (?)", (version,))
            self.connection.commit()

    def execute(self, sql: str, params: tuple[Any, ...] = ()) -> sqlite3.Cursor:
        with self.lock:
            cursor = self.connection.execute(sql, params)
            self.connection.commit()
            return cursor

    def query(self, sql: str, params: tuple[Any, ...] = ()) -> list[sqlite3.Row]:
        with self.lock:
            return list(self.connection.execute(sql, params))

    def close(self) -> None:
        with self.lock:
            self.connection.commit()
            self.connection.close()
