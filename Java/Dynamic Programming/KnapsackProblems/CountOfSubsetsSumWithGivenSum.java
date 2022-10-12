package KnapsackProblems;

public class CountOfSubsetsSumWithGivenSum {
    public static int countOfSubsets(int[] arr, int sum, int n){
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
                    table[i][j] = table[i - 1][ j - arr[ i - 1]] + table[i - 1][j];
                }
                else {
                    table[i][j] = table[i - 1][j];
                }
            }
        }


        return table[n][sum];
    }

    public static void main(String[] args) {
        int[] arr = { 2, 3, 5, 6, 8, 10};
        int sum = 10;
        System.out.println(countOfSubsets(arr, sum, arr.length));
    }
}
