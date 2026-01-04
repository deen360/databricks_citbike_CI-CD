# test_datetime_utils.py

#import os
#import sys
## Adjust the sys.path to ensure imports work correctly
#sys.path.append(os.getcwd())



import datetime
from src.utils.datetime_utils import timestamp_to_date_col
#from utils.datetime_utils import timestamp_to_date_col
import datetime
#from pyspark.sql import SparkSession ->> local


def test_timestamp_to_date_col(spark):
#def test_timestamp_to_date_col():
#    #crate a Spark session to be removed later
#    #spark = SparkSession.builder.getOrCreate() -> local
#            
#    # Create a DataFrame with a known timestamp column using a datetime object
#    #try spark and pyspartk for ds session 
#    try: 
#        from databricks.connect import DatabricksSession
#        spark = DatabricksSession.builder.getOrCreate()    
#    except ImportError:
#        try:
#            from pyspark.sql import SparkSession
#            spark = SparkSession.builder.getOrCreate()           
#        except:
#            raise ImportError(" neither DatabricksSession nor SparkSession could be imported.")
            
    data = [(datetime.datetime(2025, 4, 10, 10, 30, 0),)]
    schema = "ride_timestamp timestamp"
    df = spark.createDataFrame(data, schema=schema)
    
    # Use the utility to add a date column
    result_df = timestamp_to_date_col(spark, df, "ride_timestamp", "ride_date")
    
    # Assert that the extracted date matches the expected value
    row = result_df.select("ride_date").first()

    expected_date = datetime.date(2025, 4, 10)  # Expected: 2025-04-10

    assert row["ride_date"] == expected_date