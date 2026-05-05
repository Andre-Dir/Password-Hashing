from cpu import brute_force_cpu
from gpu import brute_force_gpu

if __name__ == "__main__":
    # contoh: hash dari "abc"
    target_hash = "900150983cd24fb0d6963f7d28e17f72"

    print("=== CPU ===")
    cpu_pw, cpu_time = brute_force_cpu(target_hash, max_len=4)

    print("\n=== GPU ===")
    gpu_pw, gpu_time = brute_force_gpu(target_hash, max_len=4)

    # benchmark sederhana
    if cpu_time > 0 and gpu_time > 0:
        speedup = cpu_time / gpu_time
        print("\n=== BENCHMARK ===")
        print(f"CPU time   : {cpu_time:.4f}s")
        print(f"GPU time   : {gpu_time:.4f}s")
        print(f"Speedup    : {speedup:.2f}x")