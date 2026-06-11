import os
import csv
import statistics
import pandas as pd
import matplotlib.pyplot as plt

from cpu import brute_force_cpu

# =====================================
# CONFIG
# =====================================

TARGET_HASH = "e1ef3dd13e63886ac067a47c5b99f494"

THREADS = [1, 2, 4, 8]

RUNS = 5

os.makedirs("results", exist_ok=True)

# =====================================
# BENCHMARK
# =====================================

raw_data = []

for p in THREADS:

    print(f"\n=== THREAD {p} ===")

    times = []

    for run in range(RUNS):

        _, elapsed = brute_force_cpu(
            TARGET_HASH,
            max_len=4,
            n_threads=p
        )

        times.append(elapsed)

        raw_data.append([
            run + 1,
            p,
            elapsed
        ])

    print(
        f"Median = {statistics.median(times):.4f}s"
    )

# =====================================
# SAVE RAW CSV
# =====================================

with open(
    "results/raw_benchmark.csv",
    "w",
    newline=""
) as f:

    writer = csv.writer(f)

    writer.writerow([
        "run",
        "threads",
        "time"
    ])

    writer.writerows(raw_data)

print("raw_benchmark.csv saved")

# =====================================
# SUMMARY TABLE
# =====================================

df = pd.DataFrame(
    raw_data,
    columns=[
        "run",
        "threads",
        "time"
    ]
)

summary = (
    df.groupby("threads")
      .agg(
          median=("time", "median"),
          minimum=("time", "min"),
          maximum=("time", "max"),
          std=("time", "std")
      )
      .reset_index()
)

t_seq = summary.loc[
    summary["threads"] == 1,
    "median"
].values[0]

summary["speedup"] = (
    t_seq /
    summary["median"]
)

summary["efficiency"] = (
    summary["speedup"] /
    summary["threads"]
)

summary.to_csv(
    "results/benchmark_summary.csv",
    index=False
)

print(summary)

# =====================================
# GRAFIK 1
# SPEEDUP
# =====================================

plt.figure(figsize=(7,5))

plt.plot(
    summary["threads"],
    summary["speedup"],
    marker="o",
    linewidth=2,
    label="Empirical"
)

plt.plot(
    summary["threads"],
    summary["threads"],
    "--",
    label="Ideal"
)

plt.xlabel("Threads")
plt.ylabel("Speedup")
plt.title("Speedup vs Threads")

plt.grid(True)

plt.legend()

plt.savefig(
    "results/speedup.png",
    dpi=150
)

plt.show()

# =====================================
# GRAFIK 2
# EFFICIENCY
# =====================================

plt.figure(figsize=(7,5))

plt.plot(
    summary["threads"],
    summary["efficiency"],
    marker="o",
    linewidth=2
)

plt.axhline(
    y=1.0,
    linestyle="--"
)

plt.xlabel("Threads")
plt.ylabel("Efficiency")

plt.title("Efficiency vs Threads")

plt.grid(True)

plt.savefig(
    "results/efficiency.png",
    dpi=150
)

plt.show()

# =====================================
# GRAFIK 3
# EXECUTION TIME
# =====================================

plt.figure(figsize=(7,5))

plt.plot(
    summary["threads"],
    summary["median"],
    marker="o",
    linewidth=2
)

plt.xlabel("Threads")

plt.ylabel("Execution Time (s)")

plt.title("Execution Time vs Threads")

plt.grid(True)

plt.savefig(
    "results/execution_time.png",
    dpi=150
)

plt.show()

print("\nAll graphs generated.")
