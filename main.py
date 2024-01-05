from pyspark.sql import SparkSession
from pyspark.sql import Row
from datetime import datetime, date
import pandas as pd

spark = SparkSession.builder.getOrCreate()

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