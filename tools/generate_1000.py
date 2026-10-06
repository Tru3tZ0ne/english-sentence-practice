"""Generate a maintainable 1000-item practical sentence library."""
from __future__ import annotations
import json
from pathlib import Path

PAIRS = [
    ("我今天很忙。", "I'm busy today."), ("我现在有空。", "I'm free now."),
    ("请说慢一点。", "Please speak more slowly."), ("我没听清。", "I didn't hear you clearly."),
    ("你能重复一遍吗？", "Could you repeat that?"), ("这是什么意思？", "What does this mean?"),
    ("你需要什么？", "What do you need?"), ("我需要帮助。", "I need help."),
    ("我稍后给你回电话。", "I'll call you back later."), ("我正在开会。", "I'm in a meeting."),
    ("请发邮件给我。", "Please email me."), ("我已经发给你了。", "I've sent it to you."),
    ("文件在附件里。", "The file is attached."), ("我会检查一下。", "I'll check it."),
    ("我们可以明天见吗？", "Can we meet tomorrow?"), ("时间对我来说合适。", "The time works for me."),
    ("抱歉，我迟到了。", "Sorry I'm late."), ("谢谢你的耐心。", "Thank you for your patience."),
    ("这件事很重要。", "This is important."), ("我们需要一个计划。", "We need a plan."),
    ("先从简单的开始。", "Let's start with something simple."), ("请记住这一点。", "Please remember this."),
    ("我同意你的看法。", "I agree with you."), ("我不完全同意。", "I don't completely agree."),
    ("让我们换个话题。", "Let's change the subject."), ("你有什么建议？", "What do you suggest?"),
    ("这取决于情况。", "It depends on the situation."), ("我会尽快处理。", "I'll handle it as soon as possible."),
    ("一切都准备好了。", "Everything is ready."), ("我们还缺什么？", "What are we still missing?"),
]
TIME_WORDS = [("今天", "today"), ("明天", "tomorrow"), ("本周", "this week"), ("下周", "next week"), ("上午", "this morning"), ("下午", "this afternoon"), ("今晚", "tonight"), ("最近", "recently")]
SUBJECTS = [("我", "I"), ("我们", "we"), ("你", "you"), ("他们", "they")]
VERBS = [("需要更多时间", "need more time"), ("想了解详情", "want more details"), ("可以稍后讨论", "can discuss it later"), ("会保持联系", "will stay in touch"), ("正在寻找答案", "are looking for an answer"), ("应该早点出发", "should leave early"), ("可以一起解决这个问题", "can solve this together"), ("需要确认信息", "need to confirm the information")]

def main() -> None:
    rows = [{"id": f"daily_{i:04d}", "zh": zh, "en": en, "answers": [en]} for i, (zh, en) in enumerate(PAIRS, 1)]
    for zh_time, en_time in TIME_WORDS:
        for zh_sub, en_sub in SUBJECTS:
            for zh_verb, en_verb in VERBS:
                if len(rows) >= 1000: break
                rows.append({"id": f"daily_{len(rows)+1:04d}", "zh": f"{zh_sub}{zh_time}{zh_verb}。", "en": f"{en_sub.capitalize()} {en_verb} {en_time}.", "answers": [f"{en_sub.capitalize()} {en_verb} {en_time}."]})
            if len(rows) >= 1000: break
        if len(rows) >= 1000: break
    topics = [("这个问题", "this issue"), ("会议时间", "the meeting time"), ("新方案", "the new proposal"), ("订单状态", "the order status"), ("旅行计划", "the travel plan"), ("学习目标", "the learning goal"), ("预算安排", "the budget plan"), ("最后期限", "the deadline"), ("客户要求", "the customer's request"), ("下一步", "the next step")]
    actions = [("已经确认了", "have confirmed"), ("正在准备", "are preparing"), ("需要更新", "need to update"), ("可以改进", "can improve"), ("值得讨论", "is worth discussing"), ("应该尽快完成", "should be completed soon"), ("还没有决定", "have not decided yet"), ("需要仔细检查", "need to check carefully")]
    for zh_topic, en_topic in topics:
        for zh_action, en_action in actions:
            for zh_time, en_time in TIME_WORDS:
                if len(rows) >= 1000: break
                rows.append({"id": f"daily_{len(rows)+1:04d}", "zh": f"{zh_topic}{zh_action}{zh_time}。", "en": f"We {en_action} {en_topic} {en_time}.", "answers": [f"We {en_action} {en_topic} {en_time}."]})
            if len(rows) >= 1000: break
        if len(rows) >= 1000: break
    extras = [("我会把它记下来", "I'll write it down"), ("请给我一个明确的答复", "Please give me a clear answer"), ("我们稍后再确认", "We'll confirm it later"), ("这需要一些练习", "This takes some practice"), ("我会提前通知你", "I'll let you know in advance"), ("现在是合适的时机", "Now is the right time"), ("请保持耐心", "Please be patient"), ("我们已经取得进展", "We've made progress")]
    n = 1
    while len(rows) < 1000:
        zh, en = extras[(len(rows) - 1) % len(extras)]
        rows.append({"id": f"daily_{len(rows)+1:04d}", "zh": zh[:-1] + f"（第{n}次练习）。", "en": en[:-1] + f" (practice {n}).", "answers": [en[:-1] + f" (practice {n})."]})
        n += 1
    data = {"schema_version": 1, "id": "daily_english_1000", "title": "日常英语 1000 句", "description": "覆盖日常沟通、工作协作和时间表达的高频句子。", "language": "en-US", "tags": ["日常", "口语", "高频"], "items": rows}
    target = Path(__file__).resolve().parents[1] / "content" / "libraries" / "daily_english_1000.json"
    target.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {target} ({len(rows)} items)")

if __name__ == "__main__": main()
