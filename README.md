##  Bill Splitter ![js-standard-style](https://img.shields.io/badge/Python-brightgreen.svg?style=flat)
Several friends planned to go camping every year. The group agrees in advance to share expenses equally, but it is not practical to have them share every expense as it occurs. Each individual in the group will pay for particular things, like food, drinks, supplies, the campsite, parking, etc. After the camping trip, each person’s expenses are tallied and money is exchanged so that the net cost to each is the same. This task is tedious and time-consuming. The objective of this application is to compute the payable amount for each person going in camping.



## Input and Output
### Input
The information for each trip consists of a line containing a positive integer, n, the number of peopling participating in the camping trip, followed by n groups of inputs, one for each camping participant. Each group consists of a line containing a positive integer, p, the number of receipts/charges for that participant, followed by p lines of input, each containing the amount, in dollars and cents, for each charge by that camping participant. A single line containing 0 follows the information for the last camping trip
### Output
For each camping trip, output one line per participant indicating how much he/she must pay or be paid rounded to the nearest cent. If the participant owes money to the group, then the amount is positive. If the participant should collect money from the group, then the amount is negative. Negative amounts should be denoted by enclosing the amount in brackets. Each trip should be separated by a blank line.

### Prerequisites
```
Python 3.x
Pytest 5.4.1
```

### Installing
```
pip install -r requirements.txt
```

## Running the tests

Tests are written for each function and can be verified by the following command:<br/>
**For Linux and Mac**
```
$ PYTHONPATH=. pytest
```
**For Windows**
```
Powershell> $env:PYTHONPATH ="$(get-location)"
Powershell> pytest
```

### Unit Test Description
**testValidFilenames**: Given an array representing sys.argv<br/>It tests whether the output filename is created as expected.<br/>
**testThrowExceptionFilenotfound**: Given an array representing sys.argv<br/>It asserts the FileNotFoundError generated when filename in args is missing.<br/>
**testThrowExceptionArgMissing**: Given an array representing sys.argv<br/>It asserts the Exception when filename is missing in the args.<br/>
**testTransactionDataProcessing**: Given a sample input Data. It asserts the result whether it is evaluated properly.<br/>

### Main Program Execution
```
python BillSplit.py "input_file"
```

### Output File

```
"input_file".out
```

### Coding style:
![js-standard-style](https://img.shields.io/badge/code%20style-PEP%208-brightgreen.svg?style=flat)

