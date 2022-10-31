print("Welcome to the Oregon Trial")
print("You set off with your family West")
print("You hear a Scream")
print("You have a Choice")
print("a. grab ur gun ")
print("b. run for your life")
user_input=input()
if user_input == "a":
    print("You shoot the bear and survive")
elif user_input == "b":
	print("you run away,but the bear eats your stuff and you die anyway!")
else:
    print("You fail to do anything and die") 

print("A mystic meets you on the roads and says he's thinking of two numbers between 1 and 10.You must guess a number between his number or you will die")
user_input=input()
if int(user_input) < 8 and int(user_input) > 4 :
	print("You guessed Right and Survived")
else:
	print("You guessed wrong and died ")

alive="alive"
history= []
while alive =="alive":
	print("challenge")
	user_input=input()
	if user_input == "1":
		alive="dead"
	history.append(user_input)	
print(history)

def challenge_1():
   print("You hear a Scream")
   print("A bear attacks you the little tummy")
   print("Yoy have a choice ")
   print("a. grab ur gun ")
   print("b. run for your life")

   user_input=input()
   if user_input == "a":
        print("You shoot the bear and survive")
        return "alive"
   elif user_input == "b":
    	print("you run away,but the bear eats your stuff and you die anyway!")
    	return "dead"
   else:
    	print("You fail to do anything and die") 
       
#print(challenge_1())
def challenge_2():
	print("A mystic meets you on the roads and says he's thinking of two numbers between 1 and 10.You must guess a number between his number or you will die")
	print("Guess a number from 1-10")
	user_input=int(input())
	if user_input > 5 and user_input < 7:
		print("Wow you somehow survive")
		return "alive"
	else:
		print("You were Wrong")
		return "dead"
#print(challenge_2())
def challenge_3():
	print("You have a cross a land known for snakes")
	print("Pick a number between 10 and 15.if u pick the unlucky number you will die ")
	user_input=int(input())
	if user_input < 10 or user_input > 15:
		print("You couldn't Follow the rules and die")
		return "dead"
	else:
	    if user_input !=13:
	    	print("the snake does not attack you")
	    	return "alive"
	    else:
	    	print("you know that was an unlucky number byt you picked it anyway and you die")
	    	return "dead"
challenge_1()
challenge_2()
challenge_3()
challenge_1()

import random 
alive="alive"
while alive == "alive":
	challenge_number=random.randint(1,3)
	if challenge_number == 1:
		alive =challenge_1()
	elif challenge_number == 2:
		alive =challenge_2()
	elif challenge_number == 3:
		alive=challenge_3()
	alive=challenge_1()
	alive=challenge_2()

 
