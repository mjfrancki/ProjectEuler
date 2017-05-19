/*
Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
*/


import java.math.BigInteger;
public class SelfPowers{


    public static void main(String[] args){

        BigInteger sum =  BigInteger.valueOf(0);
;


        for(int i = 1  ; i<=1000 ;  i++ ){


            sum = sum.add (  BigInteger.valueOf(i).pow(i) );


        }
              //System.out.println(  sum.toString()  );
              String substr = sum.toString().substring(sum.toString() .length() - 10);
              System.out.println(  substr   );
      }

}
