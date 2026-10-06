from app.content.schema import LibraryValidationError, validate_library
from app.content.library_loader import LibraryLoader
from app.database import Database
from app.services.answer_checker import AnswerChecker, normalize_answer
from app.services.progress_service import ProgressService
from app.content.wordlist_loader import WordlistLoader, WordlistValidationError
def test_normalize(): assert normalize_answer("  I’m   HERE!!! ")=="i'm here"
def test_answers(): assert AnswerChecker().check("I am completely over you",["I'm completely over you.","I am completely over you."]).correct
def test_duplicate_item():
    data={"schema_version":1,"id":"x","title":"X","items":[{"id":"a","zh":"甲","en":"A"},{"id":"a","zh":"乙","en":"B"}]}
    try: validate_library(data,"x.json"); assert False
    except LibraryValidationError: pass
def test_loader_invalid(tmp_path):
    (tmp_path/'bad.json').write_text('{bad',encoding='utf8'); loader=LibraryLoader(tmp_path); assert loader.load_all()=={} and loader.errors
def test_progress(tmp_path):
    db=Database(tmp_path/'x.db'); p=ProgressService(db); p.record('l','i','A',True); p.record('l','i','B',False); assert p.stats('l')['correct']==1 and p.stats('l')['wrong']==1; db.close()


def test_wordlist_loader(tmp_path):
    root=tmp_path/'wordlists'; folder=root/'sample'; folder.mkdir(parents=True)
    items=[]
    for number in range(2):
        items.append({"id":f"word_{number}","word":f"word{number}","meaning":f"含义{number}","phonetic":"","options":[{"text":f"含义{number}","correct":True},{"text":"甲","correct":False},{"text":"乙","correct":False},{"text":"丙","correct":False}]})
    import json
    (root/'manifest.json').write_text(json.dumps({"schema_version":1,"wordlists":[{"id":"sample","index":"sample/index.json"}]}),encoding='utf8')
    (folder/'index.json').write_text(json.dumps({"schema_version":1,"id":"sample","title":"示例","day_size":100,"word_count":2,"day_count":1,"days":[{"day":1,"file":"day-001.json","count":2}]}),encoding='utf8')
    (folder/'day-001.json').write_text(json.dumps({"schema_version":1,"wordlist_id":"sample","day":1,"items":items}),encoding='utf8')
    loader=WordlistLoader(root); indexes=loader.load_all(); assert not loader.errors
    assert loader.load_day(indexes['sample'],1)['items'][1]['word']=='word1'


def test_wordlist_rejects_duplicate_options(tmp_path):
    root=tmp_path/'wordlists'; folder=root/'sample'; folder.mkdir(parents=True)
    import json
    (root/'manifest.json').write_text(json.dumps({"schema_version":1,"wordlists":[{"index":"sample/index.json"}]}),encoding='utf8')
    (folder/'index.json').write_text(json.dumps({"schema_version":1,"id":"sample","title":"示例","day_size":100,"word_count":1,"day_count":1,"days":[{"day":1,"file":"day.json","count":1}]}),encoding='utf8')
    item={"id":"word_1","word":"sample","meaning":"样例","options":[{"text":"重复","correct":True}]*4}
    (folder/'day.json').write_text(json.dumps({"schema_version":1,"wordlist_id":"sample","day":1,"items":[item]}),encoding='utf8')
    loader=WordlistLoader(root); index=loader.load_all()['sample']
    try: loader.load_day(index,1); assert False
    except WordlistValidationError: pass
