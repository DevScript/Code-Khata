import java.util.Scanner;

class Sum{
    public static long sum(long n) {
        if(n == 0)
            return 0;
        return n + sum(n-1);
    }

    public static void main(String args[]) {
        long n;
        Scanner sc=new Scanner(System.in);
        n=sc.nextLong();

        System.out.print(sum(n));
    } 
}