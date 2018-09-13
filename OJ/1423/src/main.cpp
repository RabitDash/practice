#include <iostream>
#include <vector>
using namespace std;

int main()
{
	int n;
	while(cin >> n)
	{
		vector<int> a;
		vector<int> shit;
		int max = 0;
		a.resize(2 * n + 1);
		a[1] = 1;
		for(int i = 2; i <= n; i++)
		{
			if(i % 2 == 0)
				a[i] = a[i/2] + 1;	
			else
				a[i] = a[(i-1)/2] + a[(i-1)/2+1];
		}
		for(int i = 1; i <= n; i++)
		{
			if(max < a[i])
			{
				max = a[i];
				shit.clear();
				shit.push_back(i);
			}
			else if(max == a[i])
			{
				shit.push_back(i);
			}
		}
		cout << a[n] << endl;
		for(int i = 0; i < shit.size(); i++)
		{
			cout << shit[i] << " ";
		}
		cout << endl;
	}
	return 0;
}
