/*
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.



Answer: 837799
*/



public class LongestCollatzSeq{

        public static void main(String[] args){

          int longest = 0;
          int start = 0;
          int longestStart = 0;

          long collatz = 0;

          int count=0;

          for(int i = 1000000; i>1; i--){

              start = i;
              collatz = i;

              while(collatz > 1){

                count++;
                collatz = nextCollatz(collatz);

              }



              if (count > longest){
                 longest = count;
                 longestStart = start;
               }

                  count = 0;

          }

            System.out.println(longestStart);



        }


        public static long nextCollatz(long n){

            long next = 0;

            if(n % 2 == 0) next = n/2;
            else next = (3*n)+1;

              return next;

        }

}
