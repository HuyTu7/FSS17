import sys
sys.path.append('../utils/')
import copy
from num import NUM

def has(branch):
    out = []
    for i in range(len(branch)):
        step = branch[i]
        out.append({"attr": step['attr'], "val": step['val']})
    return out


def have(branches):
    final_branches = []
    for branch in branches:
        has_b = has(branch)
        final_branches.append({"has": has_b, 'branch': branch})
    return final_branches


def branches1(tr, out, b):
    if tr.attr:
        temp_b = {}
        temp_b['attr'], temp_b['val'], temp_b['_stats'] = tr.attr, tr.val, tr.stats
        b.append(temp_b)
    if len(b) > 0:
        out.append(b)
    for _, kid in enumerate(tr._kids):
        branches1(kid, out, copy.deepcopy(b))
    return out


def branches(tr):
    return have(branches1(tr, [], []))


def member2(twin0, twins):
    for _, twin1 in enumerate(twins):
        if twin0['attr'] == twin1['attr'] and twin0['val'] == twin1['val']:
            return True
    return False


def delta(t1, t2):
    out = []
    for _,twin in enumerate(t1):
        if not member2(twin, t2):
            out.append((twin['attr'], twin['val']))
    return out


def contrasts(branches, better):
    for i, branch1 in enumerate(branches):
        out = []
        for j, branch2 in enumerate(branches):
            if i != j:
                num1 = branch1['branch'][-1]['_stats']
                num2 = branch2['branch'][-1]['_stats']
                if better(num2.mu, num1.mu):
                    if not NUM.same(num1, num2):
                        inc = delta(branch2['has'], branch1['has'])
                        if len(inc) > 0:
                            temp_out = {'i': i, 'j': j, 'ninc': len(inc), 'muinc': num2.mu - num1.mu,
                                        'inc': inc, 'branch1': branch1['has'], 'mu1': num1.mu,
                                        'branch2': branch2['has'], 'mu2': num2.mu}
                            out.append(temp_out)
        if len(out) > 0:
            print("")
            sorted(out, key=lambda x: x['muinc'])
            print("%s max mu  %s" % (i, out[0]))
            sorted(out, key=lambda x: x['ninc'])
            print("%s min inc %s" % (i, out[0]))
        else:
            print("Empty out at i_%s" % i)
    return out


def more(x, y): return x > y
def less(x, y): return x < y
def plans(branches):    return contrasts(branches, more)
def monitors(branches): return contrasts(branches, less)