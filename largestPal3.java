/*
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

*/



public class largestPal3
{

	public static void main(String[] args) {
    int num = 0;
		int largestPal = 0;

      for(int i=100; i < 1000; i++){

				for(int j=100; j < 1000; j++){

						num = i*j;

            if( isPal(Integer.toString(num)) ){

							if(num > largestPal){
							 largestPal = num;
						  }
								
						}

				}

      }

    System.out.println(largestPal);
	}


	static boolean isPal(String s) {
	  int n = s.length();
	  for (int i = 0; i < (n/2); ++i) {
	     if (s.charAt(i) != s.charAt(n - i - 1)) {
	         return false;
	     }
	  }

	  return true;
	}




}
