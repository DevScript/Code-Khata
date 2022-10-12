package KnapsackProblems;

public class Subset_Sum {
    public static boolean subsetSum(int[] arr, int sum, int n){
        boolean[][] table = new boolean[n + 1][sum + 1];

        for (int i = 0; i < n + 1; i++) {
            for (int j = 0; j < sum + 1; j++) {
                if(i == 0){
                    table[i][j] = false;
                }
                if(j == 0){
                    table[i][j] = true;
                }
            }
        }

        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j < sum + 1; j++) {
                if(arr[i - 1] <= j){
                    table[i][j] = table[i - 1][j - arr[i - 1]] ||  table[i - 1][j];
                }
                else {
                    table[i][j] = table[i - 1][j];
                }
            }
        }
        return table[n][sum];
    }

    public static void main(String[] args) {
        int[] arr = { 2, 3, 7, 8, 11};
        int sum = 31;
        System.out.println(subsetSum(arr, sum, arr.length));
    }
}
