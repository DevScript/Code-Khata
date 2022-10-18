import java.sql.*;
import java.util.Scanner;

public class Books {
    String BookName;
    String AuthorName;
    int Edition;
    double price;
    Scanner sc = new Scanner(System.in);

    Books(String BookName, String AuthorName, int Edition, double price) {
        this.BookName = BookName;
        this.AuthorName = AuthorName;
        this.Edition = Edition;
        this.price = price;
    }

    public Books() {

    }

    public void viewBooks() {
        String dbURL = "jdbc:mysql://localhost:3306/Java";
        String username = "root";
        String password = "";

        try (Connection conn = DriverManager.getConnection(dbURL, username, password)) {

            if (conn != null) {
                //System.out.println("connected to Database");
            }
            String sql = "SELECT * FROM books";

            Statement statement = conn.createStatement();
            ResultSet result = statement.executeQuery(sql);

            int count = 0;

            while (result.next()) {
                String bookname = result.getString("BookName");
                String authorname = result.getString("AuthorName");
                double price = result.getDouble("Price");
                int edition = result.getInt("Edition");


                String output = "User #%d: %s - %s - %s - %s";
                System.out.println(String.format(output, ++count, bookname, authorname, price, edition));
            }

        } catch (Exception e) {
            System.out.println(e.getMessage());

        }
    }

    public void deleteBook() {
        System.out.println("Enter Book Name to Delete");
        String book = sc.nextLine();
        String dbURL = "jdbc:mysql://localhost:3306/Java";
        String username = "root";
        String password = "";

        try (Connection conn = DriverManager.getConnection(dbURL, username, password)) {

            if (conn != null) {
               // System.out.println("connected to Database");
            }
            String sql = "DELETE FROM books WHERE BookName=?";

            PreparedStatement statement = conn.prepareStatement(sql);
            statement.setString(1, book);

            int rowsDeleted = statement.executeUpdate();
            if (rowsDeleted > 0) {
                System.out.println("A book was deleted successfully!");
            }
        } catch (Exception e) {
            System.out.println(e.getMessage());

        }
    }

    public void updateBook() {

        System.out.println("choose any one book to update");
        String dbURL = "jdbc:mysql://localhost:3306/Java";
        String username = "root";
        String password = "";

        viewBooks();

        System.out.println("Enter BookName To update");
        String book = sc.nextLine();
        System.out.println("Enter Book Author To Update");
        String author = sc.nextLine();
        System.out.println("Enter book edition to update");
        int edition = sc.nextInt();
        System.out.println("Enter book price to update");
        double price = sc.nextDouble();


        try (Connection conn = DriverManager.getConnection(dbURL, username, password)) {



            String query2 = "UPDATE books SET BookName= '" + book + "', AuthorName= '" + author + "', Edition ='" + edition + "',Price='" + price +"' WHERE BookName = '"+book+"'";

            PreparedStatement prestatement = conn.prepareStatement(query2);
            prestatement.execute();
            System.out.println("An existing book was updated successfully!");


        }
        catch (Exception e1) {
            e1.printStackTrace();
        }

    }
}
