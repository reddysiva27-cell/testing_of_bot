from difflib import SequenceMatcher

def similarity_score(expected: str, actual: str) -> float:
    return SequenceMatcher(None, expected.lower(), actual.lower()).ratio()
