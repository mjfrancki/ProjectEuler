/*

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

Answer: 648

*/

import java.math.BigInteger;

public class FactDigitSum{


     static public void main(String[] args){


          BigInteger fact = BigInteger.valueOf(1);

                int n = 100;

                for(int i = 1;i <= n;i++){

                    fact = fact.multiply(  BigInteger.valueOf(i)  );

                }


                String factString =  fact.toString();
                int sum = 0;

                for(int i = 0; i< factString.length()  ;i++){

                      sum += Character.getNumericValue(factString.charAt(i));

                }

                System.out.println(sum);

      }


}
