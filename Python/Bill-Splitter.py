# Bill Splitter for Restaurants
# Task is to divide the total bill amount in friends equally

# We take two inputs: bill amount, and number of friends
total = int(input("Enter Total Bill Amount:"))
friends = int(input("Enter number of Friends:"))

# Then we calculate how much each person pays
eachPays = total/friends

# we show it on screen
# round function rounds it the answer to given decimal places
# round ( 123.45679,2 ) will round number to 2 decimal places
print("Each person pays",round(eachPays, 2),'/- Rupees')

'''
Expected Output:

Enter Total Bill Amount:2000
Enter number of Friends:4
Each person pays 500.0 /- Rupees

Enter Total Bill Amount:8000
Enter number of Friends:2
Each person pays 4000.0 /- Rupees

'''
