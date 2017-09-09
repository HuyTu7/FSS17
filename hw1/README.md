# FSS17
## HW1

### Descriptions: 

Read each line, kill whitepsace and anything after comment characters (`#`), break each line on comma, read rows into a list of lists (one list per row), converting strings to numbers where appropriate. Note that some column headers contain `?`: all such columns should be ignored. 

### Files: 

_ `readcsv.py`: python file to execute the work for this assignment 

_ `POM3A.csv`: given original csv table file 

_ `example.csv`: simple testing csv table file 

_ `POM3A\_test.csv`: testing csv table file with added bad lines 

### How to run:

- Assuming that you have installed python 2.7
- Search for the line: `df = readcsv.readfile("./POM3A.csv")`
- Edit the text inside the quotation for the file that you want the file `readcsv.py` to read
- Run the file as below in the terminal within the folder:
```
python readcsv.py 
```

### Report:
Time that take the program to read csv table POM3A.csv file: 0.288194
<br>
Number of rows: 10000
