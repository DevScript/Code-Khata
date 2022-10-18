/*1.	A C++ program using Object Oriented Programming concepts to 
		Input Votes for two candidates and find winner of the Election based 
		on the received votes.*/


#include<iostream>
#include<conio.h>
using namespace std;

int num = 12;
class Election {
	
	private :
		int votes;
		int cand;
		int cand1;
		int cand2;
		
	public :
		
		Election () {
			
			cand1 = 0;
			cand2 = 0;
			
		}
		
		void getvote () {
			
		cout<<"\nWrite number of candidate and press enter to submit your vote : ";
		cin>>cand;
		
		if (cand == 1)
		cand1++;
		if (cand == 2)
		cand2++;
		
		}
		
		int getvote1 () {
			
			return cand1;
		}
		
		int getvote2 () {
			
			return cand2;
		}
		
		void win ( int can1 , int can2) {
	
		if (can1>can2) 
		cout<<"\nCandidate 1 won with total "<<cand1<<" votes and percentage of : "<<(float)cand1/num *100;
			
		else if (can2>can1) 
		cout<<"\nCandidate 2 won with total "<<cand2<<" votes and percentage of : "<<(float)cand2/num *100;
		else if (can1==can2)
		cout<<"\nNo result! \nBoth have equal votes";
}

};



int main () {
	
	int person = 1;

	
	Election e1;
	
	cout<<"\t\tTWO CANDIDATES PARTICIPATTING IN ELECTIONS \n";
	cout<<"\t\tCANDIDATE 1  \n";
	cout<<"\t\tCANDIDATE 2  \n";
	
	while (person <= num) {
		
		e1.getvote();
		
		person++;
	}
	
	int vote1 = e1.getvote1();
	int vote2 = e1.getvote2();
	
	e1.win(vote1,vote2);
	
	
}
