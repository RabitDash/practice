#include <stdio.h>
#include <stdlib.h>
#include "node.h"
int main()
{
	NODE *p = init();
	printf("%d", p->data);
	return 0;
}
