import sys

word=sys.argv[1]
key=3
result = ''
for char in word:
    if char.isalpha():
        if char.isupper():
            base= ord('A')
        else:
            base= ord('a')

        shifted=(ord(char)-base+key)%26+base
        result+=chr(shifted)

print(result)