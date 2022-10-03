#Hangman
import random
#game code
def Game(wo,leng):
   print("\nTotal number of words")
   comp=print("_ "*len(wo))
   lives=6
   guesslist=[]
   count=1
   while lives>0 and leng!=0:
   	guess=input("\nPlease guess a letter: ").lower()
   	if(count==len(wo)):
   			print("\n**Congratualtion, You won**")
   			print("\n")
   			menu()
   	if(guess in wo):
   		print("\nYou guessed the right word!")
   		count+=1
   		leng=leng-1
   		lives-=1
   	elif(guess not in wo):
   		print("\nYou have guessed the wrong word")
   		guesslist.append(guess)
   		display(lives)
   		lives-=1
   		leng=leng-1
 # creating of hangman		
def display(live):
	if(live==6):
		print("|===========|")
		print("|           |")
		print("| ")
		print("| ")
		print("|")
		print("|   ")
		print("|   ")
		print("|   ")
		print("\n")
	if(live==5):
		print("|===========|")
		print("|           |")
		print("|           0")
		print("|")
		print("|")
		print("|")
		print("|")
		print("|")
		print("\n")
	if(live==4):
		print("|===========|")
		print("|           |")
		print("|           0")
		print("|          /")
		print("|")
		print("|")
		print("|")
		print("|")
		print("\n")
	if(live==3):
		print("|===========|")
		print("|           |")
		print("|           0")
		print("|          /|")
		print("|          ")
		print("|")
		print("|")
		print("|")
		print("\n")
	if(live==2):
		print("|===========|")
		print("|           |")
		print("|           0")
		print("|          /|\\")
		print("|          ")
		print("|")
		print("|")
		print("|")
		print("\n")
	if(live==1):
		print("|===========|")
		print("|           |")
		print("|           0")
		print("|          /|\\")
		print("|          / \\")
		print("|")
		print("|")
		print("|")   
#All the option available for start of pro 		
def menu():
	print("\t=======================")
	print(" \t WELCOME  TO  HANGMAN !     ")
	print("\t=======================")
	l=1
	display(l)
	print()
	print("\t1) Play HANGAMAN")
	print("\t2) Quite the Game")
	option=int(input("\nEnter your option number: "))
	if(option==1):
	   	hidden=["action","friend","advice","backup","beauty","bright","camera","career","cheese","chosen","coffee","credit","decade","decent","demand","family"]
	   	word=random.choice(hidden)
	   	word_len=len(word)
	   	
	   	Game(word,word_len)
	   	
   		
	elif(option==2):
	   	print("\n=>Thanks for your time")
	   	print("\n=>Have a nice day")
	else:
	   	print("\nInvalid input")
	   	print("1) Play HANGAMAN")
	   	print("2) Quite the Game")
 # beginning of program	
def main():
	menu()
main()
