import sys
sys.path.append('../utils/')
import math
from num import NUM
from sym import SYM
import range as RANGE
import super_range as SUPER_R


class Header:
    def __init__(self):
        self.header = []
        self.noc = -1
        self.nums = dict()
        self.syms = dict()
        self.goals =[]
        self.ignore_cols = []


class Row:
    def __init__(self, cells=None, id=-1, rank=-1):
        self.id = id
        self.cells = cells
        self.rank = rank


class ReadData:
    def __init__(self):
        self.header = Header()
        self.rows = []
        self.containers = []
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
                self.containers.append(None)
            elif cate == "$" or cate == "<" or cate == ">":
                self.header.nums[str(i)] = NUM()
                self.containers.append(NUM())
                if cate == "<" or cate == ">":
                    if cate == ">":
                        self.header.goals.append((i, 1))
                    else:
                        self.header.goals.append((i, -1))
            else:
                self.header.syms[str(i)] = SYM()
                self.containers.append(SYM())

    def format(self, val):
        try:
            fval = float(val)
            if fval.is_integer():
                return int(fval), False
            else:
                return fval, False
        except ValueError:
            return val, True

    def dominate1(self, i, j):
        e, n = math.exp(1), len(self.header.goals)
        sum1, sum2 = 0, 0
        for g in self.header.goals:
            w = g[1]
            x = self.header.nums[str(g[0])].norm(i[g[0]])
            y = self.header.nums[str(g[0])].norm(j[g[0]])
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

    def filter(self, tmp_cells, index=None):
        r = Row()
        r.id = index
        if self.header.noc == len(tmp_cells):
            for c in range(self.header.noc):
                if c not in self.header.ignore_cols:
                    tmp_cells[c], string_type = self.format(tmp_cells[c])
                    if str(c) in self.header.nums.keys() and string_type:
                        self.errorlog += "- Unexpected data type in line: %s \n" % (index + 1)
                        break
                    elif str(c) in self.header.syms.keys() and not string_type:
                        self.errorlog += "- Unexpected data type in line: %s \n" % (index + 1)
                    else:
                        r.cells = [e for i, e in enumerate(tmp_cells) if i not in self.header.ignore_cols]
                        self.rows.append(r)
                        if str(c) in self.header.syms.keys():
                            self.header.syms[str(c)].update(tmp_cells[c])
                        else:
                            self.header.nums[str(c)].update(tmp_cells[c])
        else:
            self.errorlog += "- Not consistent in term of number of columns and the length of the row at row %s \n" % (index + 1)


    def read_table(self, filename):
        with open(filename, "rb") as f2r:
            self.read_header(f2r.readline())
            index = 1
            row = f2r.readline()
            while row:
                tmp_cells = self.remove_mis(row).split(",")
                self.filter(tmp_cells, index)
                '''
                if self.header.noc == len(tmp_cells):
                    for c in range(self.header.noc):
                        if c not in self.header.ignore_cols:
                            tmp_cells[c], string_val = self.format(tmp_cells[c])
                            if str(c) in self.header.syms.keys():
                                self.header.syms[str(c)].update(tmp_cells[c])
                            elif str(c) in self.header.nums.keys():
                                if not string_val:
                                    self.header.nums[str(c)].update(tmp_cells[c])
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
                '''
                index += 1
                row = f2r.readline()
            for r in self.rows:
                r.rank = self.dominate(r)

        sort = sorted(self.rows, key=lambda r: r.rank)
        return sort
