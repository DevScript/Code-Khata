package MatrixChainMultiplication;

public class MCM_Recursive {
    public static int solve(int[] arr, int i, int j){
        if(i >= j){
            return 0;
        }
        int minCost = Integer.MAX_VALUE;
        for(int k = i; k < j; k++){
            int temp = solve(arr, i, k) + solve(arr, k+1, j) + (arr[i-1] * arr[k] * arr[j]);
            if(temp < minCost){
                minCost = temp;
            }
        }
        return minCost;
    }
    public static void main(String[] args) {
        int[] arr = {30, 20, 10, 40};
        System.out.println(solve(arr, 1, arr.length-1));
    }
}
