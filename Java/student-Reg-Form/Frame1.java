import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.FileWriter;

import java.io.IOException;
import java.sql.ResultSet;
import  java.sql.*;

import org.json.simple.JSONObject;

public class Frame1 extends JFrame implements ActionListener{
    JButton cancel,print,save,SDB,FDB;
    JTextField namet,rollnumt,batcht,sectiont,gendert,countryt,Qualift,regnot;
    JCheckBox j1,j2,j3,j4;
    JTextArea addresst;

    JComboBox countryc;
    JRadioButton m1,f1;
    String gender,education,country,name,rollnum,address,batch,section,genderd,educationd;
    JSONObject jsonObject = new JSONObject();


    Frame1() {
        getContentPane().setBackground(Color.YELLOW);
        setLayout(null);


        new JFrame("Student Registeration Form");
        setTitle("Student Registeration Form");
        setBounds(350, 80, 850, 600);




        // name
        JLabel name = new JLabel("Name");
        name.setBounds(60, 0, 50, 100);
        add(name);

        namet = new JTextField();
        namet.setBounds(150, 33, 200, 25);
        add(namet);
// rollnumber
        JLabel rollnum = new JLabel("Roll Number");
        rollnum.setBounds(60, 40, 50, 100);
        add(rollnum);

        rollnumt = new JTextField();
        rollnumt.setBounds(150, 75, 200, 25);
        add(rollnumt);
//batch
        JLabel batch = new JLabel("Batch");
        batch.setBounds(60, 80, 50, 100);
        add(batch);

        batcht = new JTextField();
        batcht.setBounds(150, 115, 200, 25);
        add(batcht);

        // section

        JLabel section = new JLabel("Section");
        section.setBounds(60, 120, 50, 100);
        add(section);
        sectiont = new JTextField();
        sectiont.setBounds(150, 155, 200, 25);
        add(sectiont);


// gender
        JLabel gender = new JLabel("Gender");
        gender.setBounds(60, 160, 50, 100);
        add(gender);
        //male
        m1 = new JRadioButton("Male");
        m1.setBounds(150, 200, 100, 25);
        add(m1);
//female
        f1 = new JRadioButton("Female");
        f1.setBounds(270, 200, 85, 25);
        add(f1);
        ButtonGroup buttonGroup = new ButtonGroup();
        buttonGroup.add(m1);
        buttonGroup.add(f1);
        //Qualification
        JLabel quali = new JLabel("Qualification");
        quali.setBounds(60, 200, 50, 100);
        add(quali);

        j1 = new JCheckBox("Matric");
        j1.setBounds(150, 240, 60, 25);
        add(j1);
        j2 = new JCheckBox("Intermediate");
        j2.setBounds(250, 240, 100, 25);
        add(j2);
        j3 = new JCheckBox("Graduate");
        j3.setBounds(150, 272, 90, 25);
        add(j3);
        j4 = new JCheckBox("Post Graduate");
        j4.setBounds(250, 272, 100, 25);
        add(j4);

// address
        JLabel address = new JLabel("Address");
        address.setBounds(60, 260, 50, 100);
        add(address);

        addresst = new JTextArea();
        addresst.setBounds(150, 300, 200, 50);
        addresst.setLineWrap(true);
        add(addresst);

// country
        JLabel country = new JLabel("Country");
        country.setBounds(60, 320, 50, 100);
        add(country);

//        JTextField countryt = new JTextField();
//        countryt.setBounds(150, 340, 200, 25);
//        add(countryt);

        countryc = new JComboBox();
        countryc.addItem("Pakistan");
        countryc.addItem("India");
        countryc.addItem("Bangladesh");
        countryc.setBounds(150, 355, 200, 25);
        add(countryc);

        // regno
        JLabel regNo = new JLabel("Reg No");
        regNo.setBounds(60, 370, 50, 100);
        add(regNo);

         regnot = new JTextField();
        regnot.setBounds(150, 405, 200, 25);
       add(regnot);

// save button
        save = new JButton("Save");
        save.setBounds(60, 470, 120, 30);
        save.setBackground(Color.BLACK);
        save.setForeground(Color.WHITE);
        save.addActionListener(this::actionPerformed);
        save.setFont(new Font("Tahoma", Font.BOLD, 15));
        add(save);

// print button
        print = new JButton("Print");
        print.setBounds(185, 470, 120, 30);
        print.setBackground(Color.BLACK);
        print.setForeground(Color.WHITE);
        print.addActionListener(this);
        print.setFont(new Font("Tahoma", Font.BOLD, 15));
        add(print);

        //Cancel button
        cancel = new JButton("Cancel");
        cancel.setBounds(310, 470, 120, 30);
        cancel.setBackground(Color.BLACK);
        cancel.setForeground(Color.WHITE);
        cancel.addActionListener(this::actionPerformed);
        cancel.setFont(new Font("Tahoma", Font.BOLD, 15));
        add(cancel);


        //insert to data base button
       SDB = new JButton("Insert DB");
        SDB.setBounds(440, 470, 120, 30);
        SDB.setBackground(Color.BLACK);
        SDB.setForeground(Color.WHITE);
        SDB.addActionListener(this::actionPerformed);
        SDB.setFont(new Font("Tahoma", Font.BOLD, 15));
        add(SDB);

        //fetch to data base button
        FDB = new JButton("Fetch DB");
        FDB.setBounds(570, 470, 120, 30);
        FDB.setBackground(Color.BLACK);
        FDB.setForeground(Color.WHITE);
        FDB.addActionListener(this::actionPerformed);
        FDB.setFont(new Font("Tahoma", Font.BOLD, 15));
        add(FDB);


        setVisible(true);

    }

    public void actionPerformed(ActionEvent e) {

        if (e.getSource() == cancel) {
            setVisible(false);
        }
        else if (e.getSource() == print) {
            try {
                setVisible(false);
                Thread.sleep(2000);
                Frame2 f2 = new Frame2();
                f2.namet2.setText(namet.getText());
                f2.rollnumt2.setText(rollnumt.getText());
                f2.batcht2.setText(batcht.getText());
                f2.sectiont2.setText(sectiont.getText());

                if (m1.isSelected()) {
                    gender = m1.getText();
                    f2.gendert2.setText(gender);
                } else if (f1.isSelected()) {
                    gender = f1.getText();
                    f2.gendert2.setText(gender);
                }

                f2.addresst2.setText(addresst.getText());

                if (j1.isSelected()) {
                    education = j1.getText();
                    f2.Qualift2.setText(education);
                }

                if (j2.isSelected()) {
                    education = j2.getText();
                    f2.Qualift2.setText(education);
                }

                if (j3.isSelected()) {
                    education = j3.getText();
                    f2.Qualift2.setText(education);
                }

                if (j4.isSelected()) {
                    education = j4.getText();
                    f2.Qualift2.setText(education);
                }
//                f2.Qualift2.setText(education);
                f2.countryt2.setText(countryc.getSelectedItem().toString());

                // for not editable Information
                f2.namet2.setEditable(false);
                f2.rollnumt2.setEditable(false);
                f2.sectiont2.setEditable(false);
                f2.batcht2.setEditable(false);
                f2.gendert2.setEditable(false);
                f2.addresst2.setEditable(false);
                f2.countryt2.setEditable(false);
                f2.Qualift2.setEditable(false);

            } catch (Exception ae) {
                System.out.println(ae.getMessage());
            }
        } else if (e.getSource() == save) {

            name = namet.getText();
            batch = batcht.getText();
            rollnum = rollnumt.getText();
            section = sectiont.getText();
            address = addresst.getText();

            if (m1.isSelected()) {
                gender = m1.getText();

            } else if (f1.isSelected()) {
                gender = f1.getText();
            }


            if (j1.isSelected()) {
                education = j1.getText();
            }

            if (j2.isSelected()) {
                education = j2.getText();
            }

            if (j3.isSelected()) {
                education = j3.getText();
            }

            if (j4.isSelected()) {
                education = j4.getText();
            }

            country = countryc.getSelectedItem().toString();

            jsonObject.put("Name is ", name);
            jsonObject.put("Name is ", rollnum);
            jsonObject.put("Name is ", section);
            jsonObject.put("Name is ", batch);
            jsonObject.put("Name is ", gender);
            jsonObject.put("Name is ", education);
            jsonObject.put("Name is ", address);
            jsonObject.put("Name is ", country);
            try {
                FileWriter file = new FileWriter("E:/output.json");
                file.write(jsonObject.toJSONString());

            } catch (IOException ee) {

                ee.printStackTrace();
            }
            setVisible(false);
            System.out.println("JSON file created: " + jsonObject);
        }

        else if (e.getSource() == FDB) {
            setVisible(false);
            Frame2 f3 = new Frame2();

            try {
                Conn c =new Conn();

                ResultSet rs =c.s.executeQuery("select * from studentinform");

                while (rs.next()){
                    //f2.namet2.setText(namet.getText());
                    f3.namet2.setText(rs.getString(1));
                    f3.rollnumt2.setText(rs.getString(2));
                    f3.batcht2.setText(rs.getString(3));
                    f3.sectiont2.setText(rs.getString(4));
                    f3.gendert2.setText(rs.getString(5));
                    f3.Qualift2.setText(rs.getString(6));
                    f3.addresst2.setText(rs.getString(7));
                    f3.countryt2.setText(rs.getString(8));

                }

            }catch (Exception ae){
                ae.printStackTrace();
            }
        }
        //insert into Data base
        else if (e.getSource() == SDB) {
            String namegd = namet.getText();
            String rollnumd = rollnumt.getText();
            String batchd = batcht.getText();
            String sectiond = sectiont.getText();

            if (m1.isSelected()) {
                genderd = m1.getText();

            } else if (f1.isSelected()) {
                genderd = f1.getText();
            }

            if (j1.isSelected()) {
                educationd = j1.getText();
            }

            if (j2.isSelected()) {
                educationd = j2.getText();
            }

            if (j3.isSelected()) {
                educationd = j3.getText();
            }

            if (j4.isSelected()) {
                educationd = j4.getText();
            }
            String addressd = addresst.getText();
            String countryd = countryc.getSelectedItem().toString();
            String regnod = regnot.getText();

            try {
                String query = "insert into studentinform values('" + namegd + "','" + rollnumd + "','" + batchd + "','" + sectiond + "','" + genderd + "','" + educationd + "','" + addressd + "','" + countryd + "','" + regnod + "')";
                Conn con = new Conn();
                con.s.executeUpdate(query);

                JOptionPane.showMessageDialog(null, "student details inserted successfully !");
                setVisible(false);
            } catch (Exception ee) {
                ee.printStackTrace();
            }
        }

    }

    public static void main(String[] args) {
        new Frame1();



    }
}
