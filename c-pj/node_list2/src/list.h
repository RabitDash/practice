typedef int Status;
typedef int Elemtype;
//Storage structure
typedef struct
{
	Elemtype *elem;
	int length;
	int size;
}SqList;

Status InitList(SqList *L);
Status DestroyList(SqList *L);
Status ClearList(SqList *L);
Status isEmpty(const SqList L);
Status getLength(const SqList L);
Status GetElem(const SqList L, int i, Elemtype *e);
Status compare(Elemtype e1,Elemtype e2);
Status FindElem(const SqList L,Elemtype e,Status (*compare)(Elemtype, Elemtype));
Status PreElem(const SqList L,Elemtype cur_e,Elemtype *pre_e);
Status NextElem(const SqList L ,Elemtype cur_e,Elemtype *next_e);
Status InsertElem(SqList *L,int i, Elemtype e);
void visit(Elemtype e);
Status DeleteElem(SqList *L,int i ,Elemtype *e);
Status TraverseList(const SqList L , void (*visit)(Elemtype));
