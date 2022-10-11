package MatrixChainMultiplication;

public class MCM_Memoization {
    static int[][] table = new int[101][101];
    public static int solve(int[] arr, int i, int j, int[][] table){
        if(i >= j){
            return 0;
        }
        if(table[i][j] != 0){
            return table[i][j];
        }
        int minCost = Integer.MAX_VALUE;
        for (int k = i; k < j; k++) {
            int temp = solve(arr, i, k, table) + solve(arr, k+1, j, table)
                    + (arr[i-1] * arr[k] * arr[j]);
            minCost = Math.min(minCost, temp);
        }
        return table[i][j] = minCost;
    }
    public static void main(String[] args) {
        int[] arr = {30, 20, 10, 40, 10, 20, 10, 30, 10};
        System.out.println(solve(arr, 1, arr.length-1, table));
    }
}
