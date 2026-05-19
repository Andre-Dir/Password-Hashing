import itertools
import string
import time
from concurrent.futures import ThreadPoolExecutor

from hashing import md5_hash


def check_passwords(password_list, target_hash):
    for password in password_list:
        if md5_hash(password) == target_hash:
            return password
    return None


def generate_combinations(charset, length):
    return [
        ''.join(p)
        for p in itertools.product(charset, repeat=length)
    ]


def brute_force_cpu(
    target_hash: str,
    max_len: int = 4,
    n_threads: int = 4,
    charset: str = None
):

    if charset is None:
        charset = string.ascii_lowercase

    start = time.time()

    print(f"[CPU] Running with {n_threads} threads")

    for length in range(1, max_len + 1):

        combinations = generate_combinations(charset, length)

        chunk_size = max(1, len(combinations) // n_threads)

        chunks = [
            combinations[i:i + chunk_size]
            for i in range(0, len(combinations), chunk_size)
        ]

        with ThreadPoolExecutor(max_workers=n_threads) as executor:

            futures = [
                executor.submit(
                    check_passwords,
                    chunk,
                    target_hash
                )
                for chunk in chunks
            ]

            for future in futures:
                result = future.result()

                if result:
                    elapsed = time.time() - start

                    print(f"[CPU FOUND] {result}")
                    print(f"[CPU TIME] {elapsed:.4f}s")

                    return result, elapsed

    print("[CPU] Not found")
    return None, time.time() - start