from app.content.schema import LibraryValidationError, validate_library
from app.content.library_loader import LibraryLoader
from app.database import Database
from app.services.answer_checker import AnswerChecker, normalize_answer
from app.services.progress_service import ProgressService
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
