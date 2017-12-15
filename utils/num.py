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

    @classmethod
    def hedges(self, i, j):
        nom = (i.n - 1.0) * (i.sd ** 2) + (j.n - 1.0) * (j.sd ** 2) * 1.0
        denom = (i.n - 1.0) + (j.n - 1.0)
        sp = 0.0 + (nom / denom) ** 0.5
        g = abs(i.mu - j.mu) / sp
        c = 1.0 - 3.0 / (4.0 * (i.n + j.n - 2.0) - 1)
        return g * c > 0.38

    @classmethod
    def ttest1(self, df, first, last, crit):
        if df <= first:
            return crit[first]
        elif df >= last:
            return crit[last]
        else:
            n1 = first
            while n1 < last:
                n2 = n1 * 2.0
                if n1 <= df <= n2:
                    old, new = crit[n1], crit[n2]
                    return 0.0 + old + (new - old) * (df - n1 + 0.0) / (n2 - n1 + 0.0)
                n1 = n1 * 2

    @classmethod
    def ttest(self, i, j):
        critical_vals = {95:{3:3.182, 6:2.447, 12:2.179, 24:2.064, 48:2.011, 96:1.985},\
                         99:{3:5.841, 6:3.707, 12:3.055, 24:2.797, 48:2.682, 96:2.625}}
        t = (i.mu - j.mu + 0.0) / math.sqrt(max(1e-64, (i.sd ** 2 + 0.0) / i.n + (j.sd ** 2 + 0.0) / j.n))
        a = (1.0 * i.sd ** 2) / i.n
        b = (1.0 * j.sd * 2) / j.n
        df = (a + b + 0.0) ** 2 / (1e-64 + a ** 2 / (i.n - 1.0) + b ** 2 / (j.n - 1.0))
        c = self.ttest1(math.floor(df + 0.5), 3, 96, critical_vals[95])
        return abs(t) > c

    @classmethod
    def same(self, i, j):
        return not (self.hedges(i, j) and self.ttest(i, j))

