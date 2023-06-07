my_list = ["Cat", "cat", "frog", "cat", "dog", "Dog"]
counters = {}

# Write some code to count the items in the list here

for item in my_list:
    if item.lower() not in counters:
        counters[item.lower()] = 1
    else:
        counters[item.lower()] += 1

print(counters)
# Should print (in any order)
# { 'cat': 3, 'dog': 2, 'frog': 1 }