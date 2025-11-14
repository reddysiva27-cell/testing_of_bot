import requests

def judge_response(prompt: str, expected: str, actual: str, model: str = "mistral") -> str:
    """
    Calls Ollama Judge model to evaluate bot's answer.
    """
    judge_prompt = (
        f"Evaluate the bot's response.\n"
        f"Prompt: {prompt}\n"
        f"Expected: {expected}\n"
        f"Actual: {actual}\n"
        f"Verdict (Correct/Partial/Incorrect) with reasoning:"
    )

    payload = {"model": model, "prompt": judge_prompt}
    response = requests.post("http://localhost:11434/api/generate", json=payload)
    response.raise_for_status()
    return response.json().get("response", "")
