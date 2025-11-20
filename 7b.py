# file: obfuscation_demo.py
import base64

# Encoded function body (Base64 of: def secret_function(x, y):\n    return (x/y )*2)
encoded_logic = base64.b64encode(b"def secret_function(x, y):\n    return (x/y )*2").decode()

def load_obfuscated_function():
    decoded = base64.b64decode(encoded_logic).decode()
    exec(decoded, globals())  # dynamically define secret_function in globals()

if __name__ == "__main__":
    load_obfuscated_function()
    result = secret_function(5, 7)
    print("Result of secret_function(5,7):", result)
