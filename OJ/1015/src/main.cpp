#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int n, k; //find max k numbers in n numbers;
	cin >> n >> k;
	vector<int> array;
	for(int i = 0; i < n; i++)
	{
		int tmp;
		cin >> tmp;
		array.push_back(tmp);
	}
	
	sort(array.begin(), array.end());
	
	int count = 0;
	for(int i = array.size() - 1;count < k;i--,count++)
	{
		cout << array[i];
		if(count != k - 1)
		{
			cout << " ";
		}
	}
	cout << flush;
	return 0;
}
