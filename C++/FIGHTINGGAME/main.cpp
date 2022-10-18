#include <iostream>//for i/o function
#include <conio.h>//for getch function
#include <windows.h>//for Beep and other function of windows
#include <stdlib.h> //for  srand, random funcion 
#include <time.h>// for selecting time for randomness
#include <mmsystem.h>//for adding sound tracks
using namespace std;

class Character//class created to hold info of character AND method to set health  
{
    int health;//member
    string name;//memeber
public:
	void start(){
		system("color 34");
	cout<<"========================================================================================"<<endl<<endl<<endl
 	    <<"     *        *******  ********* ******"<<endl
 	    <<"     *        *            *     *"<<endl
 	    <<"     *        *****        * 	 ******"<<endl
 	    <<"     *        *            *          *"<<endl
 	    <<"     ******** *******      *	 ******"<<endl<<endl<<endl
		<<"\t\t\t\t\t\t******  *******   ***   ****   *******"<<endl
		<<"\t\t\t\t\t\t*          *     *   *  *   *     *"<<endl
		<<"\t\t\t\t\t\t******     *     *****  ****      *"<<endl
		<<"\t\t\t\t\t\t     *     *     *   *  *  *      * "<<endl
		<<"\t\t\t\t\t\t******     *     *   *  *   *     *"<<endl 
		<<"........................................................................................"<<endl
 	    <<"========================================================================================"<<endl<<endl;
		Sleep(500);
		system("pause");
		system("cls");
	}
	void sound()//memeber function for sound
		{
		mciSendString("open \"s.mp3\" type mpegvideo alias mp3", NULL, 0, NULL);//open required sound track
		mciSendString("play mp3 from 0", NULL, 0, NULL);//repeat that sound to 0 seconds	
		mciSendString("play mp3 ", NULL, 0, NULL);	//play sound track
		}//sound end
	void over()//memeber function for gameover 
	{
		mciSendString("open \"k.wav\" type mpegvideo alias wav", NULL, 0, NULL);//open required sound tarck
		mciSendString("play wav from 0", NULL, 0, NULL);//repeat that sound to 0 seconds	
		mciSendString("play wav ", NULL, 0, NULL);//play that sound
		char y[]="\t\t\t\tGame Over !\n";
		for(int j=0; j<strlen(y); j++)
		{
			Sleep(100);
			cout<<y[j];//show gameover
		}//loop end
	}//over end
	void set_name(string zami)
	{		
		name=zami;
	}//setting name function end
	
	string get_name()
	{
		return name;
	}//getter used
	void set_health(int x)
	{	
		health=x;
	}//set health function end
	int get_health(){
		return health;
	}//getter used to get health
    void kick()
	{
      health-=25;//minus health
      sound();//sound effect for kick
      }//reduce health on kick function end 
    void punch()
	{
    health-=15;//minus health
      sound();//sound effect for punch
	}//reduce health on punch function end
    void slap()
	{
    health-=10;//minus health
      sound();//sound effect for slap
    }//reduce health on slap function end
    void knee()
	{
    health-=20;//minus health 
    sound();//sound effect for knee
    }//reduce health on knee function end
 void player1(Character &p1,Character &p2)//memeber function for player 1
 {
 			system("color F9");
        	cout<<"\t\t\t\tplayer  "<<p1.get_name()<<endl;
        	cout<<"\t\t\t\tyour health is :"<<p1.get_health()<<endl;
			cout<<"\t\t\t\tplease make move:"<<endl;
        	cout<<"\t\t\t\tHint: X for kick, A for punch, S for slap, Z for knee"<<endl;
     		char move;
			cout<<"\t\t\t\t"; move=getch();//asking for move want 
				switch(move)
				{
				case 'x':
    			p2.kick();
				Beep(0,750);
    			break;
				case 'X':
				p2.kick();
				Beep(0,750);
   				 break;
				case 'a':
    			p2.punch();
    			Beep(0,750);
				break;
				case 'A':
    			p2.punch();
    			Beep(0,750);
    			break;
				case 's':
    			p2.slap();
    			Beep(0,750);
    			break;
				case 'S':
    			p2.slap();
    			Beep(0,750);
  			  	break;
				case 'z':
    			p2.knee();
   			 	Beep(0,750);
    			break;
   				case 'Z':
   				 p2.knee();
    			Beep(0,750);
    				break;
    				default :
					cout<<"\t\t\t\twrong move";
					}//switch end
			}//player one end
				
	void player2(Character &p1, Character &p2)//player 2 memeber function 
	{
			system("color 09");
        	cout<<"\t\t\t\tplayer  "<<p2.get_name()<<endl;
        	cout<<"\t\t\t\tyour health is :"<<p2.get_health()<<endl;
        	cout<<"\t\t\t\tplease make move:"<<endl;
        	cout<<"\t\t\t\tHint: K for kick, L for punch, N for slap, M for knee"<<endl;
     		char move;
			 cout<<"\t\t\t\t"; move=getch();//for move that want
				switch(move)
				{
				case 'k':
   				p1.kick();
    			Beep(0,750);
    			break;
				case 'K':
				p1.kick();
				Beep(0,750);
   				 break;
				case 'L':
    			p1.punch();
    			Beep(0,750);
				break;
				case 'l':
    			p1.punch();
    			Beep(0,750);
    			break;
				case 'n':
    			p1.slap();
    			Beep(0,750);
    			break;
				case 'N':
    			p1.slap();
    			Beep(0,750);
  			  	break;
				case 'm':
    			p1.knee();
   			 	Beep(0,750);
    			break;
   				case 'M':
   				 p1.knee();
    			 Beep(0,750);
    				break;
    				default :
					cout<<"\t\t\t\twrong move";
				}//switch end
			}//player 2 end					
	void single()//memeber function for single player
	{
	srand(time(0));//used to set randomness every time
		int fturn;//used for repeatation
		fturn=rand() % 2 + 0;//repeat between 0 2 any 
			int type;
			Character p1,p2;//members of class
			string name1 ,name2;
    		p1.set_health(100);//setting initial health for player 1
    		p2.set_health(100);//setting initial health for player 2
			system("cls");
        	int auto1=0;
    		char ch;
    		do{
    			char x[]="\t\t\t\tSelect Game Type For single player:\n\n\t\t\t\t1: For Easy level \n\t\t\t\t2: For Medium level \n\t\t\t\t3: For Hard level\n";
    			for(int i=0; i<strlen(x); i++){
				Sleep(50);
				cout<<x[i];}
			cout<<"\t\t\t\t"; cin>>type;//asking for game type in single player
			switch(type){
    				case 1:
				{
					system("cls");
					cout<<"\t\t\t\tEnter name of  Player :";
    				cin.ignore(100,'\n');
    				getline(cin,name1);//getting name for player
    				p1.set_name(name1);//setting name
    				p2.set_name("Computer");
					int turn =1;
					system("cls");
			if(fturn%2!=0)//randomly checking first move
			{		
    		while(p2.get_health()>0 && p1.get_health()>0){
        	char move;
        	if(turn%2!=0) {
           	turn++;
        
					player1(p1,p2);//player one called
       			}//if end
				  	
				if(p2.get_health()<=0)//checking for p2 health if zero break
					{
    				break;
					}
					system("cls");
 		if(turn%2==0) //for used for next turn
		 {
        turn++;
        system("color 09");
        	cout<<"\t\t\t\t"<<p2.get_name()<<endl;
        	cout<<"\t\t\t\tis making move:"<<endl;
        	cout<<"\t\t\t\t";
			if(auto1<=2)
			{
    		p1.slap();
			Beep(0,750);
    		}//cheak in first 3 moves small demages
			else
			{
			Beep(0,750);
    		p1.punch();
			}//after 3rd heavy demage moves 
    		auto1++;
			system("cls");
   		}//main if end used to for selectiong ch
		}//loop end
	}//if end
	else{
			while(p2.get_health()>0 && p1.get_health()>0){
        	char move;
        	if(turn%2!=0)//checking whose move 
			{
           	turn++;
        
					system("color 09");
        	cout<<"\t\t\t\t"<<p2.get_name()<<endl;
        	cout<<"\t\t\t\tis making move:"<<endl;
			cout<<"\t\t\t\t";
			if(auto1<=2)
			{
    		p1.slap();
			Beep(0,750);
    		}//cheak in first 3 moves small demages
			else
			{
			Beep(0,750);
    		p1.punch();
			}//after 3rd heavy demage moves 
    		auto1++;
    
			system("cls");
   		
       			}
				  	
				if(p1.get_health()<=0)//checking if has health continue else break
				{
    				break;
				}
					system("cls");
 		if(turn%2==0) {
        turn++;
        player1(p1,p2);//player1 called
		   		system("cls");
   		
			}//if end
		}//loop end
	}//else end
		system("cls");
		system("color 34");
   		over();//showing game over
   		if(p2.get_health()<=0 && p1.get_health()>0)//declearing winer and loser
		{
   		cout<<"\t\t\t\tplayer 2: "<<p2.get_name()<<" Dead "<<endl;
    	cout<<"\t\t\t\tplayer 1: "<<p1.get_name()<<" Wins "<<endl;
   		}//if end
   		else 
		{
    	cout<<"\t\t\t\tPlayer 1: "<<p1.get_name()<<" Dead"<<endl;
    	cout<<"\t\t\t\tplayer 2: "<<p2.get_name()<<" Wins "<<endl;
   		}//else end
   		
   		ch='k';//restrict to use loop
		break;
    	}//case 1 finsihed
    	
		case 2://case 2 starts
		{
   					system("cls");
					cout<<"\t\t\t\tEnter name of  Player :";
    				cin.ignore(100,'\n');
    				getline(cin,name1);
    				p1.set_name(name1);//setting name
    				p2.set_name("Computer");
					system("cls");
					int turn =1;
				if(fturn%2!=0)//used for randomness
		{
    		while(p2.get_health()>0 && p1.get_health()>0)//loop start checking if both have health remain go 
			{
        	char move;
        	if(turn%2!=0) {
           	turn++;
				player1(p1,p2);           	
			   	}//if end that cheak turn 
					if(p2.get_health()<=0)
					{
    				break;
					}//health zero to terminate
  			if(turn%2==0) {
			system("cls");
        	turn++;
        	system("color 09");
        	cout<<"\t\t\t\t"<<p2.get_name()<<endl;
        	cout<<"\t\t\t\tis making move:"<<endl;
			cout<<"\t\t\t\t";
			if(auto1<=2){
    		p1.punch();
			Beep(0,750);
			}//cheak in first 3 moves small demages
			else{
    		p1.knee();
			Beep(0,750);
			}//after 3rd heavy demage moves 
    		auto1++;
		
   			system("cls");

        	}//cheak 2 players turn
   			}//loops end here
		}//if end
	else{
			while(p2.get_health()>0 && p1.get_health()>0)//loop start checking if both have health remain go 
			{
        	char move;
        	if(turn%2!=0) {
           	turn++;
			system("color 09");
        	cout<<"\t\t\t\t"<<p2.get_name()<<endl;
        	cout<<"\t\t\t\tis making move:"<<endl;
			cout<<"\t\t\t\t";
			if(auto1<3)
			{
    		p1.punch();
			Beep(0,750);
			}//cheak in first 3 moves small demages
			else{
    		p1.knee();
			Beep(0,750);
			}//after 3rd heavy demage moves 
    		auto1++;
           	
			   	}//if end that cheak turn 
					if(p1.get_health()<=0)
					{
    				break;
					}//health zero to terminate
  			if(turn%2==0) {
			system("cls");
        	turn++;
        	player1(p1,p2);//calling player 1
        	system("cls");
        	}//cheak 2 players turn
   		}//loop end
	}//else end 
		system("cls");
		system("color 34");
		over();//showing gameover
   		if(p2.get_health()<=0 && p1.get_health()>0)//declearing winner and loser
		{
   		cout<<"\t\t\t\tplayer 2: "<<p2.get_name()<<" Dead "<<endl;
    	cout<<"\t\t\t\tplayer 1: "<<p1.get_name()<<" Wins "<<endl;
   		}//if end
   		else {
    	cout<<"\t\t\t\tPlayer 1: "<<p1.get_name()<<" Dead"<<endl;
    	cout<<"\t\t\t\tplayer 2: "<<p2.get_name()<<" Wins "<<endl;
   		}//else end
    		
			break;
			ch='k';//restrict to use loop
		}//case 2 ends here
		
		case 3:{
					system("cls");
					cout<<"\t\t\t\tEnter name of  Player :";
    				cin.ignore(100,'\n');
    				getline(cin,name1);
    				p1.set_name(name1);
    				p2.set_name("Computer");
					int turn =1;//used for turns
					system("cls");
    		if(fturn%2!=0)//used for randomness 
			{
			while(p2.get_health()>0 && p1.get_health()>0)//loop start checking if both have health remain go 
			{
        	char move;
        	if(turn%2!=0) //checking whose turn
			{
           	turn++;
           		player1(p1,p2);//calling player 1
			}	//if end here
					if(p2.get_health()<=0)
					{
						break;
					}//checking if have some health continue else break
					system("cls");
  		if(turn%2==0)//checking player 2 turn 
  		{
        turn++;
        system("color 09");
        cout<<"\t\t\t\t"<<p2.get_name()<<endl;
        cout<<"\t\t\t\tis making move:"<<endl;
        cout<<"\t\t\t\t";
		if(auto1<=2){
    	p1.knee();
		Beep(0,750);
		}
		else{
    	p1.kick();
		Beep(0,750);
		}
		auto1++;
   		system("cls");
        }//if turn cheaker end
   		}//loop end
   	}//random select if end here
   	else{
   			while(p2.get_health()>0 && p1.get_health()>0)//loop start checking if both have health remain go 
			{
        	char move;
        	if(turn%2!=0) //checking whose turn
			{
		turn++;
        system("color 09");
        cout<<"\t\t\t\t"<<p2.get_name()<<endl;
        cout<<"\t\t\t\tis making move:"<<endl;
        cout<<"\t\t\t\t";
		if(auto1<=2){
    	p1.knee();
		Beep(0,750);
		}
		else{
    	p1.kick();
		Beep(0,750);
		}
		auto1++;
   		system("cls");
       }//if turn cheaker end

					if(p1.get_health()<=0)
					{
						break;
					}//checking if have some health continue else break
					system("cls");
  		if(turn%2==0)//checking player 2 turn 
  		{
        player1(p1,p2);
        turn++;
        system("cls");
   		}//if end here
   		
	   }//loop end here
	}//else end here
		system("cls");
		system("color 34");
			over();//showing game over
   		if(p2.get_health()<=0 && p1.get_health()>0)//declearing winner and loser
		   {
   		cout<<"\t\t\t\tplayer 2: "<<p2.get_name()<<" Dead "<<endl;
    	cout<<"\t\t\t\tplayer 1: "<<p1.get_name()<<" Wins "<<endl;
   		}//if end
   		else {
    	cout<<"\t\t\t\tPlayer 1: "<<p1.get_name()<<" Dead"<<endl;
    	cout<<"\t\t\t\tplayer 2: "<<p2.get_name()<<" Wins "<<endl;
   		}//else end
			ch='k';//restrict to use loop
			break;
		}//case 3 end
    		default:{
    			system("cls");
    			cout<<"\t\t\t\tInvalid Input !\n";
    			ch='z';
				break;
			}//default case end
				}//switch end here
			}while(ch=='z');//again use of switch for invalid result.
		
			}//function single_player end here
	void multiplayer(){
    	srand(time(0));//used for randomness everytime sequence zero 
		int fturn;//used for checking first turn
		fturn=rand() % 2 + 0;//can between 0 and 2
		system("cls");
    	Character p1,p2;//members of class
		string name1 ,name2;
    	p1.set_health(100);//setting health p1
    	p2.set_health(100);//setting health p1
		cout<<"\t\t\t\tEnter name of first Player :";
    	getline(cin,name1);
    	p1.set_name(name1);
    	cout<<"\t\t\t\tEnter name of Second Player :";
    	getline(cin,name2);
    	p2.set_name(name2);
    	int turn =1;
    	system("cls");
    	if(fturn%2!=0)//for random select first move
		{
    	while(p2.get_health()>0 && p1.get_health()>0)////loop start checking if both have health remain go 
		{
        char move;
        if(turn%2!=0) {
           turn++;
           player1(p1,p2);//called player 1
       	}//if end
		if(p2.get_health()<=0){
    	break;
		}	//if still have health continue
		system("cls");
  		if(turn%2==0) {
        turn++;
        player2(p1,p2);//calling player 2
      
   		system("cls");
       		}//if end 
   		}//loop end
	}//if end
	else{
		while(p2.get_health()>0 && p1.get_health()>0)////loop start checking if both have health remain go 
		{
        char move;
        if(turn%2!=0) {
           turn++;
           player2(p1,p2);//called player 2
       }//if end
		if(p1.get_health()<=0){
    	break;
		}//if still have health continue
		system("cls");
  		if(turn%2==0) {
        turn++;
        player1(p1,p2);//called player 1
    	system("cls");
       		}//if end 
   		}//LOOP end
	}//else end
		system("cls");
		system("color 34");
   		 over();//showing gameover
   		if(p2.get_health()<=0 && p1.get_health()>0)//declearing winner and loser
		   {
   		cout<<"\t\t\t\tplayer 2: "<<p2.get_name()<<" Dead "<<endl;
    	cout<<"\t\t\t\tplayer 1: "<<p1.get_name()<<" Wins "<<endl;
   		}//if end
  	 else {
    	cout<<"\t\t\t\tPlayer 1: "<<p1.get_name()<<" Dead"<<endl;
    	cout<<"\t\t\t\tplayer 2: "<<p2.get_name()<<" Wins "<<endl;
   		  }//else end		
		}//multi_player end here function		

};//class end
	int main()
	{
	Character one;
	char z;//used for repeating
	one.start();
	do{	
	system("color 0f");
	system("cls");//clear screen
	system("title WAY TO DEATH");//title set
	//Sleep(3);
    char ch;
	char game;//used to select game type
    do{
	char x[]="\t\t\t\tSelect Game Type:\n\n\t\t\t\tPress 'S' for single player \n\t\t\t\tPress 'M' For multiplayer\n";
	for(int i=0; i<strlen(x); i++){
	Sleep(50);
	cout<<x[i];}
	cout<<"\t\t\t\t"; game=getch();//selecting game type
	switch(game)//choice of game want to play
	{
		
    	case 's':{
				one.single();//single_player
				ch='k';
				break;
				}
		case 'S':{
				one.single();//single_player
				ch='k';
				break;
				}
    	case 'm':{
				one.multiplayer();//multi_player
				ch='k';
				break;
				}//case 2 of first switch end here
		case 'M':{
				one.multiplayer();//multi_player
				ch='k';
				break;
				}//case 2 of first switch end here
    	default:{
    			 system("cls");
    			cout<<"\t\t\t\tInvalid Input !\n";
				ch='z';
				break;
			}//default end here
		}//switch end
	}while(ch=='z');
    	cout<<"\t\t\t\tWant to play again press T:.....";
		}while((z=getch())=='t' || (z=getch())=='T');//checking to play again
    
		return 0;
}//main function end.
