from __future__ import annotations

import sys
from pathlib import Path


def project_root() -> Path:
    """Return the source root or the PyInstaller bundle directory."""
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent
    return Path(__file__).resolve().parent.parent


ROOT_DIR = project_root()
WEB_DIR = ROOT_DIR / "web"
LIBRARIES_DIR = ROOT_DIR / "content" / "libraries"
DATA_DIR = ROOT_DIR / "data"
LOG_DIR = ROOT_DIR / "logs"
DB_PATH = DATA_DIR / "app.db"
