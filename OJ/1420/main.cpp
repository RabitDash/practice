#include<iostream>
#include<vector>
#include<string>
#include <algorithm>
using namespace std;
string NM[105][105];
string ts(int n)
{
	string result;
	while (n) {
		result += n % 10 + '0';
		n /= 10;
	}
	reverse(result.rbegin(), result.rend());
	return result;
}

string ADD(string a, string b)
{
	string result;
	int anum[1010] = { 0 };
	int bnum[1010] = { 0 };
	int c[1010] = { 0 };
	for (int i = 0; i < a.size(); i++) {
		anum[i] = a[a.size() - i - 1] - '0';
	}
	for (int i = 0; i < b.size(); i++) {
		bnum[i] = b[b.size() - i - 1] - '0';
	}
	int p = 0;
	while (p < a.size() || p < b.size()) {
		c[p] += anum[p] + bnum[p];
		c[p + 1] = c[p] / 10;
		c[p] %= 10;
		p++;
	}
	while (c[p] == 0) {
		p--;
		if (c[p] != 0) {
			break;
		}
	}
	for (int i = p; i >= 0; i--) {
		result += c[i] + '0';
	}
	return result;
}

string MUL(string a, string b)
{
	string result;
	int len = a.size() + b.size();
	int anum[1010] = { 0 };
	int bnum[1010] = { 0 };
	int c[1010] = { 0 };
	cout << endl;
	for (int i = 0; i < a.size(); i++) {
		anum[i] = a[a.size() - i - 1] - '0';
	}
	for (int i = 0; i < b.size(); i++) {
		bnum[i] = b[b.size() - i - 1] - '0';
	}
	for (int i = 0; i < a.size(); i++) {
		for (int j = 0; j < b.size(); j++) {
			c[i + j] += anum[i] * bnum[j];
			c[i + j + 1] = c[i + j] / 10;
			c[i + j] %= 10;
		}
	}
	while (c[len] == 0) {
		len--;
		if (c[len] != 0) {
			break;
		}
	}
	for (int i = len; i >= 0; i--) {
		result += c[i] + '0';
	}
	return result;
}

string fun(int n, int m)
{
	if (!NM[m][n].empty()) {
		return NM[m][n];
	} else {
		if (n == m) {
			NM[m][n] = "1";
			return NM[m][n];
		}
		if (m == 1) {
			NM[m][n] = "1";
			return NM[m][n];
		}
		if (m > n) {
			NM[m][n] = "0";
			return NM[m][n];
		}
		NM[m][n] = ADD(MUL(fun(n - 1, m), ts(m)), fun(n - 1, m - 1));
		return NM[m][n];
	}

}

int main()
{
	int n, m;
	while (cin >> n >> m) {
		cout << fun(n, m) << endl;
	}
	return 0;
}
