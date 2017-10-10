## Regression Tree

### Description:

Building regression tree learner: 
- Apply supervised Discretization
- At each level of the tree, break the data on the ranges and find the column whose breaks most reduces the variability of the target variable (we will use dom).
- For each break, apply the regression tree learner recursively.
- Recursion stops when the breaks do not improve the supervised target score, when there are tooFew examples to break, or when the tree depth is too much.


### Files:
- `sdtree.py`: implementation of regression tree learner
- `sdtree_test.py`: implementation of testing file for sdtree

### How to run:

- Assuming that you have installed python 2.7
- Execute the command line as below in the terminal within the `regression_tree` folder:
```
python sdtree_test.py <file_name>
```

### Report:

After building the tree from auto.csv file:

```
n=392 mu=67.00 sd=177.88
horsepower = 1                          :
| displacement = 1                      :
| | model = 1                           :n=11 mu=353.00 sd=28.98
| | model = 2                           :n=12 mu=312.00 sd=45.83
| | model = 3                           :n=13 mu=327.00 sd=35.21
| | model = 5                           :
| | | origin = 3                        :n=23 mu=341.00 sd=38.68
horsepower = 2                          :
| displacement = 1                      :n=22 mu=276.00 sd=40.12
| displacement = 2                      :n=21 mu=264.00 sd=58.57
| displacement = 3                      :
| | model = 5                           :n=15 mu=248.00 sd=32.17
horsepower = 3                          :
| cylinders = 4                         :
| | displacement = 2                    :n=13 mu=202.00 sd=44.33
| cylinders = 6                         :
| | displacement = 6                    :n=18 mu=135.00 sd=20.76
horsepower = 4                          :n=33 mu=137.00 sd=41.95
horsepower = 5                          :
| model = 4                             :n=10 mu=93.00 sd=9.00
horsepower = 6                          :
| model = 1                             :
| | displacement = 8                    :n=13 mu=63.00 sd=19.34
horsepower = 7                          :
| model = 1                             :
| | displacement = 9                    :n=10 mu=25.00 sd=16.79
horsepower = 8                          :
| model = 1                             :n=19 mu=18.00 sd=18.92

```
