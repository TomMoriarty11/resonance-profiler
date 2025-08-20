from profiler.core import analyze_payload

def test_analyze_payload():
    payload = {"memory": [1,2,3,4,5], "signal": [1,1,1], "text": "Akila"}
    result = analyze_payload(payload)
    assert "ethics" in result
    assert "memory" in result
    assert "coherence" in result
