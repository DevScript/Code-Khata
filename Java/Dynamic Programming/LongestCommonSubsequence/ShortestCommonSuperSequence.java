package LongestCommonSubsequence;

public class ShortestCommonSuperSequence {
    public static int superSequence(String a, String b){
        return a.length() + b.length() - helperLCS(a, b, a.length(), b.length());
    }

    private static int helperLCS(String a, String b, int m, int n){
        int[][] table = new int[m+1][n+1];
        for (int i = 0; i < m+1; i++) {
            for (int j = 0; j < n+1; j++) {
                if(i == 0 || j == 0){
                    table[i][j] = 0;
                }
            }
        }
        for (int i = 1; i < m+1; i++) {
            for (int j = 1; j < n+1; j++) {
                if(a.charAt(i-1) == b.charAt(j-1)){
                    table[i][j] = 1 + table[i-1][j-1];
                }
                else {
                    table[i][j] = Math.max(table[i-1][j], table[i][j-1]);
                }
            }
        }
        return table[m][n];
    }

    public static void main(String[] args) {
        String a = "Zohaib";
        String b = "Zubair";
        System.out.println(superSequence(a, b));
    }

}
