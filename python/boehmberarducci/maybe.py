from boehmberarducci.functional_base import compose
from boehmberarducci.functional_base import const


class Maybe(object):

    def __init__(self, maybe):
        self.maybe = maybe

    def __call__(self, n, j):
        return self.maybe(n, j)

    def __repr__(self):
        return self("Nothing", lambda x: "Just {}".format(x))

    def __rshift__(self, function):
        return self(nothing, function)

    def __mul__(self, justs):
        return self(nothing, lambda f: f & justs)

    def __rand__(self, function):
        return self >> compose(just, function)

    def map(self, function):
        return function & self

    def __eq__(self, other):
        is_equal_nothing = other(True, const(False))
        is_equal_just = lambda j1: other(False, lambda j2: j1 == j2)
        return self(is_equal_nothing, is_equal_just)

nothing = Maybe(lambda n, j: n)
just = lambda x: Maybe(lambda n, j: j(x))
