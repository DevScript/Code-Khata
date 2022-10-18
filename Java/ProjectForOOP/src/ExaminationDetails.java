import javax.swing.*;
import  java.awt.*;
import java.awt.event.*;
import java.sql.*;
import net.proteanit.sql.DbUtils;
public class ExaminationDetails extends JFrame implements ActionListener{
   JTextField search;
   JButton submit,cancel;
   JTable table;
    ExaminationDetails(){
       setSize(1000,475);
       setLocation(280,100);
        getContentPane().setBackground(Color.WHITE);
        setLayout(null);

        //heading
        JLabel heading = new JLabel("Check Result");
        heading.setBounds(80,15,400,50);
        heading.setFont(new Font("Tahoma",Font.BOLD,24));
        add(heading);
// search y rollnum
        search  = new JTextField();
        search.setBounds(80,90,200,30);
        search.setFont(new Font("Tahoma",Font.PLAIN,18));
        add(search);


        // submit button
        submit = new JButton("Result");
        submit.setBounds(300,90,120,30);
        submit.setBackground(Color.BLACK);
        submit.setForeground(Color.WHITE);
        submit.addActionListener(this::actionPerformed);
        submit.setFont(new Font("Tahoma",Font.BOLD,15));
        add(submit);

        // cancel button
        cancel = new JButton("Back");
        cancel.setBounds(440,90,120,30);
        cancel.setBackground(Color.BLACK);
        cancel.setForeground(Color.WHITE);
        cancel.addActionListener(this::actionPerformed);
        cancel.setFont(new Font("Tahoma",Font.BOLD,15));
        add(cancel);

        // table
        table = new JTable();
        table.setFont(new Font("Tahoma",Font.PLAIN,16));
        JScrollPane jsp = new JScrollPane(table);
        jsp.setBounds(0,132,1000,310);
        add(jsp);

        //hit to mysql
        try {
            Conn c = new Conn();
            ResultSet rs =c.s.executeQuery("select * from student");
            table.setModel(DbUtils.resultSetToTableModel(rs));

        }catch (Exception e){
            e.printStackTrace();
        }

        table.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                int row=table.getSelectedRow();
              search.setText( table.getModel().getValueAt(row,2).toString());
            }
        });
        setVisible(true);
    }
    public void actionPerformed(ActionEvent e){
if (e.getSource()==submit){
   setVisible(false);
    new  Marks(search.getText());
}else {
    setVisible(false);
}
    }
    public static void main(String[] args) {
        new ExaminationDetails();
    }
}
