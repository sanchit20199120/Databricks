import os   ---to get the runtime parameter
from util import get_spark_session



def main():
    env= os.environ.get('ENVIRON')
    spark = get_spark_session(env, 'GitHub Activity - Getting Started')
    
    spark.sql('Select current_date').show()


if __name__ == '__main__':
  main()
