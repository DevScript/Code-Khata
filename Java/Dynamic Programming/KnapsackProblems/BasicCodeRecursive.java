package KnapsackProblems;

public class BasicCodeRecursive {

    public static int knapsackRecursive(int[] value, int[] weight, int capacity, int n){
        if(capacity == 0 || n == 0){
            return 0;
        }
        if(weight[n-1] <= capacity){
            return Math.max(value[n-1] + knapsackRecursive(value, weight, capacity - weight[n-1], n-1),
                    knapsackRecursive(value, weight, capacity, n-1));
        }
        else {
            return knapsackRecursive(value, weight, capacity, n-1);
        }
    }

    public static void main(String[] args) {
        int[] weight = {3,5, 2, 6};
        int[] value = {4,4, 2, 10};
        int capacity = 10;

        System.out.println(knapsackRecursive(value, weight, capacity, value.length));
    }
}
