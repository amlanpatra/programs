//Bubble sort
#include<stdio.h>
int main(void)
{
	int a[] = {26, 24, 6, 12, 11, 98};
	int b = sizeof(a) / sizeof(a[0]);
	int d = 0;
	int temp, j, start = 0, count = 1;

	while (start < b)
	{
		while ((start + count) < b)
		{
			if (a[start] > a[start + count])
			{
				//swapping numbers
				temp = a[start];
				a[start] = a[start + count];
				a[start + count] = temp;
			}
			count++;
		}
		start++;
		count = 0;
	}

	for (int i = 0; i < b; ++i)
	{
		printf("%d\n", a[i] );
	}
}