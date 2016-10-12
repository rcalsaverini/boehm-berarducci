from functools import wraps


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


def left(x):
    return Either(lambda l, r: l(x))


def right(x):
    return Either(lambda l, r: r(x))


def is_right(x):
    return x(lambda x: False, lambda x: True)


def unthrow(function):
    @wraps(function)
    def wrapped(*args, **kwargs):
        try:
            return right(function(*args, **kwargs))
        except Exception as e:
            return left(e)
    return wrapped


@unthrow
def head(list):
    return list[0]
