from pathlib import Path
import json
topics={
"education_learning":("教育与学习","education","教育、学习方法与终身成长"),
"environment_climate":("环境与气候","environment","环境保护、气候变化与可持续发展"),
"technology_internet":("科技与互联网","technology","人工智能、互联网与数字生活"),
"work_business":("职场与商务","business","职场沟通、管理与商业决策"),
"health_lifestyle":("健康与生活方式","health","健康、运动、饮食与生活习惯"),
"culture_society":("文化与社会","culture","文化差异、媒体与社会议题"),}
subjects=[("许多年轻人","many young people"),("研究人员","researchers"),("政府部门","government departments"),("普通家庭","ordinary families"),("企业管理者","business managers")]
actions=[("越来越重视","are increasingly concerned about"),("需要重新思考","need to rethink"),("可以通过合作改善","can improve through cooperation"),("必须平衡短期利益与长期影响","must balance short-term interests with long-term consequences"),("往往受到信息质量的影响","are often influenced by the quality of information")]
issues=[("如何培养独立思考能力","how to develop independent thinking"),("资源分配不均造成的后果","the consequences of unequal resource distribution"),("快速变化带来的不确定性","the uncertainty created by rapid change"),("个人选择与公共责任之间的关系","the relationship between personal choices and public responsibility"),("政策能否真正惠及弱势群体","whether policies can genuinely benefit vulnerable groups")]
connectors=[("如果相关措施得到持续执行","if relevant measures are implemented consistently"),("尽管不同群体的需求并不相同","although the needs of different groups are not identical"),("在证据仍然有限的情况下","while the available evidence remains limited"),("从长远角度来看","from a long-term perspective")]
root=Path(__file__).resolve().parents[1]/"content"/"libraries"
for lid,(title,tag,desc) in topics.items():
 rows=[]
 for szh,sen in subjects:
  for azh,aen in actions:
   for izh,ien in issues:
    for czh,cen in connectors:
     if len(rows)>=120: break
     en=f"{sen.capitalize()} {aen} {ien}, {cen}."
     rows.append({"id":f"{lid}_{len(rows)+1:03d}","zh":f"{szh}{azh}{izh}，{czh}。","en":en,"answers":[en],"notes":f"{title}主题句，适合中高级听写和口语讨论。","tags":[title,tag],"difficulty":3+(len(rows)%3)})
    if len(rows)>=120: break
   if len(rows)>=120: break
  if len(rows)>=120: break
 data={"schema_version":1,"id":lid,"title":f"{title} 120 句","description":desc,"language":"en-US","tags":[title,tag,"主题分类"],"items":rows}
 (root/f"{lid}.json").write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 print(lid,len(rows))
