# import Spark Session and functions
from pyspark.sql import SparkSession
from pyspark.sql.functions import row_number
from pyspark.sql.window import Window
from pyspark.sql.functions import lit, current_timestamp


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
        load('/Users/ketan/Desktop/sanchit/sample_data/RetailData/sales.csv/sales.csv', inferSchema="true", header="true")


# Number of records and list of column name
print(df.count())
print(df.columns)


# converting dataframe as a table  and taking ot 1000 records from the file and then write that file to my local system
'''

df.createOrReplaceTempView("salesTable")
df_new = spark.sql("select * from salesTable limit 1000")
print(df_new.count())

# writing a file in local 
df_new.write.csv('/Users/ketan/Desktop/sanchit/sample_data/sales.csv', header=True)

'''

df.show()

# using Window row_number() function  to give every row a unique id
window_spec = Window.orderBy("revenue")
print(window_spec)


# Transforming data by adding 3 new columns

df_new = df.withColumn("constant_value", lit(5)). \
        withColumn("Timestamp", current_timestamp()). \
        withColumn("row_number", row_number().over(Window.orderBy("revenue")))

print(df_new)

# write data

df_new.coalesce(16). \
        write. \
        partitionBy('product_id'). \
        mode('append'). \
        format('csv'). \
        save('/Users/ketan/PycharmProjects/Databricks/RetailData/WriteDataFromOneFileSparkApplication/')

print("Process Completed at")

