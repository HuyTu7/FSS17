import sys
sys.path.append('../utils/')
import copy


def has(branch):
    out = []
    for i in range(len(branch)):
        step = branch[i]
        out.append(step['attr'], step['val'])
    return out


def have(branches):
    for _,branch in enumerate(branches):
        branch.has = has(branch)
    return branches


def branches1(tr, out, b):
    if tr['attr']:
        b.append({'attr'=tr['attr'],'val'=tr['val'],'_stats'=tr['stats']})
    if len(b) > 0: out.append(b)
    for _, kid in enumerate(tr._kids):
        branches1(kid, out, copy.deepcopy(b))
    return out


def branches(tr):
    return have(branches1(tr,{},{}))


def member2(twin0, twins):
    for _,twin1 in enumerate(twins):
        if twin0.attr == twin1.attr and twin0.val == twin1.val:
            return True
    return False


def delta(t1, t2):
    out = []
    for _,twin in pairs(t1):
        if not member2(twin,t2):
            out.append(twin.attr, twin.val)
    return out


def contrasts(branches, better):
    for i, branch1 in enumerate(branches):
        out = {}
        for j, branch2 in enumerate(branches):
            if i == j:
                num1 = branch1[-1]['_stats']
                num2 = branch2[-1]['_stats']
                if better(num2.mu, num1.mu):
                    if not NUM.same(num1,num2):
                        inc = delta(branch2.has,branch1.has)
                        if len(inc) > 0:
                            out.append({i=i,j=j,ninc=len(inc), muinc=num2.mu - num1.mu,
                                        inc=inc, branch1=branch1.has,mu1=num1.mu,
                                        branch2=branch2.has,mu2=num2.mu})
    print("")
    table.sort(out, function (x,y) return x.muinc > y.muinc)
    print(i,"max mu  ",out[1])
    table.sort(out, function (x,y) return x.ninc < y.ninc)
    print(i,"min inc ",out[1])


def more(x,y): return x > y
def less(x,y): return x < y
def plans(branches):    return contrasts(branches, more)
def monitors(branches): return contrasts(branches, less)