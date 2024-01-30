from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql import Column
from pyspark.sql.functions import upper
from datetime import datetime, date
import pandas as pd

# Spark Session-------------------------------------------------------------------------------------
spark = SparkSession.builder.getOrCreate()

# Creating DataFrame --------------------------------------------------------------------------------

# create a PySpark DataFrame from a list of rows

df = spark.createDataFrame([
    Row(a=1, b=2., c='string1', d=date(2000, 1, 1), e=datetime(2000, 1, 1, 12, 0)),
    Row(a=2, b=3., c='string2', d=date(2000, 2, 1), e=datetime(2000, 1, 2, 12, 0)),
    Row(a=4, b=5., c='string3', d=date(2000, 3, 1), e=datetime(2000, 1, 3, 12, 0))
])
print(df.show())
print(df.printSchema())

# Create a PySpark DataFrame from a pandas DataFrame
pandas_df = pd.DataFrame({
    'a': [1, 2, 3],
    'b': [2., 3., 4.],
    'c': ['string1', 'string2', 'string3'],
    'd': [date(2000, 1, 1), date(2000, 2, 1), date(2000, 3, 1)],
    'e': [datetime(2000, 1, 1, 12, 0), datetime(2000, 1, 2, 12, 0), datetime(2000, 1, 3, 12, 0)]
})
df = spark.createDataFrame(pandas_df)
print(df.show())

# displaying top row
print(df.show(1))

# The rows can also be shown vertically
print(df.show(1, vertical=True))

# DataFrame’s column names- list of columns names will be displayed
print(df.columns)

# Show the summary of the DataFrame
print(df.describe().show())

'''
 DataFrame.collect() collects the distributed data to the driver side as the local data in Python. 
 Note that this can throw an out-of-memory error when the dataset is too large to fit in the driver side 
 because it collects all the data from executors to the driver side.
 '''

print(df.collect())

'''In order to avoid throwing an out-of-memory exception, use DataFrame.take() or DataFrame.tail()'''
print(df.take(1))

'''
PySpark DataFrame also provides the conversion back to a pandas DataFrame to leverage pandas API. 
Note that toPandas also collects all data into the driver side that can easily cause an out-of-memory-error 
when the data is too large to fit into the driver side.
'''

print(df.toPandas())


# Selecting and Accessing Data from the DataFrame-----------------------------------------------------------------------

'''
PySpark DataFrame is lazily evaluated and simply selecting a column does not trigger the computation but 
it returns a Column instance.
'''
print(df.select(df.c).show())


# Addding a new column = upper_c
print(df.withColumn('upper_c', upper(df.c)).show())

# To select a subset of rows, use DataFrame.filter().
print(df.filter(df.a == 1).show())


# Grouping --------------------------------------------------------------------------------------------------

# PySpark DataFrame with an explicit schema.
df = spark.createDataFrame([
    ['red', 'banana', 1, 10], ['blue', 'banana', 2, 20], ['red', 'carrot', 3, 30],
    ['blue', 'grape', 4, 40], ['red', 'carrot', 5, 50], ['black', 'carrot', 6, 60],
    ['red', 'banana', 7, 70], ['red', 'grape', 8, 80]], schema=['color', 'fruit', 'v1', 'v2'])
print(df.show())

print(df.groupby('color').avg().show())


# Getting Data In/Out----------------------------------------------------------------------------------------

# Read CSV file and creating  a DF
df = spark.read.csv('foo.csv', header=True)
print(df.show())

# Write dataframe  to CSV file
df.write.csv('foo.csv', header=True)


# Parquet
df.write.parquet('bar.parquet')
spark.read.parquet('bar.parquet').show()

# ORC
df.write.orc('zoo.orc')
spark.read.orc('zoo.orc').show()

# Working with SQL------------------------------------------------------------------------------------

df.createOrReplaceTempView("tableA")
spark.sql("SELECT count(*) from tableA").show()