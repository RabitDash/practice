#include <iostream>
using namespace std;

int main()
{
	int n, a;
	int max = 0, semimax = 0;
	cin >> n;
	int previous = 0;
	for(int i = 0; i < n; i++)
	{
		cin >> a;
		if(a > max)
		{
			max = a;
			semimax = previous;
		}
		else if(a > semimax)
		{
			semimax = a;
		}
		previous = a;

	}
	cout << max << " " << semimax << endl;
	return 0;
}
