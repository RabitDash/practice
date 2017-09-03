#include <stdio.h>
#include <stdlib.h>

int main()
{
	int (*fptr1)(int);
	typedef int (*fptr1)(int);
	int square(int num)
	{
		return num * num;
	}

	int n = 5;
	fptr1 = square;
	printf("%d",fptr1(n));

	return 0;
}
