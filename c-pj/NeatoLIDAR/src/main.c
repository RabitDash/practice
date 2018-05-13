//Linux COM
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct {
	unsigned char distanceL;
	unsigned char invalidFlag:1;
	unsigned char strwarnFlag:1;
	unsigned char distanceH:6;
	unsigned char signalstrL;
	unsigned char signalstrH;
} DATA;

typedef struct {
	unsigned char start;
	unsigned char index;
	unsigned char speedL;
	unsigned char speedH;
	DATA Data0;
	DATA Data1;
	DATA Data2;
	DATA Data3;
	unsigned char checksumL;
	unsigned char checksumH;
} PACK;
PACK* receive(FILE *fp)
{
	char buf[100];
	PACK* pack = (PACK*) malloc(sizeof(PACK));
	fgets(buf, 100, fp);
	int i;
	for(i = 0; i < 70; i++)
	{
		if(buf[i] == '\xFA')
		{
			memcpy(pack, &buf[i], sizeof(PACK));
			return pack;
		}
	}
}
int main()
{
	FILE *fp;
	PACK *pack;
	pack = (PACK *) malloc(sizeof(PACK));
	printf("%d\n", sizeof(PACK));
	fp = fopen("/dev/ttyUSB0", "r");
	if (fp == NULL)
		printf("shit");
	else {
		pack = receive(fp);
	}
	//do not close fp
	printf("%X\n", pack->start);
	printf("%u\n", pack->Data0.distanceL);
	return 0;
}
