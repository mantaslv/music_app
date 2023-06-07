# Step 3: Add a Track Class

Back-end complete! But adding simple strings isn't going to cut it. We want to
link these tracks to music files. Let's see how we could use another class to
implement this.

## Objectives

Learn to:
* Read and implement a fully-tested class from another developer

## Exercise

Kez has implemented a new interface to account for adding the filenames. Copy it
into your project from [interfaces/step_03](./interfaces/step_03).

To support it, Professor Snape, who is collaborating with us, has developed a
new class called `Track`. It takes: the track's title, artist, and file. It
assigns them to public fields, so that you can do this:

```python
>>> track = Track("The Boys of Summer", "DJ Sammy", "summer.mp3")
>>> track.title
"The Boys of Summer"
>>> track.artist
"DJ Sammy"
>>> track.file
"summer.mp3"
```

Snape had the option do this with a normal class. _Or_ being super fancy and
using Python Data Classes. The latest was his approach.

### Organising your classes

We spoke about Python files being modules before. Unlike other languages, it is
very common in Python to have more than one class per file. Python tends to
prefer flat directory structures without lots of folders in folders. 

Let's keep to that here and implement the `Track` class below within
`player/music_library.py`.

```python
@dataclass
class Track:
    title: str
    artist: str
    file: str

    def __str__(self):
        return f"{self.title} by {self.artist}"
```

### What about `MusicLibrary`? Do I need to change it to use `Track`?

No! Take a look at `ui/interface.py` if you want to know why.

It's a great feature of software design if you can add functionality without
changing current classes, merely adding new ones. This is called the Open/Closed
principle and it contributes the 'O' to the SOLID principles.

### What about the tests for `MusicLibrary`?

Yes, that's a good idea — and we have also been given the tests that use
instances of `Track` rather than strings.

```python
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
```

## Done?

[Go to the next challenge](./step_04.md)


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-data-engineering-challenges&prefill_File=step_03.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-data-engineering-challenges&prefill_File=step_03.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-data-engineering-challenges&prefill_File=step_03.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-data-engineering-challenges&prefill_File=step_03.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-data-engineering-challenges&prefill_File=step_03.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
