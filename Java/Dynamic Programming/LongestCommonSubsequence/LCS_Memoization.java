package LongestCommonSubsequence;

public class LCS_Memoization {

        public static int LCSMemoization(String a, String b, int m, int n, int[][] table){
            if(m == 0 || n == 0){
                return 0;
            }
            if(table[m][n] != -1){
                return table[m][n];
            }
            if(a.charAt(m-1) == b.charAt(n-1)){
                return table[m][n] = 1 + LCSMemoization(a, b, m-1, n-1, table);
            }
            else {
                return table[m][n] = Math.max(LCSMemoization(a, b, m-1, n, table), LCSMemoization(a, b, m, n-1, table));
            }
        }

        public static void main(String[] args) {
            String a = "abcdef";
            String b = "acabd";
            int[][] table = new int[a.length() + 1][b.length() + 1];
            for (int i = 0; i < a.length() + 1; i++) {
                for (int j = 0; j < b.length() + 1; j++) {
                    table[i][j] = -1;
                }
            }
            System.out.println(LCSMemoization(a, b, a.length(), b.length(), table));
        }
    }

