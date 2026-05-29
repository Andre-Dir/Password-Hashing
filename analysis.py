import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results/benchmark.csv")

t_seq = df.loc[
    df["threads"] == 1,
    "median"
].values[0]

df["speedup"] = t_seq / df["median"]

df["efficiency"] = (
    df["speedup"] /
    df["threads"]
)

# ---------- SPEEDUP ----------

plt.figure(figsize=(6,4))

plt.plot(
    df["threads"],
    df["speedup"],
    marker="o",
    label="Empirical"
)

plt.plot(
    df["threads"],
    df["threads"],
    "--",
    label="Ideal"
)

plt.xlabel("Threads")
plt.ylabel("Speedup")
plt.title("Speedup vs Threads")
plt.legend()

plt.savefig(
    "results/speedup.png",
    dpi=150
)

plt.close()

# ---------- EFFICIENCY ----------

plt.figure(figsize=(6,4))

plt.plot(
    df["threads"],
    df["efficiency"],
    marker="o"
)

plt.xlabel("Threads")
plt.ylabel("Efficiency")
plt.title("Efficiency vs Threads")

plt.savefig(
    "results/efficiency.png",
    dpi=150
)

plt.close()

# ---------- EXECUTION TIME ----------

plt.figure(figsize=(6,4))

plt.plot(
    df["threads"],
    df["median"],
    marker="o"
)

plt.xlabel("Threads")
plt.ylabel("Time (s)")
plt.title("Execution Time")

plt.savefig(
    "results/execution_time.png",
    dpi=150
)

plt.close()

print(df)