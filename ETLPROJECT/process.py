from pyspark.sql.functions import  lit
def transform(df):
    return df.withColumn("constant_value", lit(5))