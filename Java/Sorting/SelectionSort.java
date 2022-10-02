package Sorting;
/*selection sort is an in-place comparison sorting algorithm. It has an O(n²) time complexity, which makes it inefficient on large lists,
 and generally performs worse than the similar insertion sort. 
Worst complexity: n^2
Average complexity: n^2
Best complexity: n^2
Space complexity: 1
 */
public class SelectionSort {
    public static void main(String[] args) {
        int arr[] = {7, 11, 3, 10, 9, 15, -17, 100};
        int length = arr.length;

        for(int i = 0; i < (length - 1); i++) {
            int minIndex = i;
            for(int j = (i + 1); j < length; j++) {
                if(arr[j] < arr[minIndex]) {
                    minIndex = j;
                }
            }

            //swap minIndex and i
            int temp = arr[minIndex];
            arr[minIndex] = arr[i];
            arr[i] = temp;
        }

        for(int i = 0; i < length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }
}