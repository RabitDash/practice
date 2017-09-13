#include <iostream>
using namespace std;
int abs(int i)
{
	cout<<i<<endl;
	cout<<"int :"<<abs<<endl;
}
float abs(float i)
{
	cout<<i<<endl;
	cout<<"float :"<<abs<<endl;
}
double abs(double i)
{
	cout<<i<<endl;
	cout<<"double :"<<abs;
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
