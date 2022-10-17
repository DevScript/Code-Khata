import javax.swing.*;
import  java.awt.*;
import java.sql.*;
import java.awt.event.*;

public class EnterMarks extends JFrame implements ActionListener{
    Choice crollno;
    JComboBox cbsemester;
    JTextField tsubject1,tsubject2,tsubject3,tsubject4,tsubject5,tmarks1,tmarks2,tmarks3,tmarks4,tmarks5;
    JButton submit,cancel;
    EnterMarks(){
        getContentPane().setBackground(Color.WHITE);
        setLayout(null);
        setSize(1000,500);
        setLocation(260,120);
// image
        ImageIcon il = new ImageIcon(ClassLoader.getSystemResource("icons/exam.jpg"));
        Image i2 =il.getImage().getScaledInstance(400,300,Image.SCALE_DEFAULT);
        ImageIcon  i3 = new ImageIcon(i2);
        JLabel image = new JLabel(i3);
        image.setBounds(500,40,400,300);
        add(image);

        //heading
        JLabel heading = new JLabel("Enter Marks Of Students");
        heading.setBounds(50,0,500,50);
        heading.setFont(new Font("Tahoma",Font.BOLD,20));
        add(heading);


        // search by roll number
        JLabel lblrollnum = new JLabel("Select By Roll Number");
        lblrollnum.setBounds(50,70,150,20);
        add(lblrollnum);

        crollno= new Choice();
        crollno.setBounds(200,70,150,20);
        add(crollno);

        //take the roll number from Mysql
        try {
            Conn c = new Conn();
            ResultSet rs = c.s.executeQuery("select * from student ");
            while (rs.next()){
                crollno.add(rs.getString("rollNumG"));
            }
        }catch (Exception e){
            e.printStackTrace();
        }

        // semester label
        JLabel lblsemester = new JLabel("Select Semester");
        lblsemester.setBounds(50,110,150,20);
        add(lblsemester);
//comboBox
        String semester[]={"1st semester","2nd semester","3rd semester","4th semester","5th semester","6th semester","7th semester","8th semester"};

        cbsemester = new JComboBox(semester);
        cbsemester.setBounds(200,110,150,20);
        cbsemester.setBackground(Color.WHITE);
        add(cbsemester);

        // heading label
        JLabel lblentersub = new JLabel("Enter Subject");
        lblentersub.setBounds(100,150,200,40);
        add(lblentersub);


        // semester label
        JLabel lblentermarks = new JLabel("Enter Marks");
        lblentermarks.setBounds(320,150,200,40);
        add(lblentermarks);

        tsubject1=new JTextField();
tsubject1.setBounds(50,200,200,20);
add(tsubject1);

        tsubject2=new JTextField();
        tsubject2.setBounds(50,230,200,20);
        add(tsubject2);

        tsubject3=new JTextField();
        tsubject3.setBounds(50,260,200,20);
        add(tsubject3);

        tsubject4=new JTextField();
        tsubject4.setBounds(50,290,200,20);
        add(tsubject4);

        tsubject5=new JTextField();
        tsubject5.setBounds(50,320,200,20);
        add(tsubject5);
        // marks text field
        tmarks1=new JTextField();
        tmarks1.setBounds(250,200,200,20);
        add(tmarks1);

        tmarks2=new JTextField();
        tmarks2.setBounds(250,230,200,20);
        add(tmarks2);

        tmarks3=new JTextField();
        tmarks3.setBounds(250,260,200,20);
        add(tmarks3);

        tmarks4=new JTextField();
        tmarks4.setBounds(250,290,200,20);
        add(tmarks4);

        tmarks5=new JTextField();
        tmarks5.setBounds(250,320,200,20);
        add(tmarks5);

        // submit button
        submit = new JButton("Submit");
        submit.setBounds(70,360,150,25);
        submit.setBackground(Color.BLACK);
        submit.setForeground(Color.WHITE);
        submit.addActionListener(this::actionPerformed);
        submit.setFont(new Font("Tahoma",Font.BOLD,15));
        add(submit);

        // cancel button
        cancel = new JButton("Back");
        cancel.setBounds(280,360,150,25);
        cancel.setBackground(Color.BLACK);
        cancel.setForeground(Color.WHITE);
        cancel.addActionListener(this::actionPerformed);
        cancel.setFont(new Font("Tahoma",Font.BOLD,15));
        add(cancel);





        setVisible(true);
    }
    public void actionPerformed(ActionEvent e){
        if (e.getSource()==submit){
try {
   Conn c = new Conn();
   String query1 = "insert into subject values('"+crollno.getSelectedItem()+"','"+cbsemester.getSelectedItem()+"','"+tsubject1.getText()+"','"+tsubject2.getText()+"','"+tsubject3.getText()+"','"+tsubject4.getText()+"','"+tsubject5.getText()+"')";

    String query2 = "insert into marks values('"+crollno.getSelectedItem()+"','"+cbsemester.getSelectedItem()+"','"+tmarks1.getText()+"','"+tmarks2.getText()+"','"+tmarks3.getText()+"','"+tmarks4.getText()+"','"+tmarks5.getText()+"')";
c.s.executeUpdate(query1);
c.s.executeUpdate(query2);

JOptionPane.showMessageDialog(null, "Marks Inserted Sucessfully");
setVisible(false);
}catch (Exception ee){
    ee.getStackTrace();
}
        }else {
            setVisible(false);
        }
    }
    public static void main(String[] args) {
        new EnterMarks();
    }
}
