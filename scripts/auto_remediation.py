import json, os, subprocess

with open("critical.json") as f:
    findings = json.load(f)

for finding in findings.get("results", []):
    vuln_type = finding["title"]
    component = finding["component_name"]
    print(f"Auto-remediating {vuln_type} in {component}...")

    # Exemple : mise à jour dépendance vulnérable
    if "npm" in component:
        subprocess.run(["npm", "update", component])
    elif "pip" in component:
        subprocess.run(["pip", "install", "--upgrade", component])
