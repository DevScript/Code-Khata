def suma(slist): #  SUMMATORY
    sum = 0
    for x in slist: 
        if (type(x) == int or type(x) == float): 
            sum += x
        else:
            raise ValueError("Item in average list wasn't a number")
    return sum
