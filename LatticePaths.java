import java.util.Arrays;

public class LatticePaths{



public static void main(String[] args){

int size = 2;

int[][] grid = new int[size+1][size+1];

int[] start = {0,0};


int count = 0;


count += moveLeft(start, grid) + moveRight(start, grid);

System.out.println(count);

}

public static int moveLeft(int[] pos, int[][] grid){

  System.out.println(Arrays.toString(pos));


int size = 2;
int[] end = {2,1};

    if (Arrays.equals(pos,end)) return 1;

    else if (pos[0] == 2)

    return 0;



    else {

      int[] nextR = new int[] {pos[0],pos[1]+1};
      int[] nextL = new int[] {pos[0]+1,pos[1]};
      return moveRight(nextR , grid)  + moveLeft(nextL, grid);
}

}

public static int moveRight(int[] pos, int[][] grid){

System.out.println(Arrays.toString(pos));

int size = 2;
int[] end = {1,2};
  if (Arrays.equals(pos,end))

  return 1;

  else if (pos[1] == 2 )

  return 0;


  else{

  int[] nextR = new int[] {pos[0],pos[1]+1};
  int[] nextL = new int[] {pos[0]+1,pos[1]};
  return moveRight(nextR , grid)  + moveLeft(nextL, grid);
}

}



}
