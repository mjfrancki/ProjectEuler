import java.lang.Math;

public class FibNumDig{

    public static void main(String[] args){

      final double PHI = 1.6180339887498948;


      int n = 0;
      double digits =0;

          while(true){
          n++;

          digits =  Math.ceil((n * Math.log10( PHI )) -((Math.log10(5))/2))  ;



        //  System.out.println(digits);

          if(digits >= 1000) break;

          }

          System.out.println(n);

    }

}
