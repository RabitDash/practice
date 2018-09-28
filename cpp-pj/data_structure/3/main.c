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

Node* Reverse(Node* h1)
{
	Node *h2, *p, *headnode;
	headnode = h1;
    h2 = h1->next;
    h1 = h1->next->next;
	h2->next = NULL;
	p = h2;
	while(h1 != NULL)
	{
		h2 = h1;
        h1 = h1->next;
        h2->next = p;
		p = h2;
	}
    headnode->next = p;
	return headnode;
}
int main()
{
	Node *head, *h1;
	head = InitList();
	int i;
	for(i = 0; i < 20; i++)
	{
		Append(head, i);
	}
	h1 = head;
	while(head->next != NULL)
	{
		printf("%d ", head->next->elem);
		head = head->next;
	}
	head = Reverse(h1);
    while(head->next != NULL)
    {
        printf("%d ", head->next->elem);
        head = head->next;
    }
	return 0;
}
