/*

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

*/



public class largestPrimeFactor
{
	public static void main(String[] args) {
    long number = 600851475143L;
    long halfNumber = number/2;
		long factor = 0;


      for(long i = halfNumber; i > 0; i--){

					if(number % i == 0 && isPrime(i) ){
            factor = i;
						break;
					}
      }

    System.out.println(factor);
	}


 static boolean isPrime(long num) {
	    if (num == 2) return true;
	    if (num % 2 == 0) return false;
	    for (long i = 3; i * i < num; i += 2)
	        if (num % i == 0) return false;
	    return true;
		}



}
