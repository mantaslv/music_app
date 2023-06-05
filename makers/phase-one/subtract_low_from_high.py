import add_five


def subtract_low_from_high(a, b):
    if a > b:
        return a - b
    else:
        return b - a

print(subtract_low_from_high(2, 3))
# Should print "1"

print(subtract_low_from_high(3, 2))
# Should print "1"

print(add_five.add_five(subtract_low_from_high(1463, 16475)))
# Should print "15017"