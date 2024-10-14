import java.util.Scanner;

public class Solution {

    static boolean isAnagram(String a, String b) {
        String loweredA = a.toLowerCase();
        String loweredB = b.toLowerCase();
        
        char[] charsA = loweredA.toCharArray();
        char[] charsB = loweredB.toCharArray();
        
        if (charsA.length != charsB.length){
            return false;
        }
        
        for (int x = 0; x < charsA.length; x++){
            
           for (int z = 0; z < charsB.length; z++){
               
               if (charsA[z] == charsB[x]){
                   charsA[z] = 'x';
                   charsB[x] = 'x';
                   z = charsB.length;
               }
           }
            
        }
        
        int counter = 0;
        for (int e = 0; e < charsA.length; e++){
            
            if (charsA[e] == charsB[e]){
                counter++;
            }
            
        }
        
        if (counter == charsA.length){
            return true;
        }
        
        return false;
    }
    public static void main(String[] args) {
    
        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }
}