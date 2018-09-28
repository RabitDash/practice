#include <stdio.h>
#include <stdlib.h>

typedef struct Node{
	int elem;
	struct Node* next;
} Node;

Node* InitList(){
	Node* head;
	head = (Node*)malloc(sizeof(Node));
	head->next = NULL;
	return head;
}

void Append(Node* head, int elem)
{
	Node* p = head;
	while(p->next != NULL)
	{
		p = p->next;
	}
	p->next = (Node*)malloc(sizeof(Node));
	p->next->elem = elem;
	p->next->next = NULL;
}
int main()
{
	Node* head;
	head=InitList();
	int i;
	for(i = 0; i < 20; i++)
	{
		Append(head, i);
	}
	while(head->next != NULL)
	{
		printf("%d ", head->elem);
		head = head->next;
	}
	return 0;
}
