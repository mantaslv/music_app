import time

seconds = int(time.time())

# Print "Fizz" if `seconds` is divisible by 3
# Print "Buzz" if `seconds` is divisible by 5
# Print "FizzBuzz" if `seconds` is divisible by 3 and 5
# Otherwise, print `seconds`

if (seconds % 3 == 0) & (seconds % 5 == 0):
    print("FizzBuzz")
elif seconds % 3 == 0:
    print("Fizz")
elif seconds % 5 == 0:
    print("Buzz")
else:
    print("seconds")