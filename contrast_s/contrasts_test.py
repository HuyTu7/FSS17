import sys
sys.path.append('../regression_tree/')
from sdtree_test import sdTree
from contrast_sets import branches, plans, monitors


def record(data, fname):
    with open("%s_result.txt" % fname, "w") as text_file:
        text_file.write(data)


if __name__ == '__main__':
    file = sys.argv[1]
    built_tree = sdTree(file, None, 8)
    branches = branches(built_tree)

    _, plans_data = plans(branches)
    record(plans_data, "plans")
    _, monitors_data = monitors(branches)
    record(monitors_data, "monitors")