
import os, re

def check_file(file_path):
    issues = []
    with open(file_path, 'r', errors='ignore') as f:
        for num, line in enumerate(f, 1):
            if "SELECT" in line and "+" in line:
                issues.append((file_path, num, "Possible SQL Injection"))
            if "<script>" in line.lower():
                issues.append((file_path, num, "Possible XSS"))
            if any(word in line.lower() for word in ["password", "key", "token"]):
                issues.append((file_path, num, "Hardcoded Secret"))
            if "eval(" in line:
                issues.append((file_path, num, "Uses eval() - Risky"))
            if "os.system" in line or "subprocess.call" in line:
                issues.append((file_path, num, "Command Execution Risk"))
    return issues

folder = input("Enter folder path: ")
found = []

for root, dirs, files in os.walk(folder):
    for name in files:
        if name.endswith(('.py', '.js', '.html', '.php')):
            found += check_file(os.path.join(root, name))

if found:
    for f, n, i in found:
        print(f"File: {f} | Line: {n} | Issue: {i}")
else:
    print("✅ No issues found!")