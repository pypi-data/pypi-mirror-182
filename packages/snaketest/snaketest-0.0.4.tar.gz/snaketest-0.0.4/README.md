# snaketest

## instalation:
` pip install snaketest`
## runing

A small package to help test and prototype snakemake rules
```python
from  snaketest import *
```
The idea is to make the prototype as copypasteable as possible
Rou declare input and output by just initializing a snaketest class.
You can just copy paste the content of the input, output, log, params... 
```python
input = snaketest(
    table='data/table.csv',
    genome='data/genome.fa',
    sample = expand('data/sample/{sample}.csv',sample=[1,2,3]) #there's even an expand function
)
```
You can even use wildcards in them
```python
output = snaketest(
    csv='results/table_{chromosome}.csv',
)
```
But if you do you gotta create a wildcard SM which the other SM classes will refer to
```python
wildcards = snaketest(
  chromosome="chrY"
)
```
Now you can fill the code using SM variables:
```python
import pandas as pd
df = pd.read_csv(input.table)
df = df[df['chromosome']==wildcards.chromosome]
```
Because all variables are in the snakemake format, you can just test and copy paste withought needing to manually change anything.
