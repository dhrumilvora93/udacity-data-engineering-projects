## Project Description

A music streaming startup, Sparkify, has grown the user base and 
song database and want to move their processes and data onto the 
cloud. Their data resides in S3, in a directory of JSON logs on
user activity on the app, as well as a directory with JSON metadata
on the songs in their app.

ETL pipeline that extracts their data from S3, processes them using 
Spark, and loads the data back into S3. This will allow their analytics 
team to continue finding insights in what songs their users are listening to.

### ETL Design

Idea is to load the logs files from s3 and the streaming data from 
s3 to AWS EMR Cluster Memory

from the Memory move the relevent filtered and processed 
data by spilitting them into required parquet format base on the tables.

### Schema Design

Fact table
songplays - records in log data associated with song plays i.e. records with page NextSong
songplay_id,  years ,month, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
partitioned by years ,month

Dimentions table
users - users in the app
user_id, first_name, last_name, gender, level

songs - songs in music database
song_id, title, artist_id, year, duration
partitioned by year, artist_id

artists - artists in music database
artist_id, name, location, latitude, longitude

time - timestamps of records in songplays broken down into specific units
start_time, hour, day, week, month, years, weekday
partitioned by years, month


### List of scripts

dl.cfg - configuration file to store AWS Credentials
etl.py - loads the json files for songs and logs dataset from the s3 folder on the Memory then back into s3


### Steps to run

1. Provide credentials in dl.cfg
2. Provide the s3 input path where the data is located and the output bucket in etl.py
3. Run 'python etl.py'