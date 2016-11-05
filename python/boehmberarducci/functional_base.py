def compose(g, f):
    def wrap(x):
        return g(f(x))
    return wrap


def const(x):
    def wrap(y):
        return x
    return wrap
