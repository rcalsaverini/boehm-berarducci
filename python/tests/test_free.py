# from boehmberarducci.free import free
from boehmberarducci.free import pure
# from boehmberarducci.maybe import just


class TestPure(object):

    def test_pure_map(self):
        assert pure(1).map(lambda x: x + 1) == pure(2)

    # def test_pure_bind(self):
    #     assert pure(1) >> (lambda x: pure(x + 1)) == pure(2)
    #
    # def test_pure_over_pure(self):
    #     assert pure(lambda x: x + 1) * pure(1) == pure(2)
    #
    # def test_pure_over_free(self):
    #     raise Exception(pure(lambda x: x + 1) * free(just(1)))
    #
    # def test_pure_show(self):
    #     assert False
    #
    # def test_pure_equal(self):
    #     assert False
