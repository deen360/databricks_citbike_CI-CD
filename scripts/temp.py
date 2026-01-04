from databricks.connect import DatabricksSession
from utils.spark_reporting import report_spark_info

#spark = DatabricksSession.builder.remote(cluster_id="1206-190105-davv7lwz").getOrCreate()
spark = DatabricksSession.builder.getOrCreate()

# Report which session and python are being used
report_spark_info(spark)

spark.sql("SELECT 1").show()