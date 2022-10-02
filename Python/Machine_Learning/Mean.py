from Summatory import suma
def mean(nlist): # Mean
    if type(nlist) != list:
        raise ValueError('mean argument must be a list')
    return suma(nlist) / len(nlist)
