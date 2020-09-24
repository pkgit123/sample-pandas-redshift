# sample-pandas-redshift
Playbook for working with pandas and AWS Redshift (data warehouse).

The conventional way to interact with AWS Redshift using Python is via SQL statements and psycopg2 library.  However this workflow and syntax is very cumberson.  Goal to find a simple way to:
1. download data from Redshift into pandas
1. upload data from pandas into Redshift

There are some articles on the internet that suggest a solution using pandas and sqlalchemy.  However testing this solution, I find that it doesn't quite work correctly.  The table is uploaded to the "PUBLIC" schema (a built-in Redshift schema) and there is no simple way to target a different schema.

Instead this playbook uses library called `pandas_redshift`.

## Installation

```python
pip install pandas-redshift
```

## Reference: 
* https://github.com/agawronski/pandas_redshift
* https://stackoverflow.com/questions/38402995/how-to-write-data-to-redshift-that-is-a-result-of-a-dataframe-created-in-python/45452032#45452032
