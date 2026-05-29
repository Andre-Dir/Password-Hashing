import csv
import statistics

from cpu import brute_force_cpu

TARGET_HASH = "900150983cd24fb0d6963f7d28e17f72"

THREADS = [1, 2, 4, 8]
RUNS = 5


def benchmark_cpu():

    results = []

    for thread_count in THREADS:

        times = []

        print(f"\n=== THREAD {thread_count} ===")

        for run in range(RUNS):

            _, elapsed = brute_force_cpu(
                TARGET_HASH,
                max_len=4,
                n_threads=thread_count
            )

            times.append(elapsed)

        median_time = statistics.median(times)

        results.append(
            [thread_count,
             median_time,
             min(times),
             max(times)]
        )

    with open("results/benchmark.csv",
              "w",
              newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "threads",
            "median",
            "min",
            "max"
        ])

        writer.writerows(results)

    print("\nBenchmark saved.")


if __name__ == "__main__":
    benchmark_cpu()