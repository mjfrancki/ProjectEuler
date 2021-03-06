/*
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.


Answer: 4613732
*/



public class evenFib
{
	public static void main(String[] args) {

int intitial0 = 1;
int intitial1 = 2;

int fib = intitial0 + intitial1;
int curFib = fib;
int oldFib = intitial1;
int sum = 2;

      while(fib < 4000000){

          curFib = fib;

          fib = oldFib + curFib;

          if(fib % 2 == 0){

              sum += fib;

          }


         oldFib = curFib;
      }



    System.out.println(sum);
	}
}
