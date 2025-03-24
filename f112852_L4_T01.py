import sys

text= sys.argv[1]
d={}

for char in text:
    if char in d:
        d[char]+=1
    else:
        d[char]=1

print(d)