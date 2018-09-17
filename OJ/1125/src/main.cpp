#include <iostream>
using namespace std;

long FuckRecur(long n)
{
	if(n == 0)
		return 1;
	else if(n == 1)
		return 1;
	else
		return FuckRecur(n-1) + FuckRecur(n-2);
}

long FuckDP(long n)
{
	if(n == 1)
		return 1;
	else if(n == 2)
		return 2;
	long f1, f2, f3;
	f1 = 1;
	f2 = 2;
	f3 = 3;
	for(int i = 3; i <= n; i++)
	{
		f3 = f1 + f2;
		f1 = f2;
		f2 = f3;
	}
	return f3;
}

int main()
{
	long n;
	while(cin >> n)
	{
		cout << FuckDP(n) << endl;
	}
	return 0;
}
		
