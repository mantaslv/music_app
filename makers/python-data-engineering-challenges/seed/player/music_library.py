from dataclasses import dataclass

class MusicLibrary:
    def __init__(self):
        self.songs = []
    
    def all(self):
        return self.songs
    
    def add(self, song):
        self.songs.append(song)

    def remove(self, song_num):
        if song_num > len(self.songs) - 1:
            return False
        else:
            self.songs.pop(song_num)
            return True
        
@dataclass
class Track:
    title: str
    artist: str
    file: str

    def __str__(self):
        return f"{self.title} by {self.artist}"