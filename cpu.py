import itertools
import string
import time
from hashing import md5_hash

def brute_force_cpu(target_hash: str, max_len: int = 4, charset: str = None):
    if charset is None:
        charset = string.ascii_lowercase

    start = time.time()

    for length in range(1, max_len + 1):
        for attempt in itertools.product(charset, repeat=length):
            password = ''.join(attempt)

            if md5_hash(password) == target_hash:
                elapsed = time.time() - start
                print(f"[CPU FOUND] {password}")
                print(f"[CPU TIME] {elapsed:.4f}s")
                return password, elapsed

    print("[CPU] Not found")
    return None, time.time() - start
