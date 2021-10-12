from pyspark.sql import SparkSession

def get_spark_session():
    appName = "PySpark PostgreSQL Example - via psycopg2"
    master = "local"
    # Establish a SparkSession with local master.
    spark = SparkSession.builder.master(master).appName(appName).getOrCreate()
    return spark
