##import required libraries
import pyspark
import helpers
import pandas

##create spark session
spark = helpers.get_spark_session()

engine = create_engine(
    "postgresql+psycopg2://postgres:example@database/etl_pipeline?client_encoding=utf8")

movies_df = pandas.read_sql('select * from movies', engine)

# Convert Pandas dataframe to spark DataFrame
df = spark.createDataFrame(movies_df)
print(df.schema)
df.show()
