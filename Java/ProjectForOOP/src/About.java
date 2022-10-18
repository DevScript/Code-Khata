import javax.swing.*;
import java.awt.*;

public class About extends JFrame {
    About(){
        setSize(700,500);
        setLocation(400,150);
        getContentPane().setBackground(Color.WHITE);
        setLayout(null);

        //image
        ImageIcon il = new ImageIcon(ClassLoader.getSystemResource("icons/about.jpg"));
        Image i2 =il.getImage().getScaledInstance(300,200,Image.SCALE_DEFAULT);
        ImageIcon  i3 = new ImageIcon(i2);
        JLabel image = new JLabel(i3);
        image.setBounds(350,0,300,200);
        add(image);


        //heading
        JLabel heading = new JLabel("<html>University<br/Management SyStem<html>");
        heading.setBounds(70,20,300,130);
        heading.setFont(new Font("Tahoma",Font.BOLD,30));
        add(heading);


        // by name
        JLabel name = new JLabel("Developed BY Zobiya Jumani");
        name.setBounds(70,220,550,40);
       name.setFont(new Font("Tahoma",Font.BOLD,30));
        add(name);

        //my rollnumber
        JLabel rollnum = new JLabel("Roll NUmber: 21SW140");
       rollnum.setBounds(70,280,550,40);
        rollnum.setFont(new Font("Tahoma",Font.BOLD,30));
        add(rollnum);


        setVisible(true);
    }

    public static void main(String[] args) {
        new About();
    }
}
