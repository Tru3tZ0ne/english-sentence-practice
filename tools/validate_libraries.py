from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from app.content.library_loader import LibraryLoader
from app.config import LIBRARIES_DIR
loader=LibraryLoader(LIBRARIES_DIR); libs=loader.load_all()
if hasattr(sys.stdout, "reconfigure"): sys.stdout.reconfigure(encoding="utf-8")
for lib in libs.values(): print(f"[通过] {lib.source_file}: {lib.title} ({len(lib.items)} 题)")
for error in loader.errors: print(f"[失败] {error['file']}: {error['message']}")
sys.exit(1 if loader.errors else 0)
