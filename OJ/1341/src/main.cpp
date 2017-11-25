#include <iostream>
using namespace std;
int main()
{
	int n;
	while (cin >> n) {
		int a, b, c;
		int flag = 1;	// flag == 0 --> Wrong Answer  flag == 1 --> Accepted
		char oper1, oper2;
		for (int i = 0; i < n; i++) {
			cin >> a >> oper1 >> b >> oper2 >> c;
			if (a + b != c) {
				flag = 0;
			}
		}
		if (flag == 1) {
			cout << "Accepted" << endl;
		} else if (flag == 0) {
			cout << "Wrong Answer" << endl;
		}
	}
	return 0;
}
