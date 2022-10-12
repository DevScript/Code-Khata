package KnapsackProblems;

public class MemoizationCode {

    public static int knapsackRecursive(int[] value, int[] weight, int capacity, int n, int[][] matrix){
        if(capacity == 0 || n == 0){
            return 0;
        }
        if(matrix[n][capacity] != -1){
            return matrix[n][capacity];
        }
        if(weight[n-1] <= capacity){
            return Math.max(value[n-1] + knapsackRecursive(value, weight, capacity - weight[n-1], n-1, matrix),
                    knapsackRecursive(value, weight, capacity, n-1, matrix));
        }
        else {
            return knapsackRecursive(value, weight, capacity, n-1,matrix);
        }
    }

    public static void main(String[] args) {
        int[] weight = {3,5, 2, 6};
        int[] value = {4,4, 2, 10};
        int capacity = 10;
        int[][] table = new int[101][1001];
        for (int i = 0; i < 101; i++) {
            for (int j = 0; j < 1001; j++) {
                table[i][j] = -1;
            }
        }

        System.out.println(knapsackRecursive(value, weight, capacity, value.length, table));
    }
}
