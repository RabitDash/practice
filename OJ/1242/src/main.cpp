#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	long n, t;
	while(cin >> n >> t)
	{
		vector<long> health;
		long tmp;
		for(int i = 0; i < n; i++)
		{
			cin >> tmp;
			health.push_back(tmp);
		}
		sort(health.begin(), health.end());
		long count = 0;
		int i = 0;
		while(t >= 0 && i < n)
		{
			t -= health[count];
			if(t >= 0) count++;
			i++;
		}
		cout << count << endl;
	}
	return 0;
}

