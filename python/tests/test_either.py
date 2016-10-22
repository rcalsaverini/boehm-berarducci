from boehmberarducci.either import left
from boehmberarducci.either import right


class TestLeft(object):

    def test_left_map(self):
        assert left("ok").map(lambda x: "foo") == left("ok")

    def test_left_bind(self):
        assert left("ok") >> (lambda x: right("foo")) == left("ok")

    def test_left_over_left(self):
        assert left("foo") * left("ok") == left("foo")

    def test_left_over_right(self):
        assert left("foo") * right("ok") == left("foo")

    def test_left_show(self):
        assert repr(left("foo")) == "Left foo"
        assert repr(left(1)) == "Left 1"

    def test_left_equal(self):
        assert left(1) == left(1)
        assert left(1) != left(2)
        assert left(1) != right(1)


class TestRight(object):

    def test_right_map(self):
        assert right("ok").map(lambda x: "foo") == right("foo")

    def test_right_bind(self):
        assert right("ok") >> (lambda x: right("foo")) == right("foo")

    def test_right_over_right(self):
        assert right(lambda x: x + 1) * right(1) == right(2)

    def test_right_over_left(self):
        assert right(lambda x: x + 1) * left("no") == left("no")

    def test_right_show(self):
        assert repr(right("foo")) == "Right foo"
        assert repr(right(1)) == "Right 1"

    def test_right_equal(self):
        assert right(1) == right(1)
        assert right(1) != right(2)
        assert right(1) != left(1)
