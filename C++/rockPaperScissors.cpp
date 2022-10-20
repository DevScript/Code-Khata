#include <iostream>
#include <cmath>
using namespace std;

int main()
{
char player1,player2;

cout << "Paper - Rock - Scissor Game\n\n"
     << "Game Rules:\nType 'p' or 'P' for Paper\nType 's' or 'S' for Scissor\nType 'r' or 'R' for Rock\n\n";

cout << "Player 1 Turn: ";
cin >> player1;

cout << "\nPlayer 2 Turn: ";
cin >> player2;

/----------------------------------------------------------------------------------------/


if ((player1 == 's' || player1 == 'S') && (player2 == 'p' || player2 == 'P'))
{
   cout << "\nScissors cut paper!!\n"
         << "Player 1 Wins!!\n\n";
}


else if ((player1 == 'p' || player1 == 'P') && ( player2 == 's' || player2 == 'S' ))
 {
   cout << "\nScissors cut paper!!\n"
         << "Player 2 Wins!!\n\n";
}


/----------------------------------------------------------------------------------------/


else if ((player1 == 'p' || player1 == 'P') && (player2 == 'r' || player2 == 'R' ))
 {
   cout << "\nPaper covers rock!!\n"
         << "Player 1 Wins!!\n\n";
}


else if ((player1 == 'r' || player1 == 'R') && (player2 == 'p' || player2 == 'P'))
 {
   cout << "\nPaper covers rock!!\n"
         << "Player 2 Wins!!\n\n";
}


/----------------------------------------------------------------------------------------/


else if ((player1 == 'r' || player1 == 'R' ) && (player2 == 's' || player2 == 'S'))
 {
   cout << "\nRock breaks scissors!!\n"
         << "Player 1 Wins!!\n\n";
}


else if (( player1 == 's' || player1 == 'S') && (player2 == 'r' || player2 == 'R'))
 {
   cout << "\nRock breaks scissors!!\n"
         << "Player 2 Wins!!\n\n";
}


/----------------------------------------------------------------------------------------/


else if ((player1 == 'R' || player1 == 'r') && (player2 == 'R' || player2 == 'r'))
cout << "\nIt's a Draw! Nobody wins!\n\n";


else if ((player1 == 'S'|| player1 == 's') && (player2 == 'S' || player2 == 's' ))
cout << "\nIt's a Draw! Nobody wins!\n\n";


else if ((player1 == 'P' || player1 == 'p') && (player2 == 'P' || player2 == 'p'))
cout << "\nIt's a Draw! Nobody wins!\n\n";



/----------------------------------------------------------------------------------------/


else
{
 cout << "\nYou Entered Invalid Option!\n\n";
}


    return 0;
}
