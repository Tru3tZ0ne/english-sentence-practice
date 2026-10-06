from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from app.content.schema import validate_library


def build(output: Path) -> tuple[int, int]:
    output = output.resolve()
    if output == ROOT or ROOT not in output.parents:
        raise ValueError("输出目录必须位于项目目录内，且不能是项目根目录")
    if output.exists():
        shutil.rmtree(output)
    shutil.copytree(ROOT / "web", output)
    libraries_output = output / "libraries"
    libraries_output.mkdir()
    filenames: list[str] = []
    item_count = 0
    for source in sorted((ROOT / "content" / "libraries").glob("*.json")):
        data = json.loads(source.read_text(encoding="utf-8-sig"))
        library = validate_library(data, source.name)
        filenames.append(source.name)
        item_count += len(library.items)
        shutil.copy2(source, libraries_output / source.name)
    (output / "library-manifest.json").write_text(
        json.dumps(filenames, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (output / ".nojekyll").touch()
    return len(filenames), item_count


def main() -> int:
    parser = argparse.ArgumentParser(description="构建 GitHub Pages 静态站点")
    parser.add_argument("--output", type=Path, default=ROOT / "_site")
    args = parser.parse_args()
    libraries, items = build(args.output)
    print(f"Built {libraries} libraries / {items} items into {args.output.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
