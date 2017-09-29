int* bubble_sort(int* a,int len)
{
	int i,j;
	for(i = 0;i < len; i++){
		for(j = i + 1;j < len;j++){
			if(a[i] > a[j])
			{
				int tmp = a[i];
				a[i] = a[j];
				a[j] = tmp;
			}//swap a[i],a[j]
		}
	}
	return a;
}
int* insert_sort(int* a, int len)
{
	int i,j,key;
	for(j = 1; j < len; j++)
	{
		key = a[j];
		// Insert a[j] into the sorted sequence a[i..j-1]
		i = j - 1;
		while( i >= 0 && a[i] < key)
		{
			a[i + 1] = a[i];
			i--;
		}// Move elements
		a[i+1] = key;
	}
	return a;
}
