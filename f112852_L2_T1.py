import sys

if len(sys.argv) < 2:
    print("Моля, въведете списък от числа като аргументи.")
    sys.exit(1)

arr1 = sys.argv[1:]

isSorted=True

for i in range(len(arr1) - 1):
    if arr1[i]>arr1[i+1]:
        isSorted=False
        break

if isSorted:
    print("sorted")
else:
    print("unsorted")
