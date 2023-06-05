# For: fizzbuzz.py
def generate(upto):
    my_list = []
    for num in range(1, upto + 1):
        if num % 5 == 0:
            my_list.append("Buzz")
        elif num % 3 == 0:
            my_list.append("Fizz")
        else:
            my_list.append(str(num))

    result = ", ".join(my_list)

    return result