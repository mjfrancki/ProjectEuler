
/*

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
*/
public class DoubBasePal{


    public static void main(String[] args){

          String pal = "";
          int sum = 0;
        for(int i = 0; i<1000000 ;i++){


          pal = String.valueOf(i);

          if  (isPalindrome(pal)){
                pal = Integer.toBinaryString(i);
                if  (isPalindrome(pal)){
                  sum += i;
                }

          }



        }


  System.out.println(  sum  );



    }


    public static boolean isPalindrome(String str) {
        return str.equals(new StringBuilder(str).reverse().toString());
    }


}
