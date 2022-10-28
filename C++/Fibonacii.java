import java.util.Scanner;

public class Fibonacii{
    static int numberOnIndex(int n){
        if(n==1)
        return 0;
        else if(n==2 || n==3)
        return 1;
        else
        return numberOnIndex(n-1) + numberOnIndex(n-2);
    }
    public static void main(String[] args) {
        System.out.println("Enter the Index of Fibonacii:");
        Scanner sc = new Scanner(System.in);
        int index = sc.nextInt();
        System.out.println(numberOnIndex(index));
    }
}
