# Step 4: Play Some Tunes

Nothing like a few tunes to soundtrack your coding session right? Let's get
playing. But we can't have our tests playing music — that would cause a huge
racket around the office. So we'll need to learn how to use mocking to isolate
our tests from their dependencies.

## Objectives

Learn to:
* Read and implement a fully-tested class from another developer using [mocks](./refreshers/mocking.ed.md)

## Playing

There's a shell command on Macs called `afplay`. We'll use that to play our
sound files.

In [`interfaces/step_04`](./interfaces/step_04) you'll find a new `data` 
directory to paste into your project. Once it's there, run this in the terminal:

```shell
; afplay data/tunes/myfav.wav
```

You should hear a lovely tone.

To do the same in a Python project, you'll need to do something like:

```python
import subprocess

subprocess.call(["afplay", "data/tunes/myfav.wav"])
```

## Exercise

Kez has developed yet another version of the interface for you in
[`interfaces/step_04`](./interfaces/step_04). Copy it into your project.

Professor Snape has test-driven a `MusicPlayer` class that should belong in a
new package at `player/music_player.py`. What this class does is pretty much
self-explanatory after reading the above on playing tones.

**Tests**

```python
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
```

**Class**

```python
class MusicPlayer:
    def __init__(self, subprocess):
        self.subprocess = subprocess

    def play(self, file_path):
        self.subprocess.call(["afplay", file_path])
```

It should behave now like this:

```python
>>> import subprocess
>>> player = MusicPlayer(subprocess) 
    #                    ^^^^^^^^^^
    # We'll need to pass in (inject) `subprocess`
    # in order to isolate our tests.
>>> player.play("/Users/kay/Code/player/data/tunes/myfav.wav")
    # A pause while it plays the file.
>>>
```

Once you've done this, you can run the UI:

```shell
; python -m ui
Welcome to your music library!
Enter:
  a: to add a track
  p: to play a track
  d: to delete a track
  l: to list your tracks
  q: to quit
What do you pick? a
What's the title? Fav
What's the artist? Artist
What's the file? data/tunes/myfav.wav
Added successfully.
Enter:
  a: to add a track
  p: to play a track
  d: to delete a track
  l: to list your tracks
  q: to quit
What do you pick? p
1. Fav by Artist @ data/tunes/myfav.wav
Which do you want to play? 1
Playing Fav by Artist...
Done.
```

And the UI tests to verify everything is working:

```shell
; python -m unittest discover ui
....
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```

## Done?

[Go to the next challenge](./step_05.md)


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-data-engineering-challenges&prefill_File=step_04.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-data-engineering-challenges&prefill_File=step_04.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-data-engineering-challenges&prefill_File=step_04.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-data-engineering-challenges&prefill_File=step_04.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-data-engineering-challenges&prefill_File=step_04.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
