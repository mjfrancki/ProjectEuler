/*
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?

Answer: 104743
*/

public class NthPrime
{
	public static void main(String[] args) {
    int n = 10001;
    int num = 0;
    int count = 0;

while(count < n){
num ++;

if( isPrime(num) ) {
  count++ ;
}


}


  System.out.println( num );
	}



  static boolean isPrime(long num) {
    if (num == 1) return false;
    if (num == 2) return true;
    if (num % 2 == 0)
           return false;
       for (int i = 3; i * i <= num; i += 2)
           if (num % i == 0) return false;
       return true;
     }


}
