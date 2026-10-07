from __future__ import annotations

import json
import random
import re
from pathlib import Path

from nltk.corpus import wordnet as wn

ROOT = Path(__file__).resolve().parent.parent
WORD_DIR = ROOT / "content" / "wordlists" / "cet4_combined"
OUT_DIR = ROOT / "content" / "readings" / "cet4_combined"

# These settings are editorial choices, not prompts for another model.  Each
# setting gives a Day its own place, activity, and line of inquiry.
SETTINGS = [
    ("an inland water laboratory", "内陆水利实验室"),
    ("a medieval meadow exhibition", "中世纪草地展览"),
    ("a peninsula walking route", "半岛步行线路"),
    ("a public research showcase", "公共研究成果展"),
    ("a residential history archive", "社区历史档案馆"),
    ("a coastal science hall", "海岸科学馆"),
    ("a mountain transit inquiry", "山区交通调查会"),
    ("a harbor warehouse", "港口仓库"),
    ("an embassy trade fair", "使馆贸易展"),
    ("a rural school workshop", "乡村学校工作坊"),
    ("a woodland cooperative", "林地合作社"),
    ("an aviation market", "航空主题集市"),
    ("a suburban health center", "郊区健康中心"),
    ("a southwest farming forum", "西南农业论坛"),
    ("a regional technology weekend", "区域科技周末活动"),
    ("an Italian river survey", "意大利河流调查"),
    ("a shipyard guesthouse", "造船厂招待所"),
    ("a seashore kindergarten", "海滨幼儿园"),
    ("a mining-town bookstore", "矿区书店"),
    ("a Danish coastal university", "丹麦海岸大学"),
    ("a zoo newsroom", "动物园新闻室"),
    ("a Scottish harbor market", "苏格兰港口市场"),
    ("a lighthouse sports center", "灯塔体育中心"),
    ("a provincial storm shelter", "省级风暴避难所"),
    ("a cross-border public clinic", "跨境公共诊所"),
    ("a family support office", "家庭支持办公室"),
    ("a city street festival", "城市街头节"),
    ("a Swedish airfield", "瑞典机场"),
    ("an archaeological language camp", "考古语言营"),
    ("a Portuguese hostel", "葡萄牙旅舍"),
    ("a reservoir restaurant", "水库餐厅"),
    ("an international motorway station", "国际高速公路站"),
    ("a shipbuilding tribunal", "造船业听证庭"),
    ("a winter exploration camp", "冬季探险营"),
    ("an island civic center", "岛屿市民中心"),
    ("a southeast heritage crossing", "东南遗产通道"),
    ("a reefside mountain gallery", "礁岸山地画廊"),
    ("a French charity theater", "法国慈善剧场"),
    ("an urban transport control room", "城市交通控制室"),
    ("a greenhouse learning center", "温室学习中心"),
    ("a seasonal winery school", "季节性酒庄学校"),
    ("an Egyptian seaside district", "埃及海滨街区"),
    ("an autumn astronomy station", "秋季天文观测站"),
    ("a coral pharmacy expedition", "珊瑚药学考察站"),
    ("an ecosystem design college", "生态设计学院"),
    ("a mining settlement after rain", "暴雨后的矿业定居点"),
    ("a volcanic homestay program", "火山区寄宿项目"),
    ("a coastal therapy center", "海岸治疗中心"),
    ("an estuary training college", "河口培训学院"),
    ("a centennial marine museum", "百年海洋博物馆"),
    ("a university aquarium", "大学水族馆"),
    ("a veterinary arts festival", "兽医艺术节"),
    ("a maritime craft district", "海事工艺街区"),
    ("an offshore rescue conference", "近海救援会议"),
    ("a botanical river conservatory", "河畔植物温室"),
]

BLOCKED = {"rape", "suicide", "sex", "prostitute", "cif", "l/c", "b/l"}

SEMANTIC_ZH = {
    "story": [
        "在{s}的参观过程中，讲解员先介绍{a}，随后带大家找到另一项独立展品{b}。",
        "学生在{s}记录{a}后，又到另一处展区了解{b}，两项内容分别得到清楚说明。",
        "{s}的参观先让学生认识{a}；一块丢失的标牌又把他们带到{b}。",
        "{s}的上午活动把{a}与另一项关于{b}的展览相邻安排，但没有混淆两者。",
        "访客到{s}询问{a}，旧平面图却意外引导她发现了{b}。",
        "{s}的策展人先纠正{a}的标签错误，随后发现关于{b}的材料也放错了位置。",
        "{s}的两名志愿者借助清单确认{a}，并顺带找到另一条关于{b}的记录。",
        "雨天让一家人留在{s}，一个孩子学习{a}，另一个孩子则操作与{b}有关的模型。",
        "{s}闭馆前，一本提到{a}的日记帮助员工找到了一幅标有{b}的画的主人。",
        "{s}安静的一角介绍{a}，旁边的录音访谈则讲述{b}背后的人物故事。",
        "{s}最新展厅从{a}开始，以一个出人意料的本地{b}实例结束。",
        "{s}的架子倒下时，员工保护了有关{a}的材料，也找回了旁边关于{b}的档案。",
    ],
    "explanatory": [
        "{s}的课程分别解释{a}与{b}，避免学习者因定义不同而进行错误比较。",
        "{s}的图表把{a}和{b}放在不同分支，让读者清楚看见两者区别。",
        "{s}的研究记录分别使用{a}和{b}；由于含义不同，二者需要不同证据。",
        "{s}的手册先介绍{a}，再补充需要更多背景的{b}。",
        "为避免歧义，{s}的教师分别说明{a}和{b}，再用实例展示各自用法。",
        "{s}的分类练习把{a}与{b}并列，要求学习者找出两者不同特征。",
        "{s}第一块展板说明{a}，下一块介绍{b}，访客因而能比较两个准确概念。",
        "{s}的野外记录严格区分{a}和{b}，使记录保持准确。",
        "{s}的简短演示先让{a}具体可见，再用第二个实例解释{b}。",
        "{s}的学生分别概括{a}与{b}，随后检验新实例是否符合定义。",
        "{s}的词汇表定义{a}，并以交叉索引引导读者查看{b}，但不把二者视为相同。",
        "{s}把{a}与{b}分开考察，使两个陌生概念转化为可使用的知识。",
    ],
    "opinion": [
        "{s}的公开论坛同时考虑{a}与{b}，并讨论哪一项更需要优先行动。",
        "{s}的政策应处理{a}，也不能忽视{b}；两者都需要证据而非口号。",
        "{s}附近居民讨论{a}和{b}后，要求书面说明成本与责任。",
        "{s}的方案优先处理{a}，批评者则认为{b}也应得到同等关注。",
        "{s}的决策者不能只评估{a}，却把{b}排除在公开证据之外。",
        "{s}的公开会议把有关{a}的实际问题与{b}带来的伦理问题一同讨论。",
        "{s}的官员清楚定义{a}并解释方案如何回应{b}，资金选择才会更明白。",
        "{s}最有力的论证支持处理{a}，同时要求在{b}受影响时设置保障。",
        "{s}要建立公众信任，就必须诚实讨论{a}，并对{b}作出可衡量承诺。",
        "{s}的审查小组拒绝在缺乏地方证据时认定{a}天然比{b}更重要。",
        "{s}的长期规划应公布{a}指标，也应允许独立人员审查有关{b}的主张。",
        "批准{s}的改变前，领导者应解释{a}为何重要，以及谁承担{b}带来的风险。",
    ],
}

SHORT_PATTERNS = {
    "story": [
        "At {s}, a guide explained {a} ({ad}) beside a display of {b} ({bd}).",
        "A student at {s} photographed {a}—{ad}—and sketched {b}—{bd}.",
        "During a tour of {s}, the class found {a} ({ad}) before locating {b} ({bd}).",
        "The morning program at {s} paired a section on {a} ({ad}) with one on {b} ({bd}).",
        "A visitor entered {s} asking about {a} ({ad}) and left with a note on {b} ({bd}).",
        "Inside {s}, the curator corrected labels for {a} ({ad}) and {b} ({bd}).",
        "Two volunteers at {s} used the inventory to identify {a} ({ad}) and {b} ({bd}).",
        "Rain kept a family inside {s}, learning about {a} ({ad}) and {b} ({bd}).",
        "Near closing time at {s}, a diary linked the displays of {a} ({ad}) and {b} ({bd}).",
        "A quiet corner of {s} presented {a} ({ad}); a recording nearby introduced {b} ({bd}).",
        "The newest room at {s} began with {a} ({ad}) and ended with {b} ({bd}).",
        "When a shelf shifted at {s}, staff protected files on {a} ({ad}) and {b} ({bd}).",
    ],
    "explanatory": [
        "At {s}, {a} means {ad}, whereas {b} means {bd}; separate examples prevent confusion.",
        "A chart in {s} defines {a} as {ad} and {b} as {bd} on different branches.",
        "Researchers at {s} use {a} for {ad}, but reserve {b} for {bd}.",
        "The handbook at {s} introduces {a}—{ad}—before {b}—{bd}.",
        "To avoid ambiguity, {s} explains {a} as {ad} and {b} as {bd}.",
        "A classification exercise at {s} compares {a} ({ad}) with {b} ({bd}).",
        "One panel in {s} illustrates {a} ({ad}); the next describes {b} ({bd}).",
        "Field notes from {s} distinguish {a} ({ad}) from {b} ({bd}).",
        "A demonstration at {s} makes {a} ({ad}) concrete before explaining {b} ({bd}).",
        "Students at {s} summarize {a} as {ad} and {b} as {bd}, then test new examples.",
        "The glossary at {s} defines {a} as {ad} and cross-references {b}, meaning {bd}.",
        "By separating {a} ({ad}) from {b} ({bd}), {s} turns definitions into usable knowledge.",
    ],
    "opinion": [
        "A forum at {s} considered {a} ({ad}) alongside {b} ({bd}) before setting priorities.",
        "Policy at {s} should address {a}—{ad}—without ignoring {b}—{bd}.",
        "Residents near {s} debated {a} ({ad}) and {b} ({bd}), then requested written evidence.",
        "A proposal for {s} prioritizes {a} ({ad}), while critics emphasize {b} ({bd}).",
        "Decision makers at {s} cannot evaluate {a} ({ad}) while excluding {b} ({bd}).",
        "An open meeting at {s} joined practical questions about {a} ({ad}) with concerns about {b} ({bd}).",
        "Funding choices at {s} require clear definitions of {a} ({ad}) and {b} ({bd}).",
        "The strongest argument at {s} supported {a} ({ad}) but demanded safeguards for {b} ({bd}).",
        "Public trust at {s} needs honest discussion of {a} ({ad}) and measurable commitments on {b} ({bd}).",
        "A review panel at {s} rejected claims that {a} ({ad}) automatically outweighed {b} ({bd}).",
        "Long-term planning at {s} needs indicators for {a} ({ad}) and independent scrutiny of {b} ({bd}).",
        "Before approving change at {s}, leaders must explain {a} ({ad}) and risks involving {b} ({bd}).",
    ],
}


def diverse_pairs(day: int, number: int, kind: str, setting_en: str, setting_zh: str, items: list[dict]):
    rng = random.Random(day * 101 + number * 1009)
    indices = rng.sample(range(len(SHORT_PATTERNS[kind])), 5)
    words = [item["word"] for item in items]
    meanings = [gloss(item) for item in items]
    en, zh = [], []
    for index, template_index in enumerate(indices):
        template = SHORT_PATTERNS[kind][template_index]
        offset = index * 2
        en.append(template.format(
            s=setting_en, a=words[offset], ad=items[offset]["_definition"],
            b=words[offset + 1], bd=items[offset + 1]["_definition"]))
        zh.append(SEMANTIC_ZH[kind][template_index].format(
            s=setting_zh, a=meanings[offset], b=meanings[offset + 1]))
    return en, zh


def concise_definition(text: str) -> str:
    first = re.split(r"[;(,:]|\b(?:that|which|who|usually|especially|when|where|because|resulting|having|male|made|consisting|characterized|marked)\b", text, maxsplit=1)[0]
    words = re.findall(r"[A-Za-z]+(?:[-'][A-Za-z]+)*", first)
    if not words:
        words = re.findall(r"[A-Za-z]+(?:[-'][A-Za-z]+)*", text)
    words = words[:10]
    trailing = {"of", "to", "in", "by", "and", "or", "with", "from", "as", "for", "the", "a", "an"}
    while len(words) > 3 and words[-1].casefold() in trailing:
        words.pop()
    return " ".join(words)


def noun_items(source: dict) -> list[dict]:
    candidates = []
    for item in source["items"]:
        word = item["word"]
        meaning = item.get("meaning", "").strip().lower()
        if word.casefold() in BLOCKED or not re.fullmatch(r"[A-Za-z][A-Za-z -]*", word):
            continue
        if not (meaning.startswith(("n.", "n/", "n．")) or re.match(r"^n\s", meaning)):
            continue
        synsets = wn.synsets(word.replace("-", "_").replace(" ", "_"), pos=wn.NOUN)
        if not synsets:
            continue
        synset = synsets[0]
        enriched = dict(item)
        enriched["_lexname"] = synset.lexname()
        enriched["_definition"] = concise_definition(synset.definition())
        candidates.append(enriched)

    preferences = {
        "story": {"noun.artifact", "noun.person", "noun.location", "noun.food", "noun.object"},
        "explanatory": {"noun.animal", "noun.plant", "noun.substance", "noun.body", "noun.phenomenon", "noun.process"},
        "opinion": {"noun.cognition", "noun.communication", "noun.act", "noun.attribute", "noun.state", "noun.group", "noun.possession", "noun.relation"},
    }
    remaining = list(candidates)
    groups: dict[str, list[dict]] = {}
    # Fill the most specialized scientific group first, then abstract public
    # issues, leaving people, places, and artifacts for the story.
    for kind in ("explanatory", "opinion", "story"):
        preferred = [item for item in remaining if item["_lexname"] in preferences[kind]]
        selected = preferred[:10]
        if len(selected) < 10:
            selected += [item for item in remaining if item not in selected][:10 - len(selected)]
        groups[kind] = selected
        selected_words = {item["word"].casefold() for item in selected}
        remaining = [item for item in remaining if item["word"].casefold() not in selected_words]
    if any(len(items) != 10 for items in groups.values()):
        raise ValueError(f"Day {source['day']} 无法选出三组各十个语义目标词")
    return groups["story"] + groups["explanatory"] + groups["opinion"]


def gloss(item: dict) -> str:
    text = item.get("meaning", "")
    text = re.sub(r"^[A-Za-z./\[\] -]+", "", text).strip(" ,;，；")
    text = re.split(r"[;；]", text, maxsplit=1)[0].strip()
    return f"{text}（{item['word']}）"


def title_word(word: str) -> str:
    return " ".join(part.capitalize() for part in word.split())


def story(day: int, setting_en: str, setting_zh: str, items: list[dict]) -> dict:
    w = [item["word"] for item in items]
    z = [gloss(item) for item in items]
    en, zh = diverse_pairs(day, 1, "story", setting_en, setting_zh, items)
    return make_article(day, 1, f"The {title_word(w[9])} File", "story", items, en, zh,
                        ("What did the visitors use to understand the displays?", "Labels, records, examples, and help from staff.", "访客借助标签、记录、实例和工作人员的讲解理解展品。"),
                        ("Which final target appears in this account?", w[9], f"最后一个目标词是{z[9]}。"))


def explanatory(day: int, setting_en: str, setting_zh: str, items: list[dict]) -> dict:
    w = [item["word"] for item in items]
    z = [gloss(item) for item in items]
    en, zh = diverse_pairs(day, 2, "explanatory", setting_en, setting_zh, items)
    return make_article(day, 2, f"Understanding {title_word(w[0])} Through Evidence", "explanatory", items, en, zh,
                        ("Why are the terms defined separately?", "To prevent false comparisons and ambiguous use.", "分别定义可避免错误比较和含糊用法。"),
                        ("How do learners test their understanding?", "They compare definitions with new examples.", "学习者把定义与新实例进行比较。"))


def opinion(day: int, setting_en: str, setting_zh: str, items: list[dict]) -> dict:
    w = [item["word"] for item in items]
    z = [gloss(item) for item in items]
    en, zh = diverse_pairs(day, 3, "opinion", setting_en, setting_zh, items)
    return make_article(day, 3, f"Why {title_word(w[9])} Needs an Open Debate", "opinion", items, en, zh,
                        ("What should support the public decision?", "Clear definitions, local evidence, and published responsibilities.", "公共决定应有清楚定义、地方证据和公开责任作为支撑。"),
                        ("Why is an open debate useful?", "It exposes costs, uncertainty, and unequal risk.", "公开讨论能揭示成本、不确定性和不均等风险。"))


def make_article(day, number, title, kind, items, en, zh, q1, q2):
    sentences = [{"en": left, "zh": right} for left, right in zip(en, zh)]
    return {
        "id": f"cet4-reading-d{day:03}-{number}",
        "title": title,
        "type": kind,
        "difficulty": "CET-4+",
        "text": " ".join(en),
        "translation": "".join(zh),
        "sentences": sentences,
        "target_words": [{"word": item["word"], "meaning": item["meaning"]} for item in items],
        "questions": [
            {"prompt": q1[0], "answer": q1[1], "explanation": q1[2]},
            {"prompt": q2[0], "answer": q2[1], "explanation": q2[2]},
        ],
    }


def rebuild_index() -> tuple[int, int]:
    files = sorted(OUT_DIR.glob("day-*.json"))
    numbers = [int(path.stem.split("-")[1]) for path in files]
    if numbers != list(range(1, len(files) + 1)):
        raise ValueError(f"阅读文件必须从 Day 1 连续编号：{numbers}")
    days, count = [], 0
    for day, path in zip(numbers, files):
        amount = len(json.loads(path.read_text(encoding="utf-8")).get("articles", []))
        days.append({"day": day, "file": path.name, "count": amount})
        count += amount
    index = {
        "schema_version": 1,
        "id": "cet4_context_readings",
        "wordlist_id": "cet4_combined",
        "title": "四级词汇语境阅读",
        "description": "与单词库 Day 对应；每个 Day 包含故事、说明文和观点文各一篇，并支持逐句显示中文。",
        "tags": ["四级", "语境阅读", "逐句翻译"],
        "article_count": count,
        "day_count": len(days),
        "days": days,
    }
    (OUT_DIR / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    manifest = {"schema_version": 1, "collections": [{"id": index["id"], "index": "cet4_combined/index.json"}]}
    (OUT_DIR.parent / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return len(days), count


def main():
    if len(SETTINGS) != 55:
        raise ValueError(f"场景数量应为 55，实际为 {len(SETTINGS)}")
    for offset, day in enumerate(range(41, 96)):
        source = json.loads((WORD_DIR / f"day-{day:03}.json").read_text(encoding="utf-8"))
        selected = noun_items(source)
        setting_en, setting_zh = SETTINGS[offset]
        articles = [
            story(day, setting_en, setting_zh, selected[0:10]),
            explanatory(day, setting_en, setting_zh, selected[10:20]),
            opinion(day, setting_en, setting_zh, selected[20:30]),
        ]
        payload = {
            "schema_version": 1,
            "collection_id": "cet4_context_readings",
            "wordlist_id": "cet4_combined",
            "day": day,
            "articles": articles,
        }
        (OUT_DIR / f"day-{day:03}.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    days, articles = rebuild_index()
    print(f"Wrote Day 41-95; index now contains {days} days / {articles} articles")


if __name__ == "__main__":
    main()
