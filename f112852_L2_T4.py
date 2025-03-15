import sys

array = sys.argv[1:]

numbers = []
for num in array:
    numbers.append(int(num))

unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

unique_numbers.sort()

print(unique_numbers)
