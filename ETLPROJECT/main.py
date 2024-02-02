import os
from util import get_spark_session
from read import from_files
from process import transform
from write import to_files

def main():
    env = os.environ.get("ENVIRON")
    src_dir = os.environ.get("SRC_DIR")
    src_file_format = os.environ.get("SRC_FILE_FORMAT")
    src_file_pattern = f'{os.environ.get("SRC_FILE_PATTERN")}*'
    tgt_dir =os.environ.get("TGT_DIR")
    tgt_file_format = os.environ.get("TGT_FILE_FORMAT")
    spark = get_spark_session(env, 'Github Activity -Getting Started')
    spark.sql('select current_date').show()
    df = from_files(spark, src_dir, src_file_pattern, src_file_format)
    df_transform = transform(df)
    to_files(df_transform, tgt_dir, tgt_file_format)


if __name__ == '__main__':
    main()
