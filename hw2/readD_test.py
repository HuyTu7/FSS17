import time
import sys
from readData import ReadData

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