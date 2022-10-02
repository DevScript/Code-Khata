from Mean import mean
from Summatory import suma

def var(nlist): # VARIATION 
    av = mean(nlist)
    return suma([(x - mean(nlist)) ** 2 for x in nlist]) / len(nlist)
