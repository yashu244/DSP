from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

message = b"This is a secret message"

# Sign the message
signature = private_key.sign(
    message,
    padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
    hashes.SHA256()
)

# Verify signature
try:
    public_key.verify(
        signature,
        message,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )
    print("✅ Signature verified — message is authentic.")
except Exception as e:
    print("❌ Verification failed:", e)
# (Optional) Serialize keys to PEM if you want to save/load:
# priv_pem = priv.private_bytes(encoding=serialization.Encoding.PEM,
#                              format=serialization.PrivateFormat.PKCS8,
#                              encryption_algorithm=serialization.NoEncryption())
# pub_pem = pub.public_bytes(encoding=serialization.Encoding.PEM,
#                            format=serialization.PublicFormat.SubjectPublicKeyInfo)
