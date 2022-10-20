      #Q4
def minmax(data):
    data.sort()
    print(data)
    mi=data[0]
    ma=data[4]
    t=tuple((mi,ma))
    print(t)
#
data=[]
for i in range(1,5+1):
    i=int(input('enter numbers?'))
    data.append(i)
minmax(data)    
