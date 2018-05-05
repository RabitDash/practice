#include <iostream>
#include <vector>
using namespace std;

int main()
{
	int n;
	while (cin >> n) {
		vector<int> array;
		array.push_back(1);
		int tmp;
		for (int junk = 0; junk < n; junk++) {
			tmp = 0;
			for (int i = 0; i < array.size(); i++) {
				array[i] *= 2;
				array[i] += tmp;
				tmp = array[i] / 10;
				array[i] %= 10;
			}
			if(tmp != 0)
				array.push_back(tmp);
		}
		array[0] -= 1;
		for (int i = array.size() - 1; i >= 0; i--) {
			cout << array[i];
		}
		cout << endl;
	}
	return 0;
}

