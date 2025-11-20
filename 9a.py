# pii_classifier.py — simple PII detection and classification
import re, sys, os

# --- Define PII patterns ---
patterns = {
    "Email": r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
    "Phone": r"\b\d{10}\b",
    "Name": r"\b[A-Z][a-z]+ [A-Z][a-z]+\b",
    "Aadhaar": r"\b\d{4}\s\d{4}\s\d{4}\b"
}

def detect_pii(text):
    found = []
    for k, p in patterns.items():
        if re.search(p, text):
            found.append(k)
    return found or ["None"]

def classify_data(file_path):
    if not os.path.exists(file_path):
        print("File not found:", file_path)
        return

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        data = f.read()

    pii = detect_pii(data)
    data_type = "Structured" if file_path.endswith(('.csv', '.xlsx')) else "Unstructured"
    data_state = "At Rest"  # assuming local file for simplicity

    print(f"📁 File: {file_path}")
    print(f"🔹 Data Type: {data_type}")
    print(f"🔹 Data State: {data_state}")
    print(f"🔹 Detected PII: {', '.join(pii)}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python pii_classifier.py <file>")
        sys.exit(1)
    classify_data(sys.argv[1])
