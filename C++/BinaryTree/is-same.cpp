#include <bits/stdc++.h>
using namespace std;

// Definition for a binary tree node.
struct Node {
    int data;
    Node *left, *right;
    Node() : data(0), left(nullptr), right(nullptr) {}
    Node(int x) : data(x), left(NULL), right(NULL) {}
};

void insert(Node** root, Node* nn) {
    if(*root == NULL) {
        *root = nn;
    }
    else {
        if(nn->data < (*root)->data)
            insert(&((*root)->left), nn);
        if(nn->data > (*root)->data)
            insert(&((*root)->right), nn);
    }
}

bool isSameTree(Node* p, Node* q) {
    if(p == NULL && q == NULL)
        return true;
        
    // one is NULL, other one is NOT NULL
    else if(p == NULL || q == NULL) 
        return false;
        
    else if(p->data != q->data)
        return false;
    return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
}

int main() {
    Node* p=NULL, *q=NULL;
    int n;
    cout<<"Enter number of nodes in 1st tree: ";
    cin>>n;
    int x;
    cout<<"Enter nodes for 1st tree: ";
    for(int i=0; i<n; i++) {
        cin>>x;
        Node* nn=new Node(x);
        insert(&p, nn);
    }

    cout<<"Enter number of nodes in 2nd tree: ";
    cin>>n;
    cout<<"Enter nodes of 2nd tree: ";
    for(int i=0; i<n; i++) {
        cin>>x;
        Node* nn=new Node(x);
        insert(&q, nn);
    }

    if(isSameTree(p, q))
        cout<<"Same Tree"<<endl;
    else 
        cout<<"Not Same Tree"<<endl;
    return 0;
}