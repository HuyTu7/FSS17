from readData import ReadData as TBL
from sample_random import Sample as sampling


def create_r():
    range = dict()
    range['_all'] = sampling(512)
    range['n'] = 0
    range['hi'] = -2 ** 63
    range['lo'] = 2 ** 63
    range['span'] = 2 ** 64
    return range


def update(i, one, x):
    sampling.update(i['_all'], one)
    i['n'] += 1
    if x > i['hi']:
        i['hi'] = x
    if x < i['lo']:
        i['lo'] = x
    i['span'] = i['hi'] - i['lo']
    return x


def nextRange(i):
    i['now'] = create_r()
    i['ranges'].append(i['now'])
    return i


def range_manager(t, x):
    DATA = TBL()
    control_r = dict()
    control_r['x'] = x
    control_r['cohen'] = 0.2
    control_r['m'] = 0.5
    control_r['size'] = len(t),
    control_r['ranges'] = []
    control_r = nextRange(control_r)
    control_r['num'] = DATA.updates(t, control_r['x'])
    control_r['hi'] = control_r['num']['hi']

    control_r['enough'] = control_r['size'] ** control_r['m']
    control_r['epsilon'] = control_r['num']['sd'] * control_r['cohen']
    return control_r


def unsup_discret(t, x, last):
    t = sorted(t, key=lambda z: x(z))
    i = range_manager(t, x)
    for j, one in enumerate(t):
        x1 = x(one)
        update(i['now'], one, x1)
        if (j > 1 and x1 > last and
            i['now']['n'] > i['enough'] and
            i['now']['span'] > i['enough'] and
            i['num']['n'] - j > i['enough'] and
            i['num']['hi'] - x1 > i['epsilon']):
            nextRange(i)
            last = x1
    return i['ranges']


if __name__ == "__main__":
    v = [10, 9, 8, 6, 1, 2, 3, 4, 5, 11, 12, 13]
    unsup_discret(v, x, 0)
    #main(v,x,0)