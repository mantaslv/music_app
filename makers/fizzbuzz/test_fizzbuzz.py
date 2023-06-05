# For: test_fizzbuzz.py
import unittest  # This is the default Python testing library, unittest

from fizzbuzz import generate
# We import our generate function (def) from the fizzbuzz module (file)

class TestFizzbuzz(unittest.TestCase):  # Sets up a new test case
    def test_lists_values_up_to_one(self):  # This is a test, don't forget `self`!
        self.assertEqual(generate(1), "1")  # And an assertion

    def test_lists_values_up_to_two(self):
        self.assertEqual(generate(2), "1, 2")

    def test_lists_values_up_to_three(self):
        self.assertEqual(generate(3), "1, 2, Fizz")

    def test_lists_values_up_to_four(self):
        self.assertEqual(generate(4), "1, 2, Fizz, 4")

    def test_lists_values_up_to_five(self):
        self.assertEqual(generate(5), "1, 2, Fizz, 4, Buzz")
    
    def test_lists_values_up_to_fifteen(self):
        self.assertEqual(generate(15), "1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz")

    def test_lists_values_up_to_one_hundred(self):
        self.assertEqual(generate(100), "1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16, 17, Fizz, 19, Buzz, Fizz, 22, 23, Fizz, Buzz, 26, Fizz, 28, 29, FizzBuzz, 31, 32, Fizz, 34, Buzz, Fizz, 37, 38, Fizz, Buzz, 41, Fizz, 43, 44, FizzBuzz, 46, 47, Fizz, 49, Buzz, Fizz, 52, 53, Fizz, Buzz, 56, Fizz, 58, 59, FizzBuzz, 61, 62, Fizz, 64, Buzz, Fizz, 67, 68, Fizz, Buzz, 71, Fizz, 73, 74, FizzBuzz, 76, 77, Fizz, 79, Buzz, Fizz, 82, 83, Fizz, Buzz, 86, Fizz, 88, 89, FizzBuzz, 91, 92, Fizz, 94, Buzz, Fizz, 97, 98, Fizz, Buzz")

    # Start by uncommenting the above, and when you've made that pass move 
    # forward with your own tests.
