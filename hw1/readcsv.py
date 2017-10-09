import time
import sys


class readCSV():
    def __init__(self):
        self.header = []
        self.csv_df = []
        self.noc = -1
        self.header_f = False
        self.nums = []
        self.syms = []
        self.ignore_cols = []
        self.errorlog = ''

    def format(self, val):
        try:
            fval = float(val)
            if fval.is_integer():
                return int(fval), False
            else:
                return fval, False
        except ValueError:
            return val, True

    def remove_mis(self, line):
        if "#" in line:
            line = line.split("#")[0]
        line = line.strip('\n')
        line = "".join(line.split())
        return line

    def clean(self, line, l_index):
        entries = line.split(",")
        if self.header_f:
            for entry in entries:
                entry = entry.strip()
                if entry:
                    self.header.append(entry)
                else:
                    self.errorlog += "- There are null element in the header line \n"
        else:
            if self.noc == len(entries):
                row = []
                for index in range(len(entries)):
                    if index not in self.ignore_cols:
                        entry = entries[index].strip()
                        if entry:
                            string_type = self.format(entry)[1]
                            if (index in self.nums and string_type) or (index in self.syms and not string_type):
                                self.errorlog += "- There is inappropriate data type at the line %s \n" % l_index
                                break
                            else:
                                row.append(entry)
                        else:
                            self.errorlog += "- There are null element in row %s \n" % l_index
                if len(row) == self.noc - len(self.ignore_cols):
                    self.csv_df.append(row)
            else:
                self.errorlog += "- Not consistent in term of number of columns and the length of the row at row %s \n" % l_index

    def readfile(self, filename):
        with open(filename, "rb") as f2r:
            header_l = f2r.readline()
            self.header_f = True
            header_l = self.remove_mis(header_l)
            self.clean(header_l, 0)
            self.noc = len(self.header)
            self.header_f = False
            for i in range(self.noc):
                cate = self.header[i][0]
                if cate == "?":
                    self.ignore_cols.append(i)
                elif cate == "$" or cate == "<" or cate == ">":
                    self.nums.append(i)
                else:
                    self.syms.append(i)

            r_index = 2
            row = f2r.readline()
            while row:
                row = self.remove_mis(row)
                if not row.endswith(','):
                    self.clean(row, r_index)
                else:
                    self.errorlog += "- The line %s is incomplete, concatenate to the next line \n" % r_index
                    r_index += 1
                    row += self.remove_mis(f2r.readline())
                    self.clean(row, r_index)
                r_index += 1
                row = f2r.readline()

        return self.csv_df


readcsv = readCSV()
start = time.time()
filename = sys.argv[-2]
printing = int(sys.argv[-1])

df = readcsv.readfile(filename)
end = time.time()
print "Results are recorded in the output text file %s" % (filename + "_result.txt")

records_txt = open(filename + "_result.txt", "w")
records_txt.write("Time that take to read csv table: %f\n" % (end - start))
records_txt.write("Errors Log: \n%s" % readcsv.errorlog)
records_txt.write("There are %s entries in the final table\n" % len(df))
if printing:
    records_txt.write("The table after filtering is: \n")
    records_txt.write(", ".join(readcsv.header))
    records_txt.write("\n")
    for row in readcsv.csv_df:
        records_txt.write(" ".join(row))
        records_txt.write("\n")
records_txt.close()
