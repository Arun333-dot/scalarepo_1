from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from p3.config.ConfigStore import *
from p3.functions import *
from prophecy.utils import *
from p3.graph import *

def pipeline(spark: SparkSession) -> None:
    df_datasrte = datasrte(spark)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("p3")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/p3")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/p3", config = Config)(pipeline)

if __name__ == "__main__":
    main()
