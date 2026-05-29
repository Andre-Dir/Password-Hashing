import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "results/gpu_benchmark.csv"
)

plt.figure(figsize=(8,5))

plt.bar(
    df["platform"],
    df["time"]
)

plt.ylabel("Time (s)")
plt.title(
    "CPU vs GPU Execution Time"
)

plt.savefig(
    "results/cpu_gpu_comparison.png",
    dpi=150
)

plt.show()