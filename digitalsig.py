import hashlib
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa

def generate_keys():
    private_key = dsa.generate_private_key(key_size=2048, backend=default_backend())
    public_key = private_key.public_key()
    return private_key, public_key

def sign_message(private_key, message):
    message_hash = hashlib.sha256(message.encode()).digest()
    
    signature = private_key.sign(
        message_hash,
        hashes.SHA256()
    )
    return signature

def verify_signature(public_key, message, signature):
    message_hash = hashlib.sha256(message.encode()).digest()
    try:
        public_key.verify(signature, message_hash, hashes.SHA256()) 
        return True
    except Exception:
        return False

if __name__ == "__main__":
    private_key, public_key = generate_keys()

    message = input("Enter your message: ")
    
    signature = sign_message(private_key, message)
    print(f"Signature: {signature.hex()}")

    is_valid = verify_signature(public_key, message, signature)
    print(f"Is the signature valid? {is_valid}")