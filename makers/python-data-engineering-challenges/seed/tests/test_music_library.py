import unittest

from player.music_library import MusicLibrary

class TestMusicLibrary(unittest.TestCase):
    def test_constructs(self):
        MusicLibrary()

    def test_returns_empty_all(self):
        music_library = MusicLibrary()
        self.assertEqual(music_library.all(), [])

    def test_returns_one(self):
        music_library = MusicLibrary()
        music_library.add("Rolling Blackouts by The Go! Team")
        self.assertEqual(music_library.all(), ["Rolling Blackouts by The Go! Team"])