# Import required libraries
import pyspark
import helpers
import pandas

# Create spark session
spark = helpers.get_spark_session()

# Create a PostgreSQL connection using SQLAlchemy python package.
engine = create_engine(
    "postgresql+psycopg2://postgres:example@database/etl_pipeline?client_encoding=utf8")

# Pandas is used to create a DataFrame object using read_sql API.
movies_df = pandas.read_sql('select * from movies', engine)

# Convert Pandas dataframe to spark DataFrame
df = spark.createDataFrame(movies_df)
print(df.schema)
df.show()
