"""
email_sender.py
Sends report via SMTP.
"""

import smtplib
from email.mime.text import MIMEText

def send_email(report_html: str, to_email: str, smtp_server: str = "smtp.company.com"):
    """
    Sends HTML report via email.
    :param report_html: HTML report string
    :param to_email: Recipient email
    :param smtp_server: SMTP server address
    """
    msg = MIMEText(report_html, "html")
    msg["Subject"] = "Bot Test Execution Report"
    msg["From"] = "qa-bot@company.com"
    msg["To"] = to_email

    with smtplib.SMTP(smtp_server) as server:
        server.send_message(msg)
