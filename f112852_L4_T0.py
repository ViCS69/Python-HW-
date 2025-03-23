import sys

d = {'a': 1, 'b': 2, 'c': 1, 'd': 3}


inverse_d = {}
for key, value in d.items():
    if value not in inverse_d:
        inverse_d[value] = []
    inverse_d[value].append(key)

if len(sys.argv) > 1:
    try:
        search_value = int(sys.argv[1])
    except ValueError:
        sys.exit(1)
else:
    try:
        search_value = int(input("Enter the value to search for: "))
    except ValueError:
        sys.exit(1)

if search_value in inverse_d:
    print(f"Keys with value {search_value}: {inverse_d[search_value]}")
else:
    print(f"No keys found with value {search_value}")
