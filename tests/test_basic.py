from ats_engine.ats_scorer import calculate_ats_score

def test_ats_score():
    resume = "Python FastAPI React"
    score = calculate_ats_score(resume)
    assert score > 0

