# FSS17
## HW2

### Description: 

+ Read lines from CSV files one a time incrementally updating column headers for each line.
+ Headers are either Nums or Syms as determined by the magic characters in row1.
+ Num and Syms incremental maintain knowledge about `mean`, `standard deviation`, and symbol `counts` in a column. For details, see the update function in:
  + [Num](https://lualure.github.io/info/num.html)
  + [Sym](https://lualure.github.io/info/sym.html)
+ So when the table reads row1, it builds the headers of Nums and Syms. And when the other rows are read, the headers get updated.
+ Code up the domination counter (the dom function in [Tbl](https://lualure.github.io/info/tbl.html) which also uses dominate and dominate1 in [Row](https://lualure.github.io/info/row.html)
+ Test: Find and print the top and bottom ten rows of `auto.csv`, as sorted by their dom score. with the top 5 and the bottom 5 domination scores. 

### Files: 

_ `readData.py`: python file to execute the work for this assignment 

_ `auto.csv`: given original csv data table file 

### How to run:

- Assuming that you have installed python 2.7
- Execute the command line as below in the terminal within the `hw2` folder:
```
python readData.py <file_name>
```

### Report:
- Unexpected data type in line: 179, 208, 211, 234, 362, 392 
- There are 392 entries in the table
- Time that takes to read file "auto.csv": 1.376338
- Headers: 
['cylinders', '$displacement', '$horsepower', '<weight', '>acceleration', '$model', 'origin', '>mpg']
- Top 5 rows for their domination scores
```
[4, 71, 65, 1773, 19, 71, 3, 30] 318
[4, 81, 60, 1760, 16.1, 81, 3, 40] 365
[4, 79, 58, 1755, 16.9, 81, 3, 40] 388
[4, 76, 52, 1649, 16.5, 74, 3, 30] 320
[4, 72, 69, 1613, 18, 71, 3, 40] 363
```
- Bottom 5 rows for their domination scores
```
[8, 400, 175, 5140, 12, 71, 1, 10] 15
[8, 400, 150, 4997, 14, 73, 1, 10] 6
[8, 383, 180, 4955, 11.5, 71, 1, 10] 8
[8, 429, 198, 4952, 11.5, 73, 1, 10] 10
[8, 455, 225, 4951, 11, 73, 1, 10] 11
```
