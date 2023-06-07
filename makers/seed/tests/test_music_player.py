import unittest

from player.music_player import MusicPlayer


class TestMusicPlayer(unittest.TestCase):
    def testCallsTerminal(self):
        mock_subprocess = MockSubprocess()
        music_player = MusicPlayer(mock_subprocess)
        music_player.play("data/tunes/file.mp3")
        self.assertEqual(mock_subprocess.args, ["afplay", "data/tunes/file.mp3"])


class MockSubprocess:
    def __init__(self):
        self.called = False
        self.args = None

    def call(self, args):
        self.called = True
        self.args = args