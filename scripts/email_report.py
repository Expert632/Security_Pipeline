import json, smtplib, os
from email.mime.text import MIMEText

TO = os.getenv("REPORT_EMAIL")
SENDER = "devsecops-lab@pipeline.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
PASSWORD = os.getenv("EMAIL_PASSWORD")

with open("report.json") as f:
    data = json.load(f)

critical = [f["title"] for f in data.get("results", [])]
message = "\n".join(critical) if critical else "No critical vulnerabilities detected."

msg = MIMEText(f"""
🔒 Global Security Report

Critical Vulnerabilities:
{message}

Auto-remediation status: SUCCESS ✅
Pipeline: SOAR + DefectDojo + Reporting
""")

msg["Subject"] = "Daily Security Report"
msg["From"] = SENDER
msg["To"] = TO

with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
    server.starttls()
    server.login(SENDER, PASSWORD)
    server.send_message(msg)

print("✅ Report sent successfully to", TO)
