#include <stdio.h>
#include "fuck.h"

int main()
{
	FILE *fp;
	fp = fopen("shit.dat","rb+");
	STU stu;
	fread(&stu, sizeof(STU), 1, fp);
	printf("%d%d%s%lf",stu.num[1], stu.sum, stu.name, stu.shit);
	return 0;
}
