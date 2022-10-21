

a=3
b=6
c=4
d=[]
d.append(a)
d.append(b)
d.append(c)
for i in range(0,3):
    for j in range(0,3):
        for k in range (0,3):
            if i!=j and j!=k and k!=i:
                comb1=d[i]
                comb2=d[j]
                comb3=d[k]
                print(comb1,comb2,comb3)

