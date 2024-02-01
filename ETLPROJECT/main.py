import os
from util import get_spark_session
from read import from_files

def main():
    env = os.environ.get("ENVIRON")
    src_dir = os.environ.get("SRC_DIR")
    src_file_format = os.environ.get("SRC_FILE_FORMAT")
    src_file_pattern = f'{os.environ.get("SRC_FILE_PATTERN")}*'
    spark = get_spark_session(env, 'Github Activity -Getting Started')
    spark.sql('select current_date').show()
    df = from_files(spark, src_dir, src_file_pattern, src_file_format)
    df.printSchema()
    df.show()


if __name__ == '__main__':
    main()
