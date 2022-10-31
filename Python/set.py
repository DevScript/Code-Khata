#sets is unordered and unindexed 
# we use set or {elmt1,elemt2,..} to create sets
#you don't create a set by using empty {} because it would create a dictionary
s=set() 
s1={1,1,2,3,5,6,7}
#to add an element in a set we use add 
print("set before adding an element : ") 
print(s1)
print("set after adding an element :" )
s1.add(4)
print(s1)
#to determine the number of items in a set you use len 
print(len(s1))
#to delete an item from a set you use remove or discard
s1.remove(5)
s1.discard(7)
print("after removing the iteams")
print(s1)
#to join two sets you use union
s2=('ruby','python','c++')
s3=s1.union(s2)
print("the new set obtained after joining")
print(s3)
