package KnapsackProblems;

import java.util.Arrays;

public class CountOfSubsetWithGivenDifference {
    public static int CountOfSubsetsWithGivenDifference(int[] arr, int difference){
        int range = Arrays.stream(arr).sum();
        int sumOne = (range + difference)/2;

        return NoOfSubsets(arr, arr.length, sumOne);
    }
    private static int NoOfSubsets(int[] arr, int n, int sum){
        int[][] table = new int[n + 1][sum + 1];
        for (int i = 0; i < n + 1; i++) {
            for (int j = 0; j < sum + 1; j++) {
                if(i == 0){
                    table[i][j] = 0;
                }
                if(j == 0){
                    table[i][j] = 1;
                }
            }
        }
        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j < sum + 1; j++) {
                if(arr[i - 1] <= j){
                    table[i][j] = table[i - 1][ j - arr[i - 1]] + table[i -1][j];
                }
                else{
                    table[i][j] = table[i - 1][j];
                }
            }
        }
        return table[n][sum];
    }


    public static void main(String[] args) {
        int[] arr = { 1,1,1,1};
//        int[] arr = { 2, 4, 5, 1, 5};
//        int[] arr = { 9, 2, 7, 9};
        int difference = 2;
        System.out.println(CountOfSubsetsWithGivenDifference(arr, difference));
    }
}
