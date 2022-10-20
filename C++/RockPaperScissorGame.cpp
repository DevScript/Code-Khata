#include <iostream>
using namespace std;
int main()
{
    char pl_1, pl_2;
    cout << "Welcome to my program!\n";
    cout << "This is a rock paper scissors game.\n";
    cout << "Player 1, please type your decision using 'p', 'r' or 's'.\n";
    cin >> pl_1;
    cout << "Player 2, please type your decision using 'p', 'r' or 's'.\n";
    cin >> pl_2;
    if ((pl_1 == 'P' || pl_1 == 'p') && (pl_2 == 'R' || pl_2 == 'r'))
    {
        cout << "Player 1 Wins!\n" << "Paper covers Rock!\n";
    }
    else if ((pl_1 == 'R' || pl_1 == 'r') && (pl_2 == 'P' || pl_2 == 'p'))
    {
        cout << "Player 2 Wins!\n" << "Paper covers Rock!\n";
    }
    else if ((pl_1 == 'R' || pl_1 == 'r') && (pl_2 == 'S' || pl_2 == 's'))
    {
        cout << "Player 1 Wins!\n" << "Rock breaks Scissors!\n";
    }
    else if ((pl_1 == 'S' || pl_1 == 's') && (pl_2 == 'R' || pl_2 == 'r'))
    {
        cout << "Player 2 Wins!\n" << "Rock breaks Scissors!\n";
    }
    else if ((pl_1 == 'S' || pl_1 == 's') && (pl_2 == 'P' || pl_2 == 'p'))
    {
        cout << "Player 1 Wins!\n" << "Scissor cuts Paper!\n";
    }
    else if ((pl_1 == 'P' || pl_1 == 'p') && (pl_2 == 'S' || pl_2 == 's'))
    {
        cout << "Player 2 Wins!\n" << "Scissor cuts Paper!\n";
    }
    else if (((pl_1 == 'P' || pl_1 == 'p') && (pl_2 == 'P' || pl_2 == 'p')) || ((pl_1 == 'R' || pl_1 == 'r') &&
            (pl_2 == 'R' || pl_2 == 'r')) || ((pl_1 == 'S' || pl_1 == 's') && (pl_2 == 'S' || pl_2 == 's')))
    {
        cout << "No one wins! The game is a draw.\n";
    }
    else
    {
        cout << "Invalid Input. Please type 'r', 's' or 'p' to play the game.\n";
    }
    return 0;
}
