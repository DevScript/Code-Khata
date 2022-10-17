import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class Project extends JFrame implements ActionListener{
    Project(){
        setSize(1540,850);
        ImageIcon il = new ImageIcon(ClassLoader.getSystemResource("icons/0.jpg"));
        Image i2 =il.getImage().getScaledInstance(1366,768,Image.SCALE_DEFAULT);
        ImageIcon  i3 = new ImageIcon(i2);
        JLabel image = new JLabel(i3);

        JMenuBar mb = new JMenuBar();
// New information
        JMenu newInformation = new JMenu("New Information");
        newInformation.setForeground(Color.BLUE);
        mb.add(newInformation);
        JMenuItem facultyInfo = new JMenuItem("New Faculty Information");
        facultyInfo.setBackground(Color.WHITE);
        facultyInfo.addActionListener(this::actionPerformed);
        newInformation.add(facultyInfo);

        JMenuItem student_informationInfo = new JMenuItem("New Student Information");
        student_informationInfo.setBackground(Color.WHITE);
        student_informationInfo.addActionListener(this::actionPerformed);
        newInformation.add(student_informationInfo);

        // details
        JMenu details = new JMenu("View Details");
        details.setForeground(Color.RED);
        mb.add(details);

        JMenuItem facultydetails = new JMenuItem("View Faculty Details");
        facultydetails.setBackground(Color.WHITE);
        facultydetails.addActionListener(this::actionPerformed);
        details.add(facultydetails);

        JMenuItem students_details = new JMenuItem("View Students Details");
        students_details.setBackground(Color.WHITE);
        students_details.addActionListener(this::actionPerformed);
        details.add(students_details);


        // Leave
        JMenu leave = new JMenu("Apply Leave");
        leave.setForeground(Color.BLUE);
        mb.add(leave);

        JMenuItem facultyleave = new JMenuItem("Faculty Leave");
        facultyleave.setBackground(Color.WHITE);
        facultyleave.addActionListener(this::actionPerformed);
        leave.add(facultyleave);

        JMenuItem students_leave = new JMenuItem("Student Leave");
        students_leave.setBackground(Color.WHITE);
      students_leave.addActionListener(this::actionPerformed);
        leave.add(students_leave);
        // Leave Details
        JMenu leave_details = new JMenu("Leave Details");
        leave_details.setForeground(Color.RED);
        mb.add(leave_details);

        JMenuItem facultyleavedetails = new JMenuItem("Faculty Leave Details");
        facultyleavedetails.addActionListener(this::actionPerformed);
        leave_details.add(facultyleavedetails);

        JMenuItem students_leavedetails = new JMenuItem("Student Leave Details");
        students_leavedetails.setBackground(Color.WHITE);
        students_leavedetails.addActionListener(this::actionPerformed);
        leave_details.add(students_leavedetails);

        // Exam
        JMenu exam = new JMenu("Examination");
        exam.setForeground(Color.BLUE);
        mb.add(exam);

        JMenuItem examDetails = new JMenuItem("Examination Results");
        examDetails.setBackground(Color.WHITE);
        examDetails.addActionListener(this::actionPerformed);
        exam.add(examDetails);

        JMenuItem   enterMarks= new JMenuItem("Enter Marks");
      enterMarks.setBackground(Color.WHITE);
        enterMarks.addActionListener(this::actionPerformed);
        exam.add(enterMarks);

        // UpdateInfo
        JMenu updateInfo = new JMenu("Update Details");
        updateInfo.setForeground(Color.RED);
        mb.add(updateInfo);

        JMenuItem updatefacultyInfo = new JMenuItem("Update Faculty Details");
        updatefacultyInfo.setBackground(Color.WHITE);
        updatefacultyInfo.addActionListener(this::actionPerformed);

        updateInfo.add(updatefacultyInfo);

        JMenuItem   updateStudentInfo= new JMenuItem("Update Students Details");
        updateStudentInfo.setBackground(Color.WHITE);
        updateStudentInfo.addActionListener(this::actionPerformed);
       updateInfo.add(updateStudentInfo);

        // fee
        JMenu fee_details = new JMenu("Fee Details");
        fee_details.setForeground(Color.BLUE);
        mb.add(fee_details);

        JMenuItem feestructure = new JMenuItem("Fee Structure");
        feestructure.setBackground(Color.WHITE);
       feestructure.addActionListener(this::actionPerformed);
      fee_details.add(feestructure);

//        JMenuItem   feeForm= new JMenuItem("Student Fee Form");
//        feeForm.setBackground(Color.WHITE);
//        fee_details.add(feeForm);

        // Utility
        JMenu utility = new JMenu("Utility");
        utility.setForeground(Color.RED);
        mb.add(utility);

        JMenuItem notePad = new JMenuItem("Notepad");
        notePad.setBackground(Color.WHITE);
        notePad.addActionListener(this);
       utility.add(notePad);

        JMenuItem   calculator= new JMenuItem("Calculator");
        calculator.setBackground(Color.WHITE);
        calculator.addActionListener(this);
       utility.add(calculator);

        // about
        JMenu about= new JMenu("About");
        about.setForeground(Color.BLUE);

        mb.add(about);

        JMenuItem ab = new JMenuItem("about");
        ab.setBackground(Color.WHITE);
        ab.addActionListener(this);
        about.add(ab);


        // exit
        JMenu exit = new JMenu("Exit");
        exit.setForeground(Color.RED);
        mb.add(exit);

        JMenuItem ex = new JMenuItem("exit");
        ex.setBackground(Color.WHITE);
        ex.addActionListener(this);
       exit.add(ex);






        setJMenuBar(mb);

        add(image);
        setVisible(true);

    }
    public void actionPerformed(ActionEvent ae) {
        String msg = ae.getActionCommand();

        if (msg.equals("Exit")) {
            setVisible(false);
        }
        else if (msg.equals("Calculator")){
            try {
                Runtime.getRuntime().exec("calc.exe");
            }
            catch (Exception e){

            }
        }
        else if (msg.equals("Notepad")){
            try {
                Runtime.getRuntime().exec("notepad.exe");
            }
            catch (Exception e){

            }
        }else if (msg.equals("New Faculty Information")){
            new AddTeacher();
        }
        else if (msg.equals("New Student Information")){
            new AddStudent();
        }
        else if (msg.equals("View Faculty Details")){
            new TeacherDetails();
        }
        else if (msg.equals("View Students Details")){
            new StudentDetails();
        }
        else if (msg.equals("Faculty Leave")){
            new TeacherLeave();
        }
        else if (msg.equals("Student Leave")){
            new StudentLeave();
        }
        else if (msg.equals("Faculty Leave Details")){
            new TeacherLeaveDetails();
        }
        else if (msg.equals("Student Leave Details")){
            new StudentLeaveDetails();
        }
        else if (msg.equals("Update Faculty Details")){
            new UpdateTeacher();
        }
        else if (msg.equals("Update Students Details")){
            new UpdateStudents();
        }
        else if (msg.equals("Enter Marks")){
            new EnterMarks();
        }
        else if (msg.equals("Examination Results")){
            new ExaminationDetails();
        }
        else if (msg.equals("Fee Structure")){
            new FeeStructure();
        }
        else if (msg.equals("about")){
            new About();
        }
        else {
            setVisible(false);
        }
}



    public static void main(String[] args) {
        new Project();
    }
}
