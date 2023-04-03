#include <bits/stdc++.h>
using namespace std;

/* Definition for a binary tree node. */
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> bfs;

        queue<TreeNode*> q;

        if(root == NULL) // empty tree
            return bfs;

        q.push(root);

        // to keep a track of level counter
        int levelCount = 1; // reverse the level whose levelCount is Even

        while(!q.empty()) {
            int n = q.size(); // number of nodes in the queue at this level

            vector<int> level;
            for(int i = 1; i <= n; i++) {
                TreeNode *node = q.front();
                q.pop();

                level.emplace_back(node->val);

                // add the left child to queue
                if(node->left != NULL)
                    q.push(node->left);
                // add the right child to queue
                if(node->right != NULL)
                    q.push(node->right);
            }
            
            if(levelCount % 2 == 0) // reverse this to achieve Zig-Zag traversal
                reverse(level.begin(), level.end());

            bfs.emplace_back(level);

            levelCount++;
        }

        return bfs;
    }
};