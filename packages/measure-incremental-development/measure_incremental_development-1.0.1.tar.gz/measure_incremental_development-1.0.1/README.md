# Measure of Incremental Development
The Measure of Incremental Development (MID) is a metric that evaluates a student's 
adherence to incremental development given snapshots of the student's code at compilation. Currently, it has been 
developed and trained on student data from a Python-based, introductory computer science course.

## Usage

First, install the Python package in the appropriate directory with `pip` using:  
`pip install measure_incremental_development`

Second, import the `calculateMID` function in the Python file you would like to perform the calculation:  
`from measure_incremental_development.compute import calculate_mid`

Third, make the appropriate call to the `calculate_mid` function (make sure the input data is formatted correctly):  
`mid_statistic = calculate_mid(snapshots)`

Note: the input data `snapshots` should be formatted as described below

## Input Data Format

The `calculate_mid` function will take as input a *list of strings*, where each element is a string that is the exact text of the student code (including whitespace).

An example of an appropriate input:  

```python
from measure_incremental_development.compute import calculate_mid

snap1 = """def hello(name):
    print(name)"""

snap2 = """def hello(name):
    welcome_string = "Hello " + name"""

snap3 = """def hello(name):
    welcome_string = "Hello " + name
    return welcome_string"""

snapshots = [snap1, snap2, snap3]

mid_statistic = calculate_mid(snapshots)
```

## Interpretting Output

The metric will output any value greater than or equal to 0. *A lower score indicates a greater level of
incremental development*. Below are the categories of the scores:

- MID of [0 - 2]: Likely incremental
- MID of [2 - 2.5]: Somewhat incremental
- MID of [2.5-3]: Somewhat non-incremental
- MID of [3+]: Likely non-incremental

## Github Repository

The full code to calculate the Measure of Incremental Development (MID) can be found on [this Github repository](https://github.com/anshulshah99/measure-of-incremental-development).

## Additional Information and Citation

This metric was presented in a research paper presented at the 2023 SIGCSE Technical Symposium. You 
can find additional information about the motivation, development, and evaluation of the metric in 
the research paper. Use the citation below to access the paper.

Additionally, please use the following citation (in ACM Reference Format) if using this metric 
for a publication:

Anshul Shah, Michael Granado, Mrinal Sharma, John Driscoll, Leo Porter,
William G. Griswold, and Adalbert Gerald Soosai Raj. 2023. Understanding
and Measuring Incremental Development in CS1. In Proceedings of the 54th
ACM Technical Symposium on Computing Science Education V. 1 (SIGCSE
2023), March 15–18, 2023, Toronto, ON, Canada. ACM, New York, NY, USA,
7 pages. https://doi.org/10.1145/3545945.3569880
