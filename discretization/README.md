# FSS17

## Problem 3: Discretization

### Descriptions:

#### Unsupervised Discretization: [range](https://lualure.github.io/info/range)
Takes a table column of `N` numbers, sorts in, and breaks into bins of size approximately `sqrt(N)`. Note that these breaks have to satisfy the following sanity rules:

+ no range contains too few numbers `(sqrt(N))`;
+ each range is different to the next one by some epsilon value `(0.2 * standard deviation of that column)`;
+ the `span` of the range `(hi - lo)` is greater than that `epsilon`;
+ the `lo` value of one range is greater than the `hi` value of the previous range

#### Supervised Discretization: [superrange](https://lualure.github.io/info/superrange)

Reflects over the ranges found by the unsupervised discretizer. Combine ranges where some dependent variable is not changed across that combination of ranges. Specifically, sort the ranges and do a recursive descent of the ranges. At each level of the recursion, break the ranges at the point that most minimizes the expected value of the standard deviation of the dependent variable.

### Files:
- `range_1.py`: unsupervised discretization 

- `range_test.py`: testing the unsupervised discretization 

- `sample_random.py`: 
  - Random class: similar to `math.random()` as the replacement for the ANSI C rand() and srand() functions
  - Sample class: a sample of the numbers in this range;

- `readData.py`: updated Nums and Syms to be used for unsupervised and supervised discretization of data

### Report:
