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
        tracks = [Track(title=result[0], artist=result[1], file=result[2]) for result in results]
        return tracks
    
    def add(self, track):
        query = 'INSERT INTO tracks (title, artist, file) VALUES (%s, %s, %s) RETURNING id'
        values = (track.title, track.artist, track.file)
        self.cursor.execute(query, values)
        self.conn.commit()
        return self.cursor.fetchone()[0]

    # def add(self, song):
    #     insert_query = 'INSERT INTO tracks (title, artist, file) VALUES (%s, %s, %s) RETURNING id'
    #     values = (song.title, song.artist, song.file)
    #     song_id = DatabaseConnection.exec_params(insert_query, values)[0][0]
    #     song.id = song_id

    # def remove(self, song_id):
    #     delete_query = 'DELETE FROM tracks WHERE id = %s'
    #     values = (song_id,)
    #     rows_deleted = DatabaseConnection.exec_params(delete_query, values)
    #     return rows_deleted > 0

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
