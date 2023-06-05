a = 1
b = 5

for num in range(a, b + 1):
    print(num)

sum = 0

for num in range(a, b + 1):
    if num % 2 == 0:
        sum += num

print(sum)