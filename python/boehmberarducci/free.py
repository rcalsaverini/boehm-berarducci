class Free(object):

    def __init__(self, unfree):
        self.unfree = unfree

    def __eq__(self, other):
        pass

    def __repr__(self):
        case_pure = lambda x: "Pure {}".format(repr(x))
        case_free = lambda x: "Free [{}]".format(repr(x))
        return self(case_pure, case_free)

    def __call__(self, pureF, freeF):
        return self.unfree(pureF, freeF)

    def __rshift__(self, function):
        return self(function, free)

    def __rmul__(self, xs):
        return self(xs.map, free)

    def __rand__(self, function):
        return self >> (lambda x: pure(function(x)))

    def map(self, function):
        return function & self

    def join(self):
        self >> (lambda x: x)

    def iter(self, function):
        return self(lambda x: x, function)

    def interpret(self, function):
        return self(pure, lambda x: self.join(function(x)))


def pure(x):
    return Free(lambda pureF, freeF: pureF(x))


def free(fs):
    def unfree(pureF, freeF):
        freeF(fs.map(lambda f: f(pureF, freeF)))
    return Free(unfree)


def liftF(fs):
    free(fs.map(pure))
