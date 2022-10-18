import java.awt.*;
import javax.swing.*;

public class Splash extends JFrame implements Runnable {

    Thread t;
    Splash(){
        ImageIcon il = new ImageIcon(ClassLoader.getSystemResource("Saved Pictures/R.jpg"));
        Image i2 =il.getImage().getScaledInstance(1000,650,Image.SCALE_DEFAULT);
        ImageIcon  i3 = new ImageIcon(i2);
        JLabel image = new JLabel(i3);
        add(image);

        t=new Thread(this);
        t.start();
        setVisible(true);
        int x=1;
        for (int i=2; i<=600; i+=4,x+=1) {

            setLocation(600 - ((i + x) / 2), 350 - (i / 2));
            setSize(i + 3 * x, i + x / 2);
            try {
                Thread.sleep(10);
            } catch (Exception e) {
                System.out.println(e.getMessage());
            }
        }
    }
    public void run(){
        try {
           Thread.sleep(7000);
           setVisible(false);

           // next Frame
            new Login();
        }
        catch (Exception e ){
            System.out.println(e.getMessage());
        }
    }
    public static void main(String[] args) {
        new Splash();
    }
}