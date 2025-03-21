import sys

# Define the original dictionary
d = {'a': 1, 'b': 2, 'c': 1, 'd': 3}

# Create the inverted dictionary: values become keys, and keys are collected in a list
inverse_d = {}
for key, value in d.items():
    if value not in inverse_d:
        inverse_d[value] = []
    inverse_d[value].append(key)

# Obtain the search value from command line arguments if provided,
# otherwise ask for user input.
if len(sys.argv) > 1:
    try:
        search_value = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid numeric value as input.")
        sys.exit(1)
else:
    try:
        search_value = int(input("Enter the value to search for: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        sys.exit(1)

# Print the keys that correspond to the searched value
if search_value in inverse_d:
    print(f"Keys with value {search_value}: {inverse_d[search_value]}")
else:
    print(f"No keys found with value {search_value}")
