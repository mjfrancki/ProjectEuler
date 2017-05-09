/*
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
*/

public class SmallestMult{

  public static void main(String[] args) {

int num = 20 ;
int range = 20;
int count = 0;
  while(true){

      num++;

      count = 0;
      for(int i =1; i <= range; i++){

          if(num % i == 0) count++;

      }


      if (count == 20) break;


  }


    System.out.println(num);
  }

}
