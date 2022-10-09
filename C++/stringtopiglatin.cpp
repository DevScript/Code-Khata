#include<iostream>
using namespace std;
void discase1(string s);
int convert(string s);
bool isVowel(char c);
bool isyVowel(char c);
void insertsub(char c);
void insert(char c);
void display();
void subdisplay();
struct list {
	char c;
	list* next;
};
list* head;
list* tail;
list* shead;
list* stail;

int main() {
	string s;
	int run = 1;
	while (run) {
		run = 0;
		cout << "Enter the string:  ";
		cin >> s;
		convert(s);




		cout << "do you want to enter another word(1 yes/0 no)"; cin >> run;
		cout << endl;

	}
	return run;
}
int convert(string s) {
	int yes = 0;//let us know when vowel found so its break;
	int c2 = 0;//let us know if c2 satisfied
	list* temp = new list;
	temp->c = s[0];
	if (isVowel(temp->c)) {
		discase1(s);
	}
	else {
		for (int i = 0; i < s.length(); i++)
			insert(s[i]);
		for (int i = 0; i < s.length() && yes != 1; i++)
			if (!isVowel(s[i]))
				insertsub(s[i]);
			else {
				display();
				cout << '-';
				subdisplay();
				cout << "ay" << endl;
				c2 = 1;
				yes = 1;
			}
		if (c2 == 0) {
			
			for (int i = 0; i < s.length() && c2 != 1; i++)
			{
				if (!isyVowel(s[i]) || yes == 1)
					insert(s[i]);
				else {
					cout << s[i];
					cout << '-';
					display();
					cout << "ay" << endl;
					c2 = 1;
				}//else of isyvowel
			}
		}//ifc2==0wala
		if (c2 == 0) {
			for (int i = 0; i < s.length(); i++)
				insert(s[i]);
			display();
			cout << "-way";
			
		}
	}//mainelse
	return 0;
}//fun




bool isVowel(char c) {
	if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'O' || c == 'A' || c == 'E' || c == 'I' || c == 'U')
		return true;
	else return false;
}
bool isyVowel(char c) {
	if (c == 'y' || c == 'Y')
		return true;
	else return false;
}
void discase1(string s) {
	cout << s + "-way" << endl;
}
void insert(char c) {
	list* temp = new list;
	temp->c = c;
	if (head == NULL) {
		head = temp;
		head->next = NULL;
		tail = head;
	}
	else {
		tail->next = temp;
		tail = temp;
		tail->next = NULL;

	}
	temp = NULL;
	delete temp;
}
void insertsub(char c) {
	list* temp = new list;
	temp->c = c;
	if (shead == NULL) {
		shead = temp;
		shead->next = NULL;
		stail = shead;
	}
	else {
		stail->next = temp;
		stail = temp;
		stail->next = NULL;

	}
	if (head != NULL)if (head->c = temp->c)
	{
		temp = head;
		head = head->next;
		delete temp;
	}
}
void display() {
	list* temp = new list;
	while (head != NULL) {

		cout << head->c;
		temp = head;
		head = head->next;
		delete temp;
	}

}
void subdisplay() {
	list* temp = new list;
	while (shead != NULL) {

		cout << shead->c;
		temp = shead;
		shead = shead->next;
		delete temp;
	}

}
//
