"""
test_executor.py
Main orchestrator: runs bot, judge, and/or expected checks based on config.
"""

import yaml, json, argparse
from src.bot_runner import run_bot
from src.judge_runner import judge_response
from src.expected_runner import check_expected
from src.report_generator import generate_html_report
from src.email_sender import send_email

def execute_tests(config_file: str, test_file: str, context_docs: list[str]):
    # Load global config
    with open(config_file) as f:
        config = yaml.safe_load(f)
    with open(test_file) as f:
        tests = json.load(f)

    results = []
    for case in tests:
        actual = run_bot(case["prompt"], context_docs, config["bot"]["endpoint"])
        verdicts = {}

        if config["test_mode"] in ["expected", "both"]:
            verdicts["expected"] = check_expected(case["expected"], actual)

        if config["test_mode"] in ["judge", "both"]:
            verdicts["judge"] = judge_response(
                case["prompt"], case["expected"], actual,
                config["judge"]["endpoint"], config["judge"]["model"]
            )

        results.append({
            "id": case["id"],
            "prompt": case["prompt"],
            "expected": case["expected"],
            "actual": actual,
            "verdicts": verdicts
        })

    report = generate_html_report(results)
    send_email(report, config["report"]["email"])


def main():
    parser = argparse.ArgumentParser(description="Bot Test Harness Executor")
    parser.add_argument("--config", required=True, help="Path to settings.yaml")
    parser.add_argument("--suite", required=True, help="Path to test suite JSON")
    parser.add_argument("--docs", nargs="+", required=True, help="List of context docs (Markdown files)")
    args = parser.parse_args()

    # Load context docs
    context_docs = []
    for doc in args.docs:
        with open(doc) as f:
            context_docs.append(f.read())

    execute_tests(args.config, args.suite, context_docs)


if __name__ == "__main__":
    main()
