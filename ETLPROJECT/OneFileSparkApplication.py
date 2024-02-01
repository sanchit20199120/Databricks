# import Spark Session
from pyspark.sql import SparkSession

# Initiating Spark Session
spark = SparkSession. \
        builder. \
        master('local'). \
        appName('pyspark application'). \
        getOrCreate()

# reading csv file
df = spark. \
        read. \
        format('csv'). \
        load('/Users/ketan/PycharmProjects/Databricks/RetailData/store_cities.csv')

# showing result
df.show()