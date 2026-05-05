import numpy as np
import time
from numba import cuda

from generator import generate_candidates, CHARSET
from hashing import md5_hash

def brute_force_gpu(target_hash: str, max_len: int = 4, batch_cap: int = 500_000):
    start = time.time()

    for length in range(1, max_len + 1):
        print(f"[GPU] Trying length = {length}")

        total = len(CHARSET) ** length
        batch_size = min(total, batch_cap)

        # siapkan data
        indices = np.arange(batch_size, dtype=np.int32)
        output = np.zeros((batch_size, length), dtype=np.int32)

        # kirim ke GPU
        d_indices = cuda.to_device(indices)
        d_output = cuda.to_device(output)

        threads = 256
        blocks = (batch_size + threads - 1) // threads

        # generate kandidat di GPU
        generate_candidates[blocks, threads](d_indices, length, d_output)
        cuda.synchronize()

        # ambil hasil
        results = d_output.copy_to_host()

        # hashing + compare di CPU (hybrid approach)
        for row in results:
            password = ''.join(CHARSET[i] for i in row)

            if md5_hash(password) == target_hash:
                elapsed = time.time() - start
                print(f"[GPU FOUND] {password}")
                print(f"[GPU TIME] {elapsed:.4f}s")
                return password, elapsed

    print("[GPU] Not found")
    return None, time.time() - start
