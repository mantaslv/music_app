# Step 6: Make it Yours

The application is now yours to develop as you see fit. Here are some pathways
you might choose depending on what you want to learn, how much challenge you
want to take on, and how much structure or freedom you would like. Tackle them
in any order you like — you almost certainly won't complete them all.

* **[Add summary statistics about which artists are in the
  library.](#add-summary-statistics-about-which-artists-are-in-the-library)**  
  To learn about working with Python dictionaries (known in other languages as
  maps, hashes, or associative arrays).

* **[Store the music library.](#store-the-music-library)**  
  To Learn about file and/or database access using Python.

* **[Automatically detect track information just by giving the file
  path.](#automatically-detect-track-information-just-by-giving-the-file-path)**  
  To learn about installing packages in Python and develop your mocking skills.

## Add summary statistics about which artists are in the library

Looking forward to [Spotify Wrapped](http://spotify.com/wrapped/) this year? I
am. We're probably not going to make anything _that_ sophisticated, but it'd be
nice to see a breakdown of the artists in our library. Something like this:

```shell
; python -m ui
Welcome to your music library!
# You add some tracks
Enter:
  a: to add a track
  p: to play a track
  d: to delete a track
  l: to list your tracks
  s: to search your tracks
  S: to summarise your top 15 artists
  q: to quit
What do you pick? S
1. Piano Magic: 217 tracks
2. Bright Eyes: 181 tracks
3. Radiohead: 174 tracks
4. Bibio: 154 tracks
5. Casiotone for the Painfully Alone: 129 tracks
6. Broadcast: 126 tracks
7. The Avalanches: 102 tracks
8. Boards of Canada: 101 tracks
9. Misophone: 100 tracks
10. U4ia: 96 tracks
11. The Books: 95 tracks
12. Vegyn: 93 tracks
13. Islands: 92 tracks
14. Aphex Twin: 92 tracks
15. cLOUDDEAD: 89 tracks
```

Think a bit about how to achieve that. You'll probably need to learn about
[Python
dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
and perhaps [Python
tuples](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences). Consider
carefully how you want to build this into the system — what would a good Object
Oriented developer do?

<details>
<summary>How this task is relevant to Data Engineering</summary>
Building systems that count stuff and summarise a dataset - This is the bread and butter of Data Engineers. You're essentially building a mini terminal-based dashboard.

But Data Engineers don't just care about the final output. They also care that the systems they build are well written: easy to read, easy to change and easy to test.
</details>

## Store the music library

<!-- OMITTED -->

Putting in all the tracks every single time is going to annoy the users, and is
probably already annoying you. Is there a way you can store the music library
and load it in when the application is run?

To implement this you'll need to decide how to store data. Here are two
possibilities:

1. Store them in a list in a file.
2. Store them in an SQL database.

What do you think the pros and cons are? Which path will provide more useful
learning to you? Decide on this basis.

<details>
<summary>How this task is relevant to Data Engineering</summary>
Being able to interact with data stored in files and databases is a fundamental skill of data engineering.

It may help your decision to consider which of these two skills you either feel least comfortable with or have the least experience with across all of the languages you have worked in so far. Pick the approach that will allow you to practice this skill.
</details>

## Automatically detect track information just by giving the file path

Most music files contain metadata. That metadata contains information
identifying the artist, track title, year of release and so on.

It would be pretty great to use that metadata if it is present, instead of
forcing our users to type it in manually.

To do this, you'll need to:

* Take a breeze through [this archive of free
  music](https://freemusicarchive.org/) until you find something you like the
  sound of. Download it, and use it as your test file.
* Install the [`eyed3`](https://github.com/nicfit/eyeD3) module using
  [`pipenv`](https://pipenv-fork.readthedocs.io/en/latest/basics.html)
* Try it out with your test file using the docs available for `eyed3`.
* Test-drive integrating it into your app. 
* Apply your mocking skills to isolate your unit tests from `eyed3`.
* Take not that not all tracks will have metadata, so you may want to give the
  user the option of not using it.

<details>
<summary>How this task is relevant to Data Engineering</summary>
To help them manipulate and analyse data, Data Engineers will often reach for external libraries to help them.
Python in particular has a large universe of data processing and analysis libraries. 

In this task, you're learning how to manage dependencies (libraries) in Python and how to work with an external library to analyse a piece of data (the music file).
</details>

## Done?

Much like Ruby, Python has a nuanced and deliberate design philosophy which it
has brought to our industry. This is summed up in a secret feature included with
the Python interpreter. You can access it by running:

```shell
; python
>>> import this
```

I hope you've enjoyed it — Pyth-on!


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-data-engineering-challenges&prefill_File=step_06.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-data-engineering-challenges&prefill_File=step_06.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-data-engineering-challenges&prefill_File=step_06.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-data-engineering-challenges&prefill_File=step_06.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-data-engineering-challenges&prefill_File=step_06.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
