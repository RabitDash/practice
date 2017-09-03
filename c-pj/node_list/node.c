#include <stdlib.h>
struct node{
	int data;
	struct node *next;
};
struct node *init()
{
	struct node *a;
	a = (struct node*) malloc(sizeof(struct node));
	a->data = 1231;
	a->next = NULL;
	return a;
}
