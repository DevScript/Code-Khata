import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.Scanner;


public class NewBook extends Books {

    Scanner sc = new Scanner(System.in);

    NewBook() {
    }

    public void addBook() throws SQLException {
        System.out.println("Enter book Name");
        BookName = sc.nextLine();
        System.out.println("Enter Author Name");
        AuthorName = sc.nextLine();
        System.out.println("Enter Book Edition");
        Edition = sc.nextInt();
        System.out.println("Enter book price");
        price = sc.nextDouble();

        String dbURL = "jdbc:mysql://localhost:3306/Java";
        String username = "root";
        String password = "";

        try (Connection conn = DriverManager.getConnection(dbURL, username, password)) {

            if (conn!= null){
                //System.out.println("connected to Database");
            }

            String sql = "INSERT INTO books (BookName, AuthorName, Price,Edition) VALUES (?, ?, ?,?)";


            PreparedStatement statement = conn.prepareStatement(sql);
            statement.setString(1, BookName);
            statement.setString(2, AuthorName);
            statement.setDouble(3, price);
            statement.setInt(4, Edition);


            int rowsInserted = statement.executeUpdate();
            if (rowsInserted > 0) {
                System.out.println("A new book was inserted successfully!");
            }

        } catch (SQLException ex) {
            ex.printStackTrace();
        }





    }

}
