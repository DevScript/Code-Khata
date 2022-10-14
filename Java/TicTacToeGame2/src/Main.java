import java.awt.BorderLayout;
import java.awt.FlowLayout;
import java.awt.GridLayout;
import java.awt.Toolkit;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.SwingConstants;

public class Main extends JFrame implements ActionListener{

    static boolean Check=true;
    JButton buttun1,button2,button3,button4,button5,button6,button7,button8,button9,Reset,Forfit;
    JLabel Winner,Turn;

   Main() {

        //frame
        setTitle("TIC TAC TOE");

        setSize(600,600);
        setLayout(new BorderLayout());
        setResizable(false);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setDefaultLookAndFeelDecorated(false);
        setLocationRelativeTo(null);

        //Panel1
        JPanel p1=new JPanel();
        p1.setLayout(new BorderLayout());

        JLabel l1=new JLabel("Welcome to Game ");
        JLabel l2=new JLabel("  Player 1 > X");
        JLabel l3=new JLabel("Player 2 > O  ");
        Turn = new JLabel("Player 1 turn");

        p1.add(l1,BorderLayout.NORTH);
        l1.setHorizontalAlignment(SwingConstants.CENTER);
        p1.add(l2,BorderLayout.WEST);
        p1.add(l3,BorderLayout.EAST);
        p1.add(Turn,BorderLayout.CENTER);
        Turn.setHorizontalAlignment(SwingConstants.CENTER);

        add(p1,BorderLayout.NORTH);

        //Panel2
        JPanel p2=new JPanel();
        p2.setLayout(new GridLayout(3,3,6,6));

        buttun1=new JButton();
        buttun1.addActionListener(this);
        button2=new JButton();
        button2.addActionListener(this);
        button3=new JButton();
        button3.addActionListener(this);
        button4=new JButton();
        button4.addActionListener(this);
        button5=new JButton();
        button5.addActionListener(this);
        button6=new JButton();
        button6.addActionListener(this);
        button7=new JButton();
        button7.addActionListener(this);
        button8=new JButton();
        button8.addActionListener(this);
        button9=new JButton();
        button9.addActionListener(this);

        p2.add(buttun1); p2.add(button2); p2.add(button3);
        p2.add(button4); p2.add(button5); p2.add(button6);
        p2.add(button7); p2.add(button8); p2.add(button9);

        add(p2,BorderLayout.CENTER);

        //Panel3
        JPanel p3=new JPanel();
        p3.setLayout(new FlowLayout());

        Forfit = new JButton("FORFIT");
        Forfit.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if(Check) {
                    Winner.setText("Player 2 Wins");
                    Reset.setEnabled(true);
                }
                else {
                    Winner.setText("Player 1 Wins");
                    Reset.setEnabled(true);
                }
                Forfit.setEnabled(false);
            }
        });
        Reset = new JButton("RESET");
        Reset.setEnabled(false);
        Reset.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                buttun1.setText(""); buttun1.setEnabled(true);
                button2.setText(""); button2.setEnabled(true);
                button3.setText(""); button3.setEnabled(true);
                button4.setText(""); button4.setEnabled(true);
                button5.setText(""); button5.setEnabled(true);
                button6.setText(""); button6.setEnabled(true);
                button7.setText(""); button7.setEnabled(true);
                button8.setText(""); button8.setEnabled(true);
                button9.setText(""); button9.setEnabled(true);
                Winner.setText("");
                Turn.setText("Player 1 turn");
                Check=true;
                Reset.setEnabled(false);
                Forfit.setEnabled(true);
            }});
        Winner = new JLabel();

        p3.add(Forfit); p3.add(Reset); p3.add(Winner);

        add(p3,BorderLayout.SOUTH);

        //frame
        setVisible(true);
    }
    public static void main(String[] args) {
        new Main();
    }

    public void Win() {
        if((buttun1.getText()=="X" && button2.getText()=="X" && button3.getText()=="X")||
                (button4.getText()=="X" && button5.getText()=="X" && button6.getText()=="X")||
                (button7.getText()=="X" && button8.getText()=="X" && button9.getText()=="X")||
                (buttun1.getText()=="X" && button4.getText()=="X" && button7.getText()=="X")||
                (button2.getText()=="X" && button5.getText()=="X" && button8.getText()=="X")||
                (button3.getText()=="X" && button6.getText()=="X" && button9.getText()=="X")||
                (buttun1.getText()=="X" && button5.getText()=="X" && button9.getText()=="X")||
                (button3.getText()=="X" && button5.getText()=="X" && button7.getText()=="X")) {
            Winner.setText("PLAYER 1 WINS");
            Reset.setEnabled(true);
            Forfit.setEnabled(false);
        }
        else if((buttun1.getText()=="O" && button2.getText()=="O" && button3.getText()=="O")||
                (button4.getText()=="O" && button5.getText()=="O" && button6.getText()=="O")||
                (button7.getText()=="O" && button8.getText()=="O" && button9.getText()=="O")||
                (buttun1.getText()=="O" && button4.getText()=="O" && button7.getText()=="O")||
                (button2.getText()=="O" && button5.getText()=="O" && button8.getText()=="O")||
                (button3.getText()=="O" && button6.getText()=="O" && button9.getText()=="O")||
                (buttun1.getText()=="O" && button5.getText()=="O" && button9.getText()=="O")||
                (button3.getText()=="O" && button5.getText()=="O" && button7.getText()=="O")) {
            Winner.setText("PLAYER 2 WINS");
            Reset.setEnabled(true);
            Forfit.setEnabled(false);
        }
        else if((!buttun1.isEnabled() && !button2.isEnabled() && !button3.isEnabled() &&
                !button4.isEnabled() && !button5.isEnabled() && !button6.isEnabled() &&
                !button7.isEnabled() && !button8.isEnabled() && !button9.isEnabled())) {
            Winner.setText("GAME DRAW");
            Reset.setEnabled(true);
            Forfit.setEnabled(false);
        }

    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if(Check) {
            ((JButton) e.getSource()).setText("X");
            ((JButton) e.getSource()).setEnabled(false);
            Turn.setText("Player 2 turn");
            Check=false;
        }
        else {
            ((JButton) e.getSource()).setText("O");
            ((JButton) e.getSource()).setEnabled(false);
            Turn.setText("Player 1 turn");
            Check=true;
        }
        Win();
    }
}
