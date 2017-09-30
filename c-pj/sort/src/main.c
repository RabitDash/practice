#include <stdio.h>
#include "sort.h"
int main(int argv,char* argc)
{
	int a[] = {1, 3, 6, 4, 8, 9, 2, 5, 7};
	insert_sort(a, 9);
	int i;
	for(i = 0;i < 9; i++)
	{
		printf("%d",a[i]);
	}
}
