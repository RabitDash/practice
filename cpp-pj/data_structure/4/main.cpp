#include <cstdio>
#include <cstdlib>

using namespace std;

typedef struct{
	int* elem;
	int length;
	int listsize;
} SqList;

void MergeList_Sq(SqList La, SqList Lb, SqList& Lc){
	pa = La.elem;pb = Lb.elem;
	Lc.listsize = Lc.length = La.length + Lb.length;
	pc = Lc.elem = (int*) malloc(Lc.listsize * sizeof(int));
	if(!Lc.elem) exit(-1);
	pa_last = La.elem + La.length - 1;
	pb_last = Lb.elem + Lb.length - 1;
	while(pa <= pa)
