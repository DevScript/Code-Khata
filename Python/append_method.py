#to add an element at the end of the list use the method append 
#append only adds one element at a time
L1=[1,2,3,4,5]
print("list before append : ")
print(L1)
L1.append(6)
print("list after append : ")
print(L1)
#filling a list by n strings for the example we will take n=2
L=list()
for i in range(2):
    x = input("give L[{}]:".format(i))
    L.append(x)
print(L)
