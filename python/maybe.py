class Maybe(object):

    def __init__(self, maybe):
        self.maybe = maybe

    def __call__(self, n, j):
        return self.maybe(n, j)

    def __repr__(self):
        return self("Nothing", lambda x: "Just {}".format(x))

    def __rshift__(self, function):
        return self(nothing, lambda x: function(x))

    def map(self, function):
        return self >> (lambda x: just(function(x)))

nothing = Maybe(lambda n, j: n)
just = lambda x: Maybe(lambda n, j: j(x))
