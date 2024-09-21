import static java.lang.System.*;
class Prime {
    void checkPrime(int... vars){
        for (int number : vars){
            if (BigInteger.valueOf(number).isProbablePrime(5)){
                System.out.print(number + " ");
            }
        }
    System.out.println();
    }
}