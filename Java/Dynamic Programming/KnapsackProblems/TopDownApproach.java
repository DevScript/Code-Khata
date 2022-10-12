package KnapsackProblems;

public class TopDownApproach {
    public static int topDownApproach(int[] value, int[] weight, int capacity, int n){
        int[][] table = new int[n + 1][capacity + 1];

        for (int i = 0; i < n + 1; i++) {
            for (int j = 0; j < capacity + 1; j++) {
                if(i == 0 || j == 0){
                    table[i][j] = 0;
                }
            }
        }

        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j < capacity + 1; j++) {
                if(weight[i - 1] <= j){
                    // In 01 Bounded knapsack, if we have included a number that can not be included again!
                    table[i][j] = Math.max(value[i - 1] + table[i - 1][j - weight[i - 1]], table[i - 1][j]);
                }
                else {
                    table[i][j] = table[i - 1][j];
                }
            }
        }
        return table[n][capacity];
    }

    public static void main(String[] args) {
        int[] weight = {3,5, 2, 6};
        int[] value = {4,4, 2, 10};
        int capacity = 10;


        System.out.println(topDownApproach(value, weight, capacity, value.length));
    }
}
