import java.rmi.*;
import java.util.Scanner;

public class MyClient {
    public static void main(String args[]) {
        try {
            Adder stub = (Adder) Naming.lookup("rmi://localhost:5000/sonoo");
            System.out.print("Enter two numbers:\n");
            Scanner sc = new Scanner(System.in);
            int x = sc.nextInt();
            int y = sc.nextInt();
            sc.close();
            System.out.println("Result: "+ stub.add(x, y));
        } catch (Exception e) {
        }
    }
}