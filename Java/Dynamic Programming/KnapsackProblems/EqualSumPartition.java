package KnapsackProblems;

import java.util.Arrays;

public class EqualSumPartition {
    public static boolean equalSum(int[] arr){
        int sum = Arrays.stream(arr).sum();
        if(sum % 2 != 0){
            return false;
        }
        else{
            return subsetSum(arr, sum/2, arr.length);
        }
    }
    private static boolean subsetSum(int[] arr, int sum, int n){
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
                    table[i][j] = table[i - 1][j - arr[i - 1]] || table[i-1][j];
                }
                else {
                    table[i][j] = table[i - 1][j];
                }
            }
        }
        return table[n][sum];
    }

    public static void main(String[] args) {
        int[] arr = { 6, 3, 7, 8, 10};
        System.out.println(equalSum(arr));
    }
}
