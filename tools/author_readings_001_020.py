from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORD_DIR = ROOT / "content" / "wordlists" / "cet4_combined"
OUT_DIR = ROOT / "content" / "readings" / "cet4_combined"


def article(title, kind, targets, pairs, questions):
    return {"title": title, "type": kind, "targets": targets, "pairs": pairs, "questions": questions}


DATA = {
1: [
article("The Notice on the Lawn", "story", ["clarify","elect","citizen","observer","lawn","faithful"], [
("At noon, Mei found a wet election notice lying on the lawn outside her apartment block.", "中午，梅在公寓楼外的草坪上发现了一张被雨水打湿的选举通知。"),
("As a new citizen of the district, she wanted the committee to clarify where residents should vote.", "作为这个地区的新居民，她希望委员会说明居民应该去哪里投票。"),
("An elderly observer explained that the hall had changed because the original room was too small.", "一位年长的观察员解释说，投票大厅已经更换，因为原来的房间太小。"),
("Mei copied the correct address by hand and shared it with every family in the building.", "梅手写了正确地址，并把它分享给楼里的每个家庭。"),
("Her faithful attention to one small notice helped many neighbors elect their representative without confusion.", "她认真对待一张小通知，帮助许多邻居顺利选出了自己的代表。")],
[("Why had the voting place changed?","The original room was too small.","原投票室空间不足，所以更换了地点。"),("How did Mei help her neighbors?","She shared the correct address with them.","她抄下并分享了正确地址。")]),
article("Why Cities Need Visible Water", "explanatory", ["traffic","moisture","flow","visible","adjust","development"], [
("Rain seems harmless until heavy traffic and hard surfaces prevent water from entering the soil.", "雨水看似无害，但拥挤交通和硬质地面会阻止水渗入土壤。"),
("The resulting flow can carry rubbish into drains and flood streets within minutes.", "由此形成的水流会把垃圾带进排水沟，并在几分钟内淹没街道。"),
("Modern development therefore uses gardens and shallow channels to hold moisture near its source.", "因此，现代城市建设会利用花园和浅沟在源头附近留住水分。"),
("Designers keep these features visible so that workers can notice blockages and adjust them quickly.", "设计者让这些设施保持可见，以便工作人员发现堵塞并及时调整。"),
("When rainwater has space to slow down, both roads and rivers become safer.", "当雨水有空间减速时，道路和河流都会更安全。")],
[("What causes rainwater to flood streets quickly?","Traffic and hard surfaces stop it entering the soil.","硬质地面减少渗水，使雨水快速汇集。"),("Why are the channels kept visible?","So workers can inspect and adjust them.","可见设计方便检查和调整。")] ),
article("Should Lunch Menus Show the True Cost?", "opinion", ["plastic","cost","menu","price","promote","sufficient"], [
("A café menu usually shows only the price of a meal, not the waste created by its packaging.", "咖啡馆的菜单通常只显示餐费，而不显示包装造成的浪费。"),
("Some owners want a small symbol beside dishes that use no plastic and produce less rubbish.", "一些店主希望在不使用塑料且垃圾较少的菜品旁加一个小标志。"),
("The symbol could promote better choices, but customers may ignore it when time and money are limited.", "这个标志可以促进更好的选择，但当时间和金钱有限时，顾客可能会忽略它。"),
("Information alone is not sufficient; affordable reusable containers must also be available.", "只有信息并不足够，还必须提供价格合理的可重复使用容器。"),
("Cafés should reveal environmental cost clearly while keeping ordinary meals within everyone's reach.", "咖啡馆应该清楚说明环境成本，同时让普通餐食人人都能负担。")],
[("What would the proposed symbol identify?","Dishes with little plastic waste.","它标出塑料垃圾较少的菜品。"),("What else is needed besides information?","Affordable reusable containers.","还需要价格合理的可重复使用容器。")] )],
2: [
article("The Last Book from the Port", "story", ["secretary","earthquake","section","port","companion","freight"], [
("After the earthquake, a school secretary went to the port to collect a delayed box of books.", "地震后，一位学校秘书前往港口领取一箱延误的书。"),
("One section of the road was closed, so an officer guided her through a freight yard.", "一段道路被封闭，因此一名工作人员带她穿过货运场。"),
("Her only companion was a driver who knew which bridges had survived the shaking.", "她唯一的同伴是一位知道哪些桥梁经受住震动的司机。"),
("They reached the warehouse at sunset and found the books dry beneath a torn cover.", "他们在日落时到达仓库，发现书本在破损的遮布下仍保持干燥。"),
("The next morning, children read together while repairs continued around their classroom.", "第二天早上，孩子们一起阅读，而教室周围的维修仍在继续。")],
[("Why did the secretary visit the port?","To collect a delayed box of books.","她去领取延误的书箱。"),("Who helped her choose a safe route?","An officer and a driver.","工作人员和司机帮助她安全通行。")] ),
article("How a Simple Circuit Protects a Building", "explanatory", ["operator","circuit","simplify","protect","convert","terminal"], [
("A control-room operator watches a circuit that connects smoke sensors across a large terminal.", "控制室操作员监视着连接大型航站楼各处烟雾传感器的电路。"),
("Each sensor can convert heat or smoke into a small electrical signal.", "每个传感器都能把热量或烟雾转换成微弱的电信号。"),
("The system uses numbered zones to simplify the search for danger.", "系统使用编号分区来简化危险位置的查找。"),
("When two nearby sensors react, doors close automatically to protect passengers from smoke.", "当相邻两个传感器作出反应时，门会自动关闭，以保护乘客免受烟雾伤害。"),
("Regular tests are essential because one broken wire can hide an important warning.", "定期测试必不可少，因为一根断线就可能掩盖重要警报。")],
[("What do the sensors convert into an electrical signal?","Heat or smoke.","传感器把热量或烟雾转成电信号。"),("Why does the system use numbered zones?","To locate danger more easily.","编号分区能更快定位危险。")] ),
article("Relief Work Needs Local Knowledge", "opinion", ["drought","organization","international","natural","knowledge","strategy"], [
("An international organization can bring money and equipment to a region damaged by drought.", "国际组织可以把资金和设备带到遭受干旱的地区。"),
("Yet an imported strategy may fail when it ignores local wells, crops, and customs.", "然而，如果外来的策略忽视当地水井、作物和习俗，就可能失败。"),
("Residents possess practical knowledge about which natural resources remain available in each season.", "居民拥有实用知识，知道每个季节还有哪些自然资源可用。"),
("Outside specialists should present options, then let village groups test and revise them.", "外部专家应提出方案，再让村民小组测试并修改。"),
("Relief becomes more durable when technical skill and lived experience guide the same plan.", "当技术能力和生活经验共同指导一项计划时，救援成果会更加持久。")],
[("Why may an imported strategy fail?","It may ignore local conditions and customs.","忽略当地条件会让方案失效。"),("Who should test proposed solutions?","Local village groups.","当地村民小组应参与测试。")] )],
3: [
article("Paint on the Tunnel Wall", "story", ["paint","recover","ceremony","tunnel","scholar","gratitude"], [
("When the mountain tunnel reopened, a young scholar returned to the village for the ceremony.", "山岭隧道重新开放时，一位年轻学者回村参加仪式。"),
("Years earlier, an accident there had forced his family to leave while the road could recover.", "多年前，那里发生的事故迫使他的家人在道路修复期间离开。"),
("He brought blue paint and invited children to mark the safe walking path along one wall.", "他带来蓝色油漆，并邀请孩子们沿一面墙标出安全步道。"),
("Their pictures showed trains, birds, and the workers who had cleared the fallen stone.", "他们的图画描绘了火车、鸟和清理落石的工人。"),
("The finished mural expressed gratitude more clearly than the formal speeches outside.", "完成的壁画比外面的正式讲话更清楚地表达了感激。")],
[("What did the children mark with paint?","The safe walking path.","孩子们标出了安全步道。"),("What did the mural express?","Gratitude to the workers.","壁画表达了对工人的感谢。")] ),
article("Why Artificial Color Can Fade", "explanatory", ["color","artificial","distinct","process","mix","accuracy"], [
("An artificial color looks distinct because its molecules absorb some parts of light and reflect others.", "人工色彩之所以鲜明，是因为它的分子吸收部分光线并反射其余光线。"),
("Sunlight can break those molecules apart through a slow chemical process.", "阳光可以通过缓慢的化学过程分解这些分子。"),
("Heat and moisture may accelerate the change, especially when manufacturers mix unstable materials.", "热量和水分可能加速变化，尤其是在制造商混合不稳定材料时。"),
("Scientists test samples under strong lamps and measure the result with great accuracy.", "科学家在强光下测试样品，并非常精确地测量结果。"),
("Their findings help museums choose safer lighting for textiles, paintings, and photographs.", "他们的发现帮助博物馆为纺织品、画作和照片选择更安全的照明。")],
[("What can sunlight do to color molecules?","It can break them apart.","阳光会分解色彩分子。"),("How do museums use the test results?","They choose safer lighting.","测试结果用于选择更安全的灯光。")] ),
article("Practical Exams Deserve More Credit", "opinion", ["exam","credit","practical","accomplish","faculty","determine"], [
("A written exam can determine whether a student remembers facts, but it reveals little about applied skill.", "笔试可以判断学生是否记住事实，却很少反映应用能力。"),
("A practical task shows how learners plan, respond to mistakes, and accomplish a real goal.", "实践任务能显示学习者如何规划、应对错误并完成真实目标。"),
("Universities should give such work more credit, particularly in engineering, medicine, and design.", "大学应给予这类任务更多学分或权重，尤其是在工程、医学和设计领域。"),
("The faculty must still publish clear standards so that personal preference does not control marks.", "院系仍必须公布清晰标准，避免个人偏好左右成绩。"),
("A balanced assessment combines reliable knowledge tests with evidence of competent action.", "均衡的评价应把可靠的知识测试与胜任行动的证据结合起来。")],
[("What does a practical task reveal?","Planning, response to mistakes, and applied skill.","实践任务能反映规划、纠错和应用能力。"),("Why are clear standards necessary?","To prevent personal preference controlling marks.","明确标准能减少主观偏好。")] )],
4: [
article("Coffee Beside the Statue", "story", ["July","statue","audience","prejudice","voluntary","welfare"], [
("One hot July morning, volunteers served coffee beside a statue in the railway square.", "七月一个炎热的早晨，志愿者们在铁路广场的雕像旁供应咖啡。"),
("Their voluntary performance told the story of workers who had built the line a century earlier.", "他们的志愿演出讲述了一百年前修建铁路的工人的故事。"),
("At first, the audience laughed at an immigrant actor's accent, revealing an old prejudice.", "起初，观众嘲笑一位移民演员的口音，暴露出一种旧偏见。"),
("Then he described how his grandfather had risked his life on the same tracks.", "随后，他讲述了祖父如何在同一条铁轨上冒着生命危险工作。"),
("The square fell quiet, and the event raised funds for retired workers' welfare.", "广场安静下来，这场活动也为退休工人的福利筹得资金。")],
[("What changed the audience's attitude?","The actor's story about his grandfather.","演员讲述祖父的经历后，观众改变了态度。"),("What did the event fund?","Welfare for retired workers.","活动为退休工人的福利筹款。")] ),
article("How Bees Find Their Direction", "explanatory", ["bee","direction","visual","horizon","sway","dense"], [
("A bee can judge direction by comparing the sun's position with patterns of light in the sky.", "蜜蜂可以通过比较太阳位置与天空中的光线模式来判断方向。"),
("Even when clouds are dense, its visual system can detect signals that human eyes miss.", "即使云层浓密，它的视觉系统也能察觉人眼看不到的信号。"),
("Near the hive, flowers sway and landmarks may change, so the insect also remembers shapes along the horizon.", "在蜂巢附近，花朵会摇摆，地标也可能改变，因此蜜蜂还会记住地平线上的形状。"),
("Inside, it performs a dance whose angle points other bees toward food.", "回到蜂巢后，它会用舞蹈角度为其他蜜蜂指出食物方向。"),
("This tiny navigation system combines light, movement, distance, and memory.", "这套微小的导航系统结合了光线、运动、距离和记忆。")],
[("What can bees detect through dense clouds?","Patterns of light humans cannot see.","蜜蜂能探测人眼看不到的光线模式。"),("How does a bee share a food direction?","By performing a dance.","蜜蜂通过舞蹈传递方向。")] ),
article("Old Railroads Need Modern Safety", "opinion", ["railroad","preparation","organize","proper","financial","prevent"], [
("Historic railroad journeys attract visitors, but charming engines do not remove modern risks.", "历史铁路旅行很吸引游客，但迷人的老式机车并不能消除现代风险。"),
("Operators need proper preparation, trained staff, and a clear plan to prevent collisions.", "运营方需要充分准备、受训员工和明确方案来防止碰撞。"),
("Critics say the financial burden may force small heritage lines to close.", "批评者认为，经济负担可能迫使小型遗产铁路关闭。"),
("However, regional museums can organize shared inspections and equipment purchases to reduce cost.", "不过，地区博物馆可以组织联合检查和设备采购来降低成本。"),
("Preserving history is worthwhile only when passengers and workers can trust the journey.", "只有乘客和员工能够信任旅程安全时，保存历史才有意义。")],
[("What might force small heritage lines to close?","The financial burden of safety measures.","安全措施带来的经济负担可能导致关闭。"),("How can museums reduce costs?","Through shared inspections and purchases.","联合检查和采购可以降低成本。")] )],
5: [
article("The Package at Dawn", "story", ["fund","dawn","package","campus","guest","deliver"], [
("At dawn, a student carried a heavy package across an almost empty campus.", "黎明时分，一名学生抱着沉重包裹穿过几乎空无一人的校园。"),
("It contained donated physics tools bought with a community fund for the new laboratory.", "包裹里装着用社区基金购买并捐赠给新实验室的物理工具。"),
("A visiting guest had promised to demonstrate them before catching an early train.", "一位来访嘉宾答应在赶早班火车前演示这些工具。"),
("When the main door remained locked, the student called a cleaner who knew another entrance.", "当正门仍然锁着时，学生叫来一位知道另一个入口的清洁工。"),
("They managed to deliver the equipment just as the first curious class arrived.", "就在第一批充满好奇的学生到来时，他们成功送达了设备。")],
[("What was inside the package?","Donated physics tools.","包裹中是捐赠的物理工具。"),("Who knew another entrance?","A cleaner.","一名清洁工知道另一个入口。")] ),
article("Why Bubbles Grow in Heated Fluid", "explanatory", ["bubble","power","fluid","indication","below","maximum"], [
("A bubble forms in a heated fluid when faster molecules create a pocket of vapor.", "加热液体中，运动加快的分子形成蒸气空间，于是产生气泡。"),
("At first, pressure may crush tiny pockets before they reach the surface.", "起初，压力可能在微小气泡到达表面前将其压碎。"),
("As the temperature rises, larger bubbles become a visible indication that boiling is near.", "随着温度上升，更大的气泡成为即将沸腾的明显迹象。"),
("Below the boiling point, heat still moves through the liquid and changes its circulation.", "在沸点以下，热量仍会穿过液体并改变其循环。"),
("Increasing the power beyond the useful maximum only wastes energy and may spill the liquid.", "把功率提高到有效上限以上只会浪费能源，还可能使液体溢出。")],
[("What do larger bubbles indicate?","That boiling is near.","较大的气泡表示液体接近沸腾。"),("What happens if power is too high?","Energy is wasted and liquid may spill.","功率过高会浪费能源并导致溢出。")] ),
article("A Bigger Campus Is Not Always Better", "opinion", ["enlarge","requirement","prominent","shortage","architecture","future"], [
("A university may enlarge its campus when classrooms are crowded and housing is in shortage.", "当教室拥挤且住房短缺时，大学可能会扩建校园。"),
("New architecture can become a prominent symbol of confidence in the future.", "新建筑可以成为对未来充满信心的醒目标志。"),
("Yet size is not the only requirement for good education; maintenance and teaching also need money.", "然而，规模并不是良好教育的唯一条件，维护和教学同样需要资金。"),
("Before building, leaders should measure how existing rooms are used throughout the week.", "在建设之前，管理者应衡量现有房间在一周内的使用情况。"),
("Flexible schedules and renovation may solve the real problem with less land and debt.", "灵活的时间安排和翻修可能用更少土地和债务解决真正的问题。")],
[("Why might a university expand?","Because of crowded rooms and a housing shortage.","教室拥挤和住房短缺可能促使扩建。"),("What alternatives does the passage suggest?","Flexible schedules and renovation.","文章建议灵活排课和翻修。")] )],
6: [
article("A Thermometer in the Barn", "story", ["thermometer","repair","nurse","consult","hopeful","wooden"], [
("Lina, a village nurse, arrived at a wooden barn where a child was resting after a fall.", "乡村护士莉娜来到一座木制谷仓，一个孩子摔倒后正在那里休息。"),
("Her thermometer showed a normal temperature, but the boy complained that his arm felt numb.", "她的温度计显示体温正常，但男孩说手臂发麻。"),
("She used her phone to consult a doctor rather than guess at the injury.", "她用电话咨询医生，而没有猜测伤情。"),
("While the family waited for transport, a neighbor began to repair the broken gate.", "家人在等待车辆时，一位邻居开始修理损坏的大门。"),
("Everyone remained hopeful, and an X-ray later confirmed that no bone was broken.", "大家一直抱有希望，后来的X光检查证实没有骨折。")],
[("Why did Lina consult a doctor?","The boy's arm felt numb.","孩子手臂发麻，需要专业判断。"),("What did the X-ray show?","No bone was broken.","X光显示没有骨折。")] ),
article("How Seeds Know When to Grow", "explanatory", ["bright","element","nucleus","derive","transform","limitation"], [
("A dry seed contains a living plant, but its hard coat keeps the inside protected.", "干燥种子中含有活的植物胚，但坚硬外壳保护着内部。"),
("Once the soil becomes wet and the light is bright, stored food can transform into usable energy.", "土壤变湿且光线明亮后，储存的养分就能转化为可用能量。"),
("Signals from each cell's nucleus then guide growth in the root and shoot.", "随后，每个细胞核发出的信号引导根和芽的生长。"),
("The young plant must also obtain every essential element it cannot derive from stored food.", "幼苗还必须获取那些无法从储存养分中得到的必需元素。"),
("Cold, darkness, or poor soil can become a limitation even when enough water is present.", "即使水分充足，寒冷、黑暗或贫瘠土壤也可能成为限制因素。")],
[("What allows stored food to become usable energy?","Water entering the seed.","水进入种子后启动能量转化。"),("What can limit growth besides water?","Cold, darkness, or poor soil.","寒冷、黑暗或贫瘠土壤也会限制生长。")] ),
article("Repair Before Replacement", "opinion", ["fuel","electrical","dust","family","extraordinary","otherwise"], [
("When an electrical appliance stops working, a family may replace it without asking what failed.", "电器停止工作时，一个家庭可能不查原因就直接更换。"),
("Often the cause is ordinary dust, a loose connection, or one inexpensive part.", "原因往往只是普通灰尘、松动的连接或一个便宜零件。"),
("Repair saves materials and fuel used in manufacturing and transport.", "维修可以节省制造和运输中使用的材料与燃料。"),
("It should not require extraordinary technical courage: shops can publish prices and provide basic guarantees.", "维修不应需要非凡的技术勇气，商店可以公布价格并提供基本保障。"),
("Otherwise, consumers will continue to choose the certainty of a new machine over an unclear repair.", "否则，消费者会继续选择确定的新机器，而不是结果不明的维修。")],
[("What common faults does the passage mention?","Dust, a loose connection, or a cheap part.","常见故障包括灰尘、接线松动和小零件损坏。"),("How can shops encourage repair?","Publish prices and offer guarantees.","透明价格和保障能鼓励维修。")] )],
7: [
article("Dusk on Gull Island", "story", ["cliff","drown","island","dusk","fatigue","assist"], [
("At dusk, a tired birdwatcher heard shouting below the western cliff of Gull Island.", "黄昏时，一名疲惫的观鸟者听见海鸥岛西侧悬崖下有人呼喊。"),
("A kayaker had overturned and was struggling against the current, close enough to see but hard to reach.", "一名皮划艇者翻船后正在水流中挣扎，虽看得见却难以接近。"),
("Fearing he might drown, the birdwatcher called the harbor and threw down a bright rope.", "观鸟者担心他溺水，于是呼叫港口并抛下一条亮色绳索。"),
("Two fishers arrived to assist, pulling the man into their boat as fatigue weakened his grip.", "两名渔民赶来协助，在疲劳使男子握力减弱时把他拉上船。"),
("The rescue ended safely, and the island council later placed an emergency box near the path.", "救援安全结束，岛上委员会后来在小路旁设置了应急箱。")],
[("Why did the birdwatcher call the harbor?","A kayaker was in danger of drowning.","皮划艇者面临溺水危险。"),("What was added after the rescue?","An emergency box near the path.","事后小路旁增设了应急箱。")] ),
article("Why Petrol Use Falls on Short Trips", "explanatory", ["transportatio","quantity","decrease","petrol","stable","formula"], [
("The word transportatio appears misspelled in an old data table, yet the figures still tell a useful story.", "旧数据表中的 transportatio 一词拼写有误，但数据仍讲述了一个有用的事实。"),
("A cold engine burns a greater quantity of petrol during the first few minutes of a journey.", "冷发动机在旅程最初几分钟会燃烧更多汽油。"),
("Once its temperature becomes stable, the same distance requires less fuel.", "温度稳定后，行驶相同距离所需燃料会减少。"),
("This is why average consumption can decrease when several short errands become one planned route.", "因此，把几次短途差事合并成一条规划路线，可以降低平均油耗。"),
("No single formula fits every vehicle, but distance, load, and driving style explain much of the difference.", "没有一个公式适合所有车辆，但距离、载重和驾驶方式能解释大部分差异。")],
[("When does an engine use more petrol?","During the first minutes while it is cold.","冷启动后的最初几分钟油耗较高。"),("How can drivers reduce average consumption?","Combine short errands into one route.","合并短途出行可减少平均油耗。")] ),
article("Tourism Must Sustain Island Life", "opinion", ["prosperous","location","sustain","furniture","appliance","civilize"], [
("A beautiful island location can become prosperous when visitors support local boats, cafés, and guides.", "美丽的岛屿可以因游客支持当地船只、咖啡馆和导游而繁荣。"),
("However, resorts often import every appliance and item of furniture, sending much of the income away.", "然而，度假村常常进口所有电器和家具，使大量收入流向外地。"),
("Tourism should sustain ordinary life by buying local food and training residents for skilled work.", "旅游业应购买当地食品并培训居民从事技能工作，从而维持日常生活。"),
("Visitors must also avoid the arrogant belief that they arrive to civilize a remote community.", "游客也必须避免那种自以为来教化偏远社区的傲慢想法。"),
("A healthy industry treats island culture as a living relationship, not a decorative product.", "健康的产业把岛屿文化视为鲜活关系，而不是装饰性商品。")],
[("Why can tourist income leave the island?","Resorts import furniture and appliances.","进口物品会使旅游收入外流。"),("How should tourism support residents?","Buy local goods and provide skilled work.","购买本地产品并提供技能岗位。")] )],
8: [
article("The Clerk's Reading Month", "story", ["clerk","lonely","campaign","reading","encourage","create"], [
("A quiet library clerk noticed that an elderly visitor spent every afternoon alone by the window.", "一位安静的图书管理员发现，一位老人每天下午都独自坐在窗边。"),
("The man loved reading but felt too lonely to join the noisy events downstairs.", "老人喜欢阅读，却因孤独而不愿参加楼下喧闹的活动。"),
("The clerk began a month-long campaign that paired two strangers with the same short book.", "管理员发起了为期一个月的活动，让两位陌生人共读同一本短书。"),
("Simple question cards helped encourage conversation without forcing anyone to speak publicly.", "简单的问题卡鼓励交流，又不会强迫任何人公开发言。"),
("By spring, the readers had helped create three small groups that met without staff assistance.", "到了春天，读者们已经建立了三个无需员工协助的小组。")],
[("Why did the visitor avoid events?","They were noisy and he felt lonely.","他感到孤独，也不喜欢喧闹活动。"),("What helped strangers begin talking?","Question cards about a shared book.","共读书籍的问题卡帮助他们交流。")] ),
article("Why Vitamin Variety Matters", "explanatory", ["variety","vitamin","important","resemble","exceed","facility"], [
("Each vitamin works in different chemical processes, even when tablets resemble one another.", "每种维生素参与不同的化学过程，即使药片外观相似。"),
("Some help release energy from food, while others are important for blood, skin, or vision.", "有些帮助从食物中释放能量，另一些对血液、皮肤或视力很重要。"),
("A varied diet usually supplies them in safer amounts than a single concentrated product.", "多样化饮食通常比单一浓缩产品以更安全的量提供维生素。"),
("If supplements exceed the body's needs, certain vitamins can accumulate and cause harm.", "如果补充剂超过身体需要，某些维生素会积累并造成伤害。"),
("A medical facility can test a suspected shortage, but most people benefit first from improving food variety.", "医疗机构可以检测疑似缺乏，但多数人首先会从改善食物多样性中受益。")],
[("Why can some supplements be harmful?","Some vitamins accumulate when intake is excessive.","摄入过量时，某些维生素会在体内积累。"),("What is the first useful step for most people?","Improve the variety of their diet.","多数人应先改善饮食多样性。")] ),
article("Factories Should Welcome Criticism", "opinion", ["industry","suspicion","faulty","criticize","formal"], [
("When residents criticize a factory, managers sometimes treat every complaint as an attack on industry.", "居民批评工厂时，管理者有时把所有投诉都视为对工业的攻击。"),
("That response increases suspicion, especially after faulty equipment or unexplained smoke is reported.", "这种回应会增加怀疑，尤其是在有人报告设备故障或不明烟雾之后。"),
("A formal public meeting allows engineers to present evidence and neighbors to describe what they observed.", "正式公开会议让工程师展示证据，也让邻居描述他们的观察。"),
("Not every criticism will be technically correct, but each one can reveal a gap in communication.", "并非每条批评在技术上都正确，但每一条都可能揭示沟通缺口。"),
("Trust grows when a company investigates specific claims and publishes what it learns.", "企业调查具体问题并公布结果时，信任才会增长。")],
[("What increases public suspicion?","Dismissing complaints after reported problems.","在出现问题后轻视投诉会增加怀疑。"),("What should a company publish?","The results of its investigations.","企业应公布调查所得。")] )],
9: [
article("The Diamond in the Breakfast Dish", "story", ["baggage","deceit","painful","acquaintance","dish","diamond"], [
("During breakfast at a small hotel, Rosa noticed a diamond ring beneath her empty dish.", "在一家小旅馆吃早餐时，罗莎发现空盘子下面有一枚钻戒。"),
("A recent acquaintance claimed it belonged to his sister and asked Rosa to hide it in her baggage.", "一位刚认识的人声称戒指属于他的妹妹，并让罗莎把它藏进行李。"),
("His nervous voice suggested deceit, so she carried the ring directly to the manager.", "他紧张的声音暗示有欺骗，因此她把戒指直接交给经理。"),
("The true owner soon returned, fearing that the painful loss might be permanent.", "真正的主人很快回来，担心这次痛苦的损失会成为永久遗憾。"),
("Camera records showed that the stranger had found the ring first and planned to sell it.", "监控记录显示，那名陌生人先发现戒指并打算卖掉它。")],
[("Why did Rosa distrust the acquaintance?","His request and nervous voice suggested deceit.","他的要求和紧张语气令人生疑。"),("How was the truth confirmed?","Through the hotel's camera records.","酒店监控证实了真相。")] ),
article("How Glue Holds Two Surfaces", "explanatory", ["layer","glue","evaporate","friction","permanent","insert"], [
("A thin layer of glue can enter tiny spaces that look smooth to the human eye.", "一层薄胶可以进入肉眼看似光滑的表面细缝。"),
("When two pieces are pressed together, the liquid spreads and creates many points of contact.", "两件物体压在一起时，液体扩散并形成许多接触点。"),
("Water or another solvent must then evaporate, leaving stronger material behind.", "水或其他溶剂随后必须蒸发，留下更坚固的材料。"),
("Friction and chemical attraction resist movement, making the connection seem permanent.", "摩擦力和化学吸引力抵抗移动，使连接看起来很牢固。"),
("Workers sometimes insert a rough strip between surfaces because texture gives the glue more area to grip.", "工人有时会在表面间加入粗糙条带，因为纹理能让胶水抓住更大面积。")],
[("What remains after the solvent evaporates?","The stronger adhesive material.","溶剂蒸发后留下更强的黏合材料。"),("Why can a rough strip improve the bond?","It gives the glue more area to grip.","粗糙纹理增加胶水的接触面积。")] ),
article("Receipts Should Be Easy to Refuse", "opinion", ["complain","decision","receipt","sensible","moderate","tolerate"], [
("Many shops print a receipt automatically, even when the customer will throw it away immediately.", "许多商店会自动打印小票，即使顾客马上就会扔掉。"),
("A sensible system would ask for a decision before using paper, rather than after printing.", "合理的系统会在用纸前询问顾客，而不是打印后再问。"),
("Some people complain that digital records exclude customers without smartphones.", "有人抱怨电子记录会排除没有智能手机的顾客。"),
("That concern is valid, so paper must remain available at a moderate cost to the business.", "这种担忧合理，因此商家仍应以适度成本提供纸质小票。"),
("Customers should not have to tolerate waste simply because a machine's default setting is old.", "顾客不应仅因机器默认设置陈旧而忍受浪费。")],
[("When should shops ask about receipts?","Before printing them.","商店应在打印前询问。"),("Why must paper receipts remain available?","Some customers lack smartphones.","部分顾客没有智能手机。")] )],
10: [
article("The Physician's Disguise", "story", ["overnight","physician","criminal","funeral","disguise","confess"], [
("An exhausted physician boarded an overnight train after attending a distant funeral.", "一位疲惫的医生参加远方葬礼后登上了夜班列车。"),
("Across the aisle, a man in a poor disguise kept watching a report about a wanted criminal.", "过道对面，一个伪装拙劣的男人一直盯着一则通缉犯报道。"),
("When the train stopped suddenly, the man's injured ankle caused him to cry out.", "火车突然停下时，男人受伤的脚踝让他叫出声来。"),
("The physician treated him but quietly asked a guard to check his name.", "医生为他处理伤势，同时悄悄请乘警核查他的姓名。"),
("Faced with the evidence, the passenger chose to confess before they reached the next station.", "面对证据，这名乘客在抵达下一站前选择认罪。")],
[("What drew attention to the passenger?","His disguise and reaction to the report.","他的伪装以及对报道的反应引起注意。"),("When did he confess?","Before the next station.","他在到达下一站前认罪。")] ),
article("Why Food Turns Rotten", "explanatory", ["mature","rotten","produce","storage","generation","regular"], [
("Fresh produce continues to breathe and change after farmers pick it.", "新鲜农产品在采摘后仍会呼吸并发生变化。"),
("As fruit becomes mature, natural enzymes soften its structure and release sweeter smells.", "水果成熟时，天然酶会软化其结构并释放更甜的气味。"),
("Microbes use the same food, and each new generation increases quickly in warm conditions.", "微生物也利用这些食物，并在温暖环境中一代代迅速增加。"),
("Cool, dry storage slows both processes but cannot stop them forever.", "阴凉干燥的储存会减慢这两个过程，却无法永远阻止。"),
("Regular inspection removes rotten items before mold and bacteria spread to nearby food.", "定期检查可以在霉菌和细菌扩散到附近食物前清除腐烂物品。")],
[("What softens fruit as it matures?","Natural enzymes.","天然酶会使成熟水果变软。"),("Why is regular inspection useful?","It removes rotten food before microbes spread.","检查能及时清除腐烂食物，防止微生物扩散。")] ),
article("Outdoor Displays Need Restraint", "opinion", ["outdoors","display","focus","bother","enforce","disorder"], [
("Large screens outdoors can display public art, travel information, and emergency messages.", "户外大屏可以展示公共艺术、出行信息和紧急消息。"),
("They can also flash advertisements so brightly that drivers lose focus and nearby residents cannot sleep.", "它们也可能播放过亮广告，使司机分心并打扰附近居民睡眠。"),
("Cities should enforce limits on brightness and movement after dark.", "城市应执行夜间亮度和画面运动限制。"),
("Owners may argue that such rules bother business, but visual disorder imposes a cost on everyone.", "业主可能认为这些规定妨碍经营，但视觉混乱会让所有人付出代价。"),
("Clear standards can preserve useful displays while protecting streets from becoming constant advertisements.", "清晰标准既能保留有用的显示屏，也能防止街道变成持续不断的广告。")],
[("How can bright screens affect drivers?","They can make drivers lose focus.","过亮屏幕会让司机分心。"),("What limits does the writer support?","Limits on brightness and movement after dark.","作者支持限制夜间亮度和动态效果。")] )],
11: [
article("The Evidence in the Cottage", "story", ["cottage","fault","pursue","evidence","corridor","precise"], [
("Mara drove to an empty cottage after a neighbor reported a light moving behind its curtains.", "邻居报告空屋窗帘后有灯光移动后，玛拉开车赶到那座小屋。"),
("She found no broken window, but muddy marks led from the kitchen into a narrow corridor.", "她没有发现破窗，却看到泥印从厨房延伸到狭窄走廊。"),
("Rather than pursue the visitor alone, she photographed each mark as evidence and called the owner.", "她没有独自追赶来客，而是把每个痕迹拍作证据并联系屋主。"),
("A precise description of a missing key helped the police identify the owner's former partner.", "对一把遗失钥匙的准确描述帮助警方认出了屋主的前合伙人。"),
("He admitted entering the house but claimed that an unpaid debt, not theft, was at fault.", "他承认进入屋内，却声称起因是未偿债务而非盗窃。")],
[("Why did Mara photograph the marks?","To preserve them as evidence.","她拍照是为了保存证据。"),("What helped identify the visitor?","A precise description of a missing key.","对遗失钥匙的准确描述帮助确认了身份。")] ),
article("How a Submarine Changes Depth", "explanatory", ["submarine","tower","total","condense","organ","edge"], [
("A submarine controls depth by changing the amount of water and air in special ballast tanks.", "潜艇通过改变专用压载舱中的水和空气量来控制深度。"),
("To descend, valves near the tower open and water enters until the vessel's total weight increases.", "下潜时，指挥塔附近的阀门打开，海水进入，使潜艇总重量增加。"),
("To rise, compressed air pushes that water back out through openings along the edge of the hull.", "上浮时，压缩空气把海水从船体边缘的开口推出。"),
("Cool surfaces may also cause moisture to condense, so ventilation protects machines and crew.", "低温表面还可能使水汽凝结，因此通风系统会保护机器和船员。"),
("Like an organ in a body, each system must cooperate with many others to keep the vessel balanced.", "就像身体中的器官一样，每套系统都必须与其他系统协作以保持潜艇平衡。")],
[("What makes the submarine descend?","Water entering its ballast tanks.","海水进入压载舱会使潜艇下沉。"),("Why is ventilation necessary?","It controls condensed moisture.","通风能控制凝结水汽。")] ),
article("Evidence Should Lead the News", "opinion", ["description","leading","check","typical","provided","revise"], [
("A dramatic description often becomes the leading line of an online report before all facts are known.", "事实尚未查清时，夸张描述常成为网络报道的头条句。"),
("Editors should check original records and identify who provided each important claim.", "编辑应核查原始记录，并说明每项重要说法由谁提供。"),
("A typical breaking story will change as witnesses, documents, and context become available.", "典型突发新闻会随着证人、文件和背景信息出现而变化。"),
("Newsrooms must revise visible errors instead of quietly replacing old wording.", "新闻编辑部必须公开更正明显错误，而不是悄悄替换旧表述。"),
("Speed matters, but a fast report without a clear trail of evidence weakens public trust.", "速度很重要，但缺少清晰证据链的快速报道会削弱公众信任。")],
[("What should editors check?","Original records and the source of claims.","编辑应核查原始记录和消息来源。"),("Why should corrections be visible?","To preserve public trust.","公开更正有助于维护信任。")] )],
12: [
article("The Promise at the Halt", "story", ["anxiety","veteran","halt","promise","crew","adventure"], [
("A bus carrying a film crew came to a sudden halt on a narrow mountain road.", "一辆载着摄制组的巴士在狭窄山路上突然停下。"),
("Rising smoke caused anxiety until a veteran driver discovered a loose electrical cable.", "冒出的烟引发焦虑，直到一位经验丰富的司机发现松动的电缆。"),
("He made the passengers promise to remain outside while he disconnected the battery.", "他让乘客保证留在车外，自己则断开电池。"),
("Their planned adventure became a quiet evening beside the road, sharing food with nearby farmers.", "原计划的冒险变成了路边安静的一晚，大家与附近农民分享食物。"),
("The delay ruined one scene but gave the documentary an honest ending about patience and help.", "延误毁掉了一个镜头，却给纪录片带来了关于耐心与互助的真实结尾。")],
[("What caused the smoke?","A loose electrical cable.","松动电缆导致冒烟。"),("How did the delay improve the film?","It provided an honest ending.","延误为影片带来了真实结尾。")] ),
article("What a Microscope Reveals", "explanatory", ["microscope","superficial","current","diameter","interpretatio","existence"], [
("A microscope enlarges detail, but seeing a shape does not automatically explain its existence or purpose.", "显微镜放大细节，但看到形状并不会自动解释它为何存在或有何作用。"),
("A scientist first measures its diameter, color, movement, and response to the surrounding liquid.", "科学家先测量其直径、颜色、运动以及对周围液体的反应。"),
("An electrical current or chemical stain may expose structures hidden below the superficial surface.", "电流或化学染色可能揭示隐藏在表层之下的结构。"),
("The damaged word interpretatio in an old label reminds researchers to verify inherited notes.", "旧标签中残缺的 interpretatio 一词提醒研究者核实沿用下来的笔记。"),
("Reliable conclusions come from repeated observation, not one attractive image.", "可靠结论来自反复观察，而不是一张漂亮图片。")],
[("What may reveal hidden structures?","An electrical current or chemical stain.","电流或化学染色可以显现隐藏结构。"),("Why should old notes be verified?","Labels may be damaged or mistaken.","旧标签可能损坏或有误。")] ),
article("Settlements Need More Than Houses", "opinion", ["settlement","principle","friendly","conflict","communication","honourable"], [
("A new settlement can provide affordable homes yet still leave residents isolated from one another.", "新社区可以提供可负担住房，却仍可能让居民彼此隔离。"),
("Good planning follows a simple principle: daily communication should be easy, safe, and natural.", "良好规划遵循一个简单原则：日常交流应当方便、安全且自然。"),
("Friendly courtyards, shared gardens, and small shops create places where unfamiliar people can meet.", "友好的庭院、共享花园和小商店为陌生人创造相遇空间。"),
("Design cannot remove every conflict, but it can prevent minor disagreements from becoming permanent divisions.", "设计无法消除所有冲突，却能防止小分歧变成永久隔阂。"),
("An honourable housing policy treats social connection as a necessity rather than decoration.", "负责任的住房政策会把社会联系视为必需品而非装饰。")],
[("What spaces encourage communication?","Courtyards, gardens, and small shops.","庭院、花园和小商店促进交流。"),("What cannot design remove completely?","Conflict between residents.","设计无法完全消除居民冲突。")] )],
13: [
article("The Balloon over the Old Wall", "story", ["twin","balloon","imagination","historical","vision","insect"], [
("Two twin brothers found a red balloon trapped above a historical wall near their school.", "一对双胞胎兄弟在学校附近的古墙上方发现了一个被卡住的红气球。"),
("One imagined a secret signal, while the other used his practical vision to search for a string.", "一个把它想象成秘密信号，另一个则实际寻找气球线。"),
("They followed the string into tall grass and discovered an unusual insect caught beneath it.", "他们沿着线走进高草，发现一只罕见昆虫被压在下面。"),
("Their imagination gave way to careful work as they freed the creature without touching its wings.", "他们收起想象，小心操作，在不碰翅膀的情况下放走了昆虫。"),
("A museum later identified it as a local species once thought to have disappeared.", "一家博物馆后来确认它是曾被认为已经消失的本地物种。")],
[("What did the string lead the brothers to?","An unusual trapped insect.","气球线把他们带到一只被困昆虫旁。"),("Why was the discovery important?","The species was thought to have disappeared.","这种本地物种一度被认为已经消失。")] ),
article("Why Flavour Changes with Temperature", "explanatory", ["flavour","compound","function","approximate","leather","dew"], [
("Flavour depends on each chemical compound that reaches receptors in the nose and mouth.", "味道取决于到达鼻腔和口腔感受器的各种化合物。"),
("Warm food releases more aromatic molecules, so smell can perform a larger function in the experience.", "温热食物会释放更多芳香分子，因此嗅觉在体验中发挥更大作用。"),
("Cold can hide sweetness and make texture seem firm, sometimes almost like leather.", "低温会掩盖甜味并使口感显得坚韧，有时几乎像皮革。"),
("Chefs therefore use only an approximate seasoning level until a dish reaches serving temperature.", "因此，厨师在菜品达到食用温度前只做大致调味。"),
("Even morning dew on herbs may dilute their oils slightly and alter the final balance.", "即使香草上的晨露也可能轻微稀释精油，改变最终平衡。")],
[("Why does warm food often smell stronger?","It releases more aromatic molecules.","温热食物释放更多芳香分子。"),("Why is early seasoning approximate?","Flavour changes at serving temperature.","味道会随食用温度变化。")] ),
article("Local History Belongs to Everyone", "opinion", ["local","civilization","intellectual","league","democratic","limit"], [
("Local history is sometimes controlled by a small intellectual circle that decides which stories matter.", "地方历史有时由少数学术圈掌控，由他们决定哪些故事重要。"),
("That approach can reduce an entire civilization to leaders, wars, and official buildings.", "这种做法可能把整个文明缩减为领袖、战争和官方建筑。"),
("A democratic archive should also collect workers' letters, family photographs, songs, and oral memories.", "民主的档案也应收集工人书信、家庭照片、歌曲和口述记忆。"),
("Museums can form a league with schools and neighborhood groups to share equipment and training.", "博物馆可以与学校和社区团体结成联盟，共享设备和培训。"),
("Professional standards should limit false claims without silencing people whose experience was rarely recorded.", "专业标准应限制虚假说法，同时不让那些经历少有记录的人失声。")],
[("What materials should a democratic archive collect?","Everyday letters, photos, songs, and memories.","档案应收集普通人的多种生活材料。"),("What should professional standards limit?","False historical claims.","专业标准应限制虚假历史说法。")] )],
14: [
article("A Puzzle in the Medical Tent", "story", ["heart","medical","puzzle","gauge","fearful","deduce"], [
("A runner entered the medical tent with a racing heart and a fearful expression.", "一名跑者心跳很快、神情恐惧地走进医疗帐篷。"),
("The nurse used a small gauge to check his blood pressure, which was lower than expected.", "护士用小仪表测量他的血压，结果比预期低。"),
("His symptoms formed a puzzle because he had eaten well and suffered no obvious injury.", "他的症状成了谜，因为他吃得很好，也没有明显受伤。"),
("From the salt marks on his shirt, the doctor could deduce that he had lost too much fluid.", "医生从他衬衫上的盐渍推断出他流失了过多水分。"),
("Water and minerals soon restored him, and he left with a safer plan for future races.", "水和矿物质很快让他恢复，他也带着更安全的比赛计划离开。")],
[("What did the salt marks reveal?","He had lost too much fluid.","盐渍表明他流失了过多水分。"),("What treatment helped him?","Water and minerals.","水和矿物质使他恢复。")] ),
article("How Scanners Turn Light into Data", "explanatory", ["input","light","scan","downward","basic","finish"], [
("A document scanner sends a narrow line of light across a page from one edge to the other.", "文件扫描仪让一束窄光从纸张一边扫到另一边。"),
("White areas reflect more light, while dark ink sends less back to the sensor.", "白色区域反射更多光线，深色墨迹返回传感器的光更少。"),
("This changing signal becomes digital input arranged in rows as the mechanism moves downward.", "当机械装置向下移动时，变化的信号成为按行排列的数字输入。"),
("Basic software then corrects small shadows and predicts where letters begin and finish.", "基础软件随后修正小阴影，并判断字母的起止位置。"),
("A sharper scan stores more detail, but it also creates a larger file.", "更清晰的扫描会保存更多细节，但也会产生更大的文件。")],
[("How does dark ink affect reflected light?","It reflects less light to the sensor.","深色墨迹反射的光较少。"),("What is the cost of a sharper scan?","A larger digital file.","更高精度会产生更大文件。")] ),
article("Economic Debate Needs Mild Language", "opinion", ["aggressive","economic","minority","resistance","proud","mistake"], [
("Economic debate often becomes aggressive when speakers treat disagreement as a personal weakness.", "当发言者把分歧视为个人弱点时，经济讨论常会变得咄咄逼人。"),
("A political minority may then show resistance simply to defend its identity.", "政治少数派可能仅为维护身份而表现出抵制。"),
("Leaders should be proud of changing their position when stronger evidence reveals a mistake.", "当更有力证据揭示错误时，领导者应为改变立场而感到自豪。"),
("Mild language leaves room for correction without demanding public humiliation.", "温和语言为纠错留下空间，也无需公开羞辱。"),
("Firm ideas and respectful speech can exist together, and policy improves when they do.", "坚定观点与尊重表达可以并存，而两者并存时政策会更好。")],
[("Why may a minority resist a proposal?","To defend its identity during aggressive debate.","激烈争论会让少数派出于身份防御而抵制。"),("When should leaders change position?","When stronger evidence reveals a mistake.","更强证据指出错误时应改变立场。")] )],
15: [
article("A Deer on the Night Trail", "story", ["deer","dramatic","interrupt","trail","hero","sensitive"], [
("A deer can interrupt any race; that night, one suddenly stepped onto the mountain trail.", "鹿可能打断任何比赛；那天夜里，一只鹿突然踏上山地赛道。"),
("The first rider made a dramatic turn, fell, and shouted a warning to those behind him.", "第一名骑手猛然转向后摔倒，并向后方选手发出警告。"),
("Another competitor stopped to protect the sensitive animal from lights and noise.", "另一名选手停下来，保护这只对灯光和噪声敏感的动物。"),
("Spectators called him a hero, although stopping cost him a possible victory.", "观众称他为英雄，尽管停下让他失去了可能的胜利。"),
("Officials later moved the route away from a spring feeding area used by wildlife.", "官员后来把路线移离野生动物春季觅食区。")],
[("Why did the first rider turn suddenly?","A deer entered the trail.","一只鹿进入了赛道。"),("How did officials respond later?","They moved the race route.","官员后来调整了比赛路线。")] ),
article("Why Plants Grow toward Light", "explanatory", ["grow","stem","distribution","advanced","critical","liquid"], [
("A young plant uses chemical signals to decide where its stem should grow.", "幼苗利用化学信号决定茎应向哪里生长。"),
("When light comes from one side, the distribution of a growth hormone becomes uneven.", "光从一侧照来时，生长激素的分布会变得不均匀。"),
("Cells on the darker side lengthen more, bending the stem toward the light.", "背光侧细胞伸长得更多，使茎弯向光源。"),
("Water in each cell acts like internal liquid pressure, so hydration is also critical.", "每个细胞中的水形成内部液体压力，因此水分也至关重要。"),
("Advanced cameras can record this slow movement and reveal changes invisible from moment to moment.", "先进摄像机能记录这种缓慢运动，揭示肉眼逐刻看不到的变化。")],
[("Why does the stem bend?","Cells on the darker side grow longer.","背光侧细胞伸长更多。"),("What role does water play?","It provides internal pressure in cells.","水为细胞提供内部压力。")] ),
article("Public Toilets Are Essential Infrastructure", "opinion", ["public","necessary","toilet","maintenance","routine","technical"], [
("A clean public toilet is necessary for children, older people, workers, and anyone spending hours outside.", "干净的公共厕所对儿童、老人、劳动者和长时间在外的人都必不可少。"),
("Cities often build attractive facilities but fail to budget for routine maintenance.", "城市常建造漂亮设施，却没有为日常维护编列预算。"),
("The result is a locked or broken toilet that exists on a map but not in practice.", "结果就是地图上存在、实际却上锁或损坏的厕所。"),
("Technical sensors can report leaks and supply shortages, although staff must still respond promptly.", "技术传感器可以报告漏水和用品短缺，但工作人员仍须及时处理。"),
("Reliable access should be treated as basic public infrastructure, with clear standards and published inspections.", "可靠的使用条件应被视为基础公共设施，并配有清晰标准和公开检查。")],
[("What problem follows poor maintenance budgets?","Facilities become locked or broken.","维护预算不足会使设施关闭或损坏。"),("What can sensors report?","Leaks and supply shortages.","传感器可以报告漏水和用品不足。")] )],
16: [
article("The Silent Subway Lesson", "story", ["silent","lesson","subway","rush","gentleman","remarkable"], [
("During the evening rush, a subway car became silent when an elderly gentleman dropped his bag.", "晚高峰时，一位老先生的包掉落，地铁车厢突然安静下来。"),
("Hundreds of small coins rolled across the floor as the train entered a tunnel.", "列车进入隧道时，数百枚小硬币滚过地板。"),
("Without speaking, passengers formed a line and gathered every coin before the next stop.", "乘客们默默排成一列，在下一站前捡回了每枚硬币。"),
("The remarkable cooperation lasted less than two minutes and needed no leader.", "这场非凡的合作持续不到两分钟，也不需要领导者。"),
("For a child watching nearby, it became a lesson about kindness in crowded places.", "对旁边观看的孩子来说，这成了一堂关于拥挤场所中善意的课。")],
[("Why did passengers form a line?","To collect the dropped coins.","他们排队捡起掉落的硬币。"),("What lesson did the child learn?","Crowded places can still contain kindness.","孩子看到了拥挤环境中的善意。")] ),
article("How Horsepower Became a Measure", "explanatory", ["horsepower","mechanics","survey","effect","outset"], [
("At the outset of the steam age, buyers understood horses better than engines.", "蒸汽时代初期，买家对马匹比对发动机更了解。"),
("Engineers introduced horsepower to compare a machine's effect with familiar animal labor.", "工程师引入马力，用机器效果与熟悉的动物劳动进行比较。"),
("They observed working horses, measured lifted weight, and used mechanics to estimate a rate.", "他们观察工作中的马匹，测量提升重量，并利用力学估算速率。"),
("The estimate was generous, partly because sellers wanted engines to appear reliable.", "这个估计较为宽松，部分原因是卖家希望发动机显得可靠。"),
("A modern survey of motors uses more exact units, but horsepower remains useful in everyday language.", "现代电机测量使用更精确的单位，但马力在日常语言中仍很实用。")],
[("Why was horsepower introduced?","To compare engines with familiar horse labor.","马力用于把发动机与熟悉的马匹劳动比较。"),("Why was the early estimate generous?","It helped sellers present engines favorably.","较高估计有利于销售发动机。")] ),
article("Highways Should Repair Communities", "opinion", ["residence","environment","highway","influence","prosperity","division"], [
("A highway may bring regional prosperity while cutting directly through an established residential area.", "公路可能带来地区繁荣，同时穿过成熟居住区。"),
("Noise, unsafe crossings, and polluted air then influence daily life far beyond the road itself.", "噪声、不安全过街和空气污染会影响远超道路本身的日常生活。"),
("Environmental reviews should examine social division as carefully as the physical environment.", "环境审查应像评估自然环境一样仔细评估社会分隔。"),
("Where a route damages access to a residence, planners should fund bridges, parks, and sound barriers.", "路线影响住宅通行时，规划者应资助天桥、公园和隔音设施。"),
("Transport investment is fair only when it repairs the local harm that wider economic gains create.", "只有修复更广泛经济收益造成的本地伤害，交通投资才算公平。")],
[("How can a highway divide a community?","Through noise, unsafe crossings, and lost access.","噪声、过街危险和通行受阻会割裂社区。"),("What repairs does the writer suggest?","Bridges, parks, and sound barriers.","作者建议建设天桥、公园和隔音设施。")] )],
17: [
article("The Pear beside the Graph", "story", ["graph","dairy","playground","calculate","classmate","pear"], [
("Niko placed a pear beside his graph during a school presentation about lunch waste.", "尼科在介绍午餐浪费的学校演讲中，把一只梨放在图表旁。"),
("His classmate had recorded how much fruit, bread, and dairy food pupils discarded each day.", "他的同学记录了学生每天丢弃多少水果、面包和乳制品。"),
("Together they used the weekly figures to calculate how many meals the waste could equal.", "他们用每周数据计算这些浪费相当于多少顿饭。"),
("Afterward, children carried uneaten whole fruit to a shared basket near the playground.", "之后，孩子们把未吃的完整水果放到操场旁的共享篮子。"),
("The lonely pear disappeared first, taken by a hungry student after football practice.", "那只孤零零的梨最先消失，被足球训练后一名饥饿的学生拿走了。")],
[("What did the graph measure?","Food discarded at lunch.","图表统计午餐时丢弃的食物。"),("Where was uneaten fruit placed?","In a basket near the playground.","未吃的水果被放在操场旁的篮子里。")] ),
article("Why Copper Carries Current", "explanatory", ["copper","include","radiation","pulse","mechanical","route"], [
("Copper contains electrons that can move easily when voltage creates an electrical push.", "铜含有在电压推动下能够轻易移动的电子。"),
("Their route through a wire is not perfectly smooth because atoms vibrate and resist the flow.", "电子穿过导线的路径并非完全顺畅，因为原子振动会阻碍流动。"),
("That resistance produces heat, a form of radiation that must be controlled in powerful equipment.", "这种电阻会产生热量，即一种在大功率设备中必须控制的辐射。"),
("Some cables include insulation and cooling around the copper core.", "一些电缆在铜芯周围加入绝缘层和冷却结构。"),
("Engineers may send a brief pulse through a damaged line and measure its return to locate a mechanical break.", "工程师可以向损坏线路发送短脉冲并测量其返回，以定位机械断点。")],
[("What creates heat in a copper wire?","Resistance to moving electrons.","电子运动受到的电阻会产生热。"),("How can engineers locate a break?","By sending and measuring a pulse.","通过发送并测量脉冲定位断点。")] ),
article("Sponsors Should Not Control School Sport", "opinion", ["sponsor","scheme","rent","class","humble","marriage"], [
("A business sponsor can pay equipment costs or rent a field that a school could not otherwise afford.", "企业赞助者可以支付器材费用或租用学校无力承担的场地。"),
("Problems begin when the funding scheme turns pupils into permanent advertisements.", "当资助方案把学生变成永久广告时，问题就出现了。"),
("Every class deserves access, including children whose families never buy the sponsor's products.", "每个班级都应获得参与机会，包括从不购买赞助商产品的家庭。"),
("Schools should remain humble about commercial gifts and publish all conditions attached to them.", "学校应谨慎看待商业赠款，并公开所有附加条件。"),
("Like a marriage, a long partnership works only when both sides respect clear boundaries.", "就像婚姻一样，长期合作只有在双方尊重清晰边界时才能维持。")],
[("What benefit can a sponsor provide?","Equipment or field rental.","赞助者可提供器材或场地租金。"),("What should schools publish?","All conditions attached to sponsorship.","学校应公开赞助的全部条件。")] )],
18: [
article("The Draft in the Drawer", "story", ["gardener","drawer","draft","mystery","cable","launch"], [
("A gardener clearing an abandoned office found a folded draft in a locked drawer.", "一名园丁清理废弃办公室时，在锁住的抽屉里发现一份折叠草稿。"),
("It described a plan to launch a public garden on the roof of the building.", "草稿描述了在楼顶建立公共花园的计划。"),
("The mystery deepened when a cable bill showed that someone still powered a pump upstairs.", "一张电缆账单显示仍有人给楼上的水泵供电，谜团更深了。"),
("Following the sound of water, she met a former cleaner quietly caring for hundreds of seedlings.", "她循着水声发现，一名前清洁工正默默照料数百株幼苗。"),
("Together they revived the forgotten proposal and opened the garden that summer.", "他们一起重启了被遗忘的方案，并在那个夏天开放花园。")],
[("What did the draft propose?","A public roof garden.","草稿计划建立公共屋顶花园。"),("Who had maintained the seedlings?","A former cleaner.","一名前清洁工一直照料幼苗。")] ),
article("How Steam Moves a Turbine", "explanatory", ["feasible","steam","shift","sophisticated","economical","monitor"], [
("A power station heats water until expanding steam rushes across curved turbine blades.", "发电站把水加热，直到膨胀的蒸汽冲过弯曲的涡轮叶片。"),
("The force drives sophisticated machinery that a generator uses to produce electricity.", "这股力量驱动复杂机械，发电机借此产生电力。"),
("Operators monitor temperature and pressure because a small shift can reduce efficiency or damage metal.", "操作人员监控温度和压力，因为微小变化会降低效率或损坏金属。"),
("Engineers also recover heat from outgoing vapor whenever the design makes that feasible.", "只要设计可行，工程师还会回收排出蒸汽中的热量。"),
("Reusing heat makes the plant more economical and lowers the amount of fuel required.", "重复利用热量能提高经济性，并减少所需燃料。")],
[("What rotates the turbine blades?","Expanding steam.","膨胀蒸汽推动涡轮叶片。"),("Why is recovered heat useful?","It saves fuel and money.","回收热量可以节省燃料和成本。")] ),
article("Busy Lives Still Need Leisure", "opinion", ["busy","mental","living","sophisticated","nobody","lately"], [
("Many people have lately used sophisticated apps to fill every free minute with work or self-improvement.", "最近，许多人用复杂应用把每一分钟空闲都填满工作或自我提升。"),
("A busy schedule can provide purpose, but constant measurement changes living into a list of targets.", "忙碌日程可以带来目标感，但持续量化会把生活变成目标清单。"),
("Unplanned leisure supports mental recovery because attention is allowed to wander without judgment.", "无计划的闲暇让注意力不受评判地游走，有助于心理恢复。"),
("Nobody should feel guilty for walking, talking, or resting without recording a result.", "任何人都不该因为散步、聊天或休息没有记录成果而内疚。"),
("Technology serves us best when it protects free time instead of occupying all of it.", "科技在保护自由时间而非占满它时，才最能为人服务。")],
[("What risk comes from measuring every minute?","Life becomes only a list of targets.","过度量化会让生活只剩目标清单。"),("Why is unplanned leisure helpful?","It supports mental recovery.","无计划闲暇有助于心理恢复。")] )],
19: [
article("Lightning over the Glasshouse", "story", ["aircraft","policeman","voyage","glass","crop","lightning"], [
("A small aircraft ended its coastal voyage early when lightning spread across the northern sky.", "一道闪电划过北方天空，一架小飞机提前结束了沿海航程。"),
("It landed beside farmland where broken glass from a damaged greenhouse covered the road.", "飞机降落在农田旁，受损温室的碎玻璃散落在道路上。"),
("A policeman stopped traffic while the pilot helped the farmer protect a young tomato crop.", "一名警察拦停交通，飞行员则帮助农民保护幼小的番茄作物。"),
("They stretched old sheets across the plants before heavy rain arrived.", "他们在大雨到来前把旧布铺在植物上方。"),
("By morning, the storm had passed, and the unexpected visitors stayed to clear the remaining glass.", "清晨风暴过去，意外来客们留下清理剩余玻璃。")],
[("Why did the aircraft land early?","Because of lightning and a storm.","飞机因雷暴提前降落。"),("What did the pilot help protect?","A young tomato crop.","飞行员帮助保护番茄幼苗。")] ),
article("Why Oil and Water Separate", "explanatory", ["oil","combine","inner","interaction","gradual","external"], [
("Water molecules have uneven electrical charges, while most oil molecules do not.", "水分子带有不均匀电荷，而大多数油分子没有。"),
("Water therefore prefers interaction with other water molecules instead of forming bonds with oil.", "因此，水更倾向于与其他水分子相互作用，而不是与油结合。"),
("Even vigorous shaking cannot combine the two liquids permanently.", "即使猛烈摇晃也无法让两种液体永久混合。"),
("Small drops may remain mixed for a while, but gradual movement brings each liquid back to its own layer.", "小液滴可能暂时混合，但缓慢运动会让两种液体各自恢复分层。"),
("Soap changes the boundary by giving each particle an oil-friendly inner end and a water-friendly external end.", "肥皂改变边界：每个粒子都有亲油的内端和亲水的外端。")],
[("Why does water avoid oil?","Its molecules prefer bonds with other water molecules.","水分子更愿意彼此结合。"),("How does soap help?","It connects to both oil and water.","肥皂分子两端分别亲油和亲水。")] ),
article("Farmers Need Honest Weather Risk", "opinion", ["announce","considerable","crop","prepare","suspicious","refrigerator"], [
("A weather service may hesitate to announce a storm when the forecast remains uncertain.", "天气服务机构可能因预报仍不确定而犹豫是否发布风暴消息。"),
("Yet farmers need time to prepare workers, equipment, and each vulnerable crop.", "但农民需要时间为工人、设备和易受损作物做好准备。"),
("A false alarm has a considerable cost, including wasted labor and unnecessary refrigerator use.", "误报会带来可观成本，包括浪费劳力和不必要使用冷藏设备。"),
("Silence can cost far more, and people become suspicious when uncertainty is hidden.", "沉默可能造成更大损失，而隐瞒不确定性会让人产生怀疑。"),
("Forecasters should publish probability and possible impact, allowing farmers to make their own informed choice.", "预报员应公布概率和可能影响，让农民自行作出知情选择。")],
[("What costs can a false alarm create?","Wasted labor and unnecessary cooling.","误报可能浪费劳力和冷藏成本。"),("What should forecasts publish?","Probability and possible impact.","预报应公布概率和潜在影响。")] )],
20: [
article("The Torch behind the Door", "story", ["inspect","door","isolate","torch","employee","mask"], [
("While staff inspect the factory, an employee noticed a weak light moving behind a sealed storage door.", "员工检查工厂时，一名员工发现封闭储藏门后有微弱灯光移动。"),
("She put on a protective mask and used a torch to read the warning label through a window.", "她戴上防护面罩，用手电筒透过窗户读取警示标签。"),
("Because spilled powder might be dangerous, the manager chose to isolate the entire corridor.", "由于泄漏粉末可能有危险，经理决定隔离整条走廊。"),
("Firefighters entered and found a cleaner who had been locked inside by a faulty handle.", "消防员进入后发现一名清洁工因门把手故障被锁在里面。"),
("The careful response saved him without spreading the unknown material through the building.", "谨慎的应对救出了他，也没有让未知物质扩散到整栋建筑。")],
[("Why was the corridor isolated?","There might be a dangerous powder spill.","可能存在危险粉末泄漏。"),("Who was behind the door?","A cleaner locked inside.","门后是一名被困的清洁工。")] ),
article("How a Tyre Holds Weight", "explanatory", ["tyre/","tube","stretch","condition","complicated","powder"], [
("The source list writes tyre/ with a final slash, a reminder that raw vocabulary data can contain noise.", "原始词表把 tyre/ 写成末尾带斜线的形式，提醒我们原始词汇数据可能含有杂质。"),
("A tyre supports a vehicle because compressed air pushes against the inner surface in every direction.", "轮胎能支撑车辆，是因为压缩空气向各个方向推压内表面。"),
("Rubber and fabric stretch slightly, spreading the load across the area touching the road.", "橡胶和织物略微伸展，把载荷分散到接触路面的区域。"),
("Some designs contain no separate tube, which makes sealing the rim more complicated.", "有些设计没有独立内胎，因此轮圈密封更加复杂。"),
("Pressure, heat, tread condition, and even fine road powder affect grip and safety.", "气压、温度、胎纹状况甚至细小路面粉尘都会影响抓地力与安全。")],
[("What spreads a vehicle's load?","Air pressure and the flexible tyre structure.","气压和可变形轮胎结构分散载荷。"),("What makes a tubeless design harder?","The rim must be sealed carefully.","无内胎设计要求轮圈严密密封。")] ),
article("Cheap Products Can Be Expensive", "opinion", ["cheap","brilliant","synthetic","diverse","complicated","belief"], [
("A cheap product can look brilliant in a shop yet fail after a few months of ordinary use.", "便宜商品在店里可能光鲜亮丽，却会在正常使用几个月后损坏。"),
("Synthetic materials are not automatically bad; many are durable, light, and easy to clean.", "合成材料并非天然不好，许多材料耐用、轻便且易清洁。"),
("The real problem is a complicated supply chain that hides repairability and working conditions.", "真正的问题是复杂供应链掩盖了可维修性和劳动条件。"),
("Consumers with diverse incomes still deserve clear information about expected life and replacement parts.", "收入不同的消费者都应获得关于预期寿命和替换零件的清晰信息。"),
("The belief that low price always saves money disappears when the same item must be bought repeatedly.", "当同一物品必须反复购买时，低价总能省钱的观念就站不住脚了。")],
[("Are synthetic materials always poor quality?","No; many are durable and useful.","合成材料并不必然质量差。"),("What information should buyers receive?","Expected life and available replacement parts.","买家应知道预期寿命和配件供应情况。")] )],
}


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for day, drafts in DATA.items():
        source = json.loads((WORD_DIR / f"day-{day:03}.json").read_text(encoding="utf-8"))
        words = {item["word"].casefold(): item for item in source["items"]}
        articles = []
        for number, draft in enumerate(drafts, 1):
            targets = []
            for word in draft["targets"]:
                if word.casefold() not in words:
                    raise ValueError(f"Day {day}: {word} 不在当天单词中")
                targets.append({"word": words[word.casefold()]["word"], "meaning": words[word.casefold()]["meaning"]})
            sentences = [{"en": en, "zh": zh} for en, zh in draft["pairs"]]
            articles.append({
                "id": f"cet4-reading-d{day:03}-{number}", "title": draft["title"], "type": draft["type"], "difficulty": "CET-4+",
                "text": " ".join(item["en"] for item in sentences), "translation": "".join(item["zh"] for item in sentences),
                "sentences": sentences, "target_words": targets,
                "questions": [{"prompt": q, "answer": a, "explanation": e} for q, a, e in draft["questions"]],
            })
        payload = {"schema_version": 1, "collection_id": "cet4_context_readings", "wordlist_id": "cet4_combined", "day": day, "articles": articles}
        (OUT_DIR / f"day-{day:03}.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    days = [{"day": day, "file": f"day-{day:03}.json", "count": 3} for day in sorted(DATA)]
    index = {"schema_version": 1, "id": "cet4_context_readings", "wordlist_id": "cet4_combined", "title": "四级词汇语境阅读", "description": "与单词库 Day 对应；每个 Day 包含故事、说明文和观点文各一篇，并支持逐句显示中文。", "tags": ["四级", "语境阅读", "逐句翻译"], "article_count": len(days) * 3, "day_count": len(days), "days": days}
    (OUT_DIR / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    manifest = {"schema_version": 1, "collections": [{"id": index["id"], "index": "cet4_combined/index.json"}]}
    (OUT_DIR.parent / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(days)} days / {len(days) * 3} articles")


if __name__ == "__main__":
    main()
