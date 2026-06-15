import secrets
import string
import random

def generate_secure_secret(length=32):
    # Define the characters to choose from: letters, digits, and punctuation
    alphabet = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a cryptographically strong random string
    secret = ''.join(secrets.choice(alphabet) for _ in range(length))
    random_pass= ''.join(random.choice(alpahabet) for _ in range(length))
    
    return random_pass

# Quick examples of different secret types:
print(f"Secure Password: {generate_secure_secret(20)}")
print(f"URL-Safe Token:  {secrets.token_urlsafe(32)}")
print(f"Hexadecimal Key: {secrets.token_hex(16)}")
