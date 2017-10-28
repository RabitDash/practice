#include <iostream>
#include <string>
using namespace std;

int isPrime(int); // 0 represents number is not prime, 1 represents number is prime

int main()
{
	int n;
	while(cin >> n)
	{
		int sum = 0;
		for(int i = 1; i < n; i++)
		{
			if(isPrime(i) == 1)
			{
				sum += i;
			}
		}
		cout << sum << endl;
	}
	return 0;
}

int isPrime(int n)
{
	if(n < 2)
	{
		return 0;
	}
	else if(n == 2)
	{
		return 1;
	}

	for(int i = 2; i <= (n / 2); i++)
	{
		if(n % i == 0)
		{
			return 0;
		}
	}
	return 1;
}
