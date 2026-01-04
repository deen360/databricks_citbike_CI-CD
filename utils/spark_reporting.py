import sys
import logging

logger = logging.getLogger(__name__)


def report_spark_info(spark):
    """Report class, master and Python executable for a given Spark session."""
    try:
        cls = f"{spark.__class__.__module__}.{spark.__class__.__name__}"
    except Exception:
        cls = str(type(spark))
    master = getattr(getattr(spark, 'sparkContext', None), 'master', 'N/A')
    py = sys.executable
    logger.info("Spark class=%s master=%s python=%s", cls, master, py)
    print(f"Spark class={cls} master={master} python={py}")


def report_current_spark():
    """Try to find an active SparkSession (PySpark) and report it; returns True if found."""
    try:
        from pyspark.sql import SparkSession
        s = SparkSession.getActiveSession()
        if s:
            report_spark_info(s)
            return True
    except Exception:
        pass
    print("No active Spark session found.")
    return False
