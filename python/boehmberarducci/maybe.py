from functools import wraps


class Maybe(object):

    def __init__(self, maybe):
        self.maybe = maybe

    def __call__(self, n, j):
        return self.maybe(n, j)

    def __repr__(self):
        return self("Nothing", lambda x: "Just {}".format(x))

    def __rshift__(self, function):
        return self(nothing, lambda x: function(x))

    def __rmul__(self, either_fs):
        return either_fs(nothing, lambda f: f & self)

    def __rand__(self, function):
        return self >> (lambda x: just(function(x)))

    def map(self, function):
        return function & self


nothing = Maybe(lambda n, j: n)


def just(x):
    return Maybe(lambda n, j: j(x))


def unthrow(function):
    @wraps(function)
    def wrapped(*args, **kwargs):
        try:
            return just(function(*args, **kwargs))
        except Exception as e:
            return nothing


@unthrow
def head(list):
    return list[0]
