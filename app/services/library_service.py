from __future__ import annotations

from app.content.library_loader import LibraryLoader
from app.services.progress_service import ProgressService


class LibraryService:
    def __init__(self, loader: LibraryLoader, progress: ProgressService):
        self.loader, self.progress = loader, progress
        self.libraries = loader.load_all()

    def summaries(self) -> list[dict]:
        return [{"id":lib.id,"title":lib.title,"description":lib.description,"language":lib.language,
                 "tags":list(lib.tags),"item_count":len(lib.items),"stats":self.progress.stats(lib.id)}
                for lib in self.libraries.values()]

    def sequence(self, library_id: str, kind: str = "all") -> list[dict]:
        if kind == "all":
            lib=self.libraries.get(library_id); pairs=[(library_id,x.id) for x in lib.items] if lib else []
        else:
            pairs=[p for p in self.progress.item_ids(kind) if not library_id or p[0] == library_id]
        output=[]
        for lib_id,item_id in pairs:
            lib=self.libraries.get(lib_id)
            item=next((x for x in lib.items if x.id==item_id),None) if lib else None
            if item: output.append({**item.to_dict(),"library_id":lib_id,"library_title":lib.title,"language":lib.language,"favorite":self.progress.is_favorite(lib_id,item_id)})
        return output

    def has_item(self, library_id: str, item_id: str) -> bool:
        lib=self.libraries.get(library_id)
        return bool(lib and any(x.id==item_id for x in lib.items))
