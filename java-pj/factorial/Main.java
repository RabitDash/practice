import java.util.Scanner;
import java.math.BigInteger;
public class Main {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        while(s.hasNextInt())
        {
            int n;
            n = s.nextInt();
            if(n == 1)
            {
                System.out.println(1);
            }
            else if(n == 2)
            {
                System.out.println(2);
            }
            else
            {
                BigInteger now = BigInteger.valueOf(1);
                for(int i = 2; i <= n; i++)
                {
                    now = now.multiply(BigInteger.valueOf(i));
                }
                System.out.println(now.toString());
            }
        }
    }
}

