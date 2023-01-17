import java.util.Scanner;
class ExchangeSort {
    
    public static void print(int[] arr) {
        for(int elem: arr)
            System.out.print(elem+ " ");
        System.out.println("");
    }

    public static void exchangeSort(int[] arr) {
        int n=arr.length;
        for(int i=0; i<n-1; i++) {
            for(int j=i+1; j<n; j++) {
                if(arr[j] < arr[i]) { // sorting in non-decreasing order
                    // swap
                    int t=arr[i];
                    arr[i]=arr[j];
                    arr[j]=t;
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();

        int arr[]=new int[n]; // array created on the heap
        for(int i=0; i<n; i++)
            arr[i]=sc.nextInt();
        sc.close();
        // array input done
        
        // sorting
        exchangeSort(arr);

        // printing the array
        print(arr);
    }
}