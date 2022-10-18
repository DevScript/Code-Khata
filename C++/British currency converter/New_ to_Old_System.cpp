#include<iostream>
using namespace std;
int main() {
	
	float decpounds;
	cout<<"Enter decimal pounds: ";
	cin>>decpounds;     
	
	float x,y,z,x1,x2,y1,y2;
	x=(int) decpounds;   //pounds
	x1=decpounds-x;  
	y1= (x1*20);    // shelling  
	y= (int) (x1*20);
	y2= y1-y;  
	z=(int) (y2*12); //pence
	
	cout<<"Equivalent in old notation = "<<'\x9c'<<x<<"."<<y<<"."<<z<<".";
	return 0;
}
