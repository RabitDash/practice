#include <stdio.h>
#include <stdlib.h>
#define ARRAY_LENGTH(ARRAY,LEN){(LEN) = ((sizeof(ARRAY)) / (sizeof(ARRAY[0])));}
int main()
{
	int a[] = {1, 2, 3, 4, 5};
	int *p = a;
	int i;
	int len;
	ARRAY_LENGTH(a,len);
	for(i = 0; i < len; i++)
	{
		printf("%d", *(p+i));
	}
	return 0;
}
