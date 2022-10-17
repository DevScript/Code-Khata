import com.mysql.cj.protocol.Resultset;

import javax.swing.*;
import javax.xml.transform.Result;
import  java.awt.*;
import  java.sql.*;
import net.proteanit.sql.DbUtils;
import java.awt.event.*;
public class TeacherLeaveDetails extends JFrame implements ActionListener{
    Choice cempid;
    JButton search,print,cancel;
    JTable jtable;
    TeacherLeaveDetails(){
        getContentPane().setBackground(Color.WHITE);
        setLayout(null);
        setSize(1000,700);
        setLocation(250,20);

        // search by roll number
        JLabel heading = new JLabel("Search By Employee Id");
        heading.setBounds(20,20,150,20);
        add(heading);

      cempid= new Choice();
        cempid.setBounds(180,20,150,20);
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

        jtable = new JTable();
        try {
            Conn c = new Conn();
            ResultSet rs = c.s.executeQuery("select * from teacherleave ");
            jtable.setModel(DbUtils.resultSetToTableModel(rs));
        }catch (Exception e){
            e.printStackTrace();
        }

        JScrollPane jsp = new JScrollPane(jtable);
        jsp.setBounds(0,100,1000,700);
        add(jsp);

// search button
        search = new JButton("Search");
        search.setBounds(20,70,100,20);
        search.setBackground(Color.BLACK);
        search.setForeground(Color.WHITE);
        search.addActionListener(this::actionPerformed);
        search.setFont(new Font("Tahoma",Font.BOLD,15));
        add(search);

        //print button
        print = new JButton("Print");
        print.setBounds(140,70,100,20);
        print.setBackground(Color.BLACK);
        print.setForeground(Color.WHITE);
        print.addActionListener(this);
        print.setFont(new Font("Tahoma",Font.BOLD,15));
        add(print);



        // cancel button
        cancel = new JButton("Cancel");
        cancel.setBounds(260,70,100,20);
        cancel.setBackground(Color.BLACK);
        cancel.setForeground(Color.WHITE);
        cancel.addActionListener(this);
        cancel.setFont(new Font("Tahoma",Font.BOLD,15));
        add(cancel);







        setVisible(true);
    }

    public void actionPerformed(ActionEvent ae){
        if (ae.getSource()==cancel){
            setVisible(false);
        }
        else if (ae.getSource()==search){

            String query = "select * from teacherleave where empid = '"+cempid.getSelectedItem()+"'";
            try{
                Conn c = new Conn();
                ResultSet rs = c.s.executeQuery(query);
                jtable.setModel(DbUtils.resultSetToTableModel(rs));
            }catch (Exception e){
                e.printStackTrace();
            }
        }

        else if (ae.getSource()==print) {
            try{
                jtable.print();
            }catch (Exception ee){
                ee.printStackTrace();
            }
        }

    }
    public static void main(String[] args) {
        new TeacherLeaveDetails();
    }

}

