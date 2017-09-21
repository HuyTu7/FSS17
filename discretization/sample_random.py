import math

class Sample:
    def __init__(self, most):
        self._all = dict()
        self.n = 0
        self.most = most

    def update(self, x, r):
        self.n += 1
        if self._all < i.most:
            self._all[len(self._all)] = x
        elif r < float(len(self._all))/i.n:
            self._all[math.floor(1 + r*len(self._all))] = x
        else:
            pass
        return x


class Random:
    def __init__(self):
        self.seed0 = 10013
        self.seed = seed0
        self.multipler = 16807.0
        self.modulus = 2147483647.0
        self.randomtable = None

    def park_miller_randomizer(self):
        self.seed = (self.multipler * self.seed) % self.modulus
        return self.seed / self.modulus

    def rseed(self, n):
        if n:
            self.seed = n
        else:
            self.seed = self.seed0
        self.randomtable = None

    def system(self):
        return self.rseed(math.random() * self.modulus)

    def r(self, x, i):
        if not self.randomtable:
            self.randomtable = dict()
            for i in range(1, 98):
                self.randomtable[i] = self.park_miller_randomizer()
        x = self.park_miller_randomizer()
        i = 1 + math.floor(97 * x)
        x, self.randomtable[i] = self.randomtable[i], x
        return x
