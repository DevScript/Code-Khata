# Sum of digits of a number

num = input("Enter a number containing more than one digit: ")
num=num.strip()
total=0
i=0
while i<=len(num)-1:
    total+=int(num[i])
    i+=1
print(f"Sum of digits of a number is {total}")
