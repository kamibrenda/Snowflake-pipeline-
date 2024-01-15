create database weather;

use role sysadmin;

use warehouse compute_wh;

use database weather;


use schema public;

--delete the table created
delete json_weather_data;