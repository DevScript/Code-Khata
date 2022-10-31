#to insert an element in a list , in a specified index we use insert that takes as arguments the index 
# where the element will be added and then the element to add there 
L=[1,2,4,5]
print("the list before inserting the element: ")
print(L)
L.insert(2,3)
print("the list after inserting the element 3 in position 2 : ")
print(L)
#the index can also be negative 
L.insert(-1 , 6)
print("the list after inserting the element 6 in index -1 ")
print(L)
