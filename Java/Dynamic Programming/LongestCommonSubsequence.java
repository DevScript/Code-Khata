package DP_Problems;

// Program to find Longest Common Subsequence from a given String using Dynamic Programming

/* 
Dynamic programming amounts to breaking down an optimization problem into simpler sub-problems, 
and storing the solution to each sub-problem so that each sub-problem is only solved once.
*/

public class LongestCommonSubsequence_1143 {

    public int longestCommonSubsequence(String text1, String text2) {
        return helper(text1, text2, text1.length(), text2.length());
    }
    public static int helper(String s1, String s2, int m, int n){
        int[][] table = new int[m + 1][n + 1];
        for(int i = 0; i < m + 1; i++){
            for(int j = 0; j < n + 1; j++){
                if(i == 0 || j == 0){
                    table[i][j] = 0;
                }
            }
        }
        for(int i = 1; i < m + 1; i++){
            for(int j = 1; j < n + 1; j++){
                if(s1.charAt(i-1) == s2.charAt(j-1)){
                    table[i][j] = 1 + table[i-1][j-1];
                }
                else{
                    table[i][j] = Math.max(table[i-1][j] , table[i][j-1]);
                }
            }
        }
        return table[m][n];
    }
}
