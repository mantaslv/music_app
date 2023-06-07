import unittest

from player.music_library import MusicLibrary

class TestMusicLibrary(unittest.TestCase):
    def test_constructs(self):
        MusicLibrary()

    def test_returns_empty_all(self):
        music_library = MusicLibrary()
        self.assertEqual(music_library.all(), [])

    def test_adds_one(self):
        music_library = MusicLibrary()
        music_library.add("Rolling Blackouts by The Go! Team")
        self.assertEqual(music_library.all(), ["Rolling Blackouts by The Go! Team"])

    def test_adds_multiple(self):
        music_library = MusicLibrary()
        music_library.add("Rolling Blackouts by The Go! Team")
        music_library.add("Oh Yeah by Locust")
        music_library.add("Sleep on the Wing by Bibio")
        self.assertEqual(music_library.all(), ["Rolling Blackouts by The Go! Team", "Oh Yeah by Locust", "Sleep on the Wing by Bibio"])

    def test_removes_existing_song(self):
        music_library = MusicLibrary()
        music_library.add("Rolling Blackouts by The Go! Team")
        music_library.add("Oh Yeah by Locust")
        music_library.add("Sleep on the Wing by Bibio")
        self.assertEqual(music_library.remove(1), True)
        self.assertEqual(music_library.all(), ["Rolling Blackouts by The Go! Team", "Sleep on the Wing by Bibio"])

    def test_cant_remove_nonexistent_song(self):
        music_library = MusicLibrary()
        music_library.add("Rolling Blackouts by The Go! Team")
        music_library.add("Oh Yeah by Locust")
        music_library.add("Sleep on the Wing by Bibio")
        self.assertEqual(music_library.remove(20), False)
        self.assertEqual(music_library.remove(3), False)
        self.assertEqual(music_library.all(), ["Rolling Blackouts by The Go! Team", "Oh Yeah by Locust", "Sleep on the Wing by Bibio"])