# Snowflake-pipeline-

This lab is based on the analytics team at Citi Bike, a real, citywide bike sharing system in New York City, USA. The team wants to run analytics on data from their internal transactional systems to better understand their riders and how to best serve them.

We will first load structured .csv data from rider transactions into Snowflake. Later we will work with open-source, semi-structured JSON weather data to determine if there is any correlation between the number of bike rides and the weather.


The data consists of information about trip times, locations, user type, gender, age, etc. On AWS S3, the data represents 61.5M rows, 377 objects, and 1.9GB compressed.

Below is a snippet from one of the Citi Bike CSV data files:

![image](https://github.com/kamibrenda/Snowflake-pipeline-/assets/42267047/2a0fdfe2-1274-4cd6-b88e-9093bbc118a3)

The Citi Bike analytics team wants to determine how weather impacts ride counts. To do this, in this section, we will:

1.Load weather data in semi-structured JSON format held in a public S3 bucket.
2.Create a view and query the JSON data using SQL dot notation.
3.Run a query that joins the JSON data to the previously loaded TRIPS data.
4.Analyze the weather and ride count data to determine their relationship.

The JSON data consists of weather information provided by MeteoStat detailing the historical conditions of New York City from 2016-07-05 to 2019-06-25. It is also staged on AWS S3 where the data consists of 75k rows, 36 objects, and 1.1MB compressed. If viewed in a text editor, the raw JSON in the GZ files looks like:

![image](https://github.com/kamibrenda/Snowflake-pipeline-/assets/42267047/821ac170-5f31-4183-8bf1-67e568b1ca64)



