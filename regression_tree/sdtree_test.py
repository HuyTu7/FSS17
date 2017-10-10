import sys
sys.path.append('../utils/')
import sdtree as TREE
from table import TBL


def sdTree(f, y, min_d):
    TREE.tree_min_depth = min_d
    y = y or "dom"
    f = f or "auto.csv"

    tb1 = TBL(f)
    tb2 = tb1.discretize_rows(getattr(tb1, y))
    print "finishing discretizing rows"
    tr = TREE.grow(tb2, y=tb1.dom)
    print "finishing growing tree"
    TREE.tprint(tr, 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python sdtree_test.py <csv_file>")
        sys.exit(0)
    else:
        file = sys.argv[1]
        sdTree(file, None, 10)

