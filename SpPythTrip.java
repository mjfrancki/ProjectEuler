/*
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Answer:  31875000
*/



public class SpPythTrip{


  public static void main(String[] args) {

    int prod = 0;

for(int a = 1;a<1000;a++){
   for(int b = a+1; b<1000;b++){
      for(int c = b+1; c<1000;c++){


          if (   (a+b+c == 1000) && (a*a + b*b == c*c)  ){
              prod = a * b * c;
          }

     }
   }
 }


    System.out.println(prod);

  }






}
