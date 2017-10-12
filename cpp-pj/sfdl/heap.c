#include <stdio.h>
#define SIZE 7
#define SWAP(A,B) (A)=(A)^(B);(B)=(B)^(A);(A)=(A)^(B);
void heap(int*, int);
int main()
{
	int fuck[SIZE] = {9, 3, 1, 4, 5, 6, 7};
	heap(fuck, 0);
	int i;
	for(i = 0; i < 	SIZE; i++)
	{
		printf("%d ", fuck[i]);
	}
	return 0;
	//int *shit = heap(fuck);
}
void heap(int *a, int i)
{
	int l = 2 * i;
	int r = 2 * i - 1;
	int largest;
	if((l < SIZE - 1) && (a[i] < a[l]))
	{
		SWAP(a[i], a[l]);
		largest = l;
	}
	else if((r < SIZE - 1) && (a[i] < a[r]))
	{
		SWAP(a[i], a[r]);
		largest = r;
	}
	else
	{
		largest = i;
	}

	if(largest != i)
	{
		heap(a, largest);
	}

}
