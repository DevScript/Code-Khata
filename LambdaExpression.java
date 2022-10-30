interface Vehicle{
    public void functionality();  
}
public class LambdaExpression{
    public static void main(String[] args) {
        Vehicle vah = ()-> {
            System.out.println("I can be Driven");
            System.out.println("I can Take 4 persons inside me");
            System.out.println("I can reach in places in less time");
        };
        vah.functionality();
    }
}
