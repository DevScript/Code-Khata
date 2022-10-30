#include<iostream>
#include<string>
using namespace std;
class Guesstheword{
	public:
		int playgame(string word)
		
		{
			system("color 9");
			cout << "\n\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~";
	cout << "\n\n\t\t\t\t\t\t\t  Welcome to the game";
	cout << "\n\n\t\t\t\t\t\t\tYou have to guess the words";
	cout << "\n\n\t\t\t \t\t\tEach letter is represented by a dash.";
	cout << "\n\n\t\t \t\t\t\tYou have to type only one letter in one try";
	cout << "\n\n\t\t \t\t\t\t You have to try and guess the word.";
	cout << "\n\n \t\t\t\~~~~~~~~~~~~~~~~~~~~~~~~~";
    
			int misses=0;
			int exposed=0;
			string display=word;
			for(int i=0;i<display.length();i++)
			display[i]='_';
			while(exposed<word.length()){
			cout<<"\nEnter a letter : ";
				cout<<display<<":";
				char response;
				cin>>response;
				
				bool goodguess=false;
				bool duplicate=false;
				for (int i=0;i<word.length();i++)
				if (response==word[i])
				if(display[i]==word[i]){
					cout<<response<< " is already in the word\n";
					duplicate=true;
				break;
				}
				else{
				
				display[i]=word[i];
				exposed++;
				goodguess=true;
				}
				if(duplicate)
				continue;
				if(!goodguess){
				misses++;
				 cout<<response<<" is not in the word.\n";
			}
		}
		cout<<endl<<"Yay!! you guessed right it's "<<word<<".\n";
		cout<<"WOOHO!! YOU WON!!";
		return misses;
		}
};
int main(){
	
	Guesstheword obj;
	
	obj.playgame("programming");
	
	system("cls");
	cout<<"\n                  ---------------------CONGRATS!!----------------------------\n";
	cout<<"\n                  --------------YOU HAVE PASSED LEVEL 1-----------------------\n";
	cout<<"\n                  -----------IT'S TIME FOR LEVEL 2 TRY YOUR LUCK---------------\n";
	obj.playgame("fundamentals");
	system("cls");
	cout<<"\n                  ---------------------CONGRATS!!----------------------------\n";
	cout<<"\n                  --------------YOU HAVE PASSED LEVEL 2-----------------------\n";
	cout<<"\n                  -----------IT'S TIME FOR LEVEL 3 TRY YOUR LUCK---------------\n";
	obj.playgame("software");
	system("cls");
	cout<<"\n                  ---------------------CONGRATS!!----------------------------\n";
	cout<<"\n                  --------------YOU HAVE PASSED LEVEL 3-----------------------\n";
	cout<<"\n                  -----------IT'S TIME FOR LEVEL 4 TRY YOUR LUCK---------------\n";
	obj.playgame("nonpulsed");
	system("cls");
	cout<<"\n                  ---------------------CONGRATS!!----------------------------\n";
	cout<<"\n                  --------------YOU HAVE PASSED LEVEL 4-----------------------\n";
	cout<<"\n                  -----------IT'S TIME FOR LEVEL 5 TRY YOUR LUCK---------------\n";
	obj.playgame("disinterested");
	system("cls");
	cout<<"\n                  ---------------------CONGRATS!!----------------------------\n";
	cout<<"\n                  --------------YOU HAVE PASSED LEVEL 6-----------------------\n";
	cout<<"\n                  -----------IT'S TIME FOR LEVEL 7 TRY YOUR LUCK---------------\n";
	obj.playgame("rural");
	system("cls");
	cout<<"\n                  ---------------------CONGRATS!!----------------------------\n";
	cout<<"\n                  --------------YOU HAVE PASSED LEVEL 8-----------------------\n";
	cout<<"\n                  -----------IT'S TIME FOR LEVEL 9 TRY YOUR LUCK---------------\n";
	obj.playgame("penguin");
	system("cls");
	cout<<"\n                  ---------------------CONGRATS!!----------------------------\n";
	cout<<"\n                  --------------YOU HAVE PASSED LEVEL 10-----------------------\n";
	cout<<"\n                  -----------IT'S TIME FOR LEVEL 11 TRY YOUR LUCK---------------\n";
	obj.playgame("enormity");
	system("cls");
	cout<<"\n                  ---------------------CONGRATS!!----------------------------\n";
	cout<<"\n                  --------------YOU HAVE PASSED LEVEL 11-----------------------\n";
	cout<<"\n                  -----------IT'S TIME FOR LEVEL 12 TRY YOUR LUCK---------------\n";
	obj.playgame("squirrel");
	system("cls");
	cout<<"\n                  ---------------------CONGRATS!!----------------------------\n";
	cout<<"\n                  --------------YOU HAVE PASSED LEVEL 12-----------------------\n";
	cout<<"\n                  -----------IT'S TIME FOR LEVEL 13 TRY YOUR LUCK---------------\n";
	obj.playgame("weird");
	system("cls");
	cout<<"\n                  ---------------------CONGRATS!!----------------------------\n";
	cout<<"\n                  --------------YOU HAVE PASSED LEVEL 14-----------------------\n";
	cout<<"\n                  -----------IT'S TIME FOR LEVEL 15 TRY YOUR LUCK---------------\n";
	obj.playgame("intelligence");
	system("cls");
	cout<<"\n                  ---------------------CONGRATS!!----------------------------\n";
	cout<<"\n                  --------------YOU HAVE PASSED LEVEL 16-----------------------\n";
	cout<<"\n                  -----------IT'S TIME FOR LEVEL 17 TRY YOUR LUCK---------------\n";
	
}
