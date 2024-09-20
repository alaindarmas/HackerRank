import java.util.*;
class Solution{
	
	public static void main(String []argh)
	{
		Scanner sc = new Scanner(System.in);
		
		while (sc.hasNext()) {
			
            String input=sc.next();
            //Stack myStack = new Stack();

            char[] array = input.toCharArray();
            int parCounter = 0, curlyCounter = 0, brCounter = 0;
            for (int i = 0; i < array.length;i++){
               
                switch(array[i]){
                    case '{':
                        curlyCounter++;
                        break;
                    case '}':
                        curlyCounter--;
                        break;
                    case '[':
                        brCounter++;
                        break;
                    case ']':
                        brCounter--;
                        break;
                    case '(':
                        parCounter++;
                        break;
                    case ')':
                        parCounter--;
                        break;
                }

                if(parCounter < 0 || curlyCounter < 0 || brCounter < 0){
                    //System.out.println("false");
                    break;
                }

            }

            if(parCounter == 0 && brCounter == 0 && curlyCounter == 0)
                System.out.println("true");
            else
                System.out.println("false");

           
        }


		
	}
}




