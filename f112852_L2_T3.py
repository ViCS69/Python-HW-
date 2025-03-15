import sys

array = list(map(int, sys.argv[1:]))
array.sort()

isRepeating=False
for i in range(len(array)-1):
    if array[i]==array[i+1]:
        isRepeating=True

print(isRepeating)
