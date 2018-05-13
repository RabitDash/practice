#include <iostream>
using namespace std;
int shit(int n, int m, int day)
{
	if(day > 1)
		return n * (shit(n, m, day-1) + 1 + m);
	else
		return n + m;
}
int main()
{
	int n, m;
	cin >> n >> m;
	cout << shit(n, m, n);
	return 0;
}
	
