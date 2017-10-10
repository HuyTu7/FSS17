import math


class NUM:
    def __init__(self):
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.sd = 0
        self.hi = -math.exp(32)
        self.lo = math.exp(32)
        self.w = 1

    def updates(self, t, f):
        f = f or (lambda x: x)
        for _, one in enumerate(t):
            '''
            print one.cells
            print [type(c) for c in one.cells]
            print f
            print type(f)
            print f(one), type(f(one))
            '''
            #print f(one)
            self.update(f(one))
        return self

    def norm(self, x):
        return (x - self.lo) / (self.hi - self.lo + math.exp(-32))

    def update(self, x):
        self.n = self.n + 1
        if x < self.lo:
            self.lo = x
        if x > self.hi:
            self.hi = x
        delta = x - self.mu
        self.mu += delta / self.n
        self.m2 += delta * (x - self.mu)
        if self.n > 1:
            self.sd = (self.m2 / (self.n - 1)) ** 0.5
