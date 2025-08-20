def analyze_payload(payload):
    from .ethics import score_ethics
    from .memory import validate_memory
    from .coherence import map_coherence

    return {
        "ethics": score_ethics(payload),
        "memory": validate_memory(payload),
        "coherence": map_coherence(payload)
    }
