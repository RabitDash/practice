#include <iostream>
#include <vector>
using namespace std;

int gcd(int a, int b)
{
	if(a == 0)
		return b;
	else
		return gcd(b%a, a);
}
int main()
{
	int n;
	cin >> n;
	while(n != 0)
	{
		vector<int> vec;
		int tmp;
		int count = 0;
		for(int i = 0; i < n; i++)
		{
			cin >> tmp;
			vec.push_back(tmp);
		}
		for(int i = 0; i < n; i++)
		{
			for(int j = i + 1; j < n; j++)
			{
				if(gcd(vec[i],vec[j]) == 1)
				{
					count++;
				}
			}
		}
		cout << count << endl;
		cin >> n;
	}
}
