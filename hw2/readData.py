import time
import sys
import math


class Header:
    def __init__(self):
        self.header = []
        self.noc = -1
        self.nums = dict()
        self.syms = dict()
        self.goals =[]
        self.ignore_cols = []


class Row:
    def __init__(self):
        self.id = -1
        self.cells = []
        self.rank = -1


class ReadData:
    def __init__(self):
        self.header = Header()
        self.rows = []
        self.errorlog = ''

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
                self.header.nums[str(i)] = {'index': i, 'n': 0, 'mu': 0, 'm2': 0,
                                            'sd': 0, 'hi': -math.exp(32),'lo': -math.exp(32), 'w': 1}
                if cate == "<" or cate == ">":
                    if cate == ">":
                        self.header.goals.append((i, 1))
                    else:
                        self.header.goals.append((i, -1))
            else:
                self.header.syms[str(i)] = {'n': 0, 'nk': 0, 'counts': dict(),
                                            'most': 0, 'mode': None, '_ent' : None}

    def format(self, val):
        try:
            fval = float(val)
            if fval.is_integer():
                return int(val), False
            else:
                return fval, False
        except ValueError:
            return val, True

    def num_update(self, i, x):
        if i not in self.header.ignore_cols:
            col = self.header.nums[str(i)]
            col['n'] = col['n'] + 1
            if x < col['lo']:
                col['lo'] = x
            if x > col['hi']:
                col['hi'] = x
            #print " %s" %  x
            #print "Mu %s" % col['mu']
            delta = x - col['mu']
            col['mu'] += delta / col['n']
            col['m2'] += delta * (x - col['mu'])
            if col['n'] > 1:
                col['sd'] = (col['m2'] / (col['n'] - 1)) ** 0.5
            self.header.nums[str(i)] = col

    def num_norm(self, i, x):
        col = self.header.nums[str(i)]
        if i in self.header.ignore_cols:
            return x[i]
        else:
            return (x[i] - col['lo']) / (col['hi'] - col['lo'] + math.exp(-32))

    def sym_update(self, i, x):
        if i not in self.header.ignore_cols:
            x = str(x)
            col = self.header.syms[str(i)]
            col['n'] = col['n'] + 1
            col['_ent'] = None
            if x not in col['counts'].keys():
                col['nk'] += 1
                col['counts'][x] = 1
            seen = col['counts'][x] + 1
            col['counts'][x] = seen
            if seen > col['most']:
                col['most'] = seen
                col['mode'] = x
            self.header.syms[str(i)] = col

    def sym_norm(self, i, x):
        return x

    def dominate1(self, i, j):
        e, n = math.exp(1), len(self.header.goals)
        sum1, sum2 = 0, 0
        for g in self.header.goals:
            w = g[1]
            x = self.num_norm(g[0], i)
            y = self.num_norm(g[0], j)
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

    def read_table(self, filename):
        with open(filename, "rb") as f2r:
            self.read_header(f2r.readline())
            index = 1
            row = f2r.readline()
            while row:
                r = Row()
                tmp_cells = self.remove_mis(row).split(",")
                r.id = index
                string_val = False
                if self.header.noc == len(tmp_cells):
                    for c in range(self.header.noc):
                        if c not in self.header.ignore_cols:
                            tmp_cells[c], string_val = self.format(tmp_cells[c])
                            if str(c) in self.header.syms.keys():
                                self.sym_update(c, tmp_cells[c])
                            elif str(c) in self.header.nums.keys():
                                if not string_val:
                                    self.num_update(c, tmp_cells[c])
                                else:
                                    break
                            else:
                                pass
                    if not string_val:
                        r.cells = [c for i, c in enumerate(tmp_cells) if i not in self.header.ignore_cols]
                        self.rows.append(r)
                    else:
                        self.errorlog += "- Unexpected data type in line: %s \n" % (index + 1)
                else:
                    self.errorlog += "- Not consistent in term of number of columns and the length of the row at row %s \n" % (index + 1)
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
print readData.errorlog
print "There are %s entries in the table" % len(sorted_dom_scores)
print "Time that takes to read csv table: %f" % (end - start)
print readData.header.header
print "Top 5 rows for their domination scores"
for top in sorted_dom_scores[-5:]:
    print top.cells, top.id
print "\nBottom 5 rows for their domination scores"
for bottom in sorted_dom_scores[:5]:
    print bottom.cells, bottom.id




