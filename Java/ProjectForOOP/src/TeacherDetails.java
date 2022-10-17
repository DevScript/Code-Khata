
import com.mysql.cj.protocol.Resultset;

import javax.swing.*;
import javax.xml.transform.Result;
import  java.awt.*;
import  java.sql.*;
import net.proteanit.sql.DbUtils;
import java.awt.event.*;
public class TeacherDetails extends JFrame implements ActionListener{
    Choice cempId;
    JButton search,print,update,add,cancel;
    JTable jtable;
    TeacherDetails(){
        getContentPane().setBackground(Color.WHITE);
        setLayout(null);
        setSize(1000,700);
        setLocation(250,20);

        // search by roll number
        JLabel heading = new JLabel("Search By Employee Id");
        heading.setBounds(20,20,150,20);
        add(heading);

        cempId= new Choice();
        cempId.setBounds(180,20,150,20);
        add(cempId);

        //take the roll number from Mysql
        try {
            Conn c = new Conn();
            ResultSet rs = c.s.executeQuery("select * from teacher ");
            while (rs.next()){
                cempId.add(rs.getString("emploidg"));
            }
        }catch (Exception e){
            e.printStackTrace();
        }

        jtable = new JTable();
        try {
            Conn c = new Conn();
            ResultSet rs = c.s.executeQuery("select * from teacher ");
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

        // add button
        add = new JButton("Add");
        add.setBounds(260,70,100,20);
        add.setBackground(Color.BLACK);
        add.setForeground(Color.WHITE);
        add.addActionListener(this);
        add.setFont(new Font("Tahoma",Font.BOLD,15));
        add(add);

        // update button
        update = new JButton("Update");
        update.setBounds(380,70,100,20);
        update.setBackground(Color.BLACK);
        update.setForeground(Color.WHITE);
        update.addActionListener(this);
        update.setFont(new Font("Tahoma",Font.BOLD,15));
        add(update);

        // cancel button
        cancel = new JButton("Cancel");
        cancel.setBounds(500,70,100,20);
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

            String query = "select * from teacher where emploidg = '"+cempId.getSelectedItem()+"'";
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
        else if (ae.getSource()==add){

            setVisible(false);
            new AddTeacher();
        }

        else if (ae.getSource()==update) {
            setVisible(false);
            new UpdateTeacher();
        }
    }
    public static void main(String[] args) {
        new TeacherDetails();
    }

}

