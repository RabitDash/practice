#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
	int n, a; // n 为输入个数,a 为给定正整数
	cin >> n;
	for(int i = 0; i < n; i++)
	{
		cin >> a;
		printf("%o\n", a);
	}
	return 0;
}
