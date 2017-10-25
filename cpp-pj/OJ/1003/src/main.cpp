#include <iostream>
using namespace std;

int main()
{
	int a, b;
	char oper;
	int n;
	cin >> n;
	for(int i = 0; i < n; i++)
	{
		cin >> a >> oper >> b;
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
				cout << a / b << endl;
				break;
		}
	}
	return 0;
}
