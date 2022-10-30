import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import org.json.JSONObject;
import java.io.*;
class Registration implements ActionListener {
    JFrame frame = new JFrame("Form");
    JButton Save = new JButton("Save");
    JButton Display = new JButton("Display");
    DefaultComboBoxModel depatmentsName = new DefaultComboBoxModel<>(new String[]{"Software","Computer System","Electronics","Computer Science"});
    JLabel Name = new JLabel("Name:");
    JLabel Year = new JLabel("Year:");
    JLabel Semester =new JLabel("Semester:");
    JLabel Section = new JLabel("Section:");
    JLabel Roll_NO = new JLabel("Roll_NO:");
    JLabel Department = new JLabel("Department:");
    JTextField nameText = new JTextField();
    JTextField yearText =new JTextField();
    JTextField SemesterText = new JTextField();
    JTextField sectionText= new JTextField();
    JTextField roll_NoText = new JTextField();
    JComboBox departmentsChoice = new JComboBox<>();


    Registration(){
        departmentsChoice.setModel(depatmentsName);
        Name.setBounds(100,60,90,90);
        Year.setBounds(100,100,90,90);
        Semester.setBounds(100,140,90,90);
        Section.setBounds(100,180,90,90);
        Roll_NO.setBounds(100,220,90,90);
        Department.setBounds(100,260,90,90);
        nameText.setBounds(180,90,250,25);
        yearText.setBounds(180,130,250,25);
        SemesterText.setBounds(180,170,250,25);
        sectionText.setBounds(180,210,250,25);
        roll_NoText.setBounds(180,250,250,25);
        departmentsChoice.setBounds(180,290,250,25);
        Save.setBounds(330,340,100,50);
        Display.setBounds(200,340,100,50);
        Display.addActionListener(this);
        Save.addActionListener(this);
        frame.setLayout(null);
        frame.setSize(500,500);
        frame.setResizable(false);
        frame.getContentPane().setBackground(Color.LIGHT_GRAY);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.add(Name);
        frame.add(nameText);
        frame.add(Year);
        frame.add(yearText);
        frame.add(Semester);
        frame.add(SemesterText);
        frame.add(Section);
        frame.add(sectionText);
        frame.add(Roll_NO);
        frame.add(roll_NoText);
        frame.add(Department);
        frame.add(departmentsChoice);
        frame.add(Save);
        frame.add(Display);
        frame.setVisible(true);

    }
    @Override
    public void actionPerformed(ActionEvent e) {
        if(e.getSource()==Save){
            frame.dispose();
            try {
                FileWriter fw = new FileWriter("MYFile.json");
                JSONObject Obj = new JSONObject();
                Obj.put("Name",nameText.getText());
                Obj.put("Year",yearText.getText());
                Obj.put("Semester",SemesterText.getText());
                Obj.put("Section",sectionText.getText());
                Obj.put("Roll_No",roll_NoText.getText());
                Obj.put("Department",departmentsChoice.getSelectedItem().toString());
                fw.write(Obj.toString());
                fw.close();

            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
            JOptionPane.showMessageDialog(null,"SuccessFully Added To Json File");
        }
      
    }
}
public class GUIForm {
    public static void main(String[] args) {
      new Registration();

    }

}
