import json

from app.database import Database

DEFAULTS = {"theme": "system", "font_size": "medium", "auto_speak": False, "speech_rate": 1.0,
            "ignore_terminal_punctuation": True, "auto_next": False}


class SettingsService:
    def __init__(self, db: Database): self.db = db

    def get_all(self) -> dict:
        result = dict(DEFAULTS)
        for row in self.db.query("SELECT key,value FROM settings"):
            try: result[row["key"]] = json.loads(row["value"])
            except json.JSONDecodeError: pass
        return result

    def save(self, values: dict) -> dict:
        allowed = {key: values[key] for key in DEFAULTS if key in values}
        if allowed.get("theme", "system") not in {"light", "dark", "system"}: allowed["theme"] = "system"
        if allowed.get("font_size", "medium") not in {"small", "medium", "large"}: allowed["font_size"] = "medium"
        if "speech_rate" in allowed: allowed["speech_rate"] = max(.5, min(1.5, float(allowed["speech_rate"])))
        for key, value in allowed.items():
            self.db.execute("INSERT INTO settings(key,value) VALUES(?,?) ON CONFLICT(key) DO UPDATE SET value=excluded.value", (key, json.dumps(value)))
        return self.get_all()
