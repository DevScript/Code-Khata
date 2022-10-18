# Take input from
number=int(input("Enter Number for Multiplication Table:"))

# i is iterator that starts from 1 and ends at 10
for i in range(1,11):
    # f'' syntex in python is of formatted strings
    # you can add variables in these using { } notation
    print(f"{number} X {i} = {number*i}")

'''
Expected Output:
Enter Number for Multiplication Table: 3
3 X 1 = 3
3 X 2 = 6
3 X 3 = 9
3 X 4 = 12
3 X 5 = 15
3 X 6 = 18
3 X 7 = 21
3 X 8 = 24
3 X 9 = 27
3 X 10 = 30

'''
