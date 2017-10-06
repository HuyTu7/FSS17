from readData import ReadData as TBL
from sample_random import Sample as sampling
from sample_random import Random as R


def create_r():
    range = dict()
    range['_all'] = sampling(512)
    range['n'] = 0
    range['hi'] = -2 ** 63
    range['lo'] = 2 ** 63
    range['span'] = 2 ** 64
    return range


def update(i, one, x, r):
    i['_all'].update(one, r)
    i['n'] += 1
    if x > i['hi']:
        i['hi'] = x
    if x < i['lo']:
        i['lo'] = x
    i['span'] = i['hi'] - i['lo']
    return i


def nextRange(i):
    i['now'] = create_r()
    i['ranges'].append(i['now'])
    return i


def range_manager(t, x, cohen, m):
    DATA = TBL()
    control_r = dict()
    control_r['x'] = x
    control_r['cohen'] = cohen
    control_r['m'] = m
    control_r['size'] = len(t)
    control_r['ranges'] = []
    control_r = nextRange(control_r)
    control_r['num'] = DATA.updates(t, control_r['x'])
    control_r['hi'] = control_r['num']['hi']
    control_r['enough'] = control_r['size'] ** control_r['m']
    control_r['epsilon'] = control_r['num']['sd'] * control_r['cohen']
    return control_r


def val_format(val):
    try:
        fval = float(val)
        if fval.is_integer():
            return int(val)
        else:
            return fval
    except ValueError:
        return val


def unsup_discret(t, x, last, cohen, m):
    t = sorted(t, key=lambda z: x(z))
    i = range_manager(t, x, cohen, m)
    RANDOM = R()
    i = nextRange(i)
    for j, one in enumerate(t):
        x1 = x(one)
        i['now'] = update(i['now'], one, x1, RANDOM.r())
        if (j > 1 and x1 > last and
            i['now']['n'] > i['enough'] and
            i['now']['span'] > i['epsilon'] and
            i['num']['n'] - j > i['enough'] and
            i['num']['hi'] - x1 > i['epsilon']):
            i = nextRange(i)
            last = x1
    for k, range in enumerate(i['ranges']):
        if range['n'] == 0:
            del i['ranges'][k]
    return i['ranges']
