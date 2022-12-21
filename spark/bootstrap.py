import os
import ast

import pandas as pd
from pyspark.sql import SparkSession
import pyspark.sql.functions as F

from sqlalchemy import create_engine

KAFKA_APP_TOPIC = os.environ.get('KAFKA_APP_TOPIC')
KAFKA_BOOTSTRAP_SERVERS = os.environ.get('KAFKA_BOOTSTRAP_SERVERS')

DATA_DIR = "./data"
INDEX = pd.read_parquet(DATA_DIR + '/index')

CONNECTION_URI = "postgresql://postgres:postgres@postgres:5432/mocommender"

engine = create_engine(CONNECTION_URI)
engine.connect()


spark = SparkSession \
    .builder \
    .master("local[*]") \
    .appName("Mocommender") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

def recommend(T, C, N=10):
  si = T.to_numpy().argpartition(range(-1, -N, -1))

  similarity_df = C[si[-1:-(N+2):-1]].drop(T, errors="ignore")

  return pd.DataFrame(similarity_df)


def load_chunk(df, i):
    print("*******WAITING********")
    a = df.select(F.col('value')).collect()

    if len(a) == 0:
        return
    
    user_id, movie_id = ast.literal_eval(a[0][0]).values()
    chunk_loc = int(INDEX[str(movie_id)])

    print(user_id, movie_id, chunk_loc)
    df = pd.read_parquet(DATA_DIR + f'/movie_genre_chunk_{chunk_loc}')
    columns = df.columns
    a = recommend(df.loc[str(movie_id)], columns, 10)
    a['user_id'] = [user_id]*11
    a['refer_id'] = [movie_id]*11

    a.to_sql(con=engine, name="mcuserrecommend", if_exists="replace", index=False)




def main():
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
