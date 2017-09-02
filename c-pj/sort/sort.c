#include <stdio.h>

int main(){
	int a[] = {3,5,4,6,1,2,9,7,8};
	sort(a);
	int i;
	for(i = 0;i < 9;i++){
		printf("%d ",a[i]);
	}
}
