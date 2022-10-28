class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> res; // which will be our answer
        vector<string> path; // as we are generating list everythime, so at the end this will be our list
        helper(0, s, path, res); // calling to recursion function start from index 0 and string s
        return res;
    }
    // Entire recursive function, that generates all the partition substring
    void helper(int index, string s, vector<string> &path, vector<vector<string>> &res){
        // Base Condition, which means when we have done partition at the end (n), then add it to our ultimate result
        if(index == s.size()){
            res.push_back(path);
            return;
        }
        // Let's talk about partition
        for(int i = index; i < s.size(); i++){
            if(isPalindrome(s, index, i)){ // what we are checking over here is, if we partition the string from index to i Example-(0, 0) is palindrome or not
                path.push_back(s.substr(index, i - index + 1)); // take the substring and store it in our list & call the next substring from index + 1
                helper(i + 1, s, path, res); // as we have done for (0, 0) then our next will be from (1)
                path.pop_back(); // please make sure you remove when you backtrack. 
                // Why? Because let say i had partion y, so when i go back. I can't have yy
            }
        }
    }
    bool isPalindrome(string s, int start, int end){ // A simple palindromic function start from 0 go till end. And basically keep on checking till they don't cross. 
        while(start <= end){
            if(s[start++] != s[end--]) return false;
        }
        return true;
    }
};
