from Polynomial_Regression import polyreg
def linear(xlist,ylist):
    return polyreg(1,xlist,ylist)

print(linear([1,2,3],[4,5,2]))