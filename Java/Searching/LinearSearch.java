package Searching;
/*A linear search or sequential search 
is a method for finding an element within a list. 
It sequentially checks each element of the list until a match is found
or the whole list has been searched
Worst complexity: O(n)
Average complexity: O(n)
Space complexity: O(1)
Average performance: O(n/2)
*/
public class LinearSearch {
    public static void main(String[] args) {
        int arr[] = {23, 11, 89, 109, 14, 75, 48};
        int target = 48;
        int length = arr.length;
        int i;
        for(i = 0; i < length; i++) {
            if(arr[i] == target) {
                System.out.println("Found at index: " + i);
                break;
            }
        }

        if(i == length) {
            System.out.println("Not found");
        }
    }
}