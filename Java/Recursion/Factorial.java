class Factorial {
    static int factorial(int n) {
        if (n<=1) {
            return 1;
        }
        else {
            return n * factorial(n-1);
        }
    }
    public static void main(String[] args) {
        int number = 6;
        int result;
        result = factorial(number);
        System.out.println(number + " Factorial of " + number + " = " + result);
    }
}
