import unittest

from player.music_library import MusicLibrary, Track

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

    def test_adds_tracks(self):
        subject = MusicLibrary()
        subject.add(Track("Moksha", "Caspian", "file.mp3"))
        self.assertEqual(subject.all(), [Track("Moksha", "Caspian", "file.mp3")])

    def test_removes_tracks(self):
        subject = MusicLibrary()
        subject.add(Track("Moksha", "Caspian", "file.mp3"))
        subject.add(Track("Without You", "Dawn Landes", "file.mp3"))
        subject.add(Track("Dry Lips", "Lightspeed Champion", "file.mp3"))
        signal = subject.remove(1)
        self.assertTrue(signal)
        self.assertEqual(
            subject.all(),
            [
                Track("Moksha", "Caspian", "file.mp3"),
                Track("Dry Lips", "Lightspeed Champion", "file.mp3"),
            ],
        )

    def test_lists_tracks(self):
        subject = MusicLibrary()
        subject.add(Track("Moksha", "Caspian", "file.mp3"))
        subject.add(Track("Dry Lips", "Lightspeed Champion", "file.mp3"))
        self.assertEqual(
            subject.all(),
            [
                Track("Moksha", "Caspian", "file.mp3"),
                Track("Dry Lips", "Lightspeed Champion", "file.mp3"),
            ],
        )

    def test_search(self):
        lib = MusicLibrary()
        lib.add(Track("Dead Letters", "P.S. Eliot", "dl.mp3"))
        lib.add(Track("Friend Is A Four Letter Word", "CAKE", "friend.mp3"))
        lib.add(Track("Letters '98", "Havergal", "98.mp3"))
        result = lib.search(lambda track: "dead" in track.title.lower())
        self.assertEqual(list(result), [Track(title='Dead Letters', artist='P.S. Eliot', file='dl.mp3')])

    def test_tally(self):
        lib = MusicLibrary()
        lib.add(Track("Mixed Emotions", "Netsky", "file2.mp3"))
        lib.add(Track("Where Do We Go", "Dimension", "file1.mp3"))
        lib.add(Track("DJ Turn It Up", "Dimension", "file3.mp3"))
        self.assertEqual(lib.tally(), {'Dimension': 2, 'Netsky': 1})