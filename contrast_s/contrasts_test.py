import sys
sys.path.append('../regression_tree/')
from sdtree_test import sdTree
from contrast_sets import branches, plans, monitors

if __name__ == '__main__':
    file = sys.argv[1]
    built_tree = sdTree(file, None, 8)
    branches = branches(built_tree)

    plans(branches)
    monitors(branches)