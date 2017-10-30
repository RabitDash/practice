#include <iostream>
using namespace std;

int main()
{
	int n;
	while (cin >> n) {
		int matrix[n][n] = { 0 };
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				matrix[i][j] = 0;
			}
		}
		int x = 0;
		int y = 0;
		int xDir = 1;
		int yDir = 0;

		for (int num = 1; num <= n * n; num++) {
			matrix[x][y] = num;
			if (x + xDir < 0 || y + yDir < 0 || x + xDir == n
			    || y + yDir == n
			    || matrix[x + xDir][y + yDir] != 0) {
				if (xDir != 0) {
					yDir = xDir;
					xDir = 0;
				} else {
					xDir = -yDir;
					yDir = 0;
				}
			}
			x += xDir;
			y += yDir;
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				cout << matrix[i][j];
				if (j < n - 1) {
					cout << " ";
				}
			}
			cout << endl;
		}
	}
	return 0;
}
