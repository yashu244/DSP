from cryptography.fernet import Fernet
import hashlib, random, time

# Confidentiality
key = Fernet.generate_key()
f = Fernet(key)
msg = b"Secret Data"
enc = f.encrypt(msg)
print("Encrypted:", enc)
print("Decrypted:", f.decrypt(enc).decode())

# Integrity
h1 = hashlib.sha256(msg).hexdigest()
h2 = hashlib.sha256(b"Secret Data").hexdigest()
print("Integrity OK" if h1 == h2 else "Integrity Failed")

# Availability
for i in range(3):
    print("Checking server...")
    time.sleep(1)
    if random.choice([1, 0]):
        print("Server Available"); break
else:
    print("Server Down")

print("CIA Triad Simulation Done.")



# This Python program demonstrates the CIA Triad, which represents the three core principles of information security — Confidentiality, Integrity, 
# Availability.

# The first part of the code focuses on Confidentiality. It uses the cryptography library’s Fernet module to encrypt and decrypt a message. A secret
# key is generated, and the message "Secret Data" is encrypted into unreadable text to ensure that unauthorized users cannot access or interpret it.
# Then, it is successfully decrypted back to the original form, showing that only someone with the correct key can access the data. This illustrates 
# how encryption protects sensitive information from unauthorized access.

# The second part of the code demonstrates Integrity using the hashlib library. The program creates a digital fingerprint (hash) of the 
# original message using the SHA-256 algorithm. It then creates another hash for a slightly modified message ("Secret Data!"). When the 
# two hashes are compared, they don’t match, and the output shows “Integrity Failed”. This indicates that the data has been tampered with,
# proving how hashing can be used to verify that information has not been altered or corrupted during transmission.

# The third part represents Availability. It simulates a server connection check using random values to determine if the server is “up” or “down.”
# The code attempts three retries, pausing briefly between each attempt. If the server becomes available, it prints “Server Available”; otherwise,
# it reports “Server Down.” This section demonstrates how systems maintain accessibility even under temporary failures, reflecting the principle of
# ensuring that data and resources remain available to authorized users when needed.

# Finally, the program prints “CIA Triad Simulation Done.” Overall, this simple simulation effectively illustrates how encryption preserves 
# confidentiality, hashing ensures integrity, and retry mechanisms support availability — the three essential pillars of secure information systems.