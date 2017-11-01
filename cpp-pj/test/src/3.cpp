#include <iostream>
using namespace std;
void abs(int i)
{
	cout << i << endl;
}

void abs(float i)
{
	cout << i << endl;
}

void abs(double i)
{
	cout << i << endl;
}

int main()
{
	int a = 1;
	float b = 2;
	double c = 3;
	abs(a);
	abs(b);
	abs(c);
	return 0;
}
