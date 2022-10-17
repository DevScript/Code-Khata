import javax.swing.*;
import java.awt.*;
import java.util.Random;
import com.toedter.calendar.JDateChooser;
import  java.awt.event.*;

public class AddTeacher extends JFrame implements ActionListener{
    JTextField namet,fnamet,rollNumt,addresst,phonet,emailt,percent,percenxiit,nict;
    JLabel labelId;
    JComboBox cource,branch;
    JButton submit,cancel;
    JDateChooser dof;
    Random ran = new Random();
    long first4=Math.abs(ran.nextLong()%9000L)+1000L;
    AddTeacher(){
        setBounds(120,10,900,600);
        setLocation(350,50);
        setBackground(Color.WHITE);
        setLayout(null);

        //heading
        JLabel heading = new JLabel("New Teacher Details");
        heading.setBounds(310,30,500,50);
        heading.setFont(new Font("serif",Font.BOLD,30));
        add(heading);


        //name label
        JLabel name = new JLabel("Name");
        name.setBounds(50,150,100,30);
        name.setFont(new Font("serif",Font.BOLD,20));
        add(name);

        namet=new JTextField();
        namet.setBounds(200,150,150,30);
        add(namet);

        // father name label
        JLabel father_name = new JLabel("Father Name");
        father_name.setBounds(400,150,200,30);
        father_name.setFont(new Font("serif",Font.BOLD,20));
        add(father_name);

        fnamet=new JTextField();
        fnamet.setBounds(600,150,150,30);
        add(fnamet);

        // roll number label
        JLabel employee_id = new JLabel("Employee Id");
        employee_id.setBounds(50,200,200,30);
        employee_id.setFont(new Font("serif",Font.BOLD,20));
        add(employee_id);

        labelId = new JLabel("001"+first4);
        labelId.setBounds(200,200,200,30);
        labelId.setFont(new Font("serif",Font.BOLD,20));
        add(labelId);

        // Date Of Birth
        JLabel DOB = new JLabel("Date Of Birth");
        DOB.setBounds(400,200,200,30);
        DOB.setFont(new Font("serif",Font.BOLD,20));
        add(DOB);

        dof = new JDateChooser();
        dof.setBounds(600,200,150,30);
        add(dof);
        //Adress label
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

        percent=new JTextField();
        percent.setBounds(600,300,150,30);
        add(percent);

        //percentage Xii
        JLabel  percenxii= new JLabel("Class Xii (%)");
        percenxii.setBounds(50,350,200,30);
        percenxii.setFont(new Font("serif",Font.BOLD,20));
        add(percenxii);

        percenxiit=new JTextField();
        percenxiit.setBounds(200,350,150,30);
        add(percenxiit);

        //NIC
        JLabel  nic= new JLabel("NIC");
        nic.setBounds(400,350,200,30);
        nic.setFont(new Font("serif",Font.BOLD,20));
        add(nic);

        nict=new JTextField();
        nict.setBounds(600,350,150,30);
        add(nict);
//Cource label
        JLabel  courcel= new JLabel("Qualification");
        courcel.setBounds(50,400,200,30);
        courcel.setFont(new Font("serif",Font.BOLD,20));
        add(courcel);

        String courcer[]={"B.Tech","BBA","BCA","BSC","MSC","B.Com","MBA","MA","BA"};
        cource= new JComboBox(courcer);
        cource.setBounds(200,400,150,30);
        cource.setBackground(Color.cyan);
        add(cource);

        //Cource Branch
        JLabel  branchl= new JLabel("Department");
        branchl.setBounds(400,400,200,30);
        branchl.setFont(new Font("serif",Font.BOLD,20));
        add(branchl);

        String branchr[]={"Computer Science","Civil","PG","Tely Communication","Software","Electronics","Mechanical","IT","Electrical"};
        branch= new JComboBox(branchr);
        branch.setBounds(600,400,150,30);
        branch.setBackground(Color.cyan);
        add(branch);

        // submit button
        submit = new JButton("Submit");
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
            String nameg =  namet.getText();
            String fatherg = fnamet.getText();
            String emploidg = labelId.getText();
            String DoB = ((JTextField)dof.getDateEditor().getUiComponent()).getText();
            String addresg = addresst.getText();
            String phoneg = phonet.getText();
            String emailg = emailt.getText();
            String x = percent.getText();
            String xii = percenxiit.getText();
            String NIC = nict.getText();
            String educationg = (String)cource.getSelectedItem();
            String departmentg = (String)branch.getSelectedItem();

            try {
                String query = "insert into teacher values('"+nameg+"','"+fatherg+"','"+emploidg+"','"+DoB+"','"+addresg+"','"+phoneg+"','"+emailg+"','"+x+"','"+xii+"','"+NIC+"','"+educationg+"','"+departmentg+"')";
                Conn con = new Conn();
                con.s.executeUpdate(query);

                JOptionPane.showMessageDialog(null,"Student details inserted Successfully");
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
        new AddTeacher();
    }
}
