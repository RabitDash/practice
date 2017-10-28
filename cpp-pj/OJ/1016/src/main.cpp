/*
题目描述:

给定两个数的分子和分母，求两个分数的和。
输入描述：

多组输入，每组输入包含4个正整数a，b，c，d（0 < a,b,c,d < 1000），依次代表第一个数的分子，第一个数的分母，第二个数的分子，第二个数的分母
输出描述：

对于每组数据，输出的两个分数的和的小数形式，结果保留小数点后4位。
*/
#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
	int a, b; // 第一个分数 a/b
	int c, d; // 第二个分数 c/d
	double shit, fuck, result; // 分数shit/fuck,存储在result中
	while(cin >> a >> b >> c >> d)
	{
		fuck = b * d;
		shit = a * d + b * c;
		result = shit / fuck;
		cout  << setprecision(4) << fixed << result << endl;
	}
	return 0;
}
