import sys
sys.path.append('../utils/')
from sample_random import Random as R
import range_1 as RANGE


def f(z):
    return z[0]


def range_test():
    cohen = 0.2
    m = 0.5
    split = [cohen, m]
    RANDOM = R()
    RANDOM.rseed(1)
    tmp = []
    for i in range(1, 51):
        tmp.append((RANDOM.r()**2, len(tmp)+1))
    print("ranges: ")
    print("%5s\t%5s\t%5s\t%5s\n" % ("#", "n", "lo", "hi"))
    print("%5s\t%5s\t%5s\t%5s\n" % ("-----", "-----", "-----", "-----"))
    ranges = RANGE.unsup_discret(tmp, f, 0, split)
    for i, k in enumerate(ranges):
        print("%5s\t%5s\t%5.3f\t%5.3f\n" % (i, k['n'], k['lo'], k['hi']))


if __name__ == "__main__":
    range_test()
