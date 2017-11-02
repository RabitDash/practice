#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
	int n;
	cin >> n;
	for(int i = 0; i < n; i++)
	{
		char oper;
		int a,b;
		cin >> oper >> a >> b;
		switch(oper)
		{
			case '+':
				cout << a + b << endl;
				break;
			case '-':
				cout << a - b << endl;
				break;
			case '*':
				cout << a * b << endl;
				break;
			case '/':
				if( a % b != 0)
				{
					cout << setiosflags(ios::fixed);
					cout << setprecision(2) << double(a) / double(b) << endl;
				}
				else 
				{
					cout << a / b << endl;
				}
				break;
		}
	}
	return 0;
}
