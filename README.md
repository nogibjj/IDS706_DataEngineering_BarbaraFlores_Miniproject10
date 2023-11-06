[![Format](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project1/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Miniproject10/actions/workflows/format.yml)
[![Lint](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project1/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Miniproject10/actions/workflows/lint.yml)
[![Install](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project1/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Miniproject10/actions/workflows/install.yml)
[![Test](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project1/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Miniproject10/actions/workflows/test.yml)



IDS706_DataEngineering_BarbaraFlores_Miniproject10
# 📂 PySpark Data Processing

The goal of this miniproject is to leverage PySpark for efficient data processing. In Week 10, we focus on using PySpark to work with large datasets, incorporating Spark SQL queries and data transformations to meet the specified requirements. Explore the power of PySpark in this project as we dive into data processing with a focus on functionality, SQL integration, and the delivery of a PySpark script and a comprehensive output report.

## 🌳 📊 Project Structure:
```bash
.
├── LICENSE
├── Makefile
├── README.md
├── data
│   └── universal_top_spotify_songs.csv
├── images
│   ├── Step1.png
│   └── Step2.png
├── output
│   └── AnalysisResults.md
├── requirements.txt
├── setup.sh
├── src
│   └── main.py
└── test
    ├── __pycache__
    │   └── test_main.cpython-38-pytest-7.1.3.pyc
    └── test_main.py

```

## 📊 Database

For this project, we will utilize the [Top Spotify Songs in 73 Countries](https://www.kaggle.com/datasets/asaniczka/top-spotify-songs-in-73-countries-daily-updated/) dataset. This dataset provides a comprehensive view of the top songs trending in over 70 countries, offering valuable insights into the dynamics of the music industry. It includes a wide range of information on the most popular songs in the world, such as unique Spotify identifiers, song names, artists, daily rankings, daily movement in rankings, and more.

This dataset comprises 25 variables (columns) and was extracted on 2023-11-05. In total, it contains 72.959 records.


## 📦 Data Processing with PySpark

In this project, we utilize the capabilities of PySpark to efficiently process a large dataset. PySpark empowers us to read and analyze data seamlessly, combining the power of Spark SQL for advanced queries and data transformations.

You can explore the analysis code in [main.py](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Miniproject10/blob/main/src/main.py) to understand how the data processing with PySpark was performed. The output of the analysis is available in [AnalysisResults.md](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Miniproject10/blob/main/output/AnalysisResults.md) This report provides insights into the total number of countries within our dataset.

Using PySpark, we can efficiently manage large-scale data, leveraging distributed computing to perform complex operations smoothly. With built-in support for Spark SQL, we can execute SQL queries on our dataset to gain valuable insights.

**Transformations Performed:**

In our project, we executed several transformations to prepare and analyze the dataset. We prepared the dataset by converting 'name' and 'artists' values to uppercase. This enhanced data uniformity and prepared it for subsequent queries.

**Spark SQL Analysis:** 

Additionally, we leveraged Spark SQL for advanced data querying and analysis, which included counting total records, determining unique country counts, identifying top artists, and finding the most played songs. These insights effectively fulfilled the project requirements.

## 📈 Results
As previously mentioned, the results obtained from our code are stored in file [AnalysisResults.md](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Miniproject10/blob/main/output/AnalysisResults.md), which include:

### Data Analysis with PySpark

The total number of records in our dataset is: 72,958

The total number of countries in our database is: 88

#### Top Artists with Most Records

| Artist           |   Record Count |
|:-----------------|---------------:|
| TAYLOR SWIFT     |           3537 |
| BAD BUNNY        |           2600 |
| DOJA CAT         |           1083 |
| BIZARRAP, MILO J |            947 |
| TATE MCRAE       |            880 |

#### Top Songs with Most Records

| Song                                | Artist           |   Record Count |
|:------------------------------------|:-----------------|---------------:|
| GREEDY                              | TATE MCRAE       |            880 |
| PAINT THE TOWN RED                  | DOJA CAT         |            853 |
| SI NO ESTÁS                         | IÑIGO QUINTERO   |            847 |
| STRANGERS                           | KENYA GRACE      |            788 |
| SEVEN (FEAT. LATTO) (EXPLICIT VER.) | JUNG KOOK, LATTO |            662 |




## 📚User Instructions

1. Clone this repository:
   
   Go to the [repository page](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Miniproject10/tree/main), then click on "Use this template," and then "Create New Repository."

![Step 1: Clone the repository](https://raw.githubusercontent.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Miniproject10/main/images/Step1.png)


2. Create a Codespace and Set Up Your Development Environment

![Step 2: Clone the repository](https://raw.githubusercontent.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Miniproject10/main/images/Step2.png)


- Make sure you have Python 3.8 or later installed on your system.
- Install project dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Project:

- Run the project script by executing the following command:

```bash
python src/main.py
```

4. Explore the Output:

- Once the script has run successfully, you will find the analysis results in the `output/AnalysisResults.md` file. You can open this Markdown file to view the project's findings.

- Additionally, you can modify and extend the project code in the `src/main.py` file to perform further data processing and analysis as needed.

Now you're all set to work with this project! Enjoy exploring the data and performing data analysis with PySpark.
