from pyspark.sql import SparkSession
from tabulate import tabulate

def calculate_country_count():
    spark = SparkSession.builder.appName("Data Analysis with PySpark").getOrCreate()
    path = "data/universal_top_spotify_songs.csv"
    df = spark.read.csv(path, header=True, inferSchema=True)

    df.createOrReplaceTempView("spotify_data")

    # Calcular el número total de registros utilizando una consulta SQL
    total_records_query = spark.sql("""
        SELECT COUNT(*) AS total_records
        FROM spotify_data
    """)
    
    total_records = total_records_query.first()["total_records"]

    country_count = spark.sql("""
        SELECT COUNT(DISTINCT country) AS total_countries
        FROM spotify_data
    """)

    total_countries = country_count.first()["total_countries"]

    with open("output/AnalysisResults.md", "w", encoding="utf-8") as md_file:
        md_file.write("#Data Analysis with PySpark\n\n")
        md_file.write(f"The total number of records in our dataset is: {total_records}\n\n")
        md_file.write(f"The total number of countries in our database is: {total_countries}\n\n")


    spark.stop()

if __name__ == "__main__":
    calculate_country_count()
