#include <iostream>
using namespace std;
#define SWAP(A,B) (A)=(A)^(B),(B)=(B)^(A),(A)=(A)^(B);
int gcd (int, int);
int fuck(int, int);
int main()
{
	int n;
	int a, b, c;
	cin >> n;

	for(int i = 0; i < n; i++)
	{
		cin >> a >> b >> c;
		int tmp = gcd(a,b);
		cout << gcd(tmp,c) << endl;
	}	
	return 0;
}
int gcd(int a, int b)
{
	if(a < b)
	{
		SWAP(a,b)
	}
	int shang, yushu;
	while(b != 0)
	{
		yushu = a % b;
		a = b;
		b = yushu;
	}
	return a;
}
