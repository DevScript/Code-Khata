class Thread1 extends Thread{
    int counter;
    private static int Start;
    @Override
    public void run() {
        for(int i=10000;i<=Start;i++){
            
            if(i<=10200){
                System.out.println(i++);
                try{
                    Thread.sleep(20);
                }
                catch(InterruptedException e){
                    System.out.println("Exception occurred");
                }
            }
            
        }

    }
   public static void Stating(int a){
        Start=a;
    }
}

class Thread2 extends Thread{
    private static int Start;
    @Override
    public void run() {
        for(int i=10000;i<=Start;i++) {
            if (i<=104040000) {
                i++;
            System.out.println(i*i);
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    System.out.println("Exception occurred");
                }
            }
        }
    }
    public static void Stating(int a){
        Start=a;
    }
}



public class Multithreading{
    public static void main(String[] args) {
        Thread1   mt1= new Thread1();
        Thread1.Stating(200000);
        Thread2 mt2 = new Thread2();
        Thread2.Stating(104040000);
        mt1.start();
       mt2.start();

        
    }
}
