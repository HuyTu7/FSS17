import sys
import time
import os 


class readCSV():
    def __init__(self):
        self.header = []
        self.csv_df = []
        self.noc = -1
        self.header_f = False
        self.ignore_cols = []
        self.runable = True

    def format(val):
        try:
            fval = float(val)
            if fval.is_integer():
                return int(val)
            else:
                return fval
        except ValueError:
            return val

    def clean(self, line):
        if "#" in line:
            line = line.split("#")[0]
        line = line.strip('\n')
        line = "".join(line.split())
        entries = line.split(",")
        #print entries
        if self.header_f:
            for entry in entries:
                entry = entry.strip()
                #print entry
                if entry:
                    self.header.append(entry)
        else:
            if self.noc == len(entries):
                for index in range(len(entries)):
                    #print entries[index]
                    if index not in self.ignore_cols:
                        entry = entries[index].strip()
                        if entry:
                            self.csv_df[index].append(entry)
            else:
                self.runable = False
                print "Not consistent in term of number of columns and the length of the row"

    def readfile(self, filename):
        with open(filename, "rb") as f2r:
            header_l = f2r.readline()
            self.header_f = True
            self.clean(header_l)
            self.noc = len(self.header)
            self.header_f = False
            ignore_index = 0
            for i in range(self.noc):
                if self.header[i] == "?:":
                    self.ignore_cols.append(ignore_index)
                ignore_index += 1
            self.csv_df = [[] for _ in xrange(self.noc - len(self.ignore_cols))]
            while self.runable:
                row = f2r.readline()
                if row:
                    self.clean(row)
                else:
                    self.runable = False
        return self.csv_df


readcsv = readCSV()
df = readcsv.readfile("./POM3A.csv")
print len(df)


