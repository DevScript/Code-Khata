# Sometimes we get a long list of elements (maybe from excel) and we have to count them. Just add them in counterList.txt one on each line and run this. It will return a counter

with open('counterList.txt') as f:
    lines = f.readlines()

from collections import Counter 

d = Counter(lines)

d = sorted( ((v,k.strip()) for k,v in d.items()), reverse=True) 
for i,j in d:
    print(j,"-",i)
