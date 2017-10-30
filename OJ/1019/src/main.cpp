#include <iostream>
using namespace std;

int main()
{
	string s;
	cin >> s;
	for(int i = 0; i < s.length(); i++)
	{
		s[i] = s.c_str()[i] | 040;
	}
	cout << s;
	return 0;
}
