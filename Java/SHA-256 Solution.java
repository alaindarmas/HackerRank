import java.io.*;
import java.util.*;
import java.security.MessageDigest;
import javax.xml.bind.DatatypeConverter;

public class Solution {

    public static void main(String[] args) {
       try {
            MessageDigest md = MessageDigest.getInstance("SHA-256");
            Scanner sc = new Scanner(System.in);
            md.update(sc.next().getBytes());
            byte[] bytes = md.digest();
            System.out.println(DatatypeConverter.printHexBinary(bytes).toLowerCase());
        } catch(Exception e) {
            System.out.println("Error");
        }
    }
}
