class MusicLibrary:
    def __init__(self):
        self.songs = []
    
    def all(self):
        return self.songs
    
    def add(self, song):
        self.songs.append(song)

    def remove(self, song_num):
        self.songs.pop(song_num)
        return True
