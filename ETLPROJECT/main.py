import os
from util import get_spark_session
from read import from_files
from process import transform

def main():
    env = os.environ.get("ENVIRON")
    src_dir = os.environ.get("SRC_DIR")
    src_file_format = os.environ.get("SRC_FILE_FORMAT")
    src_file_pattern = f'{os.environ.get("SRC_FILE_PATTERN")}*'
    spark = get_spark_session(env, 'Github Activity -Getting Started')
    spark.sql('select current_date').show()
    df = from_files(spark, src_dir, src_file_pattern, src_file_format)
    df_transform = transform(df)
    df.printSchema()
    df.show()
    df_transform.show()
    df_transform.printSchema()


if __name__ == '__main__':
    main()
