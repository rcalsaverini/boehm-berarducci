from boehmberarducci.either import left

def test_left_is_unchanged_by_map():
    "Left is unchanged by map"
    assert left("ok").map(lambda x: "foo") == left("ok")
