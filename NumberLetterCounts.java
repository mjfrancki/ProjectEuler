public class NumberLetterCounts{


    public static void main(String[] args){

int letterCount = 0;

System.out.println( intToWord(10) );
System.out.println( intToWord(10).length() );

for(int i = 1 ;i<=1000;i++){
  System.out.println(i+" : "+ intToWord(i)+ " : " + intToWord(i).length() );

    letterCount +=  intToWord(i).length();
}


System.out.println( letterCount );

}

//should probably generlize more
public static String intToWord(int n){

    String[] words1Dig = {"","one","two","three","four","five","six","seven","eight","nine"};
    String[] words2Dig = {"ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"};
    String[] wordsMultTen = {"twenty","thirty","forty","fifty","sixty", "seventy","eighty","ninety" };
    String hund = "hundred";
    String thous = "thousand";


    String number = Integer.toString(n);
    char digit = number.charAt(0);


    if (n < 10) return words1Dig[n];
    if (n < 20) return words2Dig[(n-10)];
    if (n < 100){

          return  wordsMultTen[Character.getNumericValue(digit)-2] + words1Dig[  Integer.parseInt(number.substring(1)) ] ;

    }

    if (n < 1000){

          if(n%100 != 0)
          return   words1Dig[Character.getNumericValue(digit)] + "hundredand" + intToWord(Integer.parseInt(number.substring(1))) ;

          else
          return   words1Dig[Character.getNumericValue(digit)] + "hundred" + intToWord(Integer.parseInt(number.substring(1))) ;
    }


    return "oneThousand";
}


}
