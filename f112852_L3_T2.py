import sys

word=sys.argv[1]
key=sys.argv[2]
key_length=len(key)
result = ''
key_index = 0

for char in word:
    if char.isalpha():
        shift = ord(key[key_index % key_length]) - ord('a')
        base= ord('A') if char.isupper() else ord('a')
        shifted= (ord(char)+shift-base)%26 + base
        result+=chr(shifted)
        key_index+=1
    else:
        result+=char

print(result)