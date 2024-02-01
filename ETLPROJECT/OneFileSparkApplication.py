# import Spark Session
from pyspark.sql import SparkSession
from pyspark.sql.functions import row_number
from pyspark.sql.window import Window

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
        load('/Users/ketan/PycharmProjects/Databricks/RetailData/store_cities.csv', inferSchema="true", header="true")


# showing result
df.show()



df1 = df.withColumn("row_number", row_number().over(Window.orderBy(df.city_id.desc)))
df1.show()
