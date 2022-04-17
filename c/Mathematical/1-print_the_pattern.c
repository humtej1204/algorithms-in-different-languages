#include<stdio.h>

/* Prototypes */
void printPat(int n);

/* Main Function */
int main(void)
{
	int t;
	scanf("%d",&t);
	while(t--)
	{
		int n;
		scanf("%d",&n);
		printPat(n);
		printf("\n");
	}
}
/* Function that print the pattern */
void printPat(int n)
{
	int num = n;
	/* Decending the times we have to print the numbers */
	for (; n > 0; n--)
	{
		/* Print numbers in descendant order {3, 2, 1}*/
		for (int x = num; x >= 1; x--)
		{
			/* Print number n times */
			for (int z = 0; z < n; z++)
			{
				printf("%d", x);
				printf(" ");
			}
		}
		printf("$");
	}
}
