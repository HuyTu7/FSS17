import time
import sys
import math


class Header:
    def __init__(self):
        self.header = []
        self.noc = -1
        self.nums = []
        self.syms = []
        self.goals =[]
        self.ignore_cols = []


class Goal:
    def __init__(self):
        self.index = -1
        self.weight = 0
        self.max = (math.exp(32))
        self.min = (-math.exp(32))


class Row:
    def __init__(self):
        self.id = -1
        self.cells = []
        self.rank = -1


class ReadData:
    def __init__(self):
        self.header = Header()
        self.goals = []
        self.rows = []

    def remove_mis(self, line):
        if "#" in line:
            line = line.split("#")[0]
        line = line.strip('\n')
        line = "".join(line.split())
        return line

    def read_header(self, h_line):
        entries = self.remove_mis(h_line).split(",")
        for entry in entries:
            entry = entry.strip()
            if entry:
                self.header.header.append(entry)
        self.header.noc = len(self.header.header)
        for i in range(self.header.noc):
            cate = self.header.header[i][0]
            if cate == "?":
                self.header.ignore_cols.append(i)
            elif cate == "$" or cate == "<" or cate == ">":
                self.header.nums.append(i)
                if cate == "<" or cate == ">":
                    g = Goal()
                    g.index = i
                    self.header.goals.append(i)
                    if cate == ">":
                        g.weight = 1
                    else:
                        g.weight = -1
                    self.goals.append(g)
            else:
                self.header.syms.append(i)

    def norm(self, g_i, row_i):
        hi = g_i.max
        lo = g_i.min
        return (row_i[g_i.index] - lo) / (hi - lo + (math.exp(-32)))

    def dominate1(self, i, j):
        e, n = math.exp(1), len(self.goals)
        sum1, sum2 = 0, 0
        for g in self.goals:
            w = g.weight
            x = self.norm(g, i)
            y = self.norm(g, j)
            sum1 -= e**(w * (x - y) / n)
            sum2 -= e**(w * (y - x) / n)
        return (sum1 / n) < (sum2 / n)

    def dominate(self, i):
        tmp = 0
        for r in self.rows:
            if r.id != i.id:
                if self.dominate1(i.cells, r.cells):
                    tmp += 1
        return tmp

    def format(self, val):
        try:
            fval = float(val)
            if fval.is_integer():
                return int(val)
            else:
                return fval
        except ValueError:
            return val

    def read_table(self, filename):
        with open(filename, "rb") as f2r:
            self.read_header(f2r.readline())
            index = 0
            row = f2r.readline()
            while row:
                r = Row()
                tmp_cells = self.remove_mis(row).split(",")
                r.id = index
                for col in self.header.nums:
                    tmp_cells[col] = self.format(tmp_cells[col])
                    if col in self.header.goals:
                        ind = self.header.goals.index(col)
                        if tmp_cells[col] < self.goals[ind].min:
                            self.goals[ind].min = tmp_cells[col]
                        if tmp_cells[col] > self.goals[ind].max:
                            self.goals[ind].max = tmp_cells[col]

                r.cells = [c for i, c in enumerate(tmp_cells) if i not in self.header.ignore_cols]
                self.rows.append(r)
                index += 1
                row = f2r.readline()
            for r in self.rows:
                r.rank = self.dominate(r)

        sort = sorted(self.rows, key=lambda r: r.rank)
        return sort

readData = ReadData()
start = time.time()
filename = sys.argv[-1]
sorted_dom_scores = readData.read_table(filename)
end = time.time()
print "There are %s entries in the table" % len(sorted_dom_scores)
print "Time that takes to read csv table: %f" % (end - start)
print readData.header.header
print "Top 5 rows for their domination scores"
for top in sorted_dom_scores[-5:]:
    print top.cells, top.id
print "\nBottom 5 rows for their domination scores"
for bottom in sorted_dom_scores[:5]:
    print bottom.cells, bottom.id




