class Either(object):

    def __init__(self, either):
        self.either = either

    def __call__(self, left, right):
        return self.either(left, right)

    def __repr__(self):
        def make_repr(s):
            return lambda x: "{} {}".format(s, x)
        return self(make_repr("Left"), make_repr("Right"))

    def __rshift__(self, function):
        return self(left, function)

    def __rmul__(self, either_fs):
        return either_fs(left, lambda f: self.map(f))

    def __rand__(self, function):
        return self >> (lambda x: right(function(x)))

    def map(self, function):
        return function & self

    def __eq__(self, other):
        is_eq_left = lambda l1: other(lambda l2: l1 == l2, lambda r2: False)
        is_eq_right = lambda r1: other(lambda l2: False, lambda r2: r1 == r2)
        return self(is_eq_left, is_eq_right)


def left(x):
    return Either(lambda l, r: l(x))


def right(x):
    return Either(lambda l, r: r(x))
