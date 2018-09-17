#include <stdio.h>
#include "fuck.h"
int main()
{
	FILE *fp = fopen("shit.dat","wb");
	STU shit = {{1,2,3,4,5,6,7,8,9},3,"yesrpg!!",3.0};
	fwrite(&shit, sizeof(STU), 1, fp);
	fclose(fp);
	return 0;
}
