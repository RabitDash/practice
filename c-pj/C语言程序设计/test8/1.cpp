#include <stdio.h>

void sort(int *a);

int main()
{
	int a[10];
	int i;
	for(i=0;i<10;i++)
		scanf("%d",&a[i]);
	sort(a);
	for(i=0;i<10;i++)
		printf("%d ",a[i]);
	return 0;
}

void sort(int *a)
{
	int i,j;
	for(i=0;i<10;i++)
		for(j=0;j<10;j++)
			if(a[j] < a[i])
			{
				a[j] ^= a[i];
				a[i] ^= a[j];
				a[j] ^= a[i];
			}
}
