import psycopg2

class Track:
    def __init__(self, title, artist, file):
        self.title = title
        self.artist = artist
        self.file = file
        self.id = None

    def __str__(self):
        return f"{self.title} by {self.artist}"

class MusicLibrary:
    def __init__(self):
        self.db_name = "python_music"
        self.cursor = None
        self.connect()

    def connect(self):
        self.conn = psycopg2.connect(
            database=self.db_name,
        )
        self.cursor = self.conn.cursor()

    def create_table(self):
        query = """
            CREATE TABLE IF NOT EXISTS tracks (
                id SERIAL PRIMARY KEY,
                title TEXT NOT NULL,
                artist TEXT NOT NULL,
                file TEXT NOT NULL
            )
        """
        self.cursor.execute(query)
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def all(self):
        query = 'SELECT title, artist, file FROM tracks'
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        tracks = [Track(*result) for result in results]
        return tracks
    
    def add(self, track):
        query = 'INSERT INTO tracks (title, artist, file) VALUES (%s, %s, %s) RETURNING id'
        values = (track.title, track.artist, track.file)
        self.cursor.execute(query, values)
        self.conn.commit()
        return self.cursor.fetchone()[0]
    
    def remove(self, song_id):
        query = 'DELETE FROM tracks WHERE id = %s'
        values = (song_id,)
        self.cursor.execute(query, values)
        self.conn.commit()

    def search(self, condition):
        query = 'SELECT title, artist, file FROM tracks'
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        tracks = [Track(*result) for result in results if condition(Track(*result))]
        return tracks

    # def search(self, condition):
    #     select_query = 'SELECT title, artist, file FROM tracks'
    #     tracks = DatabaseConnection.exec_params(select_query)
    #     return [Track(*track) for track in tracks if condition(Track(*track))]

    # def tally(self):
    #     select_query = 'SELECT artist, COUNT(*) FROM tracks GROUP BY artist'
    #     tally_rows = DatabaseConnection.exec_params(select_query)
    #     tally = {artist: count for artist, count in tally_rows}

    #     return tally

    # def __del__(self):
    #     if self.env == 'production':
    #         self._connection.close()
