#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
	double amount = 22.0 / 7;
	cout << amount << endl;
	for (int i = 1; i <= 4; i++) {
		cout << setprecision(i) << amount << endl;
	}
	cout << setprecision(ios::scientific) << amount << endl;
	return 0;
}
