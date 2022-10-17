
import javax.swing.*;
import java.awt.*;
import java.sql.ResultSet;


import  java.awt.event.*;


public class UpdateTeacher extends JFrame implements ActionListener{
    JTextField addresst,phonet,emailt,tfcource,tfbranch;
    JLabel labelempid;
    JButton submit,cancel;
    Choice cempid;


    UpdateTeacher(){
        setBounds(120,10,900,600);
        setLocation(350,50);
        setBackground(Color.WHITE);
        setLayout(null);

        //heading
        JLabel heading = new JLabel("Update Teacher Details");
        heading.setBounds(50,10,500,50);
        heading.setFont(new Font("Tahoma",Font.ITALIC,35));
        add(heading);


        // search by roll number
        JLabel lblrollnum = new JLabel("Select By Employee Id");
        lblrollnum.setBounds(50,100,200,20);
        lblrollnum.setFont(new Font("serif",Font.PLAIN,20));
        add(lblrollnum);

        cempid= new Choice();
        cempid.setBounds(250,100,200,20);
        add(cempid);

        //take the roll number from Mysql
        try {
            Conn c = new Conn();
            ResultSet rs = c.s.executeQuery("select * from teacher");
            while (rs.next()){
                cempid.add(rs.getString("emploidg"));
            }
        }catch (Exception e){
            e.printStackTrace();
        }



        //name label
        JLabel name = new JLabel("Name");
        name.setBounds(50,150,100,30);
        name.setFont(new Font("serif",Font.BOLD,20));
        add(name);

        JLabel labelname =new JLabel();
        labelname.setBounds(200,150,150,30);
        labelname.setFont(new Font("serif",Font.PLAIN,18));
        add(labelname);

        // father name label
        JLabel father_name = new JLabel("Father Name");
        father_name.setBounds(400,150,200,30);
        father_name.setFont(new Font("serif",Font.BOLD,20));
        add(father_name);

        JLabel labelfather =new JLabel();
        labelfather.setBounds(600,150,150,30);
        labelfather.setFont(new Font("serif",Font.PLAIN,18));
        add(labelfather);

        // roll number label
        JLabel rollNum = new JLabel("Employee Id");
        rollNum.setBounds(50,200,200,30);
        rollNum.setFont(new Font("serif",Font.BOLD,20));
        add(rollNum);

          labelempid = new JLabel();
        labelempid.setBounds(200,200,200,30);
        labelempid.setFont(new Font("serif",Font.PLAIN,18));
        add(labelempid);

        // Date Of Birth
        JLabel DOB = new JLabel("Date Of Birth");
        DOB.setBounds(400,200,200,30);
        DOB.setFont(new Font("serif",Font.BOLD,20));
        add(DOB);

        JLabel labeldof = new JLabel();
        labeldof.setBounds(600,200,150,30);
        labeldof.setFont(new Font("serif",Font.PLAIN,18));
        add(labeldof);
        //Address label
        JLabel address = new JLabel("Address");
        address.setBounds(50,250,200,30);
        address.setFont(new Font("serif",Font.BOLD,20));
        add(address);

        addresst=new JTextField();
        addresst.setBounds(200,250,150,30);
        add(addresst);
//Phone Number
        JLabel phoneNum = new JLabel("Phone Number");
        phoneNum.setBounds(400,250,200,30);
        phoneNum.setFont(new Font("serif",Font.BOLD,20));
        add(phoneNum);

        phonet=new JTextField();
        phonet.setBounds(600,250,150,30);
        add(phonet);

        //Adress Email
        JLabel email_id = new JLabel("Email Id");
        email_id.setBounds(50,300,200,30);
        email_id.setFont(new Font("serif",Font.BOLD,20));
        add(email_id);

        emailt=new JTextField();
        emailt.setBounds(200,300,150,30);
        add(emailt);
//percentage
        JLabel percen= new JLabel("Class X (%)");
        percen.setBounds(400,300,200,30);
        percen.setFont(new Font("serif",Font.BOLD,20));
        add(percen);

        JLabel xpercent=new JLabel();
        xpercent.setBounds(600,300,150,30);
        xpercent.setFont(new Font("serif",Font.PLAIN,18));
        add(xpercent);

        //percentage Xii
        JLabel  percenxii= new JLabel("Class Xii (%)");
        percenxii.setBounds(50,350,200,30);
        percenxii.setFont(new Font("serif",Font.BOLD,20));
        add(percenxii);

        JLabel xiipercen = new JLabel();
        xiipercen.setBounds(200,350,150,30);
        xiipercen.setFont(new Font("serif",Font.PLAIN,18));
        add(xiipercen);

        //NIC
        JLabel  nic= new JLabel("NIC");
        nic.setBounds(400,350,200,30);
        nic.setFont(new Font("serif",Font.BOLD,20));
        add(nic);

        JLabel labelnic = new JLabel();
        labelnic.setBounds(600,350,150,30);
        labelnic.setFont(new Font("serif",Font.PLAIN,18));
        add(labelnic);
//Cource label
        JLabel  courcel= new JLabel("Education");
        courcel.setBounds(50,400,200,30);
        courcel.setFont(new Font("serif",Font.BOLD,20));
        add(courcel);


        tfcource= new JTextField();
        tfcource.setBounds(200,400,150,30);
        add(tfcource);

        //Cource Branch
        JLabel  branchl= new JLabel("Department");
        branchl.setBounds(400,400,200,30);
        branchl.setFont(new Font("serif",Font.BOLD,20));
        add(branchl);


        tfbranch= new JTextField();
        tfbranch.setBounds(600,400,150,30);
        add(tfbranch);

        try {
            Conn c = new  Conn();
            String query = "select * from teacher where emploidg='"+cempid.getSelectedItem()+"'";
            ResultSet rs = c.s.executeQuery(query);
            while (rs.next()){
                labelname.setText(rs.getString("nameg"));
                labelfather.setText(rs.getString("fatherg"));
                labeldof.setText(rs.getString("DoB"));
                addresst.setText(rs.getString("addresg"));
                phonet.setText(rs.getString("phone"));
                emailt.setText(rs.getString("emailg"));
                xpercent.setText(rs.getString("x"));
                xiipercen.setText(rs.getString("xii"));
                labelnic.setText(rs.getString("NIC"));
                labelempid.setText(rs.getString("emploidg"));
                tfcource.setText(rs.getString("educationg"));
                tfbranch.setText(rs.getString("departmentg"));


            }
        }catch (Exception c){
            c.printStackTrace();
        }
        cempid.addItemListener(new ItemListener() {
            @Override
            public void itemStateChanged(ItemEvent e) {
                try {
                    Conn c = new  Conn();
                    String query = "select * from teacher where emploidg='"+cempid.getSelectedItem()+"'";
                    ResultSet rs = c.s.executeQuery(query);
                    while (rs.next()){
                        labelname.setText(rs.getString("nameg"));
                        labelfather.setText(rs.getString("fatherg"));
                        labelempid.setText(rs.getString("emploidg"));

                        labeldof.setText(rs.getString("DoB"));
                        addresst.setText(rs.getString("addresg"));
                        phonet.setText(rs.getString("phoneg"));
                        emailt.setText(rs.getString("emailg"));
                        xpercent.setText(rs.getString("x"));
                        xiipercen.setText(rs.getString("xii"));
                        labelnic.setText(rs.getString("NIC"));
                        tfcource.setText(rs.getString("educationg"));
                        tfbranch.setText(rs.getString("departmentg"));


                    }
                }catch (Exception c){
                    c.printStackTrace();
                }
            }
        });
        // submit button
        submit = new JButton("Update");
        submit.setBounds(250,495,120,30);
        submit.setBackground(Color.BLACK);
        submit.setForeground(Color.WHITE);
        submit.addActionListener(this::actionPerformed);
        submit.setFont(new Font("Tahoma",Font.BOLD,15));
        add(submit);

        // cancel button
        cancel = new JButton("Cancel");
        cancel.setBounds(450,495,120,30);
        cancel.setBackground(Color.BLACK);
        cancel.setForeground(Color.WHITE);
        cancel.addActionListener(this::actionPerformed);
        cancel.setFont(new Font("Tahoma",Font.BOLD,15));
        add(cancel);








        setVisible(true);
    }
    public void actionPerformed(ActionEvent ae){
        if (ae.getSource()==submit){

            String emploidg = labelempid.getText();
            String addresg = addresst.getText();
            String phoneg = phonet.getText();
            String emailg = emailt.getText();
            String educationg = tfcource.getText();
            String departmentg = tfbranch.getText();

            try {
                String query = "update teacher set addresg='"+addresg+"',phoneg='"+phoneg+"',emailg='"+emailg+"',educationg='"+educationg+"',departmentg='"+departmentg+"'where emploidg='"+emploidg+"'";
                Conn con = new Conn();
                con.s.executeUpdate(query);

                JOptionPane.showMessageDialog(null,"teacher details updated Successfully");
                setVisible(false);
            }
            catch (Exception e){
                e.printStackTrace();
            }

        }else{
            setVisible(false);
        }
    }
    public static void main(String[] args) {
        new UpdateTeacher();
    }
}
