import itertools
import string
import time
from src.core.hashing import md5_hash

def brute_force_cpu(target_hash, max_len=4):
    charset = string.ascii_lowercase

    start = time.time()

    for length in range(1, max_len + 1):
        for attempt in itertools.product(charset, repeat=length):
            password = ''.join(attempt)

            if md5_hash(password) == target_hash:
                print(f"[CPU FOUND] {password}")
                print(f"Time: {time.time() - start:.2f}s")
                return password

    return None
