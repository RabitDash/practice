#include <iostream>
#include <vector>
using namespace std;
int dec2bin(int);
int main()
{
	int n, a;
	cin >> n;
	for(int i = 0; i < n; i++)
	{
		cin >> a;
		cout << dec2bin(a);
		cout << endl;
	}
	return 0;
}

int dec2bin(int a)
{
	int sum = 0;
	vector<int> binArray;
	while(a != 0)
	{
		binArray.push_back(a % 2);
		a = a / 2;
	}
	for(int i = binArray.size() - 1; i >= 0; i--)
	{
			sum += binArray[i];
	}
	return sum;
}
