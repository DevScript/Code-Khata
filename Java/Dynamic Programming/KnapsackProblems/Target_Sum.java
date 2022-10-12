package KnapsackProblems;

import java.util.Arrays;

public class Target_Sum {
    public static int targetSum(int[] arr, int sum){
        int range = Arrays.stream(arr).sum();
        int sumOne = (range + sum) / 2;
        return helper(arr, arr.length, sumOne);
    }
    private static int helper(int[] arr, int n, int sum){
        int[][ ] table = new int[n + 1][ sum + 1];

        for (int i = 0; i < n  + 1; i++) {
            for (int j = 0; j < sum + 1; j++) {
                if (i == 0){
                    table[i][j] = 0;
                }if (j == 0){
                    table[i][j] = 1;
                }
            }
        }
        for (int i = 1; i < n  + 1; i++) {
            for (int j = 1; j < sum + 1; j++) {
                if (arr[ i - 1] <= j){
                    table[i][j] = table[i - 1][j - arr[i - 1]] + table[i - 1][j];
                }
                else {
                    table[i][j] = table[i - 1][j];
                }
            }
        }
        return table[n][sum];
    }
    public static void main(String[] args) {
        int[] arr = {1};
        int sum = 2;
        System.out.println(targetSum(arr, sum));
    }
}
