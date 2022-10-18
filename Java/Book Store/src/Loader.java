public class Loader {
    Loader(char c){
        Thread t1 = new Thread(new Runnable() {
            @Override
            public void run() {

                try{
                    for (int i=0;i<20;i++){
                        System.out.print(c);
                        Thread.sleep(150);
                    }
                    System.out.println();
                    System.out.println("Enter your choice  ");
                }
                catch (Exception e){
                    System.out.println(e.getMessage());

                }            }

        });
        t1.start();
    }
}
