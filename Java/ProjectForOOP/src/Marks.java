import javax.swing.*;
import  java.awt.*;
import java.sql.ResultSet;
import java.awt.event.*;
public class Marks extends JFrame implements ActionListener {
    String rollno;
    JButton cancel;
    Marks(String rollno){
        this.rollno=rollno;

        setSize(500,600);
        setLocation(500,100);

        getContentPane().setBackground(Color.WHITE);
        setLayout(null);

        //heading
        JLabel heading = new JLabel("MUET");
        heading.setBounds(100,10,500,25);
        heading.setFont(new Font("Tahoma",Font.BOLD,20));
        add(heading);

        // sub heading
        JLabel subheading = new JLabel("Result Of Examination 2022");
        subheading.setBounds(100,50,500,20);
        subheading.setFont(new Font("Tahoma",Font.BOLD,18));
        add(subheading);


        // roll number
        JLabel lblrollno = new JLabel("Roll Number"+rollno);
        lblrollno.setBounds(60,100,500,20);
        lblrollno.setFont(new Font("Tahoma",Font.PLAIN,18));
        add(lblrollno);


        //semester
        JLabel lblsemester = new JLabel();
        lblsemester.setBounds(60,130,500,20);
        lblsemester.setFont(new Font("Tahoma",Font.PLAIN,18));
        add(lblsemester);


        //subect 1
        JLabel subject1= new JLabel();
        subject1.setBounds(100,200,500,20);
        subject1.setFont(new Font("Tahoma",Font.PLAIN,18));
        add(subject1);


        //subject2
        JLabel subject2 = new JLabel();
       subject2.setBounds(100,230,500,20);
        subject2.setFont(new Font("Tahoma",Font.PLAIN,18));
        add(subject2);

        //subject3
        JLabel subject3 = new JLabel();
        subject3.setBounds(100,260,500,20);
        subject3.setFont(new Font("Tahoma",Font.PLAIN,18));
        add(subject3);

        //subject4
        JLabel subject4 = new JLabel();
        subject4.setBounds(100,290,500,20);
        subject4.setFont(new Font("Tahoma",Font.PLAIN,18));
        add(subject4);

        //subject5
        JLabel subject5 = new JLabel();
        subject5.setBounds(100,320,500,20);
        subject5.setFont(new Font("Tahoma",Font.PLAIN,18));
        add(subject5);

        try{
            Conn c = new Conn();
            ResultSet rs1 = c.s.executeQuery("select * from subject where rollno ='"+rollno+"'");
            while (rs1.next()){
                subject1.setText(rs1.getString("subject1"));
                subject2.setText(rs1.getString("subject2"));
                subject3.setText(rs1.getString("subject3"));
                subject4.setText(rs1.getString("subject4"));
                subject5.setText(rs1.getString("subject5"));
            }
            ResultSet rs2 = c.s.executeQuery("select * from marks where rollno ='"+rollno+"'");
            while (rs2.next()){
                subject1.setText(subject1.getText() + "---------------" + rs2.getString("marks1"));
                subject2.setText(subject2.getText() + "---------------" +rs2.getString("marks2"));
                subject3.setText(subject3.getText() +  "---------------" +rs2.getString("marks3"));
                subject4.setText(subject4.getText()+ "---------------"+ rs2.getString("marks4"));
                subject5.setText(subject5.getText()+"---------------"+ rs2.getString("marks5"));
                lblsemester.setText("semester"+rs2.getString("semester"));


            }
        }catch (Exception e){
            e.printStackTrace();
        }
        // cancel button
        cancel = new JButton("Back");
        cancel.setBounds(250,500,120,25);
        cancel.setBackground(Color.BLACK);
        cancel.setForeground(Color.WHITE);
        cancel.addActionListener(this::actionPerformed);
        cancel.setFont(new Font("Tahoma",Font.BOLD,15));
        add(cancel);

        setVisible(true);
    }
    public void actionPerformed(ActionEvent e){

        setVisible(false);
    }
    public static void main(String[] args) {
        new Marks("");
    }
}
