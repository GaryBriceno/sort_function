from sorting_package import sort

def test_sorting_package():
    assert sort(100, 100, 100, 10) == "SPECIAL"
    assert sort(100, 100, 100, 20) == "REJECTED"
    assert sort(200, 50, 50, 10) == "SPECIAL"
    assert sort(50, 50, 50, 25) == "SPECIAL"
    assert sort(160, 160, 10, 25) == "REJECTED"
    assert sort(150, 149, 10, 19) == "SPECIAL"
    assert sort(150, 149, 10, 20) == "REJECTED"
