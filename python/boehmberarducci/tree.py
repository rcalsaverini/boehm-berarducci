from typing import NamedTuple, TypeVar, Callable

A = TypeVar("A")
R = TypeVar("R")
Branch = Callable[[R, R], R]


class BinaryTree(NamedTuple):
    constructor: Callable[[R, Branch[R]], R]

    def __call__(self, leaf: R, branch: Branch[R]):
        return self.constructor(leaf, branch)

    @classmethod
    def leaf(cls):
        def leafer(leaf: R, branch: Branch[R]) -> R:
            return leaf

        return cls(leafer)

    @classmethod
    def branch(cls, left, right):
        def brancher(leaf: R, branch: Branch[R]) -> R:
            return branch(left, right)

        return cls(brancher)

class BT(NamedTuple):
    left: "BT"
    right: "BT"