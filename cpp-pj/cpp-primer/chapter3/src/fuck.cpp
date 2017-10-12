#include <iostream>
#include <vector>
using namespace std;
int main()
{
	vector<int> array;
	int fuck;
	while(cin >> fuck)
	{
		array.push_back(fuck);
	}
	cout << array.size() << endl;
	for(auto a = array.begin(); a != array.end(); ++a)
	{
		cout << *a;
	}
	return 0;
}
