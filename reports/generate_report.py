password = input("Enter password: ")
strength = input("Enter strength: ")
entropy = float(input("Enter entropy: "))

report = f"""
Password Audit Report
=====================

Password:
{password}

Strength:
{strength}

Entropy:
{entropy} bits

Recommendation:
Use long and unique passwords.
"""

with open("reports/report.txt", "w") as file:
    file.write(report)

print("Report generated successfully.")
