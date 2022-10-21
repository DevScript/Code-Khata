#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Write a short Python function, is multiple(n, m), 
#that takes two integer values and returns True if n is a multiple of m, 
#that is,n=mi for some integer i, and False otherwise

def multiple(n,m):
    if n%m==0:
        return True
    else:
        return False
n=int(input("Enter value of n : "))
m=int(input("Enter value of m : "))
multiple(n,m)


# In[2]:


#Write a short Python function, is even(k), 
#that takes an integer value and returns True if k is even, and False otherwise. 
#However, your function cannot use the multiplication, modulo, or division operators
def isEven(n):
    return n&1
n=100
if isEven(n)==0:
    print('Even')
else:
    print('Odd')


# In[ ]:


#Create a function EvenList that takes a parameter n to input n number from users and 
#returns the list of only even numbers.
def Evenlist(n):
    user=int(input("Enter n numbers where you want to print the even numbers"))
    for i in range(0,user+1):
        if i%2==0:
            print(i,end=' ')
a=int(input('Enter a number'))        
Evenlist(a)
            


# In[ ]:


#4.Write a short Python function, minmax(data), that takes a sequence of one or more numbers, 
#and returns the smallest and largest numbers, in the form of a tuple of length two. 
#Do not use the built-in functions min or max in implementing your solution.
def minimax(data):
    for i in range(0,n+1):
        if i>10:
            print(i,'Is the smallest number')
            break
    print(n,'Is the largest number')
n=int(input("Enter any number"))
minimax(n)


# In[6]:


#Write a short Python function that takes a positive integer n
#and returns the sum of the squares of all the positive integers smaller than n.
def sumofsqr(n):
    for i in range(0,n+1):
        x=i*i
        if x==n:
            break
        print(x)
n=int(input("Enter a number"))
sumofsqr(n)


# In[12]:


#Write a short Python function that takes a positive integer n 
#and returns the sum of the squares of all the odd positive integers smaller than n.
def sumofsqrodd(n):
    for i in range(0,n+1):
        x=i*i
        if x==n:
            break
        for y in range(1,x+1):
            if y%3==0:
                print(y)
n=int(input("Enter a number"))
sumofsqrodd(n)





# In[ ]:




