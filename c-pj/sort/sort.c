#include <stdio.h>
int* bubble_sort(int* a,int len)
{
	printf("%d",len);
	int i,j;
	for(i = 0;i < len; i++){
		for(j = i + 1;j < len;j++){
			if(a[i] > a[j])
			{
				int tmp = a[i];
				a[i] = a[j];
				a[j] = tmp;
			}//swap a[i],a[j]
		}
	}
	return a;
}

