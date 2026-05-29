from cpu import brute_force_cpu
from gpu import brute_force_gpu


if __name__ == "__main__":

    target_hash = "b64eab8ce39e013604e243089c687e4f"

    print("=== CPU MULTITHREAD ===")

    cpu_pw, cpu_time = brute_force_cpu(
        target_hash,
        max_len=4,
        n_threads=8
    )

    print("\n=== GPU CUDA ===")

    gpu_pw, gpu_time = brute_force_gpu(
        target_hash,
        max_len=4
    )

    print("\n=== BENCHMARK ===")

    print(f"CPU time : {cpu_time:.4f}s")
    print(f"GPU time : {gpu_time:.4f}s")

    if gpu_time > 0:
        speedup = cpu_time / gpu_time
        print(f"Speedup : {speedup:.2f}x")