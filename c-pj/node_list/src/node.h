struct node;
typedef struct node
{
	int data;
	struct node* next;
}NODE;
struct node *init();
struct node *append(NODE*, int);
