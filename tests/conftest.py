import sys
import os
import pytest
import logging

# Run the tests from the root directory
sys.path.append(os.getcwd())

# Returning a Spark Session

logger = logging.getLogger(__name__)

def report_spark_info(spark):
    try:
        cls = f"{spark.__class__.__module__}.{spark.__class__.__name__}"
    except Exception:
        cls = str(type(spark))
    master = getattr(getattr(spark, 'sparkContext', None), 'master', 'N/A')
    python_executable = sys.executable
    logger.info("Spark class=%s master=%s python=%s", cls, master, python_executable)
    print(f"Spark class={cls} master={master} python={python_executable}")

@pytest.fixture()
def spark():
    try:
        # Prefer DatabricksSession when available
        from databricks.connect import DatabricksSession
        try:
            # serverless builder (if applicable)
            spark = DatabricksSession.builder.serverless().getOrCreate()
            logger.info("Using DatabricksSession (Spark Connect) for testing.")
            print("Using DatabricksSession (Spark Connect) for testing.")
        except Exception as e:
            # Databricks present but failed to initialize (likely auth/config); fall back to local
            logger.warning("DatabricksSession present but failed to initialize (%s), falling back to local Spark.", e)
            print(f"DatabricksSession present but failed to initialize ({e}), falling back to local Spark.")
            raise ImportError from e
    except ImportError:
        try:
            # Local Spark for testing
            from pyspark.sql import SparkSession
            python_executable = sys.executable
            logger.info("Using local SparkSession for testing (python=%s)", python_executable)
            print(f"Using local SparkSession for testing (python={python_executable})")

            # Ensure Spark uses the same Python executable as the test runner
            os.environ.setdefault("PYSPARK_PYTHON", python_executable)
            os.environ.setdefault("PYSPARK_DRIVER_PYTHON", python_executable)

            builder = SparkSession.builder \
                .master("local[1]") \
                .appName("pytest") \
                .config("spark.driver.host", "127.0.0.1") \
                .config("spark.driver.bindAddress", "127.0.0.1") \
                .config("spark.executorEnv.PYSPARK_PYTHON", python_executable) \
                .config("spark.local.ip", "127.0.0.1")

            spark = builder.getOrCreate()
        except Exception as e:
            raise ImportError("Neither Databricks Session or Spark Session are available") from e

    # Report and yield
    try:
        report_spark_info(spark)
        yield spark
    finally:
        try:
            spark.stop()
        except Exception:
            pass