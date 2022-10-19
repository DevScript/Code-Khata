#include<iostream>
using namespace std;
int main() {
	/*old system
	1 pound = 20 shilings
	1 shelling = 12 pence
	
	new system (decimal pounds)
	1 pound = 100 pence
	
	*/
	int x,y,z;
	float f1,f2;
	cout<<"Enter pounds: ";
	cin>>x;
	
	cout<<"Enter shellings: ";
	cin>>y;
	
	cout<<"Enter pence: ";
	cin>>z;
	
	f1=(float) z/12+y;
	f2=(float)f1/20+x;	
	
	cout<<"Decimal pounds: "<<'\x9c'<<f2;
		
	return 0;
}
