import random
#CREATING_RANDOM_LIST
random_list=[]
for i in range(100):
    random_list.append(random.randint(1,100))
print(random_list)
#Output :
#[96, 32, 32, 10, 97, 45, 54, 41, 34, 99, 41, 97, 79, 72, 83, 8, 1, 91, 86, 83, 7, 99, 23, 59, 83, 70, 22, 58, 30, 46, 25, 45, 93, 46, 57, 19, 81, 77, 41, 11, 80, 87, 14, 42, 21, 28, 54, 27, 47, 33, 8, 73, 74, 15, 75, 73, 28, 57, 69, 33, 53, 40, 31, 18, 49, 64, 38, 74, 20, 48, 61, 37, 54, 97, 1, 62, 29, 18, 14, 84, 83, 73, 98, 84, 58, 65, 8, 74, 72, 43, 20, 50, 14, 34, 27, 50, 87, 21, 29, 52]

#MINIMUM_NUMBER
minimum_no=[]
minimum_no.append(min(random_list))
print("Minimum value in the list is : " , minimum_no)
#Output :
#Minimum value in the list is :  [1]

#MAXIMUM_NUMBER
maximum_no=[]
maximum_no.append(max(random_list))
print("Maximum value in the list is : " , maximum_no)
#Output :
#Maximum value in the list is :  [99]
    
#INDEX OF MIN VALUE
print("Index of minimum value in list is : " , random_list.index(min(random_list)))
#Output :
#Index of minimum value in list is :  16

#INDEX OF MAX VALUE
print("Index of maximum value in list is : " , random_list.index(max(random_list)))
#Output :
#Index of maximum value in list is :  9

#MEAN_OF_VALUES
mean_of_randomlist=sum(random_list)/len(random_list)
print("Mean of values of list : " , mean_of_randomlist)
#Output :
#Mean of values of list :  50.45
