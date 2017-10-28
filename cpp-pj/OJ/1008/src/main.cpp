#include <iostream>
#include <string>
using namespace std;

string isPrime(int);

int main()
{
	int n;
	while(cin >> n)
	{
		cout << isPrime(n) << endl;
	}
	return 0;
}

string isPrime(int n)
{
	if(n <= 1)
	{
		return "fuck!";
	}
	else if(n == 2)
	{
		return "Yes";
	}
	for(int i = 2; i <= (n / 2); i++)
	{
		if(n % i == 0)
		{
			return "No";
		}
	}
	return "Yes";
}
