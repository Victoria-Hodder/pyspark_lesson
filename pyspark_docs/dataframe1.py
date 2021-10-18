from pyspark.sql import SparkSession
from datetime import datetime, date
from pyspark.sql import Row
from pyspark.sql.functions import upper, lower, pandas_udf
import pandas

# You can create a PySpark DataFrame from a list of rows
spark = SparkSession.builder.getOrCreate()

df = spark.createDataFrame([
    Row(a=1, b=2., c='string1', d=date(2000, 1, 1), e=datetime(2000, 1, 1, 12, 0)),
    Row(a=2, b=3., c='string2', d=date(2000, 2, 1), e=datetime(2000, 1, 2, 12, 0)),
    Row(a=4, b=5., c='string3', d=date(2000, 3, 1), e=datetime(2000, 1, 3, 12, 0))
])

# df.show()
# df.printSchema()
# print(df.columns)
# print(df.rows)

## Show the summary of the DataFrame
# df.select("a", "b", "c").describe().show()

##  Conversion back to a pandas DataFrame to leverage pandas APIs.
# print(df.toPandas())

## DataFrame.collect() collects the distributed data to the driver side as the local data in Python.
# print(df.collect())

## returns column instance
# print(df.a)

## df.select() takes column instances and returns another dataframe
df.select(df.c).show()

## df.filter() selects a subset of rows
# df.filter(df.a == 2).show()

## Assign new Column instance.
# df.withColumn('upper_c', upper(df.c)).show()
