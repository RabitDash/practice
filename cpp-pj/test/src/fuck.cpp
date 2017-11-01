#include <map>
#include <string>
#include <iostream>
using namespace std;

int main()
{
	map < string, string > dict;
	dict["fuck"] = "shit";
	cout << dict["fuck"];
	return 0;
}
