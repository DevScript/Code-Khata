#write all basic numpy functions here

import numpy as np

#array
a = np.array([1,2,3,4,5])
print(a)

#array with zeros
b = np.zeros(5)
print(b)

#array with ones
c = np.ones(5)
print(c)

#array with random numbers
d = np.random.rand(5)
print(d)

#array with random numbers from normal distribution
e = np.random.randn(5)
print(e)

#array with random integers
f = np.random.randint(1,100,10)

#reshape
g = f.reshape(2,5)

#linspace
h = np.linspace(0,10,20)

#eye
i = np.eye(5)

#arange
j = np.arange(0,10,2)

#zeros_like
k = np.zeros_like(j)

#ones_like
l = np.ones_like(j)

#random.rand_like
m = np.random.rand_like(j)