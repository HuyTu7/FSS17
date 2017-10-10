import copy
import sys
sys.path.append('../utils/')
from num import NUM
from sym import SYM
import range as RANGE


def below(x, y): return x < y
def above(x, y): return x > y
def sd(_): return _.sd
def ent(_): return _.ent(_)


def labels(nums):
    out = []
    for i in nums.keys():
        entry = {'label': i, 'most': nums[i]}
        out.append(entry)
    return out


def sup_discretize(things, x, y, nump, lessp, split):
    y = y or (lambda k: k[-1])
    nump = None and True or nump
    lessp = None and True or lessp
    better = lessp and below or above
    what = nump and NUM or SYM
    z = nump and sd or ent
    breaks, ranges = {}, RANGE.unsup_discret(things, x, 0, split)
    #print ranges
    #print "hello"

    def data(j):
        data_array = ranges[j]['_all']._all.values()
        return data_array

    def memo(here, stop, _memo, b4):
        b4 = what()
        if stop > here:
            inc = 1
        else:
            inc = -1
        if here != stop:
            b4 = copy.deepcopy(memo(here+inc, stop, _memo, None))
        _memo[here] = b4.updates(data(here), y)
        return _memo[here]

    def combine(lo, hi, all, bin, lvl):
        best = z(all)
        lmemo, rmemo = {}, {}
        memo(hi, lo, lmemo, None)
        memo(lo, hi, rmemo, None)
        cut, lbest, rbest = None, 0.0, 0.0
        for j in range(lo, hi):
            l = lmemo[j]
            r = rmemo[j+1]
            tmp = l.n/all.n*z(l) + r.n/all.n*z(r)
            if better(tmp, best):
                cut = j
                best = tmp
                lbest = copy.deepcopy(l)
                rbest = copy.deepcopy(r)
        if cut:
            bin = combine(lo, cut, lbest, bin, lvl+1) + 1
            bin = combine(cut+1, hi, rbest, bin, lvl+1)
        else:
            if bin not in breaks.keys():
                breaks[bin] = -10**32
            if ranges[hi]['hi'] > breaks[bin]:
                breaks[bin] = ranges[hi]['hi']
        return bin

    #print data(1)
    combine(1, len(ranges)-1, memo(1, len(ranges)-1, {}, None), 1, 0)
    return labels(breaks)