from pyspark.sql import SparkSession
from tabulate import tabulate

def perform_data_analysis():
    spark = SparkSession.builder.appName("Data Analysis with PySpark").getOrCreate()
    path = "data/universal_top_spotify_songs.csv"
    df = spark.read.csv(path, header=True, inferSchema=True)
    df.createOrReplaceTempView("spotify_data")

    country_count = spark.sql("""
        SELECT COUNT(DISTINCT country) AS total_countries
        FROM spotify_data
    """)

    markdown_table = tabulate(country_count.collect(), headers=['Country', 'Count'], tablefmt='pipe')

    with open("output/AnalysisResults.md", "w") as md_file:
        md_file.write("# Data Analysis with PySpark\n\nThe total number of countries in our database is:\n\n")  # Línea de título
        md_file.write(markdown_table)

    spark.stop()

if __name__ == "__main__":
    perform_data_analysis()
