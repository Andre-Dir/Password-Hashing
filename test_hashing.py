from hashing import md5_hash


def test_md5():
    assert md5_hash(
        "abc"
    ) == "900150983cd24fb0d6963f7d28e17f72"