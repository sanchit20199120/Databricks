import os
from util import get_spark_session

env= os.environ.get('ENVIRON')
spark = get_spark_session(env, 'GitHub Activity - Getting Started')

spark.sql('Select current_date').show()
