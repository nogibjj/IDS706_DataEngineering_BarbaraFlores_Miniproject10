[![Format](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project1/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Miniproject10/actions/workflows/format.yml)
[![Lint](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project1/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Miniproject10/actions/workflows/lint.yml)
[![Install](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project1/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Miniproject10/actions/workflows/install.yml)
[![Test](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project1/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Miniproject10/actions/workflows/test.yml)



IDS706_DataEngineering_BarbaraFlores_Miniproject10
## 📂 PySpark Data Processing

The goal of this miniproject is to leverage PySpark for efficient data processing. In Week 10, we focus on using PySpark to work with large datasets, incorporating Spark SQL queries and data transformations to meet the specified requirements. Explore the power of PySpark in this project as we dive into data processing with a focus on functionality, SQL integration, and the delivery of a PySpark script and a comprehensive output report.


### 📊 Database

For this project, we will utilize the [Top Spotify Songs in 73 Countries](https://www.kaggle.com/datasets/asaniczka/top-spotify-songs-in-73-countries-daily-updated/) dataset. This dataset provides a comprehensive view of the top songs trending in over 70 countries, offering valuable insights into the dynamics of the music industry. It includes a wide range of information on the most popular songs in the world, such as unique Spotify identifiers, song names, artists, daily rankings, daily movement in rankings, and more.

This dataset comprises 25 variables (columns) and was extracted on 2023-11-05. In total, it contains 72.959 records.


### 📦 Data Processing with PySpark

In this project, we utilize the capabilities of PySpark to efficiently process a large dataset. PySpark empowers us to read and analyze data seamlessly, combining the power of Spark SQL for advanced queries and data transformations.

You can explore the analysis code in [main.py](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Miniproject10/blob/main/src/main.py) to understand how the data processing with PySpark was performed. The output of the analysis is available in [AnalysisResults.md](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Miniproject10/blob/main/output/AnalysisResults.md) This report provides insights into the total number of countries within our dataset.

Using PySpark, we can efficiently manage large-scale data, leveraging distributed computing to perform complex operations smoothly. With built-in support for Spark SQL, we can execute SQL queries on our dataset to gain valuable insights.

**Transformations Performed:**

In our project, we executed several transformations to prepare and analyze the dataset. We prepared the dataset by converting 'name' and 'artists' values to uppercase. This enhanced data uniformity and prepared it for subsequent queries.

**Spark SQL Analysis:** 

Additionally, we leveraged Spark SQL for advanced data querying and analysis, which included counting total records, determining unique country counts, identifying top artists, and finding the most played songs. These insights effectively fulfilled the project requirements.

### Results
As previously mentioned, the results obtained from our code are stored in file [AnalysisResults.md](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Miniproject10/blob/main/output/AnalysisResults.md), which include:

## Data Analysis with PySpark

The total number of records in our dataset is: 72,958

The total number of countries in our database is: 88

### Top Artists with Most Records

| Artist           |   Record Count |
|:-----------------|---------------:|
| TAYLOR SWIFT     |           3537 |
| BAD BUNNY        |           2600 |
| DOJA CAT         |           1083 |
| BIZARRAP, MILO J |            947 |
| TATE MCRAE       |            880 |

### Top Songs with Most Records

| Song                                | Artist           |   Record Count |
|:------------------------------------|:-----------------|---------------:|
| GREEDY                              | TATE MCRAE       |            880 |
| PAINT THE TOWN RED                  | DOJA CAT         |            853 |
| SI NO ESTÁS                         | IÑIGO QUINTERO   |            847 |
| STRANGERS                           | KENYA GRACE      |            788 |
| SEVEN (FEAT. LATTO) (EXPLICIT VER.) | JUNG KOOK, LATTO |            662 |






