from config import ETHICAL_THRESHOLD

def score_ethics(payload):
    score = sum(ord(c) for c in str(payload)) % 100 / 100
    return {
        "score": score,
        "aligned": score >= ETHICAL_THRESHOLD
    }
