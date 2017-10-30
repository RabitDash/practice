#include <iostream>
using namespace std;

int main()
{
	string maxStr = "", minStr = "", tmp;
	cin >> tmp;
	minStr = tmp;
	while(cin >> tmp)
	{
		if(tmp.size() < minStr.size())
		{
			minStr = tmp;
		}
		else if(tmp.size() > maxStr.size())
		{
			maxStr = tmp;
		}
	}
	cout << maxStr << endl;
	cout << minStr << endl;
	return 0;
}
