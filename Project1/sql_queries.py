# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES
# Songplays Table Create Statement
songplay_table_create = """
    CREATE TABLE IF NOT EXISTS songplays (songplays_id SERIAL PRIMARY KEY,
                                          time_start bigint,
                                          user_id int, level varchar,
                                          song_id varchar, artist_id varchar,
                                          session_id int, location varchar,
                                          user_agent varchar) """
# USERS Table Create Statement
user_table_create = """
    CREATE TABLE IF NOT EXISTS users (user_id int PRIMARY KEY,
                                      first_name varchar,
                                      last_name varchar,
                                      gender char,
                                      level varchar) """
# Songs Table Create Statement
song_table_create = """
    CREATE TABLE IF NOT EXISTS songs (song_id varchar PRIMARY KEY,
                                      title varchar,
                                      artist_id varchar, year int,
                                      duration decimal) """
# Artists Table Create Statement
artist_table_create = """
    CREATE TABLE IF NOT EXISTS artists (artist_id varchar PRIMARY KEY,
                                        name varchar, location varchar,
                                        latitude decimal,
                                        longitude decimal) """
# Time Table Create Statement
time_table_create = """
    CREATE TABLE IF NOT EXISTS time (time_start bigint, hour int, day int,
                                     weekofyear int, month int,
                                     year int, weekday int) """
# INSERT RECORDS
# Time Table Insert Statement
songplay_table_insert = """ INSERT INTO songplays (song_id, artist_id,
                                                    time_start, user_id, level,
                                                    session_id, location,
                                                    user_agent)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s) """
# USERS Table Insert Statement
user_table_insert = """ INSERT INTO users (user_id, first_name, last_name,
                                           gender, level)
                        VALUES (%s, %s, %s, %s, %s)
                        ON CONFLICT (user_id) DO NOTHING """
# Songs Table Insert Statament
song_table_insert = """ INSERT INTO songs (song_id, title, artist_id ,
                                            year, duration)
                        VALUES (%s, %s, %s, %s, %s)
                        ON CONFLICT (song_id) DO NOTHING """
# Artists Table Insert Statament
artist_table_insert = """ INSERT INTO artists (artist_id, name, location,
                                               latitude, longitude)
                          VALUES (%s, %s, %s, %s, %s)
                          ON CONFLICT (artist_id) DO NOTHING """
# Time Table Insert Statement
time_table_insert = """ INSERT INTO time (time_start, hour, day, weekofyear,
                                           month, year, weekday)
                        VALUES (%s, %s, %s, %s, %s, %s, %s) """
# FIND SONGS
# Song Select Statament
song_select = """ SELECT s.song_id, a.artist_id
                   FROM songs s
                   JOIN artists a
                   ON s.artist_id = a.artist_id
                   WHERE s.title = %s
                   AND a.name = %s
                   AND s.duration = %s ; """

# QUERY LISTS
create_table_queries = [
    songplay_table_create,
    user_table_create,
    song_table_create,
    artist_table_create,
    time_table_create,
]
drop_table_queries = [
    songplay_table_drop,
    user_table_drop,
    song_table_drop,
    artist_table_drop,
    time_table_drop,
]
