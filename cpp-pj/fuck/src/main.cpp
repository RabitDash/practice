#include <iostream>
#include <stdio.h>
using namespace std;
class fuck
{
	public:
		int b;
		fuck()
		{
			cout << "instance created!";
		}
		~fuck()
		{
			cout << "instance destroyed!";
		}
};

int main()
{
	fuck you;
	return 0;
}
