# test_citibike_utils.py


#import os
#import sys
## Adjust the sys.path to ensure imports work correctly
#sys.path.append(os.getcwd())


import datetime
from src.citibike.citibike_utils import get_trip_duration_mins

#from citibike.citibike_utils import get_trip_duration_mins
#from pyspark.sql import SparkSession -> local

# Adjust the sys.path if needed (usually in conftest.py or at the top of your test files)

def test_get_trip_duration_mins(spark):
    
#def test_get_trip_duration_mins():
#    
#    #spark = SparkSession.builder.getOrCreate()
#    # Create a test DataFrame with known start and end timestamps using datetime objects
#    #we are doing this to avaodid error when we run it from the command line without ds session (as no spark is in  venv-dbc environment)
#    
#    try: 
#        from databricks.connect import DatabricksSession
#        spark = DatabricksSession.builder.getOrCreate()  
#        print("Using DatabricksSession for testing.")
#    except ImportError:
#        try:
#            from pyspark.sql import SparkSession
#            spark = SparkSession.builder.getOrCreate()  
#            print("Using local SparkSession for testing.")         
#        except:
#            raise ImportError(" neither DatabricksSession nor SparkSession could be imported.")
    data = [
        (datetime.datetime(2025, 4, 10, 10, 0, 0), datetime.datetime(2025, 4, 10, 10, 10, 0)),  # 10 minutes
        (datetime.datetime(2025, 4, 10, 10, 0, 0), datetime.datetime(2025, 4, 10, 10, 30, 0))   # 30 minutes
    ]
    schema = "start_timestamp timestamp, end_timestamp timestamp"
    df = spark.createDataFrame(data, schema=schema)
    
    # Apply the function to calculate trip duration in minutes
    result_df = get_trip_duration_mins(spark, df, "start_timestamp", "end_timestamp", "trip_duration_mins")
    
    # Collect the results for assertions
    results = result_df.select("trip_duration_mins").collect()
    
    # Assert that the differences are as expected
    assert results[0]["trip_duration_mins"] == 10
    assert results[1]["trip_duration_mins"] == 30