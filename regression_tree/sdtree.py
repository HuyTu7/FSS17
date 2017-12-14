import sys
sys.path.append('../utils/')
from num import NUM
tree_min_depth = 2
tree_max_depth = 10

class tree():
    def __init__(self, t, yfun, pos, attr, val):
        num = NUM()
        self._t = t
        self._kids = []
        self.yfun = yfun
        self.pos = pos
        self.attr = attr
        self.val = val
        self.stats = num.updates(t.rows, yfun)


def create(t, yfun, pos, attr, val):
    T = tree(t, yfun, pos, attr, val)
    return T


def order(t, y):
    def xpect(col):
        tmp = 0
        for _, k in col["nums"].items():
            tmp += (k.sd * k.n/float(col["n"]))
        return tmp

    def whatif(head, y):
        col = {"pos": head.pos, "what": head.txt, "nums": {}, "n": 0}
        for r in t.rows:
            x = r.cells[col["pos"]]
            if x != '?':
                col["n"] += 1
                if x not in col["nums"].keys():
                    col["nums"][x] = NUM()
                col["nums"][x].update(y(r))
        return {"key": xpect(col), "val": col}
    out = []
    for h in t.x["cols"]:
        out.append(whatif(h, y))
    out = sorted(out, key=lambda x: x["key"])
    order_out = [o["val"] for o in out]
    return order_out


def grow1(above, yfun, rows, lvl, b4, pos, attr, val):
    def pad(): return "%-20s" % ("| " * lvl)

    def likeAbove(): return above._t.copy(rows)

    if len(rows) >= tree_min_depth:
        if lvl <= tree_max_depth:
            here = (lvl == 0) and above or create(likeAbove(), yfun, pos, attr, val)
            if here.stats.sd < b4:
                if lvl > 0:
                    above._kids.append(here)
                cuts = order(here._t, yfun)
                cut = cuts[0]
                kids = {}
                for r in rows:
                    val = r.cells[cut["pos"]]
                    if val != '?':
                        rows1 = kids[val] if val in kids.keys() else []
                        rows1.append(r)
                        kids[val] = rows1
                for val in kids.keys():
                    rows1 = kids[val]
                    if len(rows1) < len(rows):
                        grow1(here, yfun, rows1, lvl+1, here.stats.sd, cut["pos"], cut["what"], val)


def grow(t, y):
    yfun = y
    root = create(t, yfun, None, None, None)
    grow1(root, yfun, t.rows, 0, 10**32, None, None, None)
    return root


def tprint(tr, lvl):
    def pad(): return '| '*(lvl-1)

    def left(x): return "%-20s" % x

    lvl = lvl or 0
    suffix = ""
    if len(tr._kids) == 0 or lvl == 0:
        suffix = "n=%s  mu=%-.2f  sd=%-.2f " % (tr.stats.n, tr.stats.mu, tr.stats.sd)

    if lvl == 0:
        print("\nThe built tree:")
        print(suffix + "\n")
    else:
        print(left(pad() + (str(tr.attr) or "") + " = " + (str(tr.val) or "")) + "\t\t:  " + suffix)
    for j in range(len(tr._kids)):
        tprint(tr._kids[j], lvl+1)


def leaf(tr, cells, bins, lvl):
    lvl = lvl or 0
    for _, kid in tr._kids.items():
        if cells[kid.pos] == kid.val:
            return leaf(kid, cells, bins, lvl+1)
    return tr

