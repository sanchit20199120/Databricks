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
        load('/Users/ketan/Desktop/sanchit/sample_data/RetailData/sales.csv/sales.csv', inferSchema="true", header="true")


# Number of records
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

# adding row number column to the df
df1 = df.withColumn("row_number", row_number().over(window_spec))
df1.show()



