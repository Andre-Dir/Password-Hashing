import numpy as np
from numba import cuda

CHARSET = "abcdefghijklmnopqrstuvwxyz0123456789"
CHARSET_SIZE = len(CHARSET)

@cuda.jit
def generate_candidates(indices, length, output):
    idx = cuda.grid(1)

    if idx < indices.size:
        val = indices[idx]

        for i in range(length):
            char_index = val % CHARSET_SIZE
            output[idx, i] = char_index
            val //= CHARSET_SIZE
