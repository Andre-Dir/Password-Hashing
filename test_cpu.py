from cpu import brute_force_cpu


def test_cpu_found():

    pw, _ = brute_force_cpu(
        "900150983cd24fb0d6963f7d28e17f72",
        max_len=3,
        n_threads=4
    )

    assert pw == "abc"