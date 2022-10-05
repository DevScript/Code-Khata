import java.util.*;
import java.math.*;
public class attendance{
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        System.out.println("Welcome!\n");
        System.out.println("1.Attendance Messages\n2.Current Attendance\n3.Leave Application\n4.Attendance Claim\n");
        System.out.println("Exit any time by pressing number 5\n");
        int choice=sc.nextInt();

        while(true){
            if(choice>=1 && choice<=4){
                if(choice==1){
                    attendancemsgs obj=new attendancemsgs();
                    obj.PastMessages();
                    obj.currentMessages();
                    System.exit(0);
                }
                else if(choice==2){
                    currentatt obj1=new currentatt();
                    obj1.pastStatus();
                    int a=(int)(Math.random()*(25-12+1)+12);
                    int b=(int)(Math.random()*(35-13+1)+13);
                    int c=(int)(Math.random()*(30-15+1)+15);
                    obj1.Currentstatus(a, b, c);
                    if(sc.nextInt()==5){
                        System.exit(0);
                    }
                }
                else if(choice==3){
                    LeaveAppl obj2=new LeaveAppl();
                    obj2.apply();
                    System.out.println("......\n");
                    for(int i=0;i<1000;i++){
                        ;
                    }
                    obj2.status();
                    if(sc.nextInt()==5){
                        System.exit(0);
                    }
                }
                else if(choice==4){
                    claimAtt obj4=new claimAtt (Math.random()*(10-1+1)+1);
                    obj4.pastStatus();
                    obj4.currentStatus(Math.random()*(20-1+1)+1);
                    if(sc.nextInt()==5){
                        System.exit(0);
                    }
                }
            }
            else{
                System.exit(0);
            }
        }
    }
}

class attendancemsgs{
    void PastMessages(){
        System.out.println("You were absent for Java class yesterday");
        System.out.println("Your OD application for 09/19 is approved");
        System.out.println("\nNO MORE PAST MESSAGES\n");
    }
    void currentMessages(){
        System.out.println("\nYou have no current messages!");
    }
}

class currentatt{
    void pastStatus(){
        int a,b,c;
        a=12;b=13;c=15;
        System.out.println("Your attendance on Java course is: "+a+"/25");
        System.out.println("Your attendance on DT course is: "+b+"/35");
        System.out.println("Your attendance on Software Engineering course is: "+c+"/30");
    }
    void Currentstatus(int a,int b, int c){
        System.out.println("\nCurrent Attendance Status:\n");
        System.out.println("Your attendance on Java course is: "+a+"/25");
        System.out.println("Your attendance on DT course is: "+b+"/35");
        System.out.println("Your attendance on Software Engineering course is: "+c+"/30");
    }
}

class claimAtt{
    int day=0;
    claimAtt(double d){
        this.day=(int) d;
    }
    void pastStatus(){
        System.out.println("You have claimed "+day+" day attendance: ");
    }
    void currentStatus(double d){
        System.out.println("You have claimed "+(int)d+" day attendance additionally");
    }
}

class LeaveAppl{
    void apply(){
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the day: ");
        sc.nextLine();
        System.out.println("Enter reason: \n");
        sc.nextLine();
        System.out.println("\nLeave application in progress....\n");
    }
    void status(){
        Random rd=new Random();
        int rand=rd.nextInt(2);
        if(rand==0){
            System.out.println("Leave not granted!");
        }
        else if(rand==1){
            System.out.println("Leave granted!");
        }
    }
}