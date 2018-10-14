import java.util.Scanner;
import java.lang.Math.*;
public class Main{
	public static void main(String[] args)
	{
		Scanner sc = new Scanner(System.in);
		while(true){
			System.out.println("是否猜拳？1:是 0:不是");
			int in = sc.nextInt();
			switch (in) {
				case 0:
					return;
				case 1:
					System.out.println("Guess!1:剪刀 2:石头 3:布");
					in = sc.nextInt();
					guess(in);
					break;
				default:
					return;
			}
		}
	}
	private static void win(int a, int b)
	{
		switch(a)
		{
			case 1:
				switch(b)
				{
					case 1:
						System.out.println("Draw");
						break;
					case 2:
						System.out.println("You Lose");
						break;
					case 3:
						System.out.println("You win");
						break;
				}
				break;
			case 2:
					switch(b)
					{
						case 2:
							System.out.println("Draw");
							break;
						case 3:
							System.out.println("You Lose");
							break;
						case 1:
							System.out.println("You win");
							break;
					}
				break;
			case 3:
				switch(b)
				{
					case 3:
						System.out.println("Draw");
						break;
					case 1:
						System.out.println("You Lose");
						break;
					case 2:
						System.out.println("You win");
						break;
				}
			break;
		}
	}
	private static void guess(int pIn){

		int computer = (int)(Math.random() * 10 / 3 + 1);
		int player = pIn; 
		String[] skill = new String[4];
		skill[1] = "剪刀";
		skill[2] = "石头";
		skill[3] = "布";
		System.out.println("Player:"+skill[player]);
		System.out.println("Computer:" + skill[computer]);
		win(player, computer);
	}
}
