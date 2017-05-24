import  java.math.BigInteger;

public class Champernownes{

    public static void main(String[] args)
    {

      BigInteger ans = BigInteger.ONE;


      for(int i =1 ; i<= 1000000; i *= 10){
      ans =  ans.multiply(  BigInteger.valueOf(   Character.getNumericValue(  ChampDig(i)) )  );
System.out.println(i + " : " + BigInteger.valueOf(  Character.getNumericValue(  ChampDig(i)) ) );
    }



      System.out.println ( ans.toString() );

    }


    public static char ChampDig(int n){

        int  d = 1;
        int digitPlace = 0;
char ans = ' ';

        for( d=1 ; d<=n ; d++){

          //digitPlace +=  (Integer.toString(d)).length();


          for(int i = 0; i < (Integer.toString(d)).length() ;i++){


              digitPlace ++;

              if(digitPlace == n)
              ans = (Integer.toString(d)).charAt(i);

              //if (digitPlace == n){

                //    return  (Integer.toString(d)).charAt(i);
              //}

          }

        }


          return ans;

    }


}
