from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Data Analysis with PySpark").getOrCreate()

path = "data/universal_top_spotify_songs.csv"
df = spark.read.csv(path, header=True, inferSchema=True)


df.show()


spark.stop()
