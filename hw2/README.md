# FSS17
## HW2

### Description: 

Read each line, kill whitepsace and anything after comment characters (`#`), break each line on comma, read rows into a list of lists (one list per row), converting strings to numbers where appropriate. Note that some column headers contain `?`: all such columns should be ignored. 

Your code should contain checks for bad lines (and bad lines should be skipped over); i.e. symbols where numbers should be and wrong number of cells (we will say that row1 has the “right” length).

### Files: 

_ `readcsv.py`: python file to execute the work for this assignment 

_ `POM3A.csv`: given original csv table file 

_ `example.csv`: simple testing csv table file 

_ `POM3A_test.csv`: testing csv table file with added bad lines 

### How to run:

- Assuming that you have installed python 2.7
- Execute the command line as below in the terminal within the `hw1` folder:
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
