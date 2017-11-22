#include <iostream>
using namespace std;

int main()
{
	int x; //总虾子数
	while(cin >> x)
	{
		int i = 0; //丢掉的虾子
		while(x > 1)
		{
			if(x % 2 == 0)
			{
				x /= 2;
			}
			else
			{
				++i;
				x = (x - 1) / 2;
			}
		}
		++i;
		cout << i << endl;
	}
}
