import math


class Sample:
    def __init__(self, most):
        self._all = dict()
        self.n = 0
        self.most = most

    def update(self, x, r):
        self.n += 1
        if len(self._all) < self.most:
            self._all[str(len(self._all))] = x
        elif r < float(len(self._all))/self.n:
            self._all[str(math.floor(1 + r*len(self._all)))] = x
        else:
            pass
        return x


class Random:
    def __init__(self):
        self.seed0 = 10013
        self.seed = self.seed0
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

    def r(self):
        if not self.randomtable:
            self.randomtable = dict()
            for i in range(1, 98):
                self.randomtable[str(i)] = self.park_miller_randomizer()
        x = self.park_miller_randomizer()
        i = 1 + math.floor(97 * x)
        x, self.randomtable[str(int(i))] = self.randomtable[str(int(i))], x
        return x
