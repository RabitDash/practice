#include <iostream>
using namespace std;

int main()
{
	int n;
	while(cin >> n)
	{
		if(n == 1)
		{
			cout << 1 << endl;
		}
		if(n == 2)
		{
			cout << 2 << endl;
		}
		else
		{
			int prev = 1;
			int now = 2;
			int result = 0;
			for(int i = 1; i < n; i++)
			{
				result += prev * now;
				prev = now;
				now = result;
			}
			cout << result << endl;
		}
	}
	return 0;
}
