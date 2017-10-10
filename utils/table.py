import copy
import random
import sys
sys.path.append('../hw2/')
from readData import ReadData
from readData import Row as ROW
from sym import SYM
from num import NUM
import super_range as SUPER_R



class TBL():
    def __init__(self, filename):
        self.rows = []
        self.spec = []
        self.goals, self.less, self.more = [], [], []
        self.name = {}
        self.read = ReadData(True)
        self.ignore_cols = []
        self.container = []
        self.all = {"syms": [], "nums": [], "cols": []}
        self.x = {"syms": [], "nums": [], "cols": []}
        self.y = {"syms": [], "nums": [], "cols": []}
        if filename.strip():
            self.fromCSV(filename)
        else:
            self.container_b = True

    def categories(self, txt):
        spec = [
            {"when": "$", "what": NUM(), "weight": 1, "where": [self.all.get("cols"), self.x.get("cols"), self.all.get("nums"), self.x.get("nums")]},
            {"when": "%", "what": NUM(), "weight": 1, "where": [self.all.get("cols"), self.x.get("cols"), self.all.get("nums"), self.x.get("nums")]},
            {"when": "<", "what": NUM(), "weight": -1, "where": [self.all.get("cols"), self.y.get("cols"), self.all.get("nums"), self.goals, self.less, self.y.get("nums")]},
            {"when": ">", "what": NUM(), "weight": 1, "where": [self.all.get("cols"), self.y.get("cols"), self.all.get("nums"), self.goals, self.more, self.y.get("nums")]},
            {"when": "!", "what": SYM(), "weight": 1, "where": [self.all.get("cols"), self.y.get("syms"), self.y.get("cols"), self.all.get("syms")]},
            {"when": "", "what": SYM(), "weight": 1, "where": [self.all.get("cols"), self.x.get("cols"), self.all.get("syms"), self.x.get("syms")]},
            {"when": "?", "what": None}
        ]
        for want in spec:
            if txt.find(want["when"]) > -1:
                return want["what"], want["weight"], want["where"]

    def fromCSV(self, f):
        self.read.read_table(f)
        self.rows = self.read.rows
        self.container = self.read.container
        self.update(self.read.header.header)
        for r in self.read.rows:
            for i in range(len(r.cells)):
                self.container[i].update(r.cells[i])

    def domr(self):
        domr = {}
        for row in self.rows:
            domr[row.id] = row.rank
        return domr

    def update(self, cells):
        fn = (len(self.spec) == 0) and self.header or self.data
        return fn(cells)

    def header(self, cells, init_cont=False):
        self.spec = cells
        for col, cell in enumerate(cells):
            what, weight, wheres = self.categories(cell)
            if init_cont:
                self.container.append(what)
            one = what
            one.pos = col
            one.txt = cell
            one.what = what
            one.weight = weight
            self.name[one.txt] = one
            for _, where in enumerate(wheres):
                where.append(one)
        return self

    def data(self, cells, old=None):
        for i in range(len(cells)):
            #print self.container
            self.container[i].update(cells[i])
        new = ROW(cells)
        if old:
            new.id = old.id
        self.rows.append(new)
        return new

    def dom(self, r):
        return self.dom_ranks[r.id]

    def discretize_headers(self):
        dh = []
        if self.spec:
            for col in self.spec:
                col = col.replace("$", "")
                col = col.replace("%", "")
                dh.append(col)
        return dh

    def discretize_rows(self, y):
        split = [0.2, 0.5]
        j = TBL("").header(self.discretize_headers(), True)
        yfun = y or j.dom

        self.dom_ranks = self.domr()

        for head in self.x["nums"]:
            cooked = j.all["cols"][head.pos]
            x = lambda r: r.cells[cooked.pos]
            cooked.bins = SUPER_R.sup_discretize(self.rows, x, yfun, True, True, split)

        for r in self.rows:
            tmp = copy.deepcopy(r.cells)
            for head in self.x["nums"]:
                cooked = j.all["cols"][head.pos]
                old = tmp[cooked.pos]
                new = SYM().discretize(cooked, old)
                tmp[cooked.pos] = new
            j.data(tmp, r)
        return j

    def copy(self, setting):
        j = TBL("")
        j.header(copy.deepcopy(self.spec), True)
        random.seed(1)
        if setting == "full":
            for r in self.rows:
                j.data(copy.deepcopy(r.cells), r)
        elif type(setting) == int:
            random.shuffle(self.rows)
            for k in range(0, setting):
                j.data(copy.deepcopy(self.rows[k].cells), self.rows[k])
        elif isinstance(setting, TBL):
            for r in setting.rows:
                j.data(copy.deepcopy(r.cells), r)
        else:
            for r in setting:
                j.data(copy.deepcopy(r.cells), r)
        return j
