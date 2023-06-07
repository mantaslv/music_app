class MusicLibrary:
    def __init__(self):
        self.songs = []
    
    def all(self):
        return self.songs
    
    def add(self, song):
        self.songs.append(song)
