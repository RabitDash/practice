#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int n;
	cin >> n;
	vector<int> array;
	for(int i = 0; i < n; i++)
	{
		int tmp;
		cin >> tmp;
		array.push_back(tmp);
	}
	
	sort(array.begin(), array.end());
	for(int i = 0; i < n; i++)
	{
		cout << array[i];
		if(i != n - 1)
		{
			cout << " ";
		}
	}
	cout << endl;
	return 0;
}
