from pathlib import Path
import json
scenes=[("日常对话","daily"),("旅游出行","travel"),("机场与航班","flight"),("酒店住宿","hotel"),("餐饮购物","service"),("工作沟通","work"),("突发情况","emergency")]
subjects=[("我","I"),("我们","we"),("你","you"),("他们","they"),("这位旅客","this traveller"),("前台工作人员","the front-desk clerk"),("航空公司代表","the airline representative"),("客户服务团队","the customer-service team")]
actions=[("想确认预订是否仍然有效","would like to confirm whether the reservation is still valid"),("需要提前了解具体的办理流程","need to understand the exact procedure in advance"),("希望在不增加额外费用的情况下调整安排","hope to change the arrangement without incurring an additional fee"),("必须仔细核对所有重要信息","must carefully verify all the important information"),("正在寻找一种更可靠、更节省时间的解决方案","are looking for a more reliable and time-efficient solution"),("担心突发变化会影响接下来的计划","are concerned that an unexpected change may affect the following plans"),("愿意按照规定提供必要的证明文件","are willing to provide the necessary supporting documents as required"),("应该在做出最终决定之前比较不同选项","should compare different options before making a final decision"),("不确定是否可以在截止时间之后提出申请","are not sure whether an application can be submitted after the deadline"),("已经为可能出现的延误准备了备用方案","have prepared a backup plan for a possible delay")]
contexts=[("在出发之前","before departure"),("当行程受到天气影响时","when the itinerary is affected by the weather"),("如果工作人员能够及时提供明确解释","if the staff can provide a clear explanation in time"),("尽管价格看起来比预期更高","although the price appears higher than expected"),("为了避免在高峰时段浪费太多时间","in order to avoid wasting too much time during peak hours"),("只要所有参与者都同意新的安排","as long as everyone involved agrees to the new arrangement"),("由于相关规定最近发生了变化","because the relevant regulations have recently changed"),("这会让整个体验更加顺利和令人安心","which would make the entire experience smoother and more reassuring")]
questions=[("你能否说明下一步应该怎么做？","Could you explain what should be done next?"),("如果出现问题，谁是最合适的联系人？","If a problem occurs, who would be the most appropriate contact?"),("这项服务是否包含在已经支付的费用中？","Is this service included in the amount already paid?"),("有没有更灵活的选择可以满足我们的需要？","Is there a more flexible option that could meet our needs?"),("我们最迟应该在什么时候到达？","When should we arrive at the latest?"),("你能保证这些信息在系统中已经更新了吗？","Can you confirm that this information has been updated in the system?")]
rows=[]
for cat,tag in scenes:
 for szh,sen in subjects:
  for azh,aen in actions:
   for czh,cen in contexts:
    for qzh,qen in questions:
     if len(rows)>=5000: break
     zh=f"{szh}{azh}，{czh}；{qzh}"
     en=f"{sen.capitalize()} {aen} {cen}. {qen}"
     rows.append({"id":f"comprehensive_{len(rows)+1:04d}","zh":zh,"en":en,"answers":[en],"notes":f"{cat}场景；难度高于英语四级，适合句子听写与口语复述。","tags":[cat,tag],"difficulty":3+(len(rows)%3)})
    if len(rows)>=5000: break
   if len(rows)>=5000: break
  if len(rows)>=5000: break
 if len(rows)>=5000: break
data={"schema_version":1,"id":"comprehensive_english_5000","title":"综合英语场景 5000 句","description":"覆盖生活、旅游、机票、机场、酒店、餐饮、购物、工作及突发情况，难度高于英语四级。","language":"en-US","tags":["综合","生活对话","旅游","机酒","四级以上"],"items":rows}
target=Path(__file__).resolve().parents[1]/"content"/"libraries"/"comprehensive_english_5000.json"
target.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"wrote {len(rows)} items")
