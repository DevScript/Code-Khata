rows=int(input("enter"))
for i in range(0,rows):
    for j in range(0,i+1):
        print("*",end="")
    print("\r")
for i in range(0,rows):
    for j in range(rows-i):
        print("*",end="")
    print("\r")
