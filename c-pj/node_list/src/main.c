#include <stdio.h>
#include <stdlib.h>
#include "node.h"

int main()
{
	NODE *p = init();
	NODE *fuck = append(p, 930);
	printf("%d\n%d\n", p->data, fuck->data);
	return 0;
}
