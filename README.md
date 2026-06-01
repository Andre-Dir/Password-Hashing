# Parallel Password Hashing using CPU Multithreading and GPU CUDA

> Final Project - Komputasi Paralel dan Terdistribusi

Implementasi brute-force password hashing menggunakan **CPU Multithreading** dan **GPU CUDA (Numba)** untuk membandingkan performa komputasi sequential dan parallel dalam proses pencarian password berdasarkan hash MD5.

---

## Features

* Sequential CPU execution
* Parallel CPU execution (Multithreading)
* GPU acceleration using CUDA
* Benchmarking & Performance Analysis
* Speedup & Efficiency Calculation
* CPU vs GPU Comparison
* Unit Testing with PyTest
* Google Colab Support

---

## Team

| Nama                     | Role                               |
| ------------------------ | ---------------------------------- |
| Fajar Oktavian Ramadhan  | Core Developer, CPU Implementation |
| Kelvin Andre Hardian     | Core Developer, GPU Implementation |
| Muhammad Shaufi Wafa B.S | Documentation & Report             |
| Giovanni Maranatha       | Presentation & Documentation       |

### Contribution Notes

Sebagian besar implementasi teknis proyek (pengembangan kode, benchmarking, testing, dan integrasi sistem) dikerjakan oleh dua anggota utama tim. Anggota lainnya berkontribusi pada dokumentasi, penyusunan laporan, dan persiapan presentasi akhir.

---

# Project Overview

Sistem menerima input berupa **hash MD5** kemudian melakukan brute-force terhadap berbagai kombinasi karakter hingga ditemukan password yang menghasilkan hash yang sama.

Contoh:

```text
Password : abc

MD5 Hash :
900150983cd24fb0d6963f7d28e17f72
```

Input:

```text
900150983cd24fb0d6963f7d28e17f72
```

Output:

```text
abc
```

---

# Technologies

* Python 3
* NumPy
* Numba CUDA
* Pandas
* Matplotlib
* PyTest
* Google Colab

---

# Project Structure

```text
Password-Hashing/
│
├── main.py
├── cpu.py
├── gpu.py
├── hashing.py
├── generator.py
├── comparator.py
│
├── benchmark.py
├── analysis.py
├── gpu_benchmark.py
├── gpu_analysis.py
│
├── tests/
│
├── results/
│
├── docs/
│
├── requirements.txt
└── README.md
```

---

# Google Colab

Project ini dikembangkan dan diuji menggunakan Google Colab dengan GPU NVIDIA Tesla T4.

Google Colab:

https://colab.research.google.com/drive/1wb1W5nEfieolUunN8JWqKsGM2iN4jsG9?usp=sharing

---

# Installation

Clone repository:

```bash
git clone <repository-url>
cd Password-Hashing
```

Install dependency:

```bash
pip install -r requirements.txt
```

---

# Running the Project

## Main Program

```bash
python main.py
```

Program akan menjalankan:

* CPU Brute Force
* GPU Brute Force
* Benchmark sederhana
* Perbandingan performa

---

# Sequential vs Parallel CPU

Project ini mendukung dua mode eksekusi CPU:

## Sequential (1 Thread)

Digunakan sebagai baseline.

Pada `main.py`:

```python
cpu_pw, cpu_time = brute_force_cpu(
    TARGET_HASH,
    max_len=4,
    n_threads=1
)
```

Karakteristik:

* Tidak menggunakan paralelisme
* Semua kandidat diproses satu per satu
* Digunakan sebagai acuan perhitungan speedup

---

## Parallel CPU (Multithreading)

Contoh:

```python
cpu_pw, cpu_time = brute_force_cpu(
    TARGET_HASH,
    max_len=4,
    n_threads=8
)
```

Karakteristik:

* Menggunakan ThreadPoolExecutor
* Ruang pencarian dibagi ke beberapa thread
* Mendukung benchmark performa paralel

Konfigurasi thread dapat diubah sesuai kebutuhan:

```python
n_threads = 1
n_threads = 2
n_threads = 4
n_threads = 8
```

---

# Changing Target Hash

Hash target dapat diubah pada file:

```text
main.py
```

Cari bagian:

```python
TARGET_HASH = "900150983cd24fb0d6963f7d28e17f72"
```

Ganti dengan hash MD5 yang ingin dicari.

Contoh:

```python
TARGET_HASH = "5f4dcc3b5aa765d61d8327deb882cf99"
```

Sistem saat ini hanya mendukung hash MD5.

---

# Unit Testing

Menjalankan seluruh unit test:

```bash
pytest
```

Expected output:

```text
3 passed
```

---

# CPU Benchmark

Menjalankan benchmark multithreading:

```bash
python benchmark.py
```

Output:

```text
results/
├── raw_benchmark.csv
└── benchmark_summary.csv
```

---

# CPU Performance Analysis

Generate grafik:

```bash
python analysis.py
```

Output:

```text
results/
├── speedup.png
├── efficiency.png
└── execution_time.png
```

---

# GPU Benchmark

Menjalankan benchmark CPU vs GPU:

```bash
python gpu_benchmark.py
```

Output:

```text
results/gpu_benchmark.csv
```

---

# GPU Performance Analysis

Generate grafik perbandingan CPU dan GPU:

```bash
python gpu_analysis.py
```

Output:

```text
results/cpu_gpu_comparison.png
```

---

# Generated Results

Folder `results/` akan berisi:

```text
raw_benchmark.csv
benchmark_summary.csv
gpu_benchmark.csv

speedup.png
efficiency.png
execution_time.png
cpu_gpu_comparison.png
```

---

# Demo Video

https://drive.google.com/file/d/1oiqD2ZtSrwgzKS3XoTwc123My9G-SL6v/view?usp=drive_link

---

# Academic Objectives

Project ini dikembangkan untuk mempelajari:

* Parallel Computing
* CPU Multithreading
* GPU Computing (CUDA)
* Benchmarking
* Speedup Analysis
* Efficiency Analysis
* Amdahl's Law
* Performance Evaluation

---

# License

This project was developed for educational purposes as a Final Project for the Parallel and Distributed Computing course.
