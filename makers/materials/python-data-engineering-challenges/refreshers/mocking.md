# Mocking

Let's take another look at the Secret Diary example:

```python
class SecretDiary:
    def __init__(self, diary):
        self._diary = diary
        # ^^^ Note that we've already injected our diary dependency here.
        # You'll need to do that in order to mock. If SecretDiary references the
        # Diary class directly, it's going to be pretty hard to isolate them.
        self._locked = True

    def unlock(self):
        self._locked = False

    def lock(self):
        self._locked = True

    def read(self):
        if self._locked:
            return "Go away!"
        else:
            return self._diary.read()


class Diary:
    def __init__(self, contents):
        self._contents = contents

    def read(self):
        return self._contents


diary = Diary("Eric Cantona is the best footballer")
secret_diary = SecretDiary(diary)

print(secret_diary.read())
# Prints: "Go away!"

secret_diary.unlock()
print(secret_diary.read())
# Prints: "Eric Cantona is the best footballer"

```

And put some tests together for `SecretDiary`:

```python
import unittest
from diary import SecretDiary, Diary


class TestSecretDiary(unittest.TestCase):
    def test_refuses_to_read_when_locked(self):
        diary = Diary("My Secret Information!")
        subject = SecretDiary(diary)
        self.assertEqual(subject.read(), "Go away!")

    def test_reads_when_unlocked(self):
        diary = Diary("My Secret Information!")
        subject = SecretDiary(diary)
        subject.unlock()
        self.assertEqual(subject.read(), "My Secret Information!")
```

This is OK — but what if Geoff comes in and breaks the `Diary` class? Then my
tests for `SecretDiary` will fail even though _I didn't do anything wrong._

We can fix this by mocking out `Diary` class, so that our tests for
`SecretDiary` aren't dependant on `Diary` at all.

Here's one way to do it:

```python
import unittest
from diary import SecretDiary


class TestSecretDiary(unittest.TestCase):
    def test_refuses_to_read_when_locked(self):
        mock_diary = MockDiary()  # We create a MockDiary instead of a Diary
        subject = SecretDiary(mock_diary)
        self.assertEqual(subject.read(), "Go away!")
        # And for good measure let's check our mock hasn't been called
        self.assertFalse(mock_diary.has_been_read)

    def test_reads_when_unlocked(self):
        mock_diary = MockDiary()
        subject = SecretDiary(mock_diary)
        subject.unlock()
        self.assertEqual(subject.read(), "Mocked diary contents")
        self.assertTrue(mock_diary.has_been_read)


# We create a mock class for Diary. It has the same methods, but it doesn't do
# anything except keep track of whether it has been called.
class MockDiary:
    def __init__(self):
        self.has_been_read = False

    def read(self):
        self.has_been_read = True
        return "Mocked diary contents"
```

We've now fully isolated `SecretDiary` from `Diary`. Geoff is powerless to
intervene. Try deleting the `Diary` class to prove it!

Here's another way, using the Python [`unittest.mock`
library](https://docs.python.org/3/library/unittest.mock.html):

```python
import unittest
from unittest.mock import Mock
from diary import SecretDiary


class TestSecretDiary(unittest.TestCase):
    def test_refuses_to_read_when_locked(self):
        mock_diary = Mock()
        subject = SecretDiary(mock_diary)
        self.assertEqual(subject.read(), "Go away!")
        mock_diary.read.assert_not_called()

    def test_reads_when_unlocked(self):
        mock_diary = Mock()
        mock_diary.read = Mock(return_value="Mocked diary contents")
        subject = SecretDiary(mock_diary)
        subject.unlock()
        self.assertEqual(subject.read(), "Mocked diary contents")
        mock_diary.read.assert_called()
```

They work in a similar way. Pick whichever approach feels better to you for now.

<!-- OMITTED -->

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-data-engineering-challenges&prefill_File=refreshers/mocking.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-data-engineering-challenges&prefill_File=refreshers/mocking.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-data-engineering-challenges&prefill_File=refreshers/mocking.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-data-engineering-challenges&prefill_File=refreshers/mocking.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-data-engineering-challenges&prefill_File=refreshers/mocking.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
