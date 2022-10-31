#a list collects elements (could be of different types) that are ordered and can be changed 

#to define a list use [ ] or list
L=[]
L=list()

#you can fill a list with elements 
L=['python' , 'programming' , 3 , 'A']

#an element of a list could be of type integer , float , char , string or a lit 
L1=['first elmt' , [1,2,3]]

#to access elements in lists use their index and don't forget the first element has 0 as an index ! 
print("this is the first element : " ,L1[0])

#to print a list we can either just call it by its name or use a for loop 
print('first printing method : ')
print(L1) 
print('second printing method : ')
for i in L1 :
    print(i)

