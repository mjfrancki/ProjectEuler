/*

In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?

*/


import java.util.*;

public class CoinSum{

    static public void main(String args[]){

          final  int P1 = 1;
          final  int P2 = 2;
          final  int P5 = 5;
          final  int P10 = 10;
          final  int P20 = 20;
          final  int P50 = 50;
          final  int L1 = 100;
          final  int L2 = 200;

   //int goal = L2;
   //int[] coins = {P1,P2,P5,P10,P20,P50,L1};


   int goal = 200;
   int[] coins = {1,2,5,10,20,50,100,200};


 System.out.println(count(coins, coins.length, goal));


      }


static long count(int S[], int m, int n ){

long[] table = new long[n+1];
	Arrays.fill(table, 0);
table[0] = 1;

    for(int i = 0; i < m; i++  )
      for (int j=S[i]; j<=n; j++)
           table[j] += table[j-S[i]];


      return table[n];

}


}
