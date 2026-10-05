from src.models import Task

def test_complete():
    t = Task("x")
    t.complete()
    assert t.done
