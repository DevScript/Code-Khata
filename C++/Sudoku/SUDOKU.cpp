#include<iostream>
#include<conio.h>
using namespace std;

const int N = 9;
unsigned int correct=0,error = 0;

					      
	char sudoku [N][N]= { {'-','-','-','7','-','-','-','6','-'},
					      {'-','8','-','5','-','9','3','-','-'},
					      {'-','5','4','3','-','6','-','-','7'},
					      {'-','4','-','1','-','8','-','-','-'},
				     	  {'7','2','6','-','4','-','8','-','-'},
					      {'8','9','-','-','-','2','-','-','3'},
					      {'4','-','-','-','3','1','6','8','-'},
					      {'5','-','-','-','-','7','2','-','-'},
					      {'1','6','-','-','9','-','-','-','-'} }      ;
	
	char solution [N][N]={{'9','1','3','7','2','4','5','6','8'},
					      {'6','8','7','5','1','9','3','4','2'},
					      {'2','5','4','3','8','6','1','9','7'},
					      {'3','4','5','1','7','8','9','2','6'},
				     	  {'7','2','6','9','4','3','8','5','1'},
					      {'8','9','1','6','5','2','4','7','3'},
					      {'4','7','9','2','3','1','6','8','5'},
					      {'5','3','8','4','6','7','2','1','9'},
					      {'1','6','2','8','9','5','7','3','4'} }      ;
					      
						  
						  
						  					      
//********************SUDOKU BOARD***************************//					      

	void sudoku_board () {
		
	int count = 1;
	cout<<"\t\t\t     *    "<<0<<"    "<<1<<"    "<<2<<"       "<<3<<"    "<<4<<"    ";
	cout<<5<<"       "<<6<<"    "<<7<<"    "<<8<<"    "<<endl;
	cout<<"           \t     \t**************************************************************\n";
	
	
	int k = 0;
	for (int r=0;r<N;r++)
	{          
		cout<<"                     \t"<<k<<"    *   "<<"|";
		k++;
		for(int c=0;c<N;c++)
		{
			cout<<sudoku[r][c]<<"    ";
			count++;
			if(c==2||c==5)
			{
				cout<<"   ";
			}	
		}
		cout<<"|\n";
		
		if(count==28||count==55) 
		{
			cout<<endl;
		}			
	}	
}

//********************ENTER AND CHECK VALUES*************************//	

void enter_and_check () {
	
	int i,j;
	unsigned int count=1;    //ENTER VALUE IN EMPTY PLACES
	
	cout<<"\nEnter place: ";
	cin>>i>>j;
	
	cout<<"\nEnter value: ";
	cin>>sudoku[i][j];
	
	if (sudoku[i][j]!=solution[i][j])    //CHECK
	{   
		error++;
	}
	else if (sudoku[i][j]==solution[i][j]) 
 	{
		correct++;
	}
	
}	
	
//********************NAME***************************//		
	
void name () {
	
	cout<<endl<<endl;
	
	cout<<"\t\t   =======================================================================\n";
	cout<<"\n\t\t       SSSS    UU    UU    DDDDD         OO      KK     KK   UU    UU   ";
	cout<<"\n\t\t     SS        UU    UU    DD   DD    OO    OO   KK  KK      UU    UU   ";
	cout<<"\n\t\t       SSS     UU    UU    DD     D   OO    OO   KKKK        UU    UU   ";
	cout<<"\n\t\t          SS   UU    UU    DD   DD    OO    OO   KK  KK      UU    UU   ";
	cout<<"\n\t\t      SSSS        UU       DDDDD         OO      KK     KK      UU      ";
	cout<<"\n\n\t\t   =======================================================================";
	cout<<endl<<endl;
}

	
	//********************INSTRUCTIONS***************************//	

void instructions () 
{
	
cout<<"\n\t 1. Sudoku is played on a grid of 9 x 9 spaces. ";
cout<<"\n\t 2. Within the rows and columns are 9 \"squares\" (made up of 3 x 3 spaces).";
cout<<"\n\t 3. Each row, column and square (9 spaces each) needs to be filled out with the numbers 1-9,"; 
cout<<"\n\t    without repeating any numbers within the row, column or square.";
cout<<"\n\t 4. Consider - as empty space.";	
cout<<"\n\t 5. If you want to enter any number in the grid , write its position (like 0 0 with a space between them) ";
cout<<"\n\t    then enter the value.";
	
cout<<"\n\t 6. If you made 5 errors , you will lose.";
cout<<"\n\t 7. You will recieve a prompt that you completed the puzzle or not.\n";


}
	
	//********************INT MAIN ()***************************//	
	
int main () {
	
	char response,response2;
	
	name ();
	
	cout<<"1   .   INSTRUCTIONS"<<endl;
	cout<<"2   .   START GAME"<<endl;
	response = getch();	
	
	if (response == '1') 
	{
		
		instructions();
		cout<<"\nPress 2 to start game ";
		response = getch();
		
	}

	if (response == '2' ) {

	do {
	
	cout<<endl<<endl<<endl<<endl;
	
	sudoku_board ();
	
	
	int c=0;
	
	for (int i=0;i<N;i++) {
		for (int j=0;j<N;j++) {
			
		if (sudoku[i][j] == '-'){
			
		 c++;
		}
	}
}


	cout<<"\nNo of empty spaces: "<<c;
	cout<<endl<<"Error count = "<<error;
		
	enter_and_check ();	
	
	system ("cls");
	
	
	
}while (error<5 && correct < 47);

if (correct == 47) {
		
		cout<<"\n\n\t\t CONGRATULATIONS YOU FINISHED THE PUZZLE!\n\n";
		
	}
	
	else if (error == 5) {
		cout<<"\n\n\t\t "<<"OOPS! You Lose!";
		cout<<"\n\n \t"<<"(Maximum Number Of Errors Reached.)\n\n";
		
	}

}
return 0;
}
