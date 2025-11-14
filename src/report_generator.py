"""
report_generator.py
Generates HTML report from test results.
"""

def generate_html_report(results: list[dict]) -> str:
    """
    Builds an HTML table report.
    :param results: List of test case results
    :return: HTML string
    """
    html = "<h1>Bot Test Report</h1><table border=1>"
    html += "<tr><th>ID</th><th>Prompt</th><th>Expected</th><th>Actual</th><th>Verdicts</th></tr>"
    for r in results:
        verdicts = ", ".join([f"{k}: {v}" for k, v in r["verdicts"].items()])
        html += f"<tr><td>{r['id']}</td><td>{r['prompt']}</td><td>{r['expected']}</td><td>{r['actual']}</td><td>{verdicts}</td></tr>"
    html += "</table>"
    return html
