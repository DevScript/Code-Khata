import javax.swing.BorderFactory;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JInternalFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

import java.awt.BorderLayout;
import java.awt.GridLayout;

public class buttonGUI implements ActionListener{
    private int count = 0;
    private JLabel label;
    private JFrame frame;
    private JButton button;

    public buttonGUI(){
        frame = new JFrame();
        button = new JButton("Click me");
        button.addActionListener(this);

        label = new JLabel("Number of clicks: 0");

        JPanel panel = new JPanel();
        panel.setBorder(BorderFactory.createEmptyBorder(30, 30, 10, 30));
        panel.setLayout(new GridLayout(0, 1));
        panel.add(button);
        panel.add(label);

        frame.add(panel, BorderLayout.CENTER);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setTitle("Our GUI");
        frame.pack();
        frame.setVisible(true);

    }

    public static void main(String[] args){
        new buttonGUI();
    }

    @Override

    public void actionPerformed(ActionEvent e){
        count++;
        label.setText("Number of clicks: " + count);

    }
}