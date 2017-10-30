#include <iostream>
using namespace std;
#define SWAP(A,B) (A)=(A)^(B),(B)=(B)^(A),(A)=(A)^(B);
int gcd (int, int);
int main()
{
	int n;
	int a, b;
	cin >> n;
	if(a < b)
	{
		SWAP(a,b)
	}
	for(int i = 0; i < n; i++)
	{
		cin >> a >> b;
		cout << gcd(a,b) << endl;
	}
	return 0;
}
int gcd(int a, int b)
{
	int shang, yushu;
	while(b != 0)
	{
		yushu = a % b;
		a = b;
		b = yushu;
	}
	return a;
}
