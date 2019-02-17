from typing import NamedTuple, Generic, TypeVar, Callable
from boehmberarducci.functional_base import compose
from boehmberarducci.functional_base import const

A = TypeVar("A")
B = TypeVar("B")
R = TypeVar("R")


class Maybe(NamedTuple, Generic[A]):
    maybe: Callable[[R, Callable[[A], R]], R]

    def __call__(self, nothing: R, just: Callable[[A], R]):
        return self.maybe(nothing, just)

    def __repr__(self):
        return self.maybe("Nothing", lambda x: f"Just {x}")

    def __rshift__(self, function):
        return self(nothing, function)

    def __mul__(self, justs):
        return self(nothing, lambda f: f & justs)

    def __rand__(self, function: Callable[[A], B]):
        return self >> compose(just, function)

    def map(self, function: Callable[[A], B]):
        return function & self

    def __eq__(self, other: "Maybe[A]") -> bool:
        is_equal_nothing: bool = other(True, const(False))

        def is_equal_just(j1): return other(False, lambda j2: j1 == j2)
        return self(is_equal_nothing, is_equal_just)


nothing = Maybe(lambda n, j: n)


def just(x): return Maybe(lambda n, j: j(x))
