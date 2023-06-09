import unittest
from ui.interface import Interface
from ui.mocks import PrintLine, InputLine, TestingConsoleIO, MockSubprocess
from unittest.mock import patch, MagicMock
from player.music_library import Track


class TestConsoleRunner(unittest.TestCase):
    OPTIONS = [
        PrintLine("Enter:"),
        PrintLine("  a: to add a track"),
        PrintLine("  p: to play a track"),
        PrintLine("  d: to delete a track"),
        PrintLine("  l: to list your tracks"),
        PrintLine("  s: to search your tracks"),
        PrintLine("  t: to summarise your top artists"),
        PrintLine("  q: to quit"),
    ]

    INTRO = [PrintLine("Welcome to your music library!"), *OPTIONS]

    SEARCH = [
        InputLine("What do you pick? ", "s"),
        PrintLine("Search by:"),
        PrintLine("  t: title"),
        PrintLine("  a: artist"),
        PrintLine("  f: file"),
        PrintLine("  *: anything"),
    ]

    QUIT = [*OPTIONS, InputLine("What do you pick? ", "q")]

    def test_adds_track_without_meta_data(self):
        with patch('player.music_library.MusicLibrary.add') as mock_add:
            with patch('player.music_library.MusicLibrary.all') as mock_all:
                mock_all.return_value = [Track("Odessa", "Caribou", "tunes/nometa.mp3")]

                testing_console_io = TestingConsoleIO(
                    *self.INTRO,
                    InputLine("What do you pick? ", "a"),
                    InputLine("What's the file? ", "tunes/nometa.mp3"),
                    PrintLine("No meta data found!"),
                    InputLine("What's the title? ", "Odessa"),
                    InputLine("What's the artist? ", "Caribou"),
                    PrintLine("Added successfully."),
                    *self.OPTIONS,
                    InputLine("What do you pick? ", "l"),
                    PrintLine("1. Odessa by Caribou @ tunes/nometa.mp3"),
                    *self.QUIT,
                )

                interface = Interface(testing_console_io, MockSubprocess())
                interface.run()
                mock_add.assert_called_once()
                self.assertTrue(testing_console_io.is_done())
    
    def test_adds_track_with_meta_data(self):
        with patch('player.music_library.MusicLibrary.add') as mock_add:
            testing_console_io = TestingConsoleIO(
                *self.INTRO,
                InputLine("What do you pick? ", "a"),
                InputLine("What's the file? ", "tunes/odessa.mp3"),
                PrintLine("Meta data found!"),
                PrintLine("Added successfully."),
                *self.QUIT,
            )
            
            interface = Interface(testing_console_io, MockSubprocess())
            interface.run()
            mock_add.assert_called_once()
            self.assertTrue(testing_console_io.is_done())

    def test_adds_track_with_meta_data_mocked(self):
        with patch('player.music_library.MusicLibrary.add') as mock_add:
            mocked_load = MagicMock()
            mocked_tag = MagicMock()
            mocked_tag.title = "Odessa"
            mocked_tag.artist = "Caribou"
            mocked_load.tag = mocked_tag

            testing_console_io = TestingConsoleIO(
                *self.INTRO,
                InputLine("What do you pick? ", "a"),
                InputLine("What's the file? ", "tunes/nometa.mp3"),
                PrintLine("Meta data found!"),
                PrintLine("Added successfully."),
                *self.QUIT,
            )

            with patch('ui.interface.eyed3.load', return_value=mocked_load):
                interface = Interface(testing_console_io, MockSubprocess())
                interface.run()

            track_args = mock_add.call_args[0][0]
            self.assertEqual(track_args.title, "Odessa")
            self.assertEqual(track_args.artist, "Caribou")
            self.assertEqual(track_args.file, "tunes/nometa.mp3")
            self.assertTrue(testing_console_io.is_done())

    def test_cannot_add_nonexistent_file(self):
        testing_console_io = TestingConsoleIO(
            *self.INTRO,
            InputLine("What do you pick? ", "a"),
            InputLine("What's the file? ", "file.mp3"),
            PrintLine("No file found!"),
            *self.QUIT,
        )
            
        interface = Interface(testing_console_io, MockSubprocess())
        interface.run()
        self.assertTrue(testing_console_io.is_done())

    def test_plays_tracks(self):
        with patch('player.music_library.MusicLibrary.all') as mock_all:
            mock_all.return_value = [
                Track("Major's Titling Victory", "The Cribs", "data/tunes/myfav.wav")
            ]

            testing_console_io = TestingConsoleIO(
                *self.INTRO,
                InputLine("What do you pick? ", "p"),
                PrintLine("1. Major's Titling Victory by The Cribs @ data/tunes/myfav.wav"),
                InputLine("Which do you want to play? ", "1"),
                PrintLine("Playing Major's Titling Victory by The Cribs..."),
                PrintLine("Done."),
                *self.QUIT,
            )
            mock_subprocess = MockSubprocess()
            interface = Interface(testing_console_io, mock_subprocess)
            interface.run()

            self.assertEqual(
                mock_subprocess.args,
                ["afplay", "data/tunes/myfav.wav"],
                "Subprocess wasn't called properly to play the file.",
            )
            self.assertTrue(testing_console_io.is_done())


    def test_searches_tracks(self):
        with patch('player.music_library.MusicLibrary.search') as mock_search:
            mock_search.side_effect = [
                [Track("Major's Titling Victory", "The Cribs", "file1.mp3")],  # First search by title
                [Track("The Milky Way over Ratlinghope", "Bibio", "file2.mp3")],  # Second search by artist
                [Track("Major's Titling Victory", "The Cribs", "file1.mp3"), Track("The Milky Way over Ratlinghope", "Bibio", "file2.mp3")],  # Third search by file
                [Track("Major's Titling Victory", "The Cribs", "file1.mp3"), Track("The Milky Way over Ratlinghope", "Bibio", "file2.mp3")],  # Fourth search by anything
                [],  # Fifth search by anything (no results)
            ]

            testing_console_io = TestingConsoleIO(
                *self.INTRO,
                *self.SEARCH,
                InputLine("What do you want to search by? ", "t"),
                InputLine("What do you want to search for? ", "vic"),
                PrintLine("1. Major's Titling Victory by The Cribs @ file1.mp3"),
                *self.OPTIONS,
                *self.SEARCH,
                InputLine("What do you want to search by? ", "a"),
                InputLine("What do you want to search for? ", "ibi"),
                PrintLine("1. The Milky Way over Ratlinghope by Bibio @ file2.mp3"),
                *self.OPTIONS,
                *self.SEARCH,
                InputLine("What do you want to search by? ", "f"),
                InputLine("What do you want to search for? ", "fi"),
                PrintLine("1. Major's Titling Victory by The Cribs @ file1.mp3"),
                PrintLine("2. The Milky Way over Ratlinghope by Bibio @ file2.mp3"),
                *self.OPTIONS,
                *self.SEARCH,
                InputLine("What do you want to search by? ", "*"),
                InputLine("What do you want to search for? ", "r"),
                PrintLine("1. Major's Titling Victory by The Cribs @ file1.mp3"),
                PrintLine("2. The Milky Way over Ratlinghope by Bibio @ file2.mp3"),
                *self.OPTIONS,
                *self.SEARCH,
                InputLine("What do you want to search by? ", "*"),
                InputLine("What do you want to search for? ", "xx"),
                *self.QUIT,
            )

            interface = Interface(testing_console_io, MockSubprocess())
            interface.run()
            self.assertTrue(testing_console_io.is_done())

            self.assertEqual(mock_search.call_count, 5)

    def test_deletes_tracks(self):
        with patch('player.music_library.MusicLibrary.all') as mock_all:
            with patch('player.music_library.MusicLibrary.remove') as mock_remove:
                tracks = [
                    Track("Major's Titling Victory", "The Cribs", "file1.mp3"),
                    Track("Be Safe (feat. Lee Ranaldo)", "The Cribs", "file2.mp3")
                ]
                updated_tracks = [
                    Track("Be Safe (feat. Lee Ranaldo)", "The Cribs", "file2.mp3")
                ]
                mock_all.side_effect = [tracks, updated_tracks, updated_tracks]  # First call returns all tracks, second call returns updated list
                mock_remove.side_effect = [True, False]  # First call deletes successfully, second call fails

                testing_console_io = TestingConsoleIO(
                    *self.INTRO,
                    InputLine("What do you pick? ", "d"),
                    PrintLine("1. Major's Titling Victory by The Cribs @ file1.mp3"),
                    PrintLine("2. Be Safe (feat. Lee Ranaldo) by The Cribs @ file2.mp3"),
                    InputLine("Which do you want to delete? ", "1"),
                    PrintLine("Deleted successfully."),
                    *self.OPTIONS,
                    InputLine("What do you pick? ", "d"),
                    PrintLine("1. Be Safe (feat. Lee Ranaldo) by The Cribs @ file2.mp3"),
                    InputLine("Which do you want to delete? ", "2"),
                    PrintLine("No such track."),
                    *self.OPTIONS,
                    InputLine("What do you pick? ", "l"),
                    PrintLine("1. Be Safe (feat. Lee Ranaldo) by The Cribs @ file2.mp3"),
                    *self.QUIT,
                )
                interface = Interface(testing_console_io, MockSubprocess())
                interface.run()
                self.assertTrue(testing_console_io.is_done())

                self.assertEqual(mock_remove.call_count, 2)

    def test_summarises_artists(self):
        with patch('player.music_library.MusicLibrary.tally') as mock_tally:
            mock_tally.return_value = {'Dimension': 2, 'Netsky': 1}

            testing_console_io = TestingConsoleIO(
                *self.INTRO,
                InputLine("What do you pick? ", "t"),
                PrintLine("1. Dimension: 2 tracks"),
                PrintLine("2. Netsky: 1 track"),
                *self.QUIT,
            )
            interface = Interface(testing_console_io, MockSubprocess())
            interface.run()
            self.assertTrue(testing_console_io.is_done())

            self.assertEqual(mock_tally.call_count, 1)

    def test_cycles_on_wrong_choice(self):
        testing_console_io = TestingConsoleIO(
            *self.INTRO,
            InputLine("What do you pick? ", "z"),
            PrintLine("No such command! Try again."),
            *self.QUIT,
        )
        interface = Interface(testing_console_io, MockSubprocess())
        interface.run()
        self.assertTrue(testing_console_io.is_done())
