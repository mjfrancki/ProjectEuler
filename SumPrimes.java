public class SumPrimes{


  public static void main(String[] args) {

int primes = 2000000;
long num = 0;
long sum = 0;

while(num < primes){

  num++;

  if(isPrime(num)){

    sum += num;

    //System.out.println(pCount + " : " + num  + " : " + sum);

 }


}


    System.out.println(sum);

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
