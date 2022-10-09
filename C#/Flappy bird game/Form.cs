using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApplication47
{
    public partial class Form1 : Form
    {    //initize variable
        int pipespeed = 5;
        int gravity = 5;
        int score = 0;

        public Form1()
        {
            InitializeComponent();
        }

        private void pipebottom_Click(object sender, EventArgs e)
        {

        }

        private void ground_Click(object sender, EventArgs e)
        {

        }

        private void gametimerevent(object sender, EventArgs e)
        {
            flappybird.Top += gravity; //move down
            pipebottom.Left -= pipespeed; //move pipes
            pipetop.Left -= pipespeed;
            Score.Text = "Score: " + score; //print score
            if(pipebottom.Left < -150) //distance of previous
            {
                pipebottom.Left = 400;  //distance of next
                score++; //increasse score
            }
            if (pipetop.Left < -300)
            {
                pipetop.Left = 550;
                score++; //inc score
            }

            if  (flappybird.Bounds.IntersectsWith(pipebottom.Bounds)  || flappybird.Bounds.IntersectsWith(pipetop.Bounds)
              || flappybird.Bounds.IntersectsWith(ground.Bounds) )
                {
                endgame();
            }

            if(score > 5 )
            {
                pipespeed = 10;
            }
            if (flappybird.Top < -25) //with sky
            {
                endgame();
            }

        }

        private void gamekeyup(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Space)  //if key pressed is space
                //with space move up
            {
                gravity = 5;  //down speed ; if -5 up
            }
        }

        private void gamekeydown(object sender, KeyEventArgs e)
        {
            if(e.KeyCode == Keys.Space) //with space move up
            {
                gravity = -5; //if 5 down
            }
        }
        private void endgame()
        {
            gametimer.Stop();
            Score.Text = " Game over!";
            MessageBox.Show("Game over and your score is " + score);

        }
    }
}
