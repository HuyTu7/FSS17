import math


class SYM:
    def __init__(self):
        self.n = 0
        self.nk = 0
        self.counts = dict()
        self.most = 0
        self.mode = None
        self._ent = None

    def update(self, x):
        x = str(x)
        self.n += 1
        self._ent = None
        if x not in self.counts.keys():
            self.nk += 1
            self.counts[x] = 1
        seen = self.counts[x] + 1
        self.counts[x] = seen
        if seen > self.most:
            self.most = seen
            self.mode = x

    def ent(self):
        if not self._ent:
            e = 0
            for _, f in self.counts.iteritems():
                e -= (f / self.n) * math.log((f / self.n), 2)
            self._ent = e
        return self._ent

    def norm(self, x):
        return x