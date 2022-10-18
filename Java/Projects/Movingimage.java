import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

class Panel extends JPanel implements ActionListener{
    final int PANEL_WIDTH=300;
    final int PANEL_HEIGHT=280;
    Image rocket;
    Image background;
    Timer timer;
    int xVelocity=2;
    int yVelocity=1;
    int x=0;
    int y=0;

    Panel(){
      this.setPreferredSize(new Dimension(PANEL_WIDTH,PANEL_HEIGHT));
      this.setBackground(Color.BLACK);
      rocket= new ImageIcon("rocket2.png").getImage();
      background= new ImageIcon("space.jpg").getImage();
      timer= new Timer(10,this);
      timer.start();
    }

    public void paint(Graphics g){
        super.paint(g);
        Graphics2D g2D= (Graphics2D) g;
        g2D.drawImage(background,0,0,null);
        g2D.drawImage(rocket,x,y,null);
    }
    @Override
    public void actionPerformed(ActionEvent e) {
        if(x>=PANEL_WIDTH-rocket.getWidth(null)||x<0){
            xVelocity= xVelocity*-1;
        }
        if(y>=PANEL_HEIGHT-rocket.getHeight(null)||y<0){
            yVelocity= yVelocity*-1;
        }
        x=x+xVelocity;
        y= y+yVelocity;
        repaint();
    }
}
class MyFrame extends JFrame{
    Panel panel=  new Panel();
    MyFrame(){
    this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    this.add(panel);
    this.pack();
    this.setVisible(true);
    }
}

public class Movingimage {
    public static void main(String[] args){
        new MyFrame();
    }
}
