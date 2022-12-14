import os
import sys

from pyspark.sql import SparkSession
import pyspark.sql.functions as F

KAFKA_APP_TOPIC = os.environ.get('KAFKA_APP_TOPIC')
KAFKA_BOOTSTRAP_SERVERS = os.environ.get('KAFKA_BOOTSTRAP_SERVERS')

DATA_DIR="./data"

spark = SparkSession \
    .builder \
    .master("local[*]") \
    .appName("Mocommender") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")


def load_chunks_index():
    global spark
    return spark.read.parquet(DATA_DIR + '/index')

def load_chunks(i):
    global spark
    return spark.read.parquet(DATA_DIR + f'/movie_genre_chunk_{i}').unpersist(true)

def load_chunk(df, i):
    print(f"****************ROW(i)****************\n\t", df.select(F.col('value')).collect())

def main():
    #chunks_index = load_chunks_index()

    lines = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", KAFKA_BOOTSTRAP_SERVERS) \
        .option("subscribe", KAFKA_APP_TOPIC) \
        .option("startingOffsets", "earliest") \
        .load()

    q = lines.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)") \
        .writeStream \
        .trigger(processingTime='5 seconds') \
        .format("console") \
        .outputMode("append") \
        .foreachBatch(load_chunk) \
        .start()

    q.awaitTermination()

if __name__ == "__main__":
    main()
