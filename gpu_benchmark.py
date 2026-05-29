import pandas as pd

from cpu import brute_force_cpu
from gpu import brute_force_gpu

TARGET_HASH = "900150983cd24fb0d6963f7d28e17f72"

results = []

# CPU Sequential

_, cpu1 = brute_force_cpu(
    TARGET_HASH,
    max_len=4,
    n_threads=1
)

results.append([
    "CPU-1",
    cpu1
])

# CPU 8 Thread

_, cpu8 = brute_force_cpu(
    TARGET_HASH,
    max_len=4,
    n_threads=8
)

results.append([
    "CPU-8",
    cpu8
])

# GPU

_, gpu = brute_force_gpu(
    TARGET_HASH,
    max_len=4
)

results.append([
    "GPU",
    gpu
])

df = pd.DataFrame(
    results,
    columns=[
        "platform",
        "time"
    ]
)

df.to_csv(
    "results/gpu_benchmark.csv",
    index=False
)

print(df)