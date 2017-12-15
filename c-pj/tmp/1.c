#include <stdio.h>
#define MIN(x,y) (x)>(y)? (x):(y)
int main()
{
	int i=10, j=15, k;
	k = 10*MIN(i,j);
	printf("%d\n",k);
	return 0;
}
