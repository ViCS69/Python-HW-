import sys

d={1:'a',2:'b',3:'c',4:'a',5:'d',6:'e',7:'a',8:'b'}

search=sys.argv[1]
result=[]
for key in d:
   if d[key]==search:
       result.append(key)

print(result)