import sys

text= sys.argv[1].lower()
d={}

for char in text:
    if char.isalpha():
        if char in d:
            d[char]+=1
        else:
            d[char]=1
result = list(d.items())
print(result)