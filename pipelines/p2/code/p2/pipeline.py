from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from p2.config.ConfigStore import *
from p2.functions import *
from prophecy.utils import *
from p2.graph import *

def pipeline(spark: SparkSession) -> None:
    df_datasrte = datasrte(spark)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("p2")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/p2")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/p2", config = Config)(pipeline)

if __name__ == "__main__":
    main()
