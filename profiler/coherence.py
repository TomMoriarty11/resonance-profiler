from config import COHERENCE_TOLERANCE

def map_coherence(payload):
    signal = payload.get("signal", [])
    coherence = abs(sum(signal) - len(signal)) / max(len(signal), 1)
    return {
        "coherence": coherence,
        "stable": coherence <= COHERENCE_TOLERANCE
    }
