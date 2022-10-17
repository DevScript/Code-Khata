import com.mysql.cj.jdbc.Driver;

import java.sql.DriverManager;
import java.sql.Connection;
import java.sql.Statement;
public class Conn {

        Connection c;
        Statement s;
        Conn(){
            try {
                Class.forName("com.mysql.cj.jdbc.Driver");
                c= DriverManager.getConnection("jdbc:mysql://localhost:3306/StudentRegisterationForm","root","123456");
                s= c.createStatement();

            }catch (Exception e){
                e.printStackTrace();
            }
        }

}
