#include <stdio.h>
#include <stdlib.h>

typedef int (*fuck)(int);
int test(int fuck)
{
	return 122;
}
int main()
{
	fuck p = test;
	int a;
	a = p(32);
	printf("%d", a);
	return 0;
}
