package PalindromePartitioning;

import java.util.Locale;

public class PalindromePartitioningRecursive {
    public static int palindromePartitioning(String s, int i, int j){
        if(i >= j){
            return 0;
        }
        if(isPalindrome(s, i, j)){
            return 0;
        }
        int minPartition = Integer.MAX_VALUE;
        for (int k = i; k < j; k++) {
            int temp = palindromePartitioning(s, i, k) + palindromePartitioning(s, k + 1, j) + 1;
            minPartition = Math.min(minPartition, temp);
        }

        return minPartition;
    }
    private static boolean isPalindrome(String s, int i, int j){
        if(i == j){
            return true;
        }
        while (i < j){
            if(s.charAt(i) != s.charAt(j)){
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
    public static void main(String[] args) {
        String string = "Mississippi";
//        String string = "NItin";
        //I have passed as lowercase
        System.out.println(palindromePartitioning(string.toLowerCase(), 0, string.length()-1));
    }
}
