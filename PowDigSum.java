/*
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?

Answer:
1366
*/


import java.math.BigInteger;


public class PowDigSum{

    public static void main(String[] args){


      BigInteger pow = BigInteger.valueOf(2);
      pow = pow.pow(1000);

        System.out.println(pow.toString());


        int sum = 0;
        for(int i = 0 ; i< (pow.toString()).length() ;i++){

          sum += Character.getNumericValue( (pow.toString()).charAt(i) );

        }

        System.out.println(sum);





    }





}
