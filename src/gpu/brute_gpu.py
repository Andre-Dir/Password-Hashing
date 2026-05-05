import numpy as np
import time
from numba import cuda

from src.core.generator import generate_candidates, CHARSET
from src.core.hashing import md5_hash

def brute_force_gpu(target_hash, length=3):
    start = time.time()

    total = len(CHARSET) ** length
    batch_size = min(total, 1000000)

    indices = np.arange(batch_size, dtype=np.int32)
    output = np.zeros((batch_size, length), dtype=np.int32)

    d_indices = cuda.to_device(indices)
    d_output = cuda.to_device(output)

    threads = 256
    blocks = (batch_size + threads - 1) // threads

    generate_candidates[blocks, threads](d_indices, length, d_output)

    results = d_output.copy_to_host()

    for row in results:
        password = ''.join(CHARSET[i] for i in row)

        if md5_hash(password) == target_hash:
            print(f"[GPU FOUND] {password}")
            print(f"Time: {time.time() - start:.2f}s")
            return password

    print("Not found")
    return None
