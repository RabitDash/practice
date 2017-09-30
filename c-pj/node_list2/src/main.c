#include <stdio.h>
#include <stdlib.h>

int main()
{
	SqList L;
	if (InitList(&L))
	{
		Elemtype e;
		printf("init_success\n");
		int i;

		for (i = 0;i < 10;i++)
		{
			InsertElem(&L,i + 1,i);
		}
		printf("length is %d\n",getLength(L));


		if(GetElem(L,1,&e))
		{
			printf("The first element is %d\n",e);
		}
		else
		{
			printf("element is not exist\n");
		}


		if (isEmpty(L))
		{
			printf("list is empty\n");
		}
		else
		{
			printf("list is not empty\n");
		}



		printf("The 5 at %d\n",FindElem(L,5,*compare));

		PreElem(L,6,&e);
		printf("The 6's previous element is %d\n",e);

		NextElem(L,6,&e);
		printf("The 6's next element is %d\n",e);

		DeleteElem(&L,1,&e);
		printf("delete first element is %d\n",e);
		printf("list:");

		TraverseList(L,visit);
		if(DestroyList(&L))
		{
			printf("\ndestroy_success\n");
		}
	}
	return 0;
}
