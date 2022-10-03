import random
def show(board):
	print(f'''
	{board[1]}  | { board[2]} | {board[3]}          1 | 2 | 3  
	  ----+------+-----                         
	{board[4]}  | {board[5]} | {board[6]}          4 | 5 | 6    
	  ----+------+-----                     
	{board[7]}  | {board[8]} | {board[9]}          7 | 8 | 9          ''')
def validinput():
	while True:
		pos=int(input("\nEnter your position: "))
		if(pos!=' '):
			if pos in range(1,10):
				pos=pos
				break
			print("\nInvalid position")
		else:
			print("\nThankyou for playing")
			exit()
	return pos

def validpos(turn,board):
	print(f'\n{turn} chance')
	pos = validinput()
	while True:
		if board[pos]== '    ':
			board[pos]= turn
			break
		else:
			print("\nPlease select new location")
			pos=validinput()
			
def check(board):
			check=0
			if(board[1]==board[2]==board[3] != '    ' or board[4]==board[5]==board[6] != '    ' or board[7]==board[8]==board[9] != '    '):
				check=1
			elif(board[1]==board[4]==board[7] != '    ' or board[2]==board[5]==board[8] != '    ' or board[3]==board[6]==board[9] != '    '):
				check=1
			elif(board[1]==board[5]==board[9] != '    ' or board[3]==board[5]==board[7] != '    ' ):
				check=1
			return check
		
		
def userinput(board,symbl):
	play1,play2=symbl[random.randint(0,1)]
	print(play1,"will play first")
	print("\n")
	show(board)
	while(True):
				for i in range(0,9):
					if(i%2==0):
						turn= ' '+play1+' '
						validpos(turn,board)
					else:
						turn= ' '+ play2+' '
						validpos(turn,board)
					show(board)
					if(i>=4):
						if(check(board)):
							print("\n")
							show(board)
							print("\n")
							print(f'{turn} won')
							print("\n")
							exit()
					if(i==8):
						print("\nNone Won it's a TIE")
						exit()
						
def main():
	print("======+============+====")
	print("     Tic  Tac  Toe     ")
	print('======+============+=====')
	print('  X  |  0  | X')
	print(' ----+-----+----')
	print('  0  |  X  | 0')
	print(' ----+-----+----')
	print('  0  |  X  | X')
	print("\n")
	board=["position" ,'    ','    ','    ','    ','    ','    ','    ','    ','    ']
	show(board)
	symbl=[('X','0'), ('0','X') ]
	while(True):
		mark=input("\nEnter your marker X\\0: ").upper()
		if mark== "X" or mark=="0":
			userinput(board,symbl)
		else:
			print("\nWrong marker try again")
	


main()
