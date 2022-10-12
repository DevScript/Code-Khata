package KnapsackProblems;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

public class MinimumSubsetSumDifference {
    public static int minimumSSDifference(int[] arr){
        int range = Arrays.stream(arr).sum();
        boolean[][] table = subsetSumWithRange(arr, range);
        List<Integer> list = new LinkedList<>();
        for (int i = 0; i <= range/2; i++) {
            if(table[arr.length][i]){
                list.add(i);
            }
        }
        int min = Integer.MAX_VALUE;
        for (Integer integer : list) {
            int value = range - 2 * integer;
            min = Math.min(min, value);
        }

        return min;
    }

    private static boolean[][] subsetSumWithRange(int[] arr, int range){
        int n = arr.length;
        boolean[][] table = new boolean[n + 1][ range + 1];

        for (int i = 0; i < n + 1; i++) {
            for (int j = 0; j < range + 1; j++) {
                if(i == 0){
                    table[i][j] = false;
                }
                if(j == 0){
                    table[i][j] = true;
                }
            }
        }

        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j < range + 1; j++) {
                if(arr[ i - 1] <= j){
                    table[i][j] = table[i -1][j - arr[i - 1]] || table[i - 1][j];
                }
                else{
                    table[i][j] = table[i - 1][j];
                }
            }
        }

        return table;
    }

    public static void main(String[] args) {
//        int[] arr = { 2, 4, 5};
        int[] arr = { 1, 2, 7, 9};
        System.out.println(minimumSSDifference(arr));
    }
}
