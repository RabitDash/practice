#include <stdio.h>

int product(int, int);

int main()
{
	int x, y, s;
	scanf("%d %d", &x, &y);
	s = product(x, y);
	printf("The mul is:%d", s);
	return 0;
}

int product(int a, int b)
{
	int mul;
	mul = a * b;
	return mul;
}
