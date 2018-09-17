#include <iostream>
#include <vector>
using namespace std;

int main()
{
	int n;
	int tmp;
	while(cin >> n)
	{
		vector<int> fuck;
		vector<int> shit;
		fuck.resize(n + 1);
		shit.resize(n + 1);
		int tmp;
		int min;
		for(int i = 1; i <= n; i++)
		{
			for(int j = 1; j <= i; j++)
			{
				cin >> tmp;
				fuck[j] = tmp;
			}
			for(int j = 1; j <= i; j++)
			{
				if(j == 1)
				{
					shit[j] += fuck[j];
				}
				else
				{
					shit[j] += (fuck[j-1] > fuck[j] ? fuck[j] : fuck[j-1]);
				}
			}
			fuck = shit;
			if( i == 1)
				min = shit[i];
			else
			min = (min < shit[i] ? min : shit[i]);
		}
		cout << min << endl;
	}
}
