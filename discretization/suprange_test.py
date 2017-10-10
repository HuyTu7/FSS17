import sys
import range_1 as RANGE
import super_range as SUPER_R
sys.path.append('../utils/')
from sample_random import Random as RANDOM
from num import NUM


def x(z): return z[0]
def y(z): return z[-1]


def klass(z):
    R = RANDOM()
    if z < 0.2: return 0.2 + 2*R.r()/100
    elif z < 0.6: return 0.6 + 2*R.r()/100
    else: return 0.9 + 2*R.r()/100


def test():
    t, n = [], NUM()
    R = RANDOM()
    split = [0.2, 0.5]
    for i in range(1, 51):
        w = R.r()
        n.update(klass(w))
        t.append((w, klass(w)))
    print("\nWe have many unsupervised ranges.")
    for j, one in enumerate(RANGE.unsup_discret(t, x, 0, split)):
        print("x", j, one)
    print("\nWe have fewer supervised ranges.")
    for j, one in enumerate(SUPER_R.sup_discretize(t, x, y, True, True, split)):
        print("super", j, one)



R = RANDOM()
R.rseed(1)
test()