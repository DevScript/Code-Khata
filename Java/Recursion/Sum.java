import java.util.Scanner;

class Sum{
    // Recursive function to find the sum of N numbers
    public static long sum(long n) {

        // base case
        if(n == 0) // sum of 0 numbers is 0
            return 0;
            
        // recursive case    
        return n + sum(n-1);
    }

    public static void main(String args[]) {
        long n;
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter n: ");
        n=sc.nextLong();
        System.out.println("Sum of "+ n + " is: " + sum(n));
    } 
}