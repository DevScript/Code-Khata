
import com.toedter.calendar.JDateChooser;

import javax.swing.*;
import  java.awt.*;
import  java.awt.event.*;
import java.sql.ResultSet;

public class TeacherLeave extends JFrame implements ActionListener{

    Choice cempid,ctime;
    JDateChooser LDate;
    JButton submit,cancel;
    TeacherLeave(){
        setSize(500,550);
        setLocation(530,100);
        setLayout(null);

        getContentPane().setBackground(Color.WHITE);

        //heading
        JLabel heading = new JLabel("Apply Leave (Teachers)");
        heading.setBounds(40,50,300,30);
        heading.setFont(new Font("serif",Font.BOLD,25));
        add(heading);

        // label of roll num
        JLabel lblrollNUM = new JLabel("Search By Employee Id");
        lblrollNUM.setBounds(60,100,200,20);
        lblrollNUM.setFont(new Font("serif",Font.PLAIN,18));
        add(lblrollNUM);
// box of roll num
        cempid= new Choice();
        cempid.setBounds(60,130,200,20);
        add(cempid);

        //take the roll number from Mysql
        try {
            Conn c = new Conn();
            ResultSet rs = c.s.executeQuery("select * from teacher ");
            while (rs.next()){
             cempid.add(rs.getString("emploidg"));
            }
        }catch (Exception e){
            e.printStackTrace();
        }

        // label of roll num
        JLabel lblDate= new JLabel("Date");
        lblDate.setBounds(60,180,200,20);
        lblDate.setFont(new Font("serif",Font.PLAIN,18));
        add(lblDate);
//Calender
        LDate = new JDateChooser();
        LDate.setBounds(60,210,200,25);
        add(LDate);


        // leave time
        JLabel lblTime = new JLabel("Time Duration");
        lblTime.setBounds(60,260,200,20);
        lblTime.setFont(new Font("serif",Font.PLAIN,18));
        add(lblTime);
// box of roll num
        ctime= new Choice();
        ctime.setBounds(60,290,200,20);
        ctime.add("Full Day");
        ctime.add("Half Day");
        add(ctime);

        // submit button
        submit = new JButton("Submit");
        submit.setBounds(60,350,100,25);
        submit.setBackground(Color.BLACK);
        submit.setForeground(Color.WHITE);
        submit.addActionListener(this::actionPerformed);
        submit.setFont(new Font("Tahoma",Font.BOLD,15));
        add(submit);

        // cancel button
        cancel = new JButton("Cancel");
        cancel.setBounds(200,350,100,25);
        cancel.setBackground(Color.BLACK);
        cancel.setForeground(Color.WHITE);
        cancel.addActionListener(this::actionPerformed);
        cancel.setFont(new Font("Tahoma",Font.BOLD,15));
        add(cancel);



        setVisible(true);
    }
    public void actionPerformed(ActionEvent e){
        if (e.getSource()==submit){
            String empid = cempid.getSelectedItem();
            String date =((JTextField) LDate.getDateEditor().getUiComponent()).getText();
            String duration= ctime.getSelectedItem();

            String query = "insert into teacherleave values('"+empid+"','"+date+"','"+duration+"')";

            try {
                Conn conn = new Conn();
                conn.s.executeUpdate(query);

                JOptionPane.showMessageDialog(null,"Leave Confirmed");
                setVisible(false);
            }catch (Exception f){
                f.printStackTrace();
            }
        }else {
            setVisible(false);
        }

    }
    public static void main(String[] args) {

        new TeacherLeave();
    }
}
