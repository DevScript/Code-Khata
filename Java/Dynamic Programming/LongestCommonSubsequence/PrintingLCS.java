package LongestCommonSubsequence;

public class PrintingLCS {
    public static String printLCS(String a, String b, int m, int n){
        int[][] table = new int[m+1][n+1];
        for (int i = 0; i < m+1; i++) {
            for (int j = 0; j < n+1; j++) {
                if(i == 0 || j == 0){
                    table[i][j] = 0;
                }
            }
        }
        for (int i = 1; i < m + 1; i++) {
            for (int j = 1; j < n + 1; j++) {
                if(a.charAt(i-1) == b.charAt(j-1)){
                    table[i][j] = 1 + table[i-1][j-1];
                }
                else {
                    table[i][j] = Math.max(table[i-1][j], table[i][j-1]);
                }
            }
        }
        StringBuilder LCS = new StringBuilder();
        int i = m, j = n;
        while (i > 0 && j > 0){
            if(a.charAt(i-1) == b.charAt(j-1)){
                LCS.append(a.charAt(i-1));
                i--; j--;
            }
            else {
                if(table[i-1][j] > table[i][j-1]){
                    i--;
                }
                else {
                    j--;
                }
            }
        }
        String returnLCS = "";
        for (int k = LCS.length()-1; k > -1; k--) {
            returnLCS += LCS.charAt(k);
        }


        return returnLCS;
    }

    public static void main(String[] args) {
        String a = "abcdef";
        String b = "asdf";
        System.out.println(printLCS(a, b, a.length(), b.length()));
    }
}
