# k_anonymity.py — simple k-anonymity demonstration
import pandas as pd

# Sample dataset (PII)
data = {
    "Name": ["Alice","Bob","Charlie","David","Eve","Frank"],
    "Age": [34, 36, 34, 35, 36, 34],
    "Zip": ["12345","12346","12345","12346","12345","12346"],
    "Disease": ["Flu","Cold","Flu","Allergy","Cold","Flu"]
}

df = pd.DataFrame(data)
print("Original Data:\n", df)

# --- Define quasi-identifiers and k ---
quasi_identifiers = ["Age","Zip"]
k = 2

# --- Simple generalization to achieve k-anonymity ---
# Generalize age to 5-year ranges
df["Age"] = df["Age"].apply(lambda x: f"{x//5*5}-{x//5*5+4}")

# Generalize zip to first 4 digits
df["Zip"] = df["Zip"].str[:4] + "X"

# Check k-anonymity: count duplicates in quasi-identifiers
group_counts = df.groupby(quasi_identifiers).size()
print("\nGroup counts (for k-anonymity check):\n", group_counts)

# Identify groups violating k-anonymity
violations = group_counts[group_counts < k]
print("\nGroups violating k-anonymity:\n", violations)

print("\nAnonymized Data:\n", df)
