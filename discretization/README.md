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
('x', 0, {'lo': 0.006301905962779143, 'hi': 0.1885467335528446, 'span': 0.18224482759006547, 'n': 9})
('x', 1, {'lo': 0.2187827654270375, 'hi': 0.31844542749153704, 'span': 0.09966266206449953, 'n': 8})
('x', 2, {'lo': 0.3462857563729797, 'hi': 0.43750006679329095, 'span': 0.09121431042031125, 'n': 8})
('x', 3, {'lo': 0.446259381923014, 'hi': 0.5983482080504057, 'span': 0.15208882612739166, 'n': 8})
('x', 4, {'lo': 0.6448972097807085, 'hi': 0.8133613824906579, 'span': 0.1684641727099494, 'n': 8})
('x', 5, {'lo': 0.8760911388677038, 'hi': 0.9985929657698576, 'span': 0.12250182690215372, 'n': 9})

We have fewer supervised ranges.
('super', 0, {'most': 0.31844542749153704, 'label': 1})
('super', 1, {'most': 0.43750006679329095, 'label': 2})
('super', 2, {'most': 0.5983482080504057, 'label': 3})
('super', 3, {'most': 0.9985929657698576, 'label': 4})
```
