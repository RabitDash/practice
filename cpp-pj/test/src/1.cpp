#include <iostream>
using namespace std;

int test(int i)
{
	std::cout << i << endl;
	return 4096;
}

int main()
{
	typedef int (*fuck) (int);
	fuck a, b, c;
	a = test;
	b = test;
	c = test;
	int s;
	s = a(32);
	std::cout << "a:" << a << endl << "b:" << b << endl << "c:" << c << endl
	    << "s:" << s;
	return 0;
}
