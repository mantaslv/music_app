import psycopg2
from dataclasses import dataclass

class Track:
    def __init__(self, id, title, artist, file):
        self.id = id
        self.title = title
        self.artist = artist
        self.file = file

    def __str__(self):
        return f"{self.title} by {self.artist}"

class MusicLibrary:
    def __init__(self, env='production'):
        self._tracks = []
        self._connection = None
        self._cursor = None
        self.env = env

        self._connection = psycopg2.connect(
            host="127.0.0.1",
            database="python_music" if env == 'production' else "python_music_test"
        )
        self._cursor = self._connection.cursor()
        self._create_table()

    def _create_table(self):
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS tracks (
            id SERIAL PRIMARY KEY,
            title VARCHAR,
            artist VARCHAR,
            file VARCHAR
        )
        '''
        self._cursor.execute(create_table_query)
        self._connection.commit()
    
    def all(self):
        select_query = 'SELECT * FROM tracks'
        self._cursor.execute(select_query)
        tracks = self._cursor.fetchall()
        return [Track(*track) for track in tracks]
    
    def add(self, song):
        insert_query = 'INSERT INTO tracks (title, artist, file) VALUES (%s, %s, %s) RETURNING id'
        values = (song.title, song.artist, song.file)
        self._cursor.execute(insert_query, values)
        song_id = self._cursor.fetchone()[0]
        self._connection.commit()
        song.id = song_id

    def remove(self, song_id):
        delete_query = 'DELETE FROM tracks WHERE id = %s'
        values = (song_id,)
        self._cursor.execute(delete_query, values)
        self._connection.commit()
        return self._cursor.rowcount > 0

    def search(self, condition):
        select_query = 'SELECT * FROM tracks'
        self._cursor.execute(select_query)
        tracks = self._cursor.fetchall()
        return [Track(*track) for track in tracks if condition(Track(*track))]

    def tally(self):
        select_query = 'SELECT artist, COUNT(*) FROM tracks GROUP BY artist'
        self._cursor.execute(select_query)
        tally_rows = self._cursor.fetchall()
        tally = {artist: count for artist, count in tally_rows}

        return tally

    def __del__(self):
        if self.env == 'production':
            self._cursor.close()
            self._connection.close()
