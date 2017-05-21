/*
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9

Answer:
2783915460
*/

import java.util.*;

public class LexPerm{


    public static void main( String args[]){


        Integer[] nums = {0,1,2,3,4,5,6,7,8,9};
        int n = nums.length;
        int temp = 0;

          int first = 0;
          int second = 0;




          for(int k =0 ;k<1000000;k++){
System.out.println(Arrays.toString(nums));


              first = findFirst(nums);


              second = findCeilofFirst(first, nums);


              swap(nums, first, second);




                 Arrays.sort(nums,first+1,nums.length);


          }





    }

     public static int findFirst(Integer[] nums) {

        for(int i = nums.length-2; i > 0; i--){



              if (nums[i] < nums[i+1]) return i;

        }

              return 0;
     }


   public static int findCeilofFirst(Integer first, Integer[] nums) {

     int smallest = 1000000;
     int indx = -1;



int i = 0;
while(first+i < nums.length-1){
  i++;
  if ( nums[first+i] > nums[first] && nums[first+i] < smallest){

     smallest = nums[first+i] ;
     indx= first+i ;
  }


}

return indx;

   }


   public static final <T> void swap (T[] a, int i, int j) {
     T t = a[i];
     a[i] = a[j];
     a[j] = t;
   }

   public static final <T> void swap (List<T> l, int i, int j) {
      Collections.<T>swap(l, i, j);
    }




}
