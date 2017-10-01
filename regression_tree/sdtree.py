import sys
sys.path.append('../discretization/')
from num import NUM
num = NUM()


class tree():
    def __init__(self, t, yfun, pos, attr, val):
        self._t = t
        self._kids = []
        self.yfun = yfun
        self.pos = pos
        self.attr = attr
        self.val = val
        self.stats = num.updates(t.rows, yfun)

