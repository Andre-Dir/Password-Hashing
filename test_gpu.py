from gpu import brute_force_gpu


def test_gpu_found():

    pw, _ = brute_force_gpu(
        "900150983cd24fb0d6963f7d28e17f72",
        max_len=3
    )

    assert pw == "abc"