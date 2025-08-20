from config import MEMORY_WINDOW

def validate_memory(payload):
    memory_trace = payload.get("memory", [])
    return {
        "valid": len(memory_trace) >= MEMORY_WINDOW,
        "trace": memory_trace[-MEMORY_WINDOW:]
    }
