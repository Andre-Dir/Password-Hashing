import hashlib

def md5_hash(text: str) -> str:
    return hashlib.md5(text.encode()).hexdigest()

def sha256_hash(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()