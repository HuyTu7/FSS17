# FSS17

## Problem 3: Discretization

### Descriptions:

#### Unsupervised Discretization: [range](https://lualure.github.io/info/range)
Takes a table column of `N` numbers, sorts in, and breaks into bins of size approximately `sqrt(N)`. Note that these breaks have to satisfy the following sanity rules:

+ no range contains too few numbers `(sqrt(N))`;
+ each range is different to the next one by some epsilon value `(0.2 * standard deviation of that column)`;
+ the `span` of the range `(hi - lo)` is greater than that `epsilon`;
+ the `lo` value of one range is greater than the `hi` value of the previous range

Note: This code follows EFD type of unsupervised discretization which stands for Equal frequency discretisation i.e. divide the numbers according to percentiles says (e.g.) lower, middle, upper third of the numbers

#### Supervised Discretization: [superrange](https://lualure.github.io/info/superrange)

Reflects over the ranges found by the unsupervised discretizer. Combine ranges where some dependent variable is not changed across that combination of ranges. Specifically, sort the ranges and do a recursive descent of the ranges. At each level of the recursion, break the ranges at the point that most minimizes the expected value of the standard deviation of the dependent variable.

### Files:
#### main:
- `range_1.py`: the implementation of unsupervised discretization 

- `super_range.py`:  the implementation of supervised discretization 

#### helpers:
- `sample_random.py`: 
  - Random class: similar to `math.random()` as the replacement for the ANSI C rand() and srand() functions
  - Sample class: a sample of the numbers in this range;

- `num.py`: the implementation of NUM class extracted from `readData.py` from hw2 for numeric type of data operating

- `sym.py`: the implementation of SYM class extracted from `readData.py` from hw2 for symbolic type of data operating
 
#### tests:
- `range_test.py`: testing the unsupervised discretization 

- `suprange_test.py`: testing the supervised discretization 

### How to run:

- Assuming that you have installed python 2.7
- Execute the command line as below in the terminal within the `discretization` folder to test the unsupervised and supervised discretization:
```
python suprange_test.py 
```

### Report:

Results after running the test file:
```
We have many unsupervised ranges.
('x', 0, {'lo': 0.006301905962779143, 'hi': 0.2566107857304675, 'span': 0.2503088797676884, 'n': 26})
('x', 1, {'lo': 0.2621757547660618, 'hi': 0.47683985646666954, 'span': 0.21466410170060773, 'n': 26})
('x', 2, {'lo': 0.4996578257994996, 'hi': 0.9985929657698576, 'span': 0.498935139970358, 'n': 48})

We have fewer supervised ranges.
('super', 0, {'most': 0.47683985646666954, 'label': 1})
('super', 1, {'most': 0.9985929657698576, 'label': 2})
```
