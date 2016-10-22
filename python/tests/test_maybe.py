from boehmberarducci.maybe import just
from boehmberarducci.maybe import nothing


class TestNothing(object):

    def test_nothing_map(self):
        assert nothing.map(lambda x: "foo") == nothing

    def test_nothing_bind(self):
        assert nothing >> (lambda x: just("foo")) == nothing

    def test_nothing_over_nothing(self):
        assert nothing * nothing == nothing

    def test_nothing_over_just(self):
        assert nothing * just("ok") == nothing

    def test_nothing_show(self):
        assert repr(nothing) == "Nothing"

    def test_nothing_equal(self):
        assert nothing == nothing
        assert nothing != just(1)


class TestJust(object):

    def test_just_map(self):
        assert just("ok").map(lambda x: "foo") == just("foo")

    def test_just_bind(self):
        assert just("ok") >> (lambda x: just("foo")) == just("foo")

    def test_just_over_just(self):
        assert just(lambda x: x + 1) * just(1) == just(2)

    def test_just_over_nothing(self):
        assert just(lambda x: x + 1) * nothing == nothing

    def test_just_show(self):
        assert repr(just("foo")) == "Just foo"
        assert repr(just(1)) == "Just 1"

    def test_just_equal(self):
        assert just(1) == just(1)
        assert just(1) != just(2)
        assert just(1) != nothing
