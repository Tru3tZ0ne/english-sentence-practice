from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]/"content"/"libraries"
src=root/"ielts_advanced_3000.json"
data=json.loads(src.read_text(encoding="utf-8"))
topics=[("ielts_education","雅思·教育与学习"),("ielts_environment","雅思·环境与气候"),("ielts_technology","雅思·科技与互联网"),("ielts_society","雅思·政府与社会"),("ielts_cities","雅思·城市与交通"),("ielts_health_work","雅思·健康与就业")]
items=data["items"]; chunk=len(items)//len(topics)
for i,(lid,title) in enumerate(topics):
 part=items[i*chunk:(i+1)*chunk] if i<len(topics)-1 else items[i*chunk:]
 for item in part: item["tags"]=[title.split("·",1)[1],"IELTS","长句"]
 out={"schema_version":1,"id":lid,"title":f"{title} 500 句","description":f"{title}主题的雅思 7.0 长句练习。","language":"en-GB","tags":[title.split("·",1)[1],"IELTS","7.0"],"items":part}
 (root/f"{lid}.json").write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
src.unlink()
print("created",len(topics),"topic libraries")
