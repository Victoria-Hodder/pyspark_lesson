import psycopg2
import pandas as pd
from pyspark.sql import SparkSession
from sqlalchemy import create_engine

def get_spark_session():
    appName = "PySpark PostgreSQL Example - via psycopg2"
    master = "local"
    spark = SparkSession.builder.master(master).appName(appName).getOrCreate()
    return spark
