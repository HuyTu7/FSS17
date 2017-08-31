import time

class readCSV():
    def __init__(self):
        self.header = []
        self.csv_df = []
        self.noc = -1
        self.header_f = False
        self.ignore_cols = []

    def format(val):
        try:
            fval = float(val)
            if fval.is_integer():
                return int(val)
            else:
                return fval
        except ValueError:
            return val

    def clean(self, line, l_index):
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
                    print "There are null element in the header line"
        else:
            if self.noc == len(entries):
                row = []
                for index in range(len(entries)):
                    #print entries[index]
                    if index not in self.ignore_cols:
                        entry = entries[index].strip()
                        if entry:
                            row.append(entry)
                        else:
                            print "There are null element in row %s" % l_index
                self.csv_df.append(row)
            else:
                print "Not consistent in term of number of columns and the length of the row at row %s" % l_index

    def readfile(self, filename):
        with open(filename, "rb") as f2r:
            header_l = f2r.readline()
            self.header_f = True
            self.clean(header_l, 0)
            self.noc = len(self.header)
            self.header_f = False
            for i in range(self.noc):
                if self.header[i][0] == "?":
                    self.ignore_cols.append(i)
            r_index = 0
            row = f2r.readline()
            while row:
                self.clean(row, r_index)
                r_index += 1
                row = f2r.readline()

        return self.csv_df


readcsv = readCSV()
start = time.time()
df = readcsv.readfile("./example.csv")
end =  time.time()
print "Time that take to read csv table: %f" % (end - start)
print df
print len(df)