from pathlib import Path
import json
subjects=[("教育系统","the education system"),("地方政府","local governments"),("许多雇主","many employers"),("年轻人","young people"),("城市规划者","urban planners"),("公共卫生机构","public health agencies"),("科技公司","technology companies"),("普通家庭","ordinary families"),("环境组织","environmental organisations"),("大学研究人员","university researchers")]
verbs=[("应该优先投资于","should prioritise investment in"),("必须认真评估","must carefully evaluate"),("可以通过合作改善","can improve"),("需要制定长期策略来应对","need long-term strategies to address"),("往往低估了","often underestimate"),("正在努力减少","are working to reduce"),("有责任公开说明","have a responsibility to explain"),("能够显著促进","are capable of significantly promoting"),("不应忽视","should not overlook"),("可以从经验中吸取教训并改革","can learn from experience and reform")]
objects=[("教育机会的不平等","inequality in educational opportunities"),("快速城市化带来的压力","the pressures created by rapid urbanisation"),("人工智能对就业市场的影响","the impact of artificial intelligence on the labour market"),("气候变化造成的长期风险","the long-term risks caused by climate change"),("心理健康服务的可及性","the accessibility of mental health services"),("公共交通基础设施的不足","the shortage of public transport infrastructure"),("社交媒体对公共讨论的影响","the influence of social media on public debate"),("生活成本持续上升的问题","the problem of rising living costs"),("数据隐私与个人自由之间的平衡","the balance between data privacy and personal freedom"),("可持续消费习惯的培养","the development of sustainable consumption habits")]
clauses=[("如果决策者只关注短期经济增长","if decision makers focus solely on short-term economic growth"),("在资源分配日益紧张的背景下","as resources become increasingly constrained"),("只要相关政策得到公平执行","provided that relevant policies are implemented fairly"),("尽管公众对这项改革仍有疑虑","although the public remains concerned about this reform"),("这不仅会改善社会公平，也会提高整体生产率","which would improve social equity as well as overall productivity"),("从而避免把成本转嫁给下一代","thereby avoiding the transfer of costs to future generations")]
frames=[("这一趋势表明","This trend suggests that"),("从长远来看，研究显示","In the long run, research indicates that"),("一个合理的观点是","A reasonable argument is that"),("值得注意的是","It is worth noting that"),("许多专家认为","Many experts believe that")]
rows=[]
for fzh,fen in frames:
 for szh,sen in subjects:
  for vzh,ven in verbs:
   for ozh,oen in objects:
    for czh,cen in clauses:
     if len(rows)>=3000: break
     rows.append({"id":f"ielts_{len(rows)+1:04d}","zh":f"{fzh}，{szh}{vzh}{ozh}，{czh}。","en":f"{fen} {sen} {ven} {oen}, {cen}.","answers":[f"{fen} {sen} {ven} {oen}, {cen}."],"notes":"IELTS 7.0 进阶长句；建议先理解从句结构，再进行听写。","tags":["IELTS","长句"],"difficulty":4})
    if len(rows)>=3000: break
   if len(rows)>=3000: break
  if len(rows)>=3000: break
 if len(rows)>=3000: break
data={"schema_version":1,"id":"ielts_advanced_3000","title":"雅思 7.0 进阶长句 3000 句","description":"面向 IELTS 7.0 水平的学术与社会议题长句听写练习。","language":"en-GB","tags":["雅思","7.0","长句","学术"],"items":rows}
target=Path(__file__).resolve().parents[1]/"content"/"libraries"/"ielts_advanced_3000.json"
target.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"wrote {len(rows)} items")
