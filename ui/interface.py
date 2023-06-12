from player.music_library import MusicLibrary, Track
from player.music_player import MusicPlayer
import eyed3
import os.path


class Interface:
    def __init__(self, console, subprocess):
        self.console = console
        self.music_library = MusicLibrary()
        self.music_player = MusicPlayer(subprocess)

    def run(self):
        self.console.print("Welcome to your music library!")
        while True:
            choice = self._prompt()
            if choice == "a":
                self._add_track()
            elif choice == "p":
                self._play_track()
            elif choice == "d":
                self._remove_track()
            elif choice == "l":
                self._list_tracks(self.music_library.all())
            elif choice == "s":
                self._search_tracks()
            elif choice == "t":
                self._summarise(self.music_library.tally())
            elif choice == "q":
                return
            else:
                self.console.print("No such command! Try again.")
                
    def _summarise(self, tally):
        sorted_tally = dict(sorted(tally.items(), key=lambda x:x[1], reverse=True))

        for position, (artist, freq) in enumerate(sorted_tally.items(), start=1):
            plural_suffix = 's' if freq > 1 else ''
            summary = f"{position}. {artist}: {freq} track{plural_suffix}"
            self.console.print(summary)

    def _prompt(self):
        self.console.print("Enter:")
        self.console.print("  a: to add a track")
        self.console.print("  p: to play a track")
        self.console.print("  d: to delete a track")
        self.console.print("  l: to list your tracks")
        self.console.print("  s: to search your tracks")
        self.console.print("  t: to summarise your top artists")
        self.console.print("  q: to quit")
        return self.console.input("What do you pick? ")

    def _add_track(self):
        file = self.console.input("What's the file? ")

        if (os.path.isfile(file)):
            if eyed3.load(file).tag != None:
                self.console.print("Meta data found!")
                audiofile = eyed3.load(file)
                title = audiofile.tag.title
                artist = audiofile.tag.artist
            else:
                self.console.print("No meta data found!")
                title = self.console.input("What's the title? ")
                artist = self.console.input("What's the artist? ")

            self.music_library.add(Track(title, artist, file))
            self.console.print("Added successfully.")
        else:
            self.console.print("No file found!")

    def _list_tracks(self, tracks):
        for idx, track in enumerate(tracks):
            self.console.print(
                f"{idx + 1}. {track.title} by {track.artist} @ {track.file}"
            )

    def _search_tracks(self):
        self.console.print("Search by:")
        self.console.print("  t: title")
        self.console.print("  a: artist")
        self.console.print("  f: file")
        self.console.print("  *: anything")
        choice = self.console.input("What do you want to search by? ")
        search = self.console.input("What do you want to search for? ").lower()
        if choice == "t":
            found = self.music_library.search(
                lambda track: search in track.title.lower()
            )
            self._list_tracks(found)
        elif choice == "a":
            found = self.music_library.search(
                lambda track: search in track.artist.lower()
            )
            self._list_tracks(found)
        elif choice == "f":
            found = self.music_library.search(
                lambda track: search in track.file.lower()
            )
            self._list_tracks(found)
        elif choice == "*":
            found = self.music_library.search(
                lambda track: (search in track.title.lower())
                or (search in track.artist.lower())
                or (search in track.file.lower())
            )
            self._list_tracks(found)
        else:
            self.console.print("No such field!")

    def _play_track(self):
        self._list_tracks(self.music_library.all())
        track_id = int(self.console.input("Which do you want to play? ")) - 1
        tracks = self.music_library.all()
        if track_id >= 0 and track_id < len(tracks):
            track = tracks[track_id]
            self.console.print(f"Playing {track.title} by {track.artist}...")
            self.music_player.play(track.file)
            self.console.print("Done.")
        else:
            self.console.print("No such track.")

    def _remove_track(self):
        self._list_tracks(self.music_library.all())
        track_id = int(self.console.input("Which do you want to delete? ")) - 1
        if self.music_library.remove(track_id):
            self.console.print("Deleted successfully.")
        else:
            self.console.print("No such track.")


class ConsoleIO:
    def print(self, message):
        print(message)

    def input(self, prompt=None):
        if prompt is None:
            return input()
        return input(prompt)
