package Sorting;
/*Bubble sort, sometimes referred to as sinking sort,
is a simple sorting algorithm that repeatedly steps through 
the input list element by element, comparing the current element
with the one after it, swapping their values if needed 
Worst complexity: n^2
Average complexity: n^2
Best complexity: n
Space complexity: 1
  */

public class BubbleSort {
    public static void main(String[] args) {
        int arr[] = {7, 11, 3, 10, 9, 15, -17, 100};
        int length = arr.length;
        int flag=0;

        for(int i = 0; i < (length - 1); i++) {
            for(int j = 0; j < (length - 1 - i); j++) {
                if(arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    flag=1;
                }
                
            }
            if(flag==0){
                break;
            }
        }

        for(int i = 0; i < length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }
}