#define GET_ARRAY_LEN(array, len){len = (sizeof(array)/sizeof(array[0]));}
int* bubble_sort(int* ARRAY, int LENGTH);
int* insert_sort(int* ARRAY, int LENGTH);
int*   swap_sort(int* ARRAY, int LENGTH);
int*   heap_sort(int* ARRAY, int LENGTH);
int*   fuck_sort(int* ARRAY, int LENGTH);
