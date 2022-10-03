/*
1. Divide the unsorted list into n sublists, each containing one element (a list of one element is considered sorted).
2. Repeatedly merge sublists to produce new sorted sublists until there is only one sublist remaining. This will be the sorted list.
Worst complexity: n*log(n)
Average complexity: n*log(n)
Best complexity: n*log(n)
Space complexity: n
*/
public class MergeSort {
    static void merge(int arr[], int left, int mid, int right) {
        int leftSize = mid - left + 1;
        int rightSize = right - mid;
        int leftArr[] = new int[leftSize];
        int rightArr[] = new int[rightSize];

        for(int i = 0; i < leftSize; i++) {
            leftArr[i] = arr[left + i];
        }

        for(int i = 0; i < rightSize; i++) {
            rightArr[i] = arr[mid + 1 + i];
        }

        int i = 0, j = 0, k = left;
        while(i < leftSize && j < rightSize) {
            if(leftArr[i] < rightArr[j]) {
                arr[k] = leftArr[i];
                i++;
            }
            else {
                arr[k] = rightArr[j];
                j++;
            }
            k++;
        }

        while(i < leftSize) {
            arr[k] = leftArr[i];
            i++;
            k++;
        }

        while(j < rightSize) {
            arr[k] = rightArr[j];
            j++;
            k++;
        }
    }

    static void mergeSort(int arr[], int left, int right) {
        if(left < right) {
            int mid = left + (right - left) / 2;
            mergeSort(arr, left, mid);
            mergeSort(arr, mid + 1, right);
            merge(arr, left, mid, right);
        }
    }

    public static void main(String[] args) {
        int arr[] = {7, 11, 3, 10, 9, 15, -17, 100};
        int length = arr.length;

        mergeSort(arr, 0, length - 1);

        for(int i = 0; i < length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }
}
