from Mean import mean
def median(list):
    for x in list:
        if (type(x) != int and type(x) != float): 
            raise ValueError("Item in average list wasn't a number")
    sort = sorted(list)
    leng = len(sort)
    if leng%2 == 0:
        return mean(sort[int(leng/2)-1:int(leng/2)+1])
    else:
        return sort[int(leng/2)]



