# FSS17
## HW1

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
python readcsv.py <file_name>
```

### Report:
Number of rows within the table: 10000
<br>
Time that take the program to read csv table `POM3A.csv` file: 0.288194
