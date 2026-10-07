from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORD_DIR = ROOT / "content" / "wordlists" / "cet4_combined"
OUT_DIR = ROOT / "content" / "readings" / "cet4_combined"


def A(title, kind, targets, pairs, questions):
    return {"title": title, "type": kind, "targets": targets, "pairs": pairs, "questions": questions}


DATA = {
21: [
A("Signals Beside the Frozen Pond", "story", ["repeatedly","seek","calculator","fragment","arbitrary","cent","captain","sequence","track","confident"], [
("Captain Luo repeatedly called into the February darkness while his rescue team followed a narrow track beside the frozen pond.", "二月的黑夜里，罗队长反复呼喊，救援队沿着结冰池塘边的一条窄路前进。"),
("They had come to seek a missing surveyor whose calculator and a torn map fragment lay near a broken fence.", "他们来寻找一名失踪的测量员，围栏断口附近留着他的计算器和一块撕破的地图碎片。"),
("Instead of making an arbitrary turn, the captain studied the sequence of footprints and noticed a one-cent coin pressed into fresh mud.", "队长没有随意转弯，而是研究脚印的先后顺序，并发现一枚一分硬币陷在新泥里。"),
("That tiny sign led them to a shed, and the whole team felt confident when a weak voice answered from inside.", "这个微小的迹象把他们引到一间棚屋；里面传来微弱回应时，全队都确信找对了地方。")],
[("What objects did the team find near the fence?","A calculator and a map fragment.","围栏附近有计算器和地图碎片。"),("Why did the captain choose the path to the shed?","He followed the sequence of footprints and the coin.","他依据脚印顺序和硬币这一线索作出判断。")]),
A("When Evidence Changes a Decision", "explanatory", ["dying","pit","evaluate","effort","real","democracy","mostly","dissolve","february","undo"], [
("In February, a town planned to fill an old clay pit where reeds were dying and mostly stagnant water covered the ground.", "二月，一个小镇计划填平一处旧黏土坑；那里的芦苇正在枯死，积水覆盖了大部分地面。"),
("Engineers first had to evaluate whether the danger was real, so they measured the water and recorded wildlife after rain.", "工程师首先要评估危险是否真实存在，因此他们检测水质，并记录雨后的野生动物。"),
("The survey showed that a modest restoration effort could revive the wetland, whereas concrete would dissolve neither the pollution nor public concern.", "调查表明，适度的修复工作可以让湿地恢复，而浇筑混凝土既不能消除污染，也不能化解公众担忧。"),
("Local democracy allowed residents to review the evidence and undo the earlier decision before irreversible work began.", "当地的民主程序让居民审查证据，并在不可逆的工程开始前撤销了原决定。")],
[("What did the survey show?","Restoration could revive the wetland.","调查表明修复工作能够让湿地恢复。"),("How did residents affect the plan?","They reviewed the evidence and reversed the decision.","居民审查证据后推翻了原方案。")]),
A("Privacy Must Survive an Emergency", "opinion", ["pain","final","loud","private","reliable","dial","stimulate","communicate","hunt","upright"], [
("During a mountain rescue, a loud public appeal may stimulate useful reports, but it can also expose a family's private pain.", "山区救援时，大声公开呼吁可能带来有用线索，也可能暴露一个家庭的私人痛苦。"),
("Officials should communicate through one reliable channel and give witnesses a number they can dial without joining an online hunt for blame.", "官方应通过一个可靠渠道发布信息，并为目击者提供可拨打的号码，避免他们加入网络追责。"),
("An upright rescue service checks each claim before sharing it, even when reporters demand a final answer immediately.", "正直的救援机构会在发布前核实每条说法，即使记者要求立即给出最终答案。"),
("Speed matters, yet respect for victims should remain part of emergency practice rather than an obstacle to it.", "速度固然重要，但尊重受害者应当是应急工作的组成部分，而不是其障碍。")],
[("Why should officials use one reliable channel?","To reduce rumors and protect private information.","这样可以减少谣言并保护隐私。"),("What should happen before a claim is shared?","It should be checked.","信息发布前应当经过核实。")])],
22: [
A("The Fall in the Hay Barn", "story", ["sympathize","conscious","manner","spoil","require","magnificent","atomic","strengthen","surroundings","stair"], [
("At a magnificent old farm, Lena slipped on the last stair to a hay barn and struck her shoulder against the door.", "在一座美丽的老农场里，莉娜在通往干草仓的最后一级楼梯上滑倒，肩膀撞上了门。"),
("She remained conscious and described the accident in a calm manner, although every movement hurt.", "她仍然清醒，并以平静的方式讲述事故，尽管每次移动都会疼痛。"),
("Her friends wanted to sympathize by lifting her at once, but the dispatcher said the surroundings might require a safer method.", "朋友们想立刻扶起她表示关心，但调度员说周围环境可能需要更安全的处理方式。"),
("Waiting did not spoil the rescue; a rigid board helped strengthen her support, while a tiny atomic clock in the radio recorded each step of the response.", "等待没有耽误救援；硬板加强了支撑，而无线电里微小的原子钟记录了应对过程的每一步。")],
[("Where did Lena fall?","On the stair to the hay barn.","她在通往干草仓的楼梯上摔倒。"),("Why did her friends wait before moving her?","The surroundings required a safer method.","周围环境要求采用更安全的搬运方法。")]),
A("How the Body Returns to Alertness", "explanatory", ["elementary","shade","hay","duty","confidence","hurt","unique","beef","coordinate","bite"], [
("An elementary first-aid check begins with shade, fresh air, and a clear question to learn whether an injured person can answer.", "基础急救检查从阴凉处、新鲜空气和一个清楚的问题开始，以判断伤者能否回答。"),
("Pain from a bite or a fall may hurt badly, but helpers have a duty to observe breathing before offering water or food such as beef.", "咬伤或跌倒造成的疼痛可能很剧烈，但救助者有责任先观察呼吸，再决定是否给水或牛肉等食物。"),
("The brain has a unique task: it must coordinate balance, speech, memory, and movement as consciousness returns.", "大脑承担着独特任务：意识恢复时，它必须协调平衡、语言、记忆和动作。"),
("Simple responses build confidence, just as stacked hay bales need firm support rather than hopeful guessing.", "简单而稳定的反应能建立信心，就像堆放的干草捆需要牢固支撑，而不能依靠乐观猜测。")],
[("What should helpers observe before offering food?","The injured person's breathing.","救助者应先观察伤者的呼吸。"),("What does the brain coordinate as consciousness returns?","Balance, speech, memory, and movement.","大脑会协调平衡、语言、记忆与动作。")]),
A("Every Farm Needs a Poison Plan", "opinion", ["laugh","slender","van","dim","sleeve","beginning","cushion","vigorous","consciousness","equip"], [
("A slender warning label is easy to miss in a dim shed, especially when a chemical bottle rolls beneath a van seat.", "昏暗棚屋里，细小的警告标签很容易被忽略，尤其当化学品瓶滚到货车座位下面时。"),
("Farms should equip every vehicle with gloves, a protective sleeve, and a cushion that keeps containers upright from the beginning of a trip.", "农场应为每辆车配备手套、防护套和固定容器的软垫，从行程一开始就让容器保持直立。"),
("A worker who loses consciousness needs a vigorous emergency response, not a nervous laugh or an uncertain search for instructions.", "工人失去意识时需要有力的紧急处置，而不是紧张的笑声或临时翻找说明。"),
("Written plans, repeated drills, and visible labels turn poison control from a personal memory test into a shared safety system.", "书面方案、反复演练和醒目标识能把有毒物管理从个人记忆测试变成共同安全体系。")],
[("What equipment should farm vehicles carry?","Gloves, a protective sleeve, and a stabilizing cushion.","车辆应配备手套、防护套和固定软垫。"),("Why are written plans useful?","They create a shared safety system.","书面方案能建立共同的安全体系。")])],
23: [
A("Eleven Calls from the Forest", "story", ["comprehension","blast","cigarette","weave","equipment","manager","limited","vital","site","hate"], [
("A field manager at a remote forest site heard a blast and saw smoke weave between the pines just after sunset.", "日落后不久，一处偏远森林地点的现场经理听到爆响，看见烟雾在松树间穿行。"),
("The crew had limited equipment, but their map comprehension was vital because the nearest road curved around a steep ridge.", "队员的设备有限，但读图能力至关重要，因为最近的道路绕过一条陡峭山脊。"),
("They found that a discarded cigarette had ignited dry leaves near a storage box, something every worker had been taught to hate and prevent.", "他们发现一支被丢弃的香烟点燃了储物箱附近的干叶；每个工人都受过训练，要厌恶并防止这种行为。"),
("After eleven radio calls, firefighters reached the site and stopped a small accident from becoming a regional disaster.", "经过十一次无线电联络，消防员到达现场，阻止了一场小事故演变成区域灾难。")],
[("What started the fire?","A discarded cigarette.","火灾由一支被丢弃的香烟引起。"),("Why was map comprehension vital?","The access road curved around a ridge.","进场道路绕过山脊，因此读图很重要。")]),
A("Why Dosage Instructions Need Precision", "explanatory", ["new","forest","executive","outside","eleven","no","inform","volume","cover","naval"], [
("A new medicine label must inform patients exactly how much liquid to take, because a line marking eleven millilitres is not the same as a full spoon.", "新药标签必须准确告知患者服用多少液体，因为十一毫升的刻线不等于满满一勺。"),
("The stated volume should cover children and adults separately, with no assumption that body size follows a simple rule.", "标明的剂量应分别涵盖儿童和成人，不能假定体型遵循简单规则。"),
("Outside a hospital, clear wording matters as much as it does on a naval vessel or at an isolated forest station.", "在医院之外，清楚的说明同样重要，无论是在军舰上还是偏远森林站。"),
("An executive may approve the package, but pharmacists and patients should test whether ordinary readers can understand it under pressure.", "管理人员可以批准包装，但药师和患者应测试普通读者能否在压力下理解说明。")],
[("Why are children and adults listed separately?","Their safe doses may differ.","儿童与成人的安全剂量可能不同。"),("Who should test the wording?","Pharmacists and patients.","药师和患者应参与测试说明文字。")]),
A("Smoke-Free Entrances Are Reasonable", "opinion", ["gentle","hello","invite","laundry","wicked","lose","universal","probably","forty","May"], [
("A gentle sign saying hello should invite visitors into a building, not force them through cigarette smoke beside the door.", "写着“你好”的温和标牌应欢迎访客进入建筑，而不是迫使他们穿过门口的烟雾。"),
("Smoke-free entrances should become a universal rule for schools, clinics, and even a neighborhood laundry.", "无烟入口应成为学校、诊所乃至社区洗衣店的普遍规则。"),
("The policy is not a claim that smokers are wicked; it simply recognizes that others may lose clean air during the first forty steps of a visit.", "这项政策不是说吸烟者邪恶，而只是承认其他人可能在进门的前四十步失去清洁空气。"),
("A marked smoking area will probably work better than punishment, and a review each May can reveal whether the arrangement remains fair.", "划定吸烟区可能比惩罚更有效，每年五月进行审查则能看出安排是否仍然公平。")],
[("What places should have smoke-free entrances?","Schools, clinics, laundries, and other public buildings.","学校、诊所、洗衣店等公共建筑都应设无烟入口。"),("What alternative to punishment does the writer suggest?","A clearly marked smoking area.","作者建议设置标识清楚的吸烟区。")])],
24: [
A("The Violin Case in the Mirror", "story", ["mirror","beer","willing","popular","luck","missing","upset","concert","gross","fleet"], [
("After a popular harbor concert, Niko noticed in a café mirror that his violin case was missing from the chair behind him.", "一场受欢迎的港口音乐会结束后，尼科从咖啡馆的镜子里发现身后的椅子上少了小提琴盒。"),
("He was upset and feared that bad luck had followed him from the stage, where a spilled beer had already stained his coat.", "他很不安，担心坏运气从舞台一路跟来；此前洒出的啤酒已经弄脏了他的外套。"),
("A waiter was willing to check the gross receipts and camera record while sailors from a nearby fleet searched the pavement.", "一名服务员愿意查看总收入记录和监控，附近舰队的水手则在路面寻找。"),
("They found the case under a delivery cart, moved there by staff who had cleared the crowded doorway.", "他们在送货车下找到了琴盒；工作人员清理拥挤门口时把它移到了那里。")],
[("How did Niko notice the missing case?","He saw the empty chair in a mirror.","他从镜子中看到椅子空了。"),("Where was the violin case found?","Under a delivery cart.","琴盒在送货车下面被找到。")]),
A("Reading a Volcano's Small Movements", "explanatory", ["opportunity","weakness","desirable","urge","likewise","professional","deposit","movement","accelerate","estimate"], [
("A volcano gives scientists an opportunity to study how pressure changes beneath the ground long before an eruption.", "火山让科学家有机会研究喷发前很久地下压力如何变化。"),
("A professional team measures each small movement and examines mineral deposit patterns that may reveal a weakness in the rock.", "专业团队测量每一次微小移动，并检查可能显示岩石薄弱处的矿物沉积形态。"),
("Gas output can accelerate suddenly; temperature may likewise rise, yet no single signal provides a desirable estimate on its own.", "气体排放可能突然加速，温度也可能同样升高，但任何单一信号都不能独立给出理想估计。"),
("Officials must resist the urge to announce certainty and instead compare several instruments across time.", "官员必须克制宣布确定结论的冲动，而应比较多种仪器在一段时间内的数据。")],
[("What can mineral deposits reveal?","A weakness in the rock.","矿物沉积可以显示岩石薄弱处。"),("Why should several instruments be compared?","No single signal gives a reliable estimate.","单一信号无法给出可靠估计。")]),
A("A Film Title Should Tell the Truth", "opinion", ["erect","optional","volcano","brother","exit","pronunciation","movie","tempt","could","gather"], [
("A movie title could tempt a large audience with the word volcano even when the story is mainly about one brother running a hotel with his sibling.", "即使故事主要讲兄弟俩经营旅馆，电影标题也可能用“火山”一词吸引大量观众。"),
("Marketing teams may erect dramatic posters near every exit and treat accurate pronunciation of a foreign place name as optional.", "营销团队可能在每个出口附近竖起夸张海报，并把外国地名的准确发音当成可有可无。"),
("Such promotion can gather attention quickly, but disappointed viewers will remember the gap between the promise and the film.", "这种宣传能迅速聚集关注，但失望的观众会记住承诺与影片之间的差距。"),
("Creative titles are welcome when they express the movie's central conflict instead of borrowing danger that never appears.", "只要标题表达电影的核心冲突，而不是借用从未出现的危险，创意标题就值得欢迎。")],
[("Why might viewers feel disappointed?","The title promises danger that the film does not show.","标题承诺了影片中并未出现的危险。"),("When does the writer support creative titles?","When they reflect the central conflict.","当标题反映核心冲突时，作者支持创意表达。")])],
25: [
A("Music at the Last Harvest", "story", ["inhabitant","harvest","settle","contemporary","stove","review","musician","peasant","concentrate","advance"], [
("Every inhabitant of the valley gathered after the final harvest to hear a contemporary musician perform in an old grain hall.", "最后一次收获后，山谷里的居民都聚到旧粮仓，听一位当代音乐家演出。"),
("Mara, the daughter of a peasant family, placed a small stove near the entrance and asked children to settle before the first song.", "出身农民家庭的玛拉在入口附近放了一只小炉子，并让孩子们在第一首曲子前安静坐好。"),
("The audience had to concentrate as the music began to advance from a single quiet note to the rhythm of machines and rain.", "观众必须集中注意力，因为音乐从一个安静音符推进到机器与雨水的节奏。"),
("In a later review, a visitor wrote that the performance connected modern life with the labor behind every crop.", "一位访客后来在评论中写道，这场演出把现代生活与每一茬作物背后的劳动联系起来。")],
[("Where did the performance take place?","In an old grain hall.","演出在一座旧粮仓里举行。"),("What did the music connect?","Modern life and agricultural labor.","音乐连接了现代生活与农业劳动。")]),
A("Why Fire Needs Oxygen", "explanatory", ["whip","inherit","compute","suspect","thrive","ray","carpet","largely","farewell","insist"], [
("A flame can whip sideways in a draft because hot gas rises and fresh oxygen moves toward the burning material.", "火焰会在气流中猛然偏向一侧，因为热气上升，新鲜氧气流向燃烧材料。"),
("Researchers compute the rate of burning with sensors and suspect poor ventilation when smoke spreads largely across the ceiling like a dark carpet.", "研究人员用传感器计算燃烧速度；当烟雾像黑色地毯一样大面积铺满天花板时，他们会怀疑通风不良。"),
("A narrow ray of light can reveal that moving smoke, while plants that thrive after a fire may inherit space cleared by the heat.", "一束窄光可以显现流动的烟，而火后茁壮生长的植物可能获得高温清出的空间。"),
("Safety teachers insist that people say farewell to possessions and leave immediately rather than return through toxic smoke.", "安全教师坚持认为，人们应舍弃财物立即离开，而不是穿过有毒烟雾返回。")],
[("Why can a flame bend in a draft?","Moving oxygen feeds the fire from one side.","流动的氧气从一侧助燃，使火焰偏转。"),("What should people do during a fire?","Leave possessions and exit immediately.","人们应放下财物并立即撤离。")]),
A("Farm Policy Should Reward Resilience", "opinion", ["policy","depress","switch","brown","oxygen","merely","hungry","trumpet","lady","bottle"], [
("A good farm policy should not merely reward the largest harvest while smaller growers remain hungry for stable income.", "良好的农业政策不应只奖励最大收成，而让小种植户仍渴望稳定收入。"),
("When drought turns fields brown and can depress production, farmers need support to switch crops, protect soil oxygen, and store water in every available bottle or tank.", "干旱使田地变黄并压低产量时，农民需要支持来更换作物、保护土壤氧气，并把水储存在可用瓶罐或水箱中。"),
("A minister may trumpet one successful scheme beside a well-dressed lady at a fair, but a photograph cannot measure resilience.", "部长可能在展会上站在衣着得体的女士旁，大力宣传一项成功计划，但照片无法衡量韧性。"),
("Funding should follow long-term soil health, reliable household food, and evidence that farms can withstand another dry season.", "资金应依据长期土壤健康、家庭粮食保障，以及农场能否承受下一个旱季的证据来分配。")],
[("What should policy help farmers do during drought?","Change crops, protect soil, and store water.","政策应帮助农民换种、护土并储水。"),("What should determine funding?","Long-term resilience and food security.","资金应由长期韧性和粮食保障决定。")])],
}

DATA.update({
26: [
A("The Midnight Radio Library", "story", ["nod","lead","dictation","eighteen","panel","hat","pencil","utter","radio","judgement"], [
("At midnight, a radio presenter invited eighteen students into the town library for a live dictation contest.", "午夜，一名电台主持人邀请十八名学生来到镇图书馆参加直播听写比赛。"),
("Each contestant received a pencil and a paper hat, while a glass panel separated the studio from the reading room.", "每位参赛者都拿到一支铅笔和一顶纸帽，玻璃隔板把演播室与阅览室分开。"),
("When the lead reader began to utter unfamiliar words, one nervous child looked up and saw his teacher nod calmly.", "领读者开始念出生词时，一个紧张的孩子抬头看见老师平静地点头。"),
("The judges valued careful listening over speed, a judgement that turned the unusual broadcast into a lesson about patience.", "评委重视认真倾听而非速度；这一判断让这次特别广播成了一堂耐心课。")],
[("How many students joined the contest?","Eighteen.","共有十八名学生参赛。"),("What did the judges value?","Careful listening over speed.","评委更重视认真倾听。")]),
A("From Fibre to Strong Cloth", "explanatory", ["breath","pie","library","line","restrict","adequate","basically","import","basketball","improvement"], [
("A fibre is basically a thin line of material, yet thousands of fibres can form cloth strong enough for a basketball shoe.", "纤维基本上是一条细材料，但成千上万条纤维可以构成足够结实的篮球鞋面料。"),
("Natural fibres must allow adequate airflow so that heat and each breath of moisture can leave the skin.", "天然纤维必须允许充分通风，让热量和每一缕湿气离开皮肤。"),
("Manufacturers may import special threads, but a local library of samples helps them restrict waste and compare durability.", "制造商可以进口特殊线材，但本地样品库能帮助他们限制浪费并比较耐用性。"),
("Even a pie-shaped test patch can reveal an improvement when its woven directions respond differently to pressure.", "即使是一块馅饼形测试布，也能通过不同编织方向对压力的反应显示改进。")],
[("Why must cloth allow airflow?","To release heat and moisture.","布料要释放热量和湿气。"),("What can a test patch reveal?","Whether the fabric has improved.","测试布能显示面料是否得到改进。")]),
A("A Railway Is More Than a Track", "opinion", ["blow","objective","bake","harmony","dash","let","implication","railway","fibre","plane"], [
("A railway plan drawn on a flat plane may look objective, but each straight line has an implication for the community it crosses.", "画在平面上的铁路方案看似客观，但每一条直线都会对沿线社区产生影响。"),
("Fast trains dash past homes, their noise can blow across fields, and vibration may disturb ovens where small businesses bake food.", "高速列车从住宅旁疾驰，噪声吹过田野，震动还可能影响小店烘烤食品的炉具。"),
("Planners should let residents discuss bridges, paths, and the fibre of neighborhood life before fixing the route.", "规划者应让居民在确定路线前讨论桥梁、道路和社区生活的内在联系。"),
("Real harmony comes from changing a design when local evidence is strong, not from asking everyone to accept a finished map.", "真正的和谐来自在地方证据充分时修改设计，而不是要求所有人接受一张定稿地图。")],
[("What may trains disturb besides homes?","Fields and small food businesses.","列车还可能影响田野和小型食品商户。"),("How can planners create harmony?","By consulting residents and changing the route when needed.","规划者应听取居民意见并在必要时调整路线。")])],
27: [
A("The Measure That Stopped the Line", "story", ["in","lag","pity","centre","patience","banana","remedy","measurement","grammatical","treat"], [
("In a packaging factory, a conveyor began to lag whenever a banana box reached the centre sensor.", "在一家包装厂里，每当香蕉箱到达中央传感器时，传送带就开始变慢。"),
("The supervisor resisted the temptation to treat the delay as bad luck and asked for a precise measurement of every box.", "主管没有把延误当成倒霉，而是要求精确测量每个箱子。"),
("With patience, a technician found that one label contained a grammatical error that made the scanner expect the wrong size.", "技术员耐心检查后发现，一张标签存在语法错误，导致扫描器预期了错误尺寸。"),
("It was a pity to stop the line, but correcting the code was a cheap remedy that prevented a much larger breakdown.", "停线很可惜，但修正代码是便宜的补救办法，并防止了更大的故障。")],
[("What caused the conveyor to slow?","A label error made the scanner expect the wrong size.","标签错误让扫描器预期了错误尺寸。"),("Why was stopping the line worthwhile?","It prevented a larger breakdown.","停线避免了更严重的故障。")]),
A("Measuring Height Without Climbing", "explanatory", ["scissors","command","justice","military","type","fashion","own","big","export","glove"], [
("A surveyor can estimate a big tower's height by comparing its shadow with the shadow of a pole of known length.", "测量员可以把高塔的影子与已知长度杆子的影子比较，从而估算塔高。"),
("This type of geometry once served military mapping, but students can test it with their own ruler, glove, or upright stick.", "这种几何方法曾用于军事制图，但学生可以用自己的尺子、手套或直立木棍来测试。"),
("The method does not command perfect weather; it needs clear sunlight and careful timing rather than equipment chosen for fashion, such as laser scissors.", "这种方法并不要求完美天气；它需要清晰阳光和准确计时，而不是激光剪刀之类时髦设备。"),
("Openly sharing the calculation supports scientific justice, because anyone can examine it before the result is used in an export project.", "公开计算过程有助于科学公正，因为结果用于出口项目之前，任何人都能检查。")],
[("What two shadows are compared?","The tower's shadow and a pole's shadow.","比较高塔与已知杆子的影子。"),("What conditions does the method need?","Clear sunlight and careful timing.","这种方法需要清晰阳光和准确计时。")]),
A("Export Growth Should Not Hide Waste", "opinion", ["deck","grant","phase","tremble","anxious","faint","geometry","height","native","consume"], [
("During the first phase of an export boom, a factory deck may tremble under heavier machines while nearby families grow anxious about noise.", "出口繁荣的第一阶段，厂房平台可能在更重的机器下震动，附近家庭则对噪声感到焦虑。"),
("A government grant can raise output to a new height, yet it should also fund cleaner geometry for workspaces and safer routes for trucks.", "政府补助可以把产量推到新高度，但也应资助更合理的工作空间布局和更安全的货车路线。"),
("Native plants may fade under dust, and workers may feel faint if factories consume air, water, and attention faster than they recover.", "本地植物可能因灰尘而衰败；如果生产消耗空气、水和注意力的速度超过恢复速度，工人也可能头晕。"),
("Trade deserves support only when its visible profit includes the cost of protecting health and place.", "只有当可见利润包含保护健康与地方环境的成本时，贸易才值得支持。")],
[("What concerns may accompany an export boom?","Noise, dust, unsafe traffic, and worker health.","出口增长可能伴随噪声、灰尘、交通与健康问题。"),("When does the writer support trade?","When profit accounts for health and environmental protection.","利润计入健康与环境保护成本时才应支持贸易。")])],
28: [
A("A Proposal in the Rain", "story", ["tailor","yawn","admit","proposal","eighth","dear","participate","or","rainy","mutual"], [
("On a rainy evening, an elderly tailor climbed to the eighth floor to present a proposal for repairing the community hall.", "一个雨夜，一位年长裁缝爬到八楼，提出修缮社区礼堂的建议。"),
("Several residents began to yawn, but he had to admit that his dear old building needed more than fresh curtains or paint.", "几位居民开始打哈欠，但他承认，这座珍爱的老建筑需要的不只是新窗帘或油漆。"),
("He asked every tenant to participate by listing one skill, from wiring to budgeting, that could serve their mutual goal.", "他请每位住户参与，列出一项能服务共同目标的技能，从布线到预算都可以。"),
("The room became lively as people discovered that shared work could make the plan affordable and keep the hall open.", "大家发现共同劳动能让方案负担得起并保住礼堂，房间里顿时活跃起来。")],
[("Why did the tailor visit the eighth floor?","To present a repair proposal.","他去八楼提出修缮方案。"),("How could tenants participate?","By contributing a useful skill.","住户可以贡献一项有用技能。")]),
A("What Organic Farming Changes", "explanatory", ["extensive","record","adapt","apart","cup","claw","drip","generator","substantial","afterward"], [
("An organic farm keeps an extensive record of soil, insects, weather, and each cup of water used on a test plot.", "有机农场会详细记录土壤、昆虫、天气以及试验田使用的每一杯水。"),
("Drip irrigation keeps roots moist while leaving leaves apart from wet soil, where a beetle's claw may carry disease.", "滴灌保持根部湿润，同时让叶片远离湿土，因为甲虫的爪可能传播病害。"),
("A solar generator can power pumps, but farmers must adapt planting dates before they expect a substantial change in yield.", "太阳能发电机可以为水泵供电，但农民必须调整播种日期，之后才能期待产量显著变化。"),
("Afterward, several seasons of records show whether the new system improved soil rather than merely changing a label.", "随后，数个季节的记录会显示新体系是否真正改善土壤，而不只是换了标签。")],
[("Why are leaves kept away from wet soil?","To reduce the spread of disease.","这样可以减少病害传播。"),("How can farmers judge the system?","By comparing records across several seasons.","农民可比较多个季节的记录来判断。")]),
A("Villages Need Reliable Local Power", "opinion", ["organic","stir","conquest","investigate","rural","lucky","vehicle","communist","provide","cloudy"], [
("A rural clinic should not depend on being lucky enough to have a clear day whenever it must charge a medical vehicle.", "乡村诊所不应依赖好运，不能只有晴天才能给医疗车辆充电。"),
("Solar panels can provide clean power, while an organic fuel system may help during cloudy weeks, but both require storage and repair skills.", "太阳能板可以提供清洁电力，有机燃料系统则可在多云数周时帮忙，但两者都需要储能和维修技能。"),
("Communities should investigate ownership openly; a generator must not become a political conquest claimed by a communist group or any other party.", "社区应公开调查所有权；发电机不应成为某个共产党组织或任何其他政党争夺的政治战利品。"),
("Local committees can stir debate, test costs, and choose a mixed system that keeps essential services running.", "地方委员会可以推动讨论、检验成本，并选择保障基本服务运转的混合系统。")],
[("Why is solar power alone sometimes insufficient?","Cloudy periods reduce its output.","多云时期会降低太阳能产出。"),("Who should decide how local power is owned?","The community through an open process.","社区应通过公开程序决定所有权。")])],
29: [
A("The Exhibit That Carried a Load", "story", ["passage","correspond","manufacture","page","engineering","exhibit","upward","generate","injury","born"], [
("For an engineering exhibit, three students built a bridge from paper and recorded its manufacture on every page of a notebook.", "为了工程展览，三名学生用纸造了一座桥，并在笔记本的每一页记录制造过程。"),
("The bridge had to carry weights through a narrow passage while cameras watched its centre bend upward and downward.", "纸桥必须在狭窄通道中承受重物，摄像机记录桥中央上下弯曲。"),
("Their measurements did not correspond at first, because one sensor began to generate heat and produced a false reading that could have caused an injury.", "起初测量结果互不对应，因为一个传感器发热并产生错误读数，可能导致人员受伤。"),
("The final design was born from that failure: they moved the sensor, repeated the test, and explained the mistake beside the exhibit.", "最终设计从这次失败中诞生：他们移动传感器、重做试验，并在展品旁解释错误。")],
[("What material was the bridge made from?","Paper.","桥由纸制成。"),("How did the students fix the false reading?","They moved the hot sensor and repeated the test.","他们移动发热传感器并重新测试。")]),
A("Why Turbine Blades Have a Shape", "explanatory", ["load","trial","conductor","beg","density","goose","chance","considerate","east","live"], [
("A turbine blade turns when moving air places a different load on its curved and flatter surfaces.", "当流动空气在叶片弯曲面与较平表面施加不同载荷时，涡轮叶片就会转动。"),
("Engineers run a live trial with smoke so they can see where air changes direction instead of leaving performance to chance.", "工程师用烟雾进行现场试验，以观察空气在哪里转向，而不是把性能交给偶然。"),
("Air density changes with temperature, so a design for an east coast may behave differently inland; even a passing goose becomes a safety factor.", "空气密度随温度变化，因此为东海岸设计的设备在内陆可能表现不同；甚至飞过的鹅也会成为安全因素。"),
("A considerate site manager will not beg a conductor to ignore vibration, because the electrical and mechanical systems must be tested together.", "体谅他人的现场经理不会恳求负责人忽略振动，因为电气与机械系统必须一起测试。")],
[("What makes a turbine blade turn?","Unequal air pressure on its surfaces.","叶片两侧不均等的空气作用力使其转动。"),("Why does location affect design?","Air density and local conditions differ.","不同地点的空气密度和环境条件不同。")]),
A("Manufacturing Needs Honest Risk Maps", "opinion", ["unconscious","lane","typist","conservative","diagram","logical","house","desk","turbine","bed"], [
("A logical safety diagram should show more than the shortest lane between a desk and the factory door.", "合乎逻辑的安全图不应只显示办公桌到工厂门口的最短通道。"),
("It must mark turbine noise, chemical storage, every emergency bed, and places where an unconscious worker could be hidden behind machinery.", "它必须标出涡轮噪声、化学品存放处、急救床位，以及昏迷工人可能被机器遮挡的位置。"),
("A conservative manager may keep the old plan because a typist has already printed copies for every house, but convenience is weak evidence.", "保守的经理可能因打字员已为每栋房屋打印副本而保留旧方案，但方便并不是有力证据。"),
("Workers who use the floor daily should revise the map, test each route, and record hazards that managers cannot see from an office.", "每天使用车间的工人应修改地图、测试每条路线，并记录管理者在办公室看不到的危险。")],
[("What hazards should a safety map show?","Noise, chemicals, emergency beds, and hidden areas.","安全图应显示噪声、化学品、急救床位和遮挡区域。"),("Who should help revise the map?","Workers who use the factory floor.","日常在车间工作的员工应参与修改。")])],
30: [
A("Fourteen Minutes of Silence", "story", ["outline","blue","variation","dead","peace","receiver","shot","explosive","embarrass","spacecraft"], [
("The control room turned blue on its screens when a spacecraft receiver stopped sending data fourteen minutes before landing.", "着陆前十四分钟，宇宙飞船接收器停止发送数据，控制室屏幕变成蓝色。"),
("A dead channel could mean an explosive failure, yet the flight director followed the emergency outline and refused to guess.", "失效信道可能意味着爆炸性故障，但飞行主管依照应急提纲，没有贸然猜测。"),
("The discovery did not embarrass the engineer for long: a small variation in software timing had blocked every second shot of information.", "一名工程师发现软件计时的微小变化阻断了每第二组信息，因而感到尴尬。"),
("She reset the link, data returned, and the room held its peace until the craft landed safely.", "她重置连接，数据随即恢复；直到飞船安全着陆，控制室一直保持安静。")],
[("What interrupted the data?","A small software timing variation.","软件计时的微小变化中断了数据。"),("Why did the team remain quiet?","They were waiting for a safe landing.","他们在等待飞船安全着陆。")]),
A("Nitrogen Is Useful and Dangerous", "explanatory", ["complaint","fourteen","broad","chimney","stranger","possess","latter","defeat","separate","on"], [
("Nitrogen makes up a broad share of air, but a person cannot notice when it pushes oxygen out of a closed room.", "氮气占空气很大比例，但当它在密闭房间排挤氧气时，人无法察觉。"),
("A factory may possess fourteen cylinders for cooling; the latter danger appears when a leaking tank stands near a low chimney or basement.", "工厂可能拥有十四只冷却气瓶；当泄漏气瓶位于低烟囱或地下室附近时，后一种危险就会出现。"),
("A headache complaint from a stranger should be taken seriously, and people must stay on the safe side of a barrier.", "陌生人诉说头痛也应受到重视，人们必须留在隔离带安全一侧。"),
("Ventilation and separate oxygen alarms can defeat the invisible hazard before anyone enters to investigate.", "通风与独立氧气警报器可以在人员进入调查前消除这种看不见的危险。")],
[("Why is a nitrogen leak hard to notice?","Nitrogen has no obvious warning and can displace oxygen.","氮气没有明显警示，却会排挤氧气。"),("What equipment reduces the risk?","Ventilation and separate oxygen alarms.","通风设备与独立氧气报警器可降低风险。")]),
A("Safety Approval Must Be Independent", "opinion", ["withdraw","nitrogen","theoretical","crush","creative","approve","clothe","bath","thoughtful","from"], [
("A theoretical safety model may look impressive, but regulators should not approve an explosive plant from diagrams alone.", "理论安全模型可能看起来很出色，但监管者不应只凭图纸批准爆炸物工厂。"),
("Independent inspectors must test nitrogen alarms, examine whether emergency suits can clothe workers safely, and see if a safety bath is reachable.", "独立检查员必须测试氮气警报器，检查应急服能否保护工人，并确认安全淋浴是否可达。"),
("A thoughtful company will withdraw a weak design before machinery can crush a worker, then invite creative alternatives from the people on site.", "周到的公司会在机器可能压伤工人前撤回薄弱设计，并邀请现场人员提出有创意的替代方案。"),
("Approval is credible only when evidence comes from reviewers who do not profit from a rapid launch.", "只有证据来自不会因快速投产获利的审查者，批准才可信。")],
[("What should inspectors test?","Alarms, protective clothing, and emergency baths.","检查员应测试警报器、防护服和安全淋浴。"),("When is approval credible?","When independent reviewers examine real evidence.","独立审查者核查实际证据时，批准才可信。")])],
})

DATA.update({
31: [
A("The Garden Above the Hospital", "story", ["ground","it","devil","collective","loss","invest","possibility","retire","hospital","intermediate"], [
("When a city hospital proposed a garden above its intermediate care floor, some officials called it an expensive possibility.", "一家市医院提议在中级护理楼层上方建花园时，一些官员认为这只是昂贵的设想。"),
("A nurse about to retire argued that patients needed contact with the ground and seasons after months of collective loss.", "一名即将退休的护士认为，在共同经历数月失落后，患者需要接触土地和四季。"),
("The devil was in the engineering details: soil weight, drainage, and safe access all required the hospital to invest carefully.", "难点藏在工程细节中：土壤重量、排水和安全通行都要求医院谨慎投资。"),
("It opened a year later, and families used the quiet space to talk beyond the sound of medical machines.", "一年后花园开放，家属们在这片安静空间里交谈，暂时远离医疗机器的声音。")],
[("Who first defended the garden idea?","A nurse who was about to retire.","一名即将退休的护士支持这个想法。"),("What engineering issues had to be solved?","Soil weight, drainage, and safe access.","需要解决土壤重量、排水和安全通行问题。")]),
A("How Crystals Take Shape", "explanatory", ["block","crystal","firm","guide","headquarters","everything","conclude","number","frequent","freedom"], [
("A crystal grows when a large number of atoms join a repeating pattern instead of settling with complete freedom.", "大量原子按重复图案结合，而不是完全自由地排列时，晶体就会生长。"),
("Temperature and concentration guide the pattern; frequent disturbance can block growth or produce many small forms.", "温度与浓度引导这种图案；频繁扰动会阻碍生长，或形成许多小晶体。"),
("In a firm research headquarters, scientists change one condition at a time because everything from dust to vibration may affect the result.", "在严谨的研究总部，科学家一次只改变一个条件，因为从灰尘到振动的一切都可能影响结果。"),
("They conclude that structure matters only after images and measurements agree across repeated experiments.", "只有图像与测量在重复实验中一致时，他们才得出结构规律的结论。")],
[("What guides a crystal's pattern?","Temperature and concentration.","温度和浓度引导晶体图案。"),("Why do scientists change one condition at a time?","Many factors can affect growth.","因为许多因素都会影响晶体生长。")]),
A("Retirement Should Include Real Choice", "opinion", ["impressive","candidate","performance","elsewhere","fifty","fit","except","comfort","perfect","lodge"], [
("An impressive retirement village may advertise a perfect lodge, regular concerts, and comfortable rooms to anyone over fifty.", "一座亮眼的退休社区可能向五十岁以上的人宣传完美小屋、定期音乐会和舒适房间。"),
("Yet each candidate should ask whether the place can fit changing health needs and whether family may stay overnight.", "但每位申请者都应询问这里能否适应不断变化的健康需求，以及家人能否留宿。"),
("Good performance figures mean little if they exclude residents who left for care elsewhere or if every service except basic comfort costs extra.", "如果数据排除了去别处接受护理的住户，或除基本舒适外每项服务都额外收费，再好的业绩数字也意义有限。"),
("Older people deserve clear contracts and the freedom to compare ownership, rental, and community options before deciding.", "老年人在决定前应获得清楚合同，并能自由比较产权、租赁与社区等选择。")],
[("What should candidates ask about?","Changing care needs, family visits, and extra costs.","申请者应询问护理变化、家属探访和额外收费。"),("Why may performance figures mislead?","They may omit residents who left for care.","数据可能漏掉已经离开接受护理的住户。")])],
32: [
A("The Dragon Under the Plaster", "story", ["influential","mend","fortnight","just","procession","manual","rapid","draw","dragon","breeze"], [
("An influential merchant paid workers to mend a cracked wall before the spring procession passed through the old district.", "一位有影响力的商人出资，让工人在春季游行经过老城区前修补开裂墙面。"),
("The manual repair seemed routine until a rapid scrape of plaster revealed the painted eye of a dragon.", "手工修复看似普通，直到快速刮去一层灰泥后露出一只彩绘龙眼。"),
("For a fortnight, conservators worked in a light breeze, using photographs to draw the missing pattern without inventing detail.", "接下来的两周，修复师在微风中工作，借助照片勾画缺失图案，不凭空添加细节。"),
("They finished just before the parade, and people slowed beneath the recovered mural instead of rushing past it.", "他们恰在游行前完工，人们在恢复的壁画下放慢脚步，不再匆匆走过。")],
[("What did workers discover?","A painted dragon beneath the plaster.","工人在灰泥下发现了一条彩绘龙。"),("How did conservators avoid inventing details?","They used photographs as evidence.","他们用照片作为依据。")]),
A("How Emergency Networks Recover", "explanatory", ["remind","furnish","niece","explore","attach","possible","overcoat","disturb","recovery","innocent"], [
("An emergency network can attach a temporary antenna to a vehicle and furnish power from a portable battery.", "应急网络可以把临时天线装到车辆上，并由便携电池供电。"),
("Teams first explore which towers remain possible to use, taking care not to disturb damaged structures or innocent residents nearby.", "团队先探查哪些通信塔还能使用，同时注意不扰动受损结构，也不打扰附近无辜居民。"),
("A simple card may remind volunteers to carry an overcoat, spare cable, water, and the phone number of a relative such as a niece.", "一张简单卡片可以提醒志愿者携带大衣、备用电缆、水，以及侄女等亲属的电话号码。"),
("Recovery becomes faster when equipment, people, and messages have several routes rather than one fragile centre.", "设备、人员与消息拥有多条路线而非一个脆弱中心时，恢复会更快。")],
[("What can power a temporary antenna?","A portable battery.","便携电池可以为临时天线供电。"),("Why should networks have several routes?","One route may fail in an emergency.","紧急情况下单一路线可能失效。")]),
A("Historic Streets Can Serve Daily Life", "opinion", ["crime","fortunately","cousin","leisure","hard","extra","gap","relate","fate","faith"], [
("Preserving a historic street becomes hard when officials relate every broken window to crime and every repair to tourism.", "当官员把每扇破窗都与犯罪联系、把每次维修都与旅游挂钩时，保护历史街道就变得困难。"),
("Fortunately, a neighborhood is not a museum: a cousin may visit, children need leisure space, and residents carry extra shopping home.", "幸运的是，社区不是博物馆：表亲会来访，孩子需要休闲空间，居民还要把额外采购带回家。"),
("A gap between heritage rules and daily needs can decide the fate of a building by making ordinary maintenance impossible.", "遗产规定与日常需要之间的差距可能让普通维护无法进行，从而决定建筑命运。"),
("Public faith grows when grants support safe wiring, accessible doors, and homes that remain affordable to the people who care for them.", "当补助支持安全布线、无障碍入口，以及让照料建筑的人仍负担得起住房时，公众信任才会增长。")],
[("Why is a neighborhood unlike a museum?","People must live ordinary daily lives there.","社区居民还要在那里过日常生活。"),("What kinds of repairs should grants support?","Safe, accessible, affordable improvements.","补助应支持安全、无障碍且可负担的改造。")])],
33: [
A("Monday Wind on the Canal", "story", ["canal","forecast","dress","none","corporation","intensity","purse","Monday","dismiss","define"], [
("On Monday, the weather forecast warned that wind intensity would rise along the canal by noon.", "周一的天气预报警告，运河沿线风力将在中午前增强。"),
("A woman in a red dress saw an open purse on a bench, but none of the boat passengers claimed it.", "一名穿红裙的女子在长椅上看到一个敞开的钱包，但船上乘客都不认领。"),
("The canal corporation could not dismiss the warning, so staff closed the exposed pier and tried to define the owner's route from ticket records.", "运河公司不能忽视预警，于是员工关闭了暴露的码头，并试图从票务记录确定失主路线。"),
("When the owner returned, she found both her purse and a safe indoor place to wait for the storm.", "失主返回时，既找回了钱包，也找到了安全的室内地点躲避风暴。")],
[("Why was the pier closed?","The forecast predicted strong wind.","预报显示会出现强风。"),("How did staff search for the owner?","They checked ticket records.","员工查看票务记录寻找失主。")]),
A("Why Fishing Disputes Grow", "explanatory", ["contribute","exchange","november","fifth","frame","accompany","daily","dispute","cough","wind"], [
("A fishing dispute often begins when several boats frame the same bay as their traditional ground.", "渔业争端常始于多艘船都把同一海湾视为传统渔场。"),
("Daily catch records contribute evidence, but crews must exchange data in a shared format; the fifth column cannot mean weight for one boat and value for another.", "每日捕捞记录能提供证据，但船员必须用共同格式交换数据；第五列不能在一艘船上表示重量，在另一艘船上表示价值。"),
("Wind, a November storm, or a fisherman's cough may reduce effort, so raw totals need context to accompany them.", "风、十一月风暴或渔民咳嗽都可能减少作业量，因此原始总数需要背景说明。"),
("Agreements become possible when people compare like with like and separate poor seasons from deliberate rule breaking.", "当人们进行同类比较，并把歉收季与故意违规区分开时，协议才有可能达成。")],
[("Why must boats use a shared data format?","Otherwise the same column may mean different things.","否则同一列在不同船上可能含义不同。"),("What factors can reduce fishing effort?","Weather and crew illness.","天气与船员生病都会减少作业量。")]),
A("A Cinema Can Be an Emergency Shelter", "opinion", ["recommend","kid","burden","radioactive","heat","fisherman","gym","lack","obvious","submerge"], [
("A coastal town may recommend its gym as an emergency shelter, yet an old cinema can offer thick walls, seats, and backup heat.", "沿海小镇可能推荐体育馆作为应急避难所，但老电影院也能提供厚墙、座椅和备用供暖。"),
("The choice is not obvious: a fisherman arriving soaked may need dry space, while each kid needs toilets and a quiet corner.", "选择并不明显：浑身湿透的渔民需要干燥空间，每个孩子则需要厕所和安静角落。"),
("Planners must check flood maps so that water cannot submerge the entrance, and verify that no radioactive material or fuel is stored nearby.", "规划者必须检查洪水地图，确保入口不会被淹，并确认附近没有放射性物质或燃料。"),
("Using several buildings shares the burden and prevents a lack of one resource from closing the entire shelter system.", "使用多栋建筑可以分担压力，也能防止某一种资源不足导致整个避难体系关闭。")],
[("What advantages can a cinema offer?","Strong walls, seats, space, and backup heat.","电影院可提供坚固墙体、座椅、空间和备用供暖。"),("Why should several buildings be used?","They share the burden and reduce single-point failure.","多处避难能分担压力并减少单点失效。")])],
34: [
A("The Physicist and the Broken Fountain", "story", ["nursery","physicist","love","raw","reaction","temple","dispose","failure","eagle","tin"], [
("A retired physicist visited a temple nursery each week because his love of teaching led him to help children question ordinary objects.", "一位退休物理学家每周到寺庙托儿所，因为他喜欢帮助孩子探索日常物品。"),
("When the courtyard fountain failed, the children blamed a tin eagle that had fallen into the basin.", "庭院喷泉发生故障时，孩子们怪罪掉进水池的一只锡鹰。"),
("He treated their idea as a raw hypothesis, observed the pump's reaction, and found leaves blocking the inlet instead.", "他把孩子们的想法当作初步假设，观察水泵反应，最终发现真正原因是树叶堵住入口。"),
("They learned to dispose of garden waste properly and to see failure as an invitation to test evidence rather than assign blame.", "他们学会妥善处理园林废物，也懂得把故障视为检验证据的机会，而不是急于归咎。")],
[("What actually blocked the fountain?","Leaves in the pump inlet.","树叶堵住了水泵入口。"),("What lesson did the children learn?","Test evidence before assigning blame.","他们学会先检验证据再归责。")]),
A("How Stone Fountains Circulate Water", "explanatory", ["fountain","its","pack","pioneer","dance","tender","precious","outcome","fog","letter"], [
("A fountain sends water upward because a pump gives it pressure, and gravity brings the water back to its basin.", "喷泉向上喷水，是因为水泵提供压力，而重力又把水带回水池。"),
("Early builders could pack channels with clay; a pioneer might describe the design in a letter, although exact plans were precious and rare.", "早期建造者会用黏土填实水道；先驱可能在信中描述设计，但精确图纸珍贵而稀少。"),
("Fine drops dance in the air and form a cool fog, while tender stone edges slowly wear away.", "细小水滴在空中跳动，形成凉雾，而脆弱的石边会逐渐磨损。"),
("The final outcome depends on balanced flow, clean filters, and maintenance that respects both sculpture and machinery.", "最终效果取决于平衡水流、清洁过滤器，以及兼顾雕塑与机械的维护。")],
[("Why does fountain water return to the basin?","Gravity pulls it down.","重力把水带回水池。"),("What determines the fountain's long-term outcome?","Balanced flow, filters, and careful maintenance.","水流、过滤和细致维护决定长期效果。")]),
A("A Treaty Needs Words People Understand", "opinion", ["punish","efficient","not","distinction","slope","furthermore","treaty","language","discuss","grateful"], [
("A treaty is not efficient merely because diplomats sign it quickly or because its language sounds formal.", "条约并不会仅因外交官迅速签署或语言正式就变得高效。"),
("People living on either slope of a border must understand the distinction between a legal duty and a voluntary promise.", "生活在边界两侧山坡的人必须理解法律义务与自愿承诺之间的区别。"),
("Furthermore, communities should discuss how violations will be investigated; vague rules can punish the weak while powerful actors escape.", "此外，社区应讨论如何调查违规；模糊规定可能惩罚弱者，却让强势者逃脱。"),
("Citizens may be grateful for peace, but lasting trust requires translations, public meetings, and clear ways to challenge a decision.", "公民会感谢和平，但持久信任还需要译文、公开会议，以及挑战决定的清晰途径。")],
[("What distinction must residents understand?","The difference between duties and voluntary promises.","居民要理解义务与自愿承诺的区别。"),("What supports lasting trust?","Clear translations, meetings, and appeal procedures.","清楚译文、公开会议和申诉程序有助于持久信任。")])],
35: [
A("The Arena Appraisal", "story", ["appraisal","approach","appropriate","apt","arc","arena","armor","arrange","arrangement","array"], [
("Before reopening the city arena, an engineer began an appraisal of its roof, whose steel arc had supported an array of lights for forty years.", "城市竞技场重开前，一名工程师开始评估屋顶；钢制拱梁已支撑一整排灯具四十年。"),
("Her approach was to arrange sensors beneath the structure while workers in appropriate safety armor inspected every joint.", "她的方法是在结构下方布置传感器，同时让穿着合适防护装备的工人检查每个接头。"),
("The old seating arrangement was apt for concerts but narrowed two emergency exits during sports events.", "旧座位布置适合音乐会，却在体育赛事期间缩窄了两个紧急出口。"),
("The team kept the graceful roof, moved several rows, and proved that preservation and safety could share one design.", "团队保留优美屋顶，移动几排座位，证明保护与安全可以共存于同一设计。")],
[("What did the roof support?","An array of lights.","屋顶支撑着一排灯具。"),("Why was the seating changed?","It narrowed emergency exits.","旧座位布置缩窄了紧急出口。")]),
A("How Investigators Establish a Cause", "explanatory", ["arrest","arrogant","artery","articulate","artillery","ascend","ascertain","ascribe","aspiration","assassination"], [
("Investigators must ascertain facts before they ascribe a disaster to a person, a weapon, or an arrogant political ambition.", "调查人员必须先查明事实，才能把灾难归因于某个人、武器或傲慢的政治野心。"),
("In an assassination inquiry, residue from artillery or a blocked artery may each suggest a cause, but neither alone justifies an arrest.", "在暗杀调查中，火炮残留物或堵塞动脉都可能提示死因，但任何单项都不足以支持逮捕。"),
("Evidence should ascend from observation to testing and then to a conclusion that experts can articulate clearly.", "证据应从观察上升到检验，再形成专家能够清楚表达的结论。"),
("The aspiration of a fair inquiry is accuracy, including the willingness to revise a theory when new facts appear.", "公正调查追求准确，也包括在新事实出现时修正理论的意愿。")],
[("Why is one clue insufficient for arrest?","A clue may suggest but not prove a cause.","线索只能提示原因，不能单独证明。"),("What should happen when new facts appear?","Investigators should revise their theory.","新事实出现时应修正理论。")]),
A("Athletes Need Authority Over Their Data", "opinion", ["assault","assert","asset","assignment","assimilate","assumption","assurance","athlete","atlas","atmosphere"], [
("A wearable sensor can be an asset to an athlete, mapping sleep, training routes, and even the atmosphere around a competition.", "可穿戴传感器可以成为运动员的有用资产，记录睡眠、训练路线，甚至比赛环境。"),
("Yet a team assignment should not include unlimited rights to assimilate private health data into a commercial atlas.", "但球队任务不应包括把私人健康数据无限纳入商业图谱的权利。"),
("The assumption that consent is automatic can become an assault on privacy, especially when a young athlete fears losing selection.", "把同意视为理所当然可能构成对隐私的侵犯，尤其当年轻运动员担心落选时。"),
("Players should assert control through limited permissions, deletion rights, and written assurance that medical records will not be sold.", "运动员应通过有限授权、删除权和书面保证来掌握控制权，确保医疗记录不会被出售。")],
[("What can wearable sensors record?","Sleep, routes, health, and environmental data.","设备可记录睡眠、路线、健康和环境数据。"),("What protections should athletes receive?","Limited permissions, deletion rights, and no data sales.","运动员应有有限授权、删除权和禁止数据出售的保障。")])],
})

DATA.update({
36: [
A("Lunch Beneath the Cathedral", "story", ["bust","buzz","bypass","cafeteria","calcium","calorie","cane","cannon","canon","canvas"], [
("A new cafeteria opened beside the cathedral, where a stone bust and a painted canvas watched over the lunch tables.", "大教堂旁开了一家新自助餐厅，石质半身像和彩绘画布俯视着午餐桌。"),
("Its menu listed every calorie and source of calcium, yet an electric buzz from the kitchen disturbed an old man carrying a cane.", "菜单列出每份食物的热量和钙来源，但厨房传来的电流嗡嗡声打扰了一位拄手杖的老人。"),
("The cook traced the sound to a fan whose belt had slipped, then used a service bypass so diners could remain safely outside the work area.", "厨师发现声音来自皮带滑落的风扇，随后启用维修旁路，让顾客安全留在作业区外。"),
("When the bell sounded like a distant cannon, the organist joked that quiet repair had joined the building's unwritten canon of hospitality.", "钟声如远处大炮般响起时，风琴师开玩笑说，安静维修已加入这座建筑不成文的待客准则。")],
[("What caused the buzzing sound?","A slipped fan belt.","风扇皮带滑落造成了嗡嗡声。"),("Why was a bypass used?","To keep diners away from the repair area.","旁路让顾客远离维修区。")]),
A("From Clay to Ceramic", "explanatory", ["cape","capsule","caption","captive","cardinal","carve","casualty","catastrophe","cater","cathedral"], [
("Ceramic begins as clay that workers shape by hand or carve with a tool, then heat until its particles bind firmly.", "陶瓷始于手工塑形或工具雕刻的黏土，随后经加热让颗粒牢固结合。"),
("A test capsule placed in the kiln changes color at a cardinal temperature, giving the potter evidence that a firing stage is complete.", "放在窑内的测试胶囊会在关键温度变色，为陶工提供烧制阶段完成的证据。"),
("Museums may caption a jar from a coastal cape or a cathedral, but they should not keep its makers captive inside a romantic story.", "博物馆可以说明陶罐来自海角或大教堂，但不应把制作者禁锢在浪漫化故事里。"),
("A cracked vessel is not a catastrophe or a human casualty; careful conservation can cater for study while showing the damage honestly.", "器物开裂不是灾难，更不是人员伤亡；细致保护既能满足研究需要，也能诚实展示损伤。")],
[("How does a test capsule help a potter?","It changes color at an important temperature.","测试胶囊在关键温度变色。"),("How should museums show damaged ceramics?","Preserve them while showing damage honestly.","博物馆应保护器物并如实展示损伤。")]),
A("A Census Must Count People Carefully", "opinion", ["catholic","caution","cautious","cavity","cellar","cemetery","census","ceramic","cereal","certainty"], [
("A census should use caution when asking whether a person is Catholic, owns a cellar, or lives beside a cemetery.", "人口普查询问一个人是否为天主教徒、是否有地窖或是否住在墓地旁时，应保持谨慎。"),
("Such details may help plan schools, cereal supplies, housing, or conservation of a ceramic district, but they can also expose private lives.", "这些信息可能帮助规划学校、谷物供应、住房或陶瓷街区保护，但也会暴露私人生活。"),
("Officials must be cautious about certainty: an empty cavity in a form may mean refusal, confusion, or a question that does not fit the household.", "官员必须谨慎看待确定性：表格里的空白可能意味着拒答、困惑，或问题不适合该家庭。"),
("Trust grows when the purpose of each question is explained and personal records cannot be used to punish respondents.", "解释每个问题的用途，并确保个人记录不会用于惩罚受访者，才能建立信任。")],
[("Why can census details be sensitive?","They may reveal private beliefs and living conditions.","普查信息可能暴露私人信仰与居住情况。"),("What may a blank answer mean?","Refusal, confusion, or a poorly fitting question.","空白可能表示拒答、困惑或问题不适用。")])],
37: [
A("The Meeting After the Spill", "story", ["concede","conceive","conception","concise","confer","confidential","configuration","conform","confront","confusion"], [
("After a chemical spill, factory managers had to confront residents whose conception of safety had changed overnight.", "化学品泄漏后，工厂管理者不得不面对那些安全观念一夜改变的居民。"),
("They used a school-hall meeting to confer, while a concise map showed the pipe configuration without revealing confidential employee records.", "双方在学校礼堂协商，一张简明地图展示了管道配置，同时没有泄露员工机密记录。"),
("The director had to concede that an alarm did not conform to the written standard, ending confusion about who had heard it.", "厂长不得不承认一只警报器不符合书面标准，从而结束了关于谁听到警报的混乱争论。"),
("Together they decided to conceive a public testing schedule, turning an abstract idea of accountability into a visible routine.", "双方共同构想公开测试日程，把抽象的问责概念变成可见的日常程序。")],
[("What did the map protect?","Confidential employee information.","地图保护了员工机密信息。"),("What did the director admit?","An alarm failed to meet the standard.","厂长承认警报器不符合标准。")]),
A("How Several Reports Become One Finding", "explanatory", ["conscientious","consecutive","consensus","consequent","conserve","console","consolidate","conspicuous","constituent","constrain"], [
("A conscientious research team gathers consecutive observations before trying to consolidate them into one account.", "认真的研究团队会收集连续观察，再把它们整合为一个结论。"),
("Each constituent report keeps its source and date, while a computer console highlights conspicuous gaps or conflicting measurements.", "每份组成报告都保留来源与日期，计算机控制台则标出明显缺口或冲突测量。"),
("Rules constrain careless editing and conserve minority evidence, so consensus does not simply erase an unusual result.", "规则限制草率编辑并保留少数证据，因此共识不会简单抹去异常结果。"),
("A consequent finding is stronger because readers can trace how separate observations supported it and where uncertainty remains.", "由此得出的结论更有力，因为读者能追溯不同观察如何支持它，以及不确定性仍在哪里。")],
[("What does the console highlight?","Gaps and conflicting measurements.","控制台会标出缺口和冲突测量。"),("Why is minority evidence conserved?","Consensus should not erase unusual results.","共识不应抹去异常结果。")]),
A("Consumers Deserve Pollution Data", "opinion", ["consultant","consumer","contaminate","contemplate","contend","contention","continuity","contradict","contribution","contrive"], [
("A consumer deciding between two products should know whether either factory may contaminate a river.", "消费者在两种产品间选择时，应知道相关工厂是否可能污染河流。"),
("A company consultant may contend that disclosure threatens commercial continuity, then contrive a narrow report that hides the largest discharge.", "公司顾问可能声称披露会威胁商业连续性，并设计一份狭窄报告来隐藏最大排放。"),
("That argument can contradict claims of social contribution and create contention among communities asked to bear the risk.", "这种说法可能与企业的社会贡献主张矛盾，并在被要求承担风险的社区中引发争议。"),
("People can contemplate price, quality, and pollution together only when data use common units and independent inspectors verify them.", "只有数据采用统一单位并经独立检查员核实，人们才能同时权衡价格、质量与污染。")],
[("What information should consumers receive?","Comparable, verified pollution data.","消费者应获得可比较、经核实的污染数据。"),("Why can narrow reports create contention?","They hide risks that communities must bear.","报告隐瞒了社区必须承担的风险。")])],
38: [
A("The Detective on Platform Six", "story", ["designate","destined","destiny","destructive","detach","detain","detective","deteriorate","deviate","diagnose"], [
("Police designate one carriage as the possible scene of a theft, and a detective boards the train destined for the coast.", "警方把一节车厢指定为可能的盗窃现场后，一名侦探登上了开往海岸的列车。"),
("She does not detain every passenger or treat suspicion as destiny; instead, she asks staff to detach a damaged lock and examines its marks.", "她没有扣留所有乘客，也没有把怀疑当作命运，而是拆下损坏的锁检查痕迹。"),
("The scratches showed that the door had begun to deteriorate and would deviate from its rail whenever the train turned sharply.", "划痕表明车门已经开始老化，列车急转时就会偏离轨道。"),
("The evidence lets her diagnose the fault and prevent a destructive accusation: the missing case slid into a service space rather than being stolen.", "她的判断避免了破坏性的指控：丢失的箱子是滑进维修空间，并非被盗。")],
[("What did the lock marks reveal?","The door was deteriorating and moving off its rail.","锁的痕迹表明车门老化并偏离轨道。"),("Where was the missing case?","In a service space.","箱子滑进了维修空间。")]),
A("How Medicines Spread Through Water", "explanatory", ["differentiate","diffuse","dignity","dilemma","dilute","diminish","dine","diploma","diplomat","directory"], [
("When a substance begins to diffuse through water, its molecules move from crowded areas toward places where fewer are present.", "一种物质开始在水中扩散时，分子会从密集区域向稀疏区域移动。"),
("Adding clean water can dilute the concentration but does not necessarily diminish the total amount of the substance.", "加入清水可以稀释浓度，但不一定减少该物质的总量。"),
("Students learn to differentiate these ideas through measurements, not through a diploma, a directory, or the authority of a visiting diplomat.", "学生要通过测量区分这些概念，而不是依靠文凭、名录或来访外交官的权威。"),
("A classroom dilemma about whether it is safe to dine near a laboratory should be resolved with evidence and respect for everyone's dignity.", "是否能在实验室附近进餐这一课堂难题，应以证据和对每个人尊严的尊重来解决。")],
[("What does dilution change?","Concentration, not necessarily total amount.","稀释改变浓度，但不一定改变总量。"),("How should safety dilemmas be resolved?","With evidence and respect.","安全难题应以证据和尊重来解决。")]),
A("Transport Updates Must Be Clear", "opinion", ["disastrous","discern","discount","discreet","discrepancy","discrete","discriminate","dismay","dispatch","disperse"], [
("During a disastrous transport failure, officials should dispatch clear updates before crowds disperse toward unsafe alternatives.", "发生灾难性交通故障时，官员应在乘客分散前往不安全替代路线前发布清楚更新。"),
("Passengers need to discern discrete facts: which line is closed, when buses leave, and whether a ticket discount applies.", "乘客需要辨认一项项明确事实：哪条线路关闭、公交何时发车，以及票价折扣是否适用。"),
("A discrepancy between an app and a station board causes dismay, while vague language may discriminate against travelers who read slowly.", "应用与站牌信息不一致会令人沮丧，含糊语言还可能不利于阅读较慢的旅客。"),
("Staff can remain discreet about personal incidents while still giving the public enough verified information to choose a safe route.", "员工可以对个人事件保持谨慎保密，同时仍向公众提供足够的核实信息来选择安全路线。")],
[("Which facts do passengers need?","Closures, departure times, and ticket rules.","乘客需要关闭线路、发车时间和票务规则。"),("What causes dismay?","Conflicting information across channels.","不同渠道信息冲突会令人沮丧。")])],
39: [
A("Across the Equator with an Old Map", "story", ["epoch","equator","erosion","erroneous","erupt","escort","essence","esthetic","eternal","ethnic"], [
("A research boat crossed the equator carrying an old map from an epoch when sailors drew coastlines by eye.", "一艘研究船穿越赤道，带着一张来自旧时代的地图；当时水手凭肉眼绘制海岸线。"),
("Its elegant, almost esthetic curves were erroneous where erosion had removed a beach and a volcano had begun to erupt offshore.", "地图优美得近乎艺术的曲线在一些地方已经错误，因为侵蚀带走了海滩，近海火山也开始喷发。"),
("A local ethnic council sent an escort who explained that the essence of the island was not an eternal shape but a changing relationship with water.", "当地族群委员会派来一名向导，他解释说，岛屿的本质不是永恒形状，而是与水不断变化的关系。"),
("The team redrew the shore and added community names that earlier charts had ignored.", "团队重新绘制海岸，并加入早期海图忽略的社区名称。")],
[("Why was the old coastline wrong?","Erosion and volcanic activity had changed it.","侵蚀和火山活动改变了海岸。"),("What did the new map add?","Community place names.","新地图加入了社区地名。")]),
A("Why Species Become Extinct", "explanatory", ["evoke","exceptional","exclusive","execution","exemplify","exempt","exile","exotic","expedition","expel"], [
("An exceptional storm can expel animals from a small habitat, but extinction usually follows several pressures acting together.", "异常风暴会把动物赶出小型栖息地，但灭绝通常源于多种压力共同作用。"),
("An exotic predator may take eggs, an exclusive road may divide feeding ground, and human activity can force a population into exile.", "外来捕食者会吃掉鸟蛋，专用道路会割裂觅食地，人类活动还会迫使种群离开家园。"),
("A field expedition can exemplify the process by tracking survival and reproduction rather than relying on images that merely evoke sadness.", "野外考察队可以通过追踪生存与繁殖来说明这个过程，而不是只依靠唤起悲伤的图像。"),
("No species is exempt from ecology, so conservation plans need careful execution across land, water, and local livelihoods.", "任何物种都不能脱离生态规律，因此保护计划需要在土地、水域与当地生计之间认真执行。")],
[("Why does extinction usually happen?","Several pressures act together.","灭绝通常由多种压力共同造成。"),("What should expeditions track?","Survival and reproduction.","考察应追踪生存与繁殖情况。")]),
A("Exploration Budgets Need Public Value", "opinion", ["expend","expenditure","expertise","expire","explicit","exposition","exquisite","extinct","extinguish","extract"], [
("An expedition may expend public money to extract ice, rock, or biological samples that require rare expertise to interpret.", "考察可能花费公共资金提取冰、岩石或生物样本，而解读这些样本需要稀缺专业知识。"),
("Its budget should make each major expenditure explicit, including storage after grants expire and protection for an extinct species site.", "预算应明确列出每项主要支出，包括资助到期后的保存费用，以及对灭绝物种遗址的保护。"),
("An exquisite exposition in a museum can share results, but beautiful displays cannot extinguish questions about local consent or damaged land.", "博物馆里精美的展览可以分享成果，但漂亮陈列无法消除有关当地同意或土地受损的问题。"),
("Funding is justified when data remain accessible, communities benefit, and researchers account for both discovery and repair.", "当数据持续开放、社区受益，且研究人员同时对发现与修复负责时，资助才有正当性。")],
[("What costs should budgets include?","Storage, protection, and long-term responsibilities.","预算应包括保存、保护和长期责任成本。"),("When is public funding justified?","When results are accessible and communities benefit.","成果开放且社区受益时，公共资助才合理。")])],
40: [
A("The Historian in the Gloom", "story", ["gloom","gloomy","gorgeous","gossip","gown","gracious","graphic","graze","grease","grief"], [
("A historian entered a gloomy valley at dawn, carrying a graphic map and wearing a borrowed graduation gown against the cold.", "黎明时，一位历史学家走进阴郁山谷，带着图解地图，并借来一件毕业礼服御寒。"),
("Village gossip claimed that a gorgeous house beyond the ridge was abandoned after a family grief, but the records told a quieter story.", "村里流言说山脊外一座华丽房屋因家庭悲剧而废弃，但档案讲述了一个更平静的故事。"),
("She slipped on grease near a barn and suffered a light graze, whereupon a gracious farmer invited her inside to clean it.", "她在谷仓附近踩到油脂滑倒，受了轻微擦伤；一位和善的农民请她进屋清理伤口。"),
("In the gloom of the attic, they found letters proving that the owners had donated the house as a school and moved away voluntarily.", "在阁楼的昏暗中，他们找到信件，证明屋主自愿把房子捐作学校后搬走。")],
[("What did village gossip claim?","A family tragedy had caused the house to be abandoned.","流言称家庭悲剧导致房屋废弃。"),("What did the letters prove?","The house had been donated as a school.","信件证明房子被捐作学校。")]),
A("How Hardy Herbs Survive", "explanatory", ["grieve","grim","grin","groan","groove","grope","guardian","hamper","handbook","handicap"], [
("A hardy herb survives a grim winter by slowing growth and storing energy below ground, where ice cannot easily reach it.", "耐寒药草通过减慢生长并把能量储存在地下来度过严冬，因为冰不易到达那里。"),
("A groove in a leaf may guide water to the root, while fine hairs act as a guardian against wind and hungry insects.", "叶片上的沟槽可把水引向根部，细毛则像守卫一样抵挡风和饥饿昆虫。"),
("Gardeners need not groan or grope for magic advice: a local handbook can explain how wet soil may hamper roots and handicap spring recovery.", "园丁不必呻吟或摸索神奇秘诀；本地手册会说明湿土如何妨碍根系并阻碍春季恢复。"),
("Healthy new leaves can make a gardener grin, yet a failed plant is no reason to grieve before checking soil, light, and drainage.", "健康新叶会让园丁露出笑容，但植物失败时，在检查土壤、光照和排水前不必悲伤。")],
[("Where do hardy herbs store energy?","Below ground.","耐寒药草把能量储存在地下。"),("What conditions should gardeners check?","Soil, light, and drainage.","园丁应检查土壤、光照与排水。")]),
A("Heritage Trails Need More Than Signs", "opinion", ["hardy","hasty","hatch","haul","haunt","hawk","heave","heighten","heir","hemisphere"], [
("A heritage trail can heighten respect for a landscape, but a hasty line of signs will not protect the people and wildlife living there.", "遗产步道可以增强人们对景观的尊重，但匆忙竖起的一排标牌无法保护当地居民与野生动物。"),
("A hawk may haunt a cliff in one hemisphere, while hardy families haul supplies up the same path and heave water from a deep well.", "一只鹰可能常在某个半球的悬崖出没，而坚韧的家庭也沿同一路径拖运物资、从深井提水。"),
("Officials should not hatch a tourism plan with an outside heir to land rights while excluding residents who maintain the route.", "官员不应与外来的土地继承人策划旅游方案，却排除维护路线的居民。"),
("Visitor limits, local guides, and maintenance fees can share benefits while keeping the trail useful beyond a single season.", "游客限额、当地向导和维护费可以共享收益，并让步道在一个季节之后仍然有用。")],
[("Who uses the trail besides tourists?","Local families and wildlife.","当地家庭和野生动物也使用这条路线。"),("What measures can protect the trail?","Visitor limits, local guides, and maintenance fees.","游客限额、当地向导与维护费可保护步道。")])],
})

def rebuild_index() -> tuple[int, int]:
    day_files = sorted(OUT_DIR.glob("day-*.json"))
    numbered = []
    for path in day_files:
        match = re.fullmatch(r"day-(\d{3})\.json", path.name)
        if match:
            numbered.append((int(match.group(1)), path))
    expected = list(range(1, len(numbered) + 1))
    actual = [day for day, _ in numbered]
    if actual != expected:
        raise ValueError(f"阅读文件必须从 Day 1 连续编号：{actual}")
    days = []
    article_count = 0
    for day, path in numbered:
        payload = json.loads(path.read_text(encoding="utf-8"))
        count = len(payload.get("articles", []))
        days.append({"day": day, "file": path.name, "count": count})
        article_count += count
    index = {
        "schema_version": 1,
        "id": "cet4_context_readings",
        "wordlist_id": "cet4_combined",
        "title": "四级词汇语境阅读",
        "description": "与单词库 Day 对应；每个 Day 包含故事、说明文和观点文各一篇，并支持逐句显示中文。",
        "tags": ["四级", "语境阅读", "逐句翻译"],
        "article_count": article_count,
        "day_count": len(days),
        "days": days,
    }
    (OUT_DIR / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    manifest = {"schema_version": 1, "collections": [{"id": index["id"], "index": "cet4_combined/index.json"}]}
    (OUT_DIR.parent / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return len(days), article_count


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
                source_word = words[word.casefold()]
                targets.append({"word": source_word["word"], "meaning": source_word["meaning"]})
            sentences = [{"en": en, "zh": zh} for en, zh in draft["pairs"]]
            articles.append({
                "id": f"cet4-reading-d{day:03}-{number}",
                "title": draft["title"],
                "type": draft["type"],
                "difficulty": "CET-4+",
                "text": " ".join(item["en"] for item in sentences),
                "translation": "".join(item["zh"] for item in sentences),
                "sentences": sentences,
                "target_words": targets,
                "questions": [{"prompt": q, "answer": a, "explanation": e} for q, a, e in draft["questions"]],
            })
        payload = {
            "schema_version": 1,
            "collection_id": "cet4_context_readings",
            "wordlist_id": "cet4_combined",
            "day": day,
            "articles": articles,
        }
        (OUT_DIR / f"day-{day:03}.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    days, articles = rebuild_index()
    print(f"Wrote Day 21-40; index now contains {days} days / {articles} articles")

if __name__ == "__main__":
    main()
