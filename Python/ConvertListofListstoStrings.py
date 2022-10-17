# Convert List of lists to Strings

a= [["M", "y"],["C", "o", "d", "e"]]
res = list(map(''.join, a))
print(*res, sep=" ")
