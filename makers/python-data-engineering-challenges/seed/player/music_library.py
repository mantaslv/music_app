from dataclasses import dataclass

class MusicLibrary:
    def __init__(self):
        self._tracks = []
    
    def all(self):
        return self._tracks
    
    def add(self, song):
        self._tracks.append(song)

    def remove(self, song_num):
        if song_num > len(self._tracks) - 1:
            return False
        else:
            self._tracks.pop(song_num)
            return True
        
    def search(self, condition):
        return [track for track in self._tracks if condition(track)]
        
        
@dataclass
class Track:
    title: str
    artist: str
    file: str

    def __str__(self):
        return f"{self.title} by {self.artist}"