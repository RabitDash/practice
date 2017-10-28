import java.util.*;
public class Main{
	private static int[][] matrix;
	public static void main(String args[])
	{
		Scanner ss = new Scanner(System.in);
		while(ss.hasNext()){
		int n = Integer.parseInt(ss.nextLine());
       		matrix = new int[n][n];
        	for (int num = 1, x = 0, y = 0, xDir = 1, yDir = 0; num <= n * n; num++) {
        	     matrix[x][y] = num;
        	     if (x + xDir < 0 || y + yDir < 0 || x + xDir == n || y + yDir == n || matrix[x + xDir][y + yDir] != 0) {//如果到边界了就换方向
        	         if (xDir != 0) {
        	             yDir = xDir;
        	             xDir = 0;
        	         } else {
        	             xDir = -yDir;
        	             yDir = 0;
        	         }
        	     }
        	     x += xDir;
        	     y += yDir;
        	}
		for(int i = 0; i < n; i++)
		{
			for(int j = 0; j < n; j++)
			{
				System.out.print(matrix[j][i]);
				if(j < n - 1)
				{
					System.out.print(" ");
				}
			}
			System.out.println();
		}
		}
   	 }	
}
