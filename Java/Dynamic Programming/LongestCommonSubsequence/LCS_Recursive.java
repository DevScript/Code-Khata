package LongestCommonSubsequence;

public class LCS_Recursive {
    public static int LCSRecursive(String a, String b, int m, int n){
        if(m == 0 || n == 0){
            return 0;
        }
        if(a.charAt(m-1) == b.charAt(n-1)){
            return 1 + LCSRecursive(a, b, m-1, n-1);
        }
        else {
            return Math.max(LCSRecursive(a, b, m-1, n), LCSRecursive(a, b, m, n-1));
        }
    }

    public static void main(String[] args) {
        String a = "abcdef";
        String b = "adsfe";
        System.out.println(LCSRecursive(a, b, a.length(), b.length()));
    }
}
