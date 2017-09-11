#include <stdio.h>
#include <stdlib.h>

typedef int (*func)(int);

int* map(func fun, int* list, int list_len)
{
	int i;
	for (i = 0; i < list_len; i++)
	{
		list[i] = fun(list[i]);
	}
	return list;
}

int plus(int num)
{
	return num + 2;
}

int main()
{
	int data[] = {1, 2, 3 ,4 ,5 ,6 ,7 ,8};
	int i;
	int* result = map(plus, data, 8);
	for (i = 0; i < 8; i++)
	{
		printf("%d", result[i]);
	}
	return 0;
}
