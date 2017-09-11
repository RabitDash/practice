#include <stdio.h>

int fuck()
{
	static int i;
	i = 12;
	printf("\nfuck:%d", i);
	return 0;
}
