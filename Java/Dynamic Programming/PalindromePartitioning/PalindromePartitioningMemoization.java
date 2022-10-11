package PalindromePartitioning;

public class PalindromePartitioningMemoization {
    public static int[][] table = new int[1001][1001];
    public static int cutPalindrome(String s, int i, int j){
        if(i >= j){
            return 0;
        }

        if(table[i][j] != 0){
            return table[i][j];
        }
        if(isPalindrome(s, i, j)){
            return 0;
        }
        int minCuts = Integer.MAX_VALUE;
        for (int k = i; k < j; k++) {
            //Checking here for both to avoid unnecessary function call
            int left = (table[i][k] != 0) ? table[i][k] : cutPalindrome(s, i , k);
            int right = (table[k+1][j] != 0) ? table[k+1][j] : cutPalindrome(s, k+1 , j);
            int temp = left + right + 1;
            minCuts = Math.min(temp, minCuts);
        }
        return minCuts;
    }
    private static boolean isPalindrome(String s, int i, int j){
        if(i==j){
            return true;
        }
        while (i < j){
            if(s.charAt(i) != s.charAt(j)){
                return false;
            }
            i++; j--;
        }
        return true;
    }

    public static void main(String[] args) {
        String s1 = "ffpp";
        String s2 = "Mississippi";
        System.out.println(cutPalindrome(s1, 0, s1.length()-1));
    }
}
