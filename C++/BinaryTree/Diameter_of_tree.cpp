#include <iostream>
using namespace std;
 
// Data structure to store a binary tree node
struct Node
{
    int data;
    Node *left, *right;
 
    Node(int data)
    {
        this->data = data;
        this->left = this->right = nullptr;
    }
};
 
// Function to find the diameter of the binary tree. Note that the function
// returns the height of the subtree rooted at a given node, and the diameter
// is updated within the function as it is passed by reference
int getDiameter(Node* root, int &diameter)
{
    // base case: tree is empty
    if (root == nullptr) {
        return 0;
    }
 
    // get heights of left and right subtrees
    int left_height = getDiameter(root->left, diameter);
    int right_height = getDiameter(root->right, diameter);
 
    // calculate diameter "through" the current node
    int max_diameter = left_height + right_height + 1;
 
    // update maximum diameter (note that diameter "excluding" the current
    // node in the subtree rooted at the current node is already updated
    // since we are doing postorder traversal)
    diameter = max(diameter, max_diameter);
 
    // it is important to return the height of the subtree rooted at the current node
    return max(left_height, right_height) + 1;
}
 
int getDiameter(Node* root)
{
    int diameter = 0;
    getDiameter(root, diameter);
 
    return diameter;
}
 
int main()
{
    Node* root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->left->right = new Node(4);
    root->right->left = new Node(5);
    root->right->right = new Node(6);
    root->right->left->left = new Node(7);
    root->right->left->right = new Node(8);
 
    cout << "The diameter of the tree is " << getDiameter(root);
 
    return 0;
}