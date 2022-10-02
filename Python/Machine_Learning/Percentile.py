def perc(p,nlist): # PERCENTILE
    nlist = sorted(nlist)
    
    if type(nlist) != list:
        raise ValueError('Average argument must be a list')
    if (type(p) != int and type(p) != float) or p > 100 or p < 0:
        raise ValueError('Invalid Percentage')
    for x in nlist: 
        if type(x) != int and type(x) != float:
            raise ValueError("Item in average list wasn't a number") 

    rank = (p/100) * (len(nlist)-1)
    if rank%1 == 0:
        return nlist[int(rank)]
    else:
        inp = rank - int(rank)
        return nlist[int(rank)] + round((inp*(nlist[int(rank)+1]-nlist[int(rank)])),14)
