"""
expected_runner.py
Deterministic evaluation against predefined expected answers.
"""

def check_expected(expected: str, actual: str) -> str:
    """
    Simple deterministic check.
    :param expected: Expected answer string
    :param actual: Bot's actual answer
    :return: PASS/FAIL verdict
    """
    if expected.strip().lower() in actual.strip().lower():
        return "PASS"
    return "FAIL"
