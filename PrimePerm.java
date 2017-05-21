/*

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?

*/

import java.util.*;

public class PrimePerm{

    public static void main(String[] args){


int[] primes = new int[3];

for(int i =1000; i < 9999; i++){


      if (isPrime(i)){

      primes[0] = primes[1];
      primes[1] = primes[2];
      primes[2] = i;


        if (isArithmetic(primes)){
          //  if(isPermutation(  Integer.toString(primes[0]), Integer.toString(primes[1]) )  &&  isPermutation(Integer.toString(primes[1]), Integer.toString(primes[2]))  ){

            System.out.println( Arrays.toString(primes) );

        //    }

        }




      }


}




    }



    static boolean isPrime(int num) {
      if (num == 1) return false;
      if (num == 2) return true;
      if (num % 2 == 0)
             return false;
         for (int i = 3; i * i <= num; i += 2)
             if (num % i == 0) return false;
         return true;
       }



//only for arrays of length 3
  static boolean isArithmetic(int[] nums) {


          return (  Math.abs( nums[0] - nums[1])  ==   Math.abs(nums[1] - nums[2])  );


  }


static public boolean isPermutation(String str1, String str2) {

    if (str1.length() != str2.length())
      return false;

    char[] a = str1.toCharArray();
    char[] b = str2.toCharArray();

    Arrays.sort(a);
    Arrays.sort(b);

    return Arrays.equals(a, b);
}



}
