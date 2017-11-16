#include <iostream>
using namespace std;
void learn_lambda_func_1()
{
	int value_1 = 1;
	auto copy_value_1 = [value_1]
	{
		return value_1;
	};
	value_1 = 100;
	auto stored_value_1 = copy_value_1();
	cout << "value_1=" << value_1 << endl;
	cout << "stored_value_1=" << stored_value_1 << endl;
}
void learn_lambda_func_2()
{
	int value_2 = 1;
	auto copy_value_2 = [&value_2]
	{
		return value_2;
	};
	value_2 = 100;
	auto stored_value_2 = copy_value_2();
	cout << "value_2=" << value_2 << endl;
	cout << "stored_value_2=" << stored_value_2 << endl;
}
int main()
{
	learn_lambda_func_1();
	learn_lambda_func_2();
	return 0;
}
