#include <iostream>
using namespace std;

class Node {
public:
    int data;
    Node* next;

    Node(int d=0) {
        data=d;
        next=NULL;
    }
};

void add(Node* &head, Node* nn) {
    if(head == NULL) {
        head=nn;
        return;
    }

    Node* ptr=head;
    while(ptr->next != NULL) {
        ptr=ptr->next;
    }

    ptr->next=nn;
}

bool detectCycle(Node* head) {
    Node *slow=head, *fast=head;

    while(fast!=NULL && fast->next != NULL) {
        slow=slow->next;
        fast=fast->next->next;

        if(fast == slow)
            return true;
    }
}

void display(Node* ptr) {
    while(ptr != NULL){
        cout<<ptr->data<<' ';
        ptr=ptr->next;
    }
    cout<<endl;
}

int main() {
    Node* head=NULL;
    Node *one=new Node(10);
    Node *two=new Node(20);
    Node *three=new Node(30);
    Node *four=new Node(40);
    
    
    add(head, one);
    add(head, two);
    add(head, three);
    add(head, four);

    four->next = two; // explicitly creating a loop

    if(detectCycle(head))
        cout<<"Cycle exists."<<endl;
    else {
        cout<<"Cycle doesn't exist."<<endl;
        display(head);
    }
    return 0;
}