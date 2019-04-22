# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = (
				"""
				CREATE TABLE songplays (
					songplay_id SERIAL PRIMARY KEY, 
					start_time TIME WITHOUT TIME ZONE,
					user_id INTEGER NOT NULL,
					level VARCHAR(255) NOT NULL,
					song_id VARCHAR(255) NOT NULL,
					artist_id VARCHAR(255) NOT NULL,
					session_id INTEGER,
					location VARCHAR(100) NOT NULL,
					user_agent VARCHAR(255) NOT NULL)
				"""
				)

user_table_create = (
				"""
				CREATE TABLE users (
					user_id VARCHAR(255),
					first_name VARCHAR(255),
					last_name VARCHAR(255),
					gender VARCHAR(100),
					level VARCHAR(255))
				""")

song_table_create = (
				"""
				CREATE TABLE songs (
					song_id VARCHAR(255) NOT NULL,
					title VARCHAR(255) NOT NULL,
					artist_id VARCHAR(255) NOT NULL,
					year INTEGER NOT NULL,
					duration FLOAT NOT NULL)
				""")

artist_table_create = (
				"""
				CREATE TABLE artists (
					artist_id VARCHAR(255),
					name VARCHAR(255),
					location VARCHAR(255),
					lattitude FLOAT,
					longitude FLOAT)
				""")

time_table_create = (
				"""
				CREATE TABLE time (
					start_time time without time zone NOT NULL,
					hour INT NOT NULL,
					day INT NOT NULL,
					week INT NOT NULL,
					month INT NOT NULL,
					year INT NOT NULL,
					weekday INT NOT NULL)
				""")

# INSERT RECORDS

songplay_table_insert = (
				"""
				INSERT INTO songplays (
					start_time,
					user_id,
					level,
					song_id,
					artist_id,
					session_id,
					location,
					user_agent)
				VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
				""")

user_table_insert = (
				"""
				INSERT INTO users (user_id, first_name, last_name, gender, level)
				VALUES (%s, %s, %s, %s, %s)
				""")

song_table_insert = (
				"""
				INSERT INTO songs (song_id, title, artist_id, year, duration)
				VALUES (%s, %s, %s, %s, %s)
				""")

artist_table_insert = (
				"""
				INSERT INTO artists (artist_id, name, location, lattitude, longitude)
				VALUES (%s, %s, %s, %s, %s)
				""")

time_table_insert = (
				"""
				INSERT INTO time (start_time, hour, day, week, month, year, weekday)
				VALUES (%s, %s, %s, %s, %s, %s, %s)
				""")

# FIND SONGS
song_select = (""" SELECT songs.song_id, songs.artist_id FROM songs JOIN artists ON songs.artist_id = artists.artist_id """)

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]