/*

Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Pentagonal	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.

Answer: 1533776805
*/

public class TriPentHex{


        public static void main(String[] args){

          long n = 40755 ;

              while(true){
                  n++;

                  if( isTri(n) && isPent(n) && isHex(n) ){
                    break;
                  }

              }


                  System.out.println(n);


        }


        public static boolean isTri(long x) {

            if (x < 0)
              return false;

            final long n = (long) Math.sqrt(2 * x);
            return n * (n + 1) / 2 == x;

        }

        public static boolean isPent(long x) {

          return Math.sqrt(1+24*x) % 6 == 5;

         }

        public static boolean isHex(long x) {


          return Math.sqrt(1 + 8 * x) % 4 == 3;

        }


}
