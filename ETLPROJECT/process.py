from pyspark.sql.functions import lit, current_timestamp
from pyspark.sql.functions import row_number
from pyspark.sql.window import Window
def transform(df):
    # adding new column with default value 5
    return df.withColumn("constant_value", lit(5)). \
        withColumn("Timestamp", current_timestamp()). \
        withColumn("row_number", row_number().over(Window.orderBy("revenue")))  # adding new column with row number

