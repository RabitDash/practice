#include <stdlib.h>
typedef struct node{
	int data;
	struct node *next;
} NODE;
NODE* init()
{
	NODE *head;
	head = (NODE*) malloc(sizeof(NODE));
	head->data = 1231;
	head->next = NULL;
	return head;
}

NODE* append(NODE* head, int data)
{
	NODE* append;
	NODE* now;
	now = head;
	while(now->next != NULL)
	{
		now->next = now->next->next;
	}
	append = (NODE*) malloc(sizeof(NODE));
	append->data = data;
	now->next = append;
	return append;
}	
