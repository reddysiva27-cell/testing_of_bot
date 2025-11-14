import requests

def run_bot(prompt: str, context_docs: list[str], model: str = "llama2") -> str:
    """
    Calls Ollama Bot model with prompt + context.
    """
    payload = {
        "model": model,
        "prompt": f"Context:\n{''.join(context_docs)}\n\nUser: {prompt}\nAnswer:"
    }
    response = requests.post("http://localhost:11434/api/generate", json=payload)
    response.raise_for_status()
    return response.json().get("response", "")
