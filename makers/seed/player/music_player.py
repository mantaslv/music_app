class MusicPlayer:
    def __init__(self, subprocess):
        self.subprocess = subprocess

    def play(self, file_path):
        self.subprocess.call(["afplay", file_path])