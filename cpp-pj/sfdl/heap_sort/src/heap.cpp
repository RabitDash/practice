#include <iostream>
#define SIZE 7
#define SWAP(A,B) (A)=(A)^(B);(B)=(B)^(A);(A)=(A)^(B);
#define LEFT(i) 2*(i)
#define RIGHT(i) 2*(i)+1
using namespace std;

void max_heapify(int *a, int i, int heap_size)
{
	int l = LEFT(i);
	int r = RIGHT(i);
	int largest;
	if ((l < heap_size) && (a[l] > a[i])) {
		largest = l;
	} else {
		largest = i;
	}

	if ((r < heap_size) && (a[r] > a[largest])) {
		largest = r;
	}

	if (largest != i) {
		SWAP(a[i], a[largest]);
		max_heapify(a, largest, heap_size);
	}

}

void build_max_heap(int *a, int heap_size)
{
	for (int i = SIZE / 2; i >= 0; i--) {
		max_heapify(a, i, heap_size);
	}
}

void heap_sort(int *a)
{
	int heap_size = SIZE;
	build_max_heap(a, heap_size);
	for (int i = SIZE - 1; i >= 1; i--) {
		SWAP(a[0], a[i]);
		heap_size = heap_size - 1;
		max_heapify(a, 0, heap_size);
	}
}

int main()
{
	int fuck[SIZE] = { 9, 3, 1, 4, 5, 6, 7 };
	heap_sort(fuck);
	int i;
	for (i = 0; i < SIZE; i++) {
		cout << fuck[i] << " ";
	}
	cout << endl;
	return 0;
}
