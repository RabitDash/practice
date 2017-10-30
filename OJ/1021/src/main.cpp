#include <iostream>
using namespace std;

int main()
{
	int fuck;
	while(cin >> fuck)
	{
		if( fuck % 7 > 0)
		{
			cout << fuck % 7 << endl;
		}
		else
		{
			cout << 7 << endl;
		}
	}
	return 0;
}
