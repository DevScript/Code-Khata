# Convert List of lists to Set

a= [[1,2,3,4],["a", "a", "b", "e"],["Sam", "John"]]
res = list(map(set,a))
print(*res, sep=" ")
