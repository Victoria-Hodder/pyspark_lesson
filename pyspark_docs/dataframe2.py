from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

## Create a PySpark DataFrame with an explicit schema.
df = spark.createDataFrame([
    ['red', 'banana', 1, 10], ['blue', 'banana', 2, 20],
    ['red', 'carrot', 3, 30], ['blue', 'grape', 4, 40],
    ['red', 'carrot', 5, 50], ['black', 'carrot', 6, 60],
    ['red', 'banana', 7, 70], ['red', 'grape', 8, 80]],
    schema=['color', 'fruit', 'num1', 'num2'])

# df.show()

df.groupby('fruit').avg().show()
