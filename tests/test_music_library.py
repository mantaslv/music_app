import unittest
import psycopg2
from player.music_library import MusicLibrary, Track

class TestMusicLibrary(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Connect to the test database
        cls.connection = psycopg2.connect(
            host="127.0.0.1",
            database="python_music_test"
        )
        cls.cursor = cls.connection.cursor()
        cls.music_library = MusicLibrary(env='test')

    @classmethod
    def tearDownClass(cls):
        # Clean up the test database and close the connection
        cls.cursor.close()
        cls.connection.close()

    def setUp(self):
        # Clear any existing data in the test database before each test
        self.cursor.execute("DELETE FROM tracks")
        self.connection.commit()

    def test_constructs(self):
        self.assertIsInstance(self.music_library, MusicLibrary)

    def test_returns_empty_all(self):
        self.assertEqual(self.music_library.all(), [])

    def test_adds_one(self):
        track = Track(title="Rolling Blackouts", artist="The Go! Team", file="file1.mp3")
        self.music_library.add(track)
        all_tracks = self.music_library.all()
        self.assertEqual(all_tracks[0].artist, track.artist)

    def test_adds_multiple(self):
        track1 = Track(title="Rolling Blackouts", artist="The Go! Team", file="file1.mp3")
        track2 = Track(title="Oh Yeah", artist="Locust", file="file2.mp3")
        track3 = Track(title="Sleep on the Wing", artist="Bibio", file="file3.mp3")
        self.music_library.add(track1)
        self.music_library.add(track2)
        self.music_library.add(track3)
        self.assertEqual(len(self.music_library.all()), 3)
        self.assertEqual(self.music_library.all()[2].artist, track3.artist)

    def test_removes_existing_song(self):
        track1 = Track(title="Rolling Blackouts", artist="The Go! Team", file="file1.mp3")
        track2 = Track(title="Oh Yeah", artist="Locust", file="file2.mp3")
        track3 = Track(title="Sleep on the Wing", artist="Bibio", file="file3.mp3")
        self.music_library.add(track1)
        self.music_library.add(track2)
        self.music_library.add(track3)
        self.assertTrue(self.music_library.remove(track2.id))
        self.assertEqual(len(self.music_library.all()), 2)
        self.assertEqual(self.music_library.all()[0].title, track1.title)
        self.assertEqual(self.music_library.all()[1].title, track3.title)

    def test_cant_remove_nonexistent_song(self):
        track1 = Track(title="Rolling Blackouts", artist="The Go! Team", file="file1.mp3")
        track2 = Track(title="Oh Yeah", artist="Locust", file="file2.mp3")
        track3 = Track(title="Sleep on the Wing", artist="Bibio", file="file3.mp3")
        self.music_library.add(track1)
        self.music_library.add(track2)
        self.music_library.add(track3)
        self.assertFalse(self.music_library.remove(20))
        self.assertFalse(self.music_library.remove(track3.id + 1))
        self.assertEqual(len(self.music_library.all()), 3)

    def test_search(self):
        track1 = Track(title="Dead Letters", artist="P.S. Eliot", file="dl.mp3")
        track2 = Track(title="Friend Is A Four Letter Word", artist="CAKE", file="friend.mp3")
        track3 = Track(title="Letters '98", artist="Havergal", file="98.mp3")
        self.music_library.add(track1)
        self.music_library.add(track2)
        self.music_library.add(track3)
        result = self.music_library.search(lambda track: "dead" in track.title.lower())
        self.assertEqual(result[0].title, track1.title)

    def test_tally(self):
        track1 = Track(title="Mixed Emotions", artist="Netsky", file="file2.mp3")
        track2 = Track(title="Where Do We Go", artist="Dimension", file="file1.mp3")
        track3 = Track(title="DJ Turn It Up", artist="Dimension", file="file3.mp3")
        self.music_library.add(track1)
        self.music_library.add(track2)
        self.music_library.add(track3)
        self.assertEqual(self.music_library.tally(), {'Dimension': 2, 'Netsky': 1})
