The purpose of this database is to load data from Sparkify is to load the data in the star schema from the songs files and the logs files for optimized for querying song play analysis

Schema Design

Fact table
songplays - records in log data associated with song plays i.e. records with page NextSong
songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

Dimentions table
users - users in the app
user_id, first_name, last_name, gender, level

songs - songs in music database
song_id, title, artist_id, year, duration

artists - artists in music database
artist_id, name, location, latitude, longitude

time - timestamps of records in songplays broken down into specific units
start_time, hour, day, week, month, year, weekday


List of scripts

sql_queries.py - includes (CRUD) queries
create_tables.py - Resets the database by droppoing and recreating the tables
etl.py - loads the json files for songs and logs dataset from the data folder on the db
