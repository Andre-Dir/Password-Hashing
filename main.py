from cpu import brute_force_cpu
from gpu import brute_force_gpu


if __name__ == "__main__":

    target_hash = "24bc50d85ad8fa9cda686145cf1f8aca"

    print("=== CPU MULTITHREAD ===")

    cpu_pw, cpu_time = brute_force_cpu(
        target_hash,
        max_len=5,
    )

    print("\n=== GPU CUDA ===")

    gpu_pw, gpu_time = brute_force_gpu(
        target_hash,
        max_len=5
    )

    print("\n=== BENCHMARK ===")

    print(f"CPU time : {cpu_time:.4f}s")
    print(f"GPU time : {gpu_time:.4f}s")

    if gpu_time > 0:
        speedup = cpu_time / gpu_time
        print(f"Speedup : {speedup:.2f}x")
