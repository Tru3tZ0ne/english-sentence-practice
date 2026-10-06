from pathlib import Path
import json
topics={
"relationships_emotions":("人际与情绪","表达感受、建立边界与处理人际分歧"),
"family_social":("家庭与社交","家庭安排、朋友聚会与日常社交"),
"medical_english":("医疗与问诊","描述症状、预约就诊与理解医嘱"),
"housing_rental":("租房与居住","看房、合同、维修与邻里沟通"),
"banking_finance":("银行与金融","账户、转账、支付与个人预算"),
"public_services_law":("公共服务与法律","证件、行政手续、规则与权益"),
"academic_discussion":("学术讨论","观点论证、研究方法与课堂讨论"),
"complaints_negotiation":("投诉与协商","说明问题、提出方案与达成共识")}
openers=[("坦率地说","To be frank"),("就目前的情况而言","As far as the current situation is concerned"),("根据我得到的信息","According to the information I have received"),("为了避免进一步的误解","To avoid any further misunderstanding"),("从实际角度来看","From a practical perspective")]
statements=[("我需要更清楚地了解可供选择的方案","I need a clearer understanding of the available options"),("我们应该先确认双方最关心的问题","we should first identify the concerns that matter most to both sides"),("这个决定可能产生比预期更长远的影响","this decision may have more far-reaching consequences than expected"),("我希望工作人员能够提供书面说明","I would like the staff to provide a written explanation"),("我们仍然需要一些可靠证据才能作出判断","we still need reliable evidence before reaching a conclusion"),("如果能够提前沟通，很多问题本来可以避免","many of these problems could have been avoided through earlier communication")]
endings=[("因此，我希望今天能找到一个合理的解决办法。","Therefore, I hope we can find a reasonable solution today."),("在继续之前，你能否解释一下具体流程？","Could you explain the exact procedure before we continue?"),("这不仅关系到费用，也关系到双方的信任。","This concerns not only the cost but also the trust between both parties."),("如果条件允许，我愿意考虑一个折中的选择。","I would be willing to consider a compromise if circumstances permit."),("请告诉我还需要提供哪些证明材料。","Please let me know what additional supporting documents are required.")]
root=Path(__file__).resolve().parents[1]/"content"/"libraries"
for lid,(title,desc) in topics.items():
 rows=[]
 for ozh,oen in openers:
  for szh,sen in statements:
   for ezh,een in endings:
    if len(rows)>=120: break
    en=f"{oen}, {sen}. {een}"
    rows.append({"id":f"{lid}_{len(rows)+1:03d}","zh":f"{ozh}，{szh}。{ezh}","en":en,"answers":[en],"notes":f"{title}场景的中高级表达。","tags":[title,"场景英语"],"difficulty":3+(len(rows)%3)})
   if len(rows)>=120: break
  if len(rows)>=120: break
 data={"schema_version":1,"id":lid,"title":f"{title} 120 句","description":desc,"language":"en-US","tags":[title,"主题分类","中高级"],"items":rows}
 (root/f"{lid}.json").write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 print(lid,len(rows))
