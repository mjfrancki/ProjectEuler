public class sumSqDiff
{

  public static void main(String[] args) {

      double squares = 0;

      for(int i=1;i<=100;i++){
       squares +=  Math.pow(i, 2);
      }

      int sum = 0;

      for(int i=1;i<=100;i++){
       sum += i;
      }

      double sqOfsum =  Math.pow(sum, 2);
      int dif = (int)sqOfsum - (int)squares;
     System.out.println(dif);

  }



}
