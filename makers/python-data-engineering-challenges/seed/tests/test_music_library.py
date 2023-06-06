import unittest

from player.music_library import MusicLibrary

class TestMusicLibrary(unittest.TestCase):
    def test_constructs(self):
        MusicLibrary()

    def test_returns_empty_all(self):
        music_library = MusicLibrary()
        self.assertEqual(music_library.all(), [])