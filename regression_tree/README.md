## Regression Tree

### Description:

Building regression tree learner: 
- Apply supervised Discretization
- At each level of the tree, break the data on the ranges and find the column whose breaks most reduces the variability of the target variable (we will use dom).
- For each break, apply the regression tree learner recursively.
- Recursion stops when the breaks do not improve the supervised target score, when there are tooFew examples to break, or when the tree depth is too much.
