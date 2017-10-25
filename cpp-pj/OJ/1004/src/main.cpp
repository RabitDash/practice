#include <iostream>
#include <string>
#include <algorithm>
#include <sstream>
using namespace std;

int main()
{
	string a, b;
	cin >> a >> b;
	string max, min;	
	string result;
	stringstream ss;

	if(a.length() > b.length())
	{
		max = a;
		min = b;
	}
	else
	{
		max = b;
		min = a;
	}

	reverse(max.begin(), max.end());
	reverse(min.begin(), min.end());

	int jinwei = 0;
	int i = 0;

	for(; i < min.length(); i++)
	{
		int he = max[i] + min[i] - '0' - '0' + jinwei;
		jinwei = he / 10;
		int current = he % 10;
		ss << current;
	}
	int flag = 0;
	if((min.length() == max.length()) && (jinwei > 0))
	{
		result = ss.str();
		reverse(result.begin(), result.end());
		cout << jinwei << result << endl;
	}
	else{
	for(int n = i; n < max.length(); n++)
	{
		int he = max[n] +  jinwei - '0';
		jinwei = he / 10;
		int current = he % 10;
		ss << current;
	}

	if (flag == 1)
	{
		cout << jinwei;
	}
	
	result = ss.str();
	reverse(result.begin(), result.end());
	cout << result;
	cout << endl;

	}
	return 0;
}
