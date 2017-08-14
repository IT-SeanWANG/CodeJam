#include <stdio.h>
#include <stdlib.h>

int main()
{
	int m, n;
	int *a;
	scanf("%d", &m);
	scanf("%d", &n);

	a=(int *)malloc(n*sizeof(int));
	int i=0;
	int j=0;
	for(i=0; i<n; i++)
	{
		scanf("%d", &a[i]);
	}

///sort

	int maxl=0;
	int sum=0;
	for(i=0; i<n; i++)
		sum +=a[i];
	maxl=sum/m;
//judge
	int tmpsum=0;
	while(1)
	{
		tmpsum=0;
		for(i=0; i<n; i++)
			tmpsum+=(a[i]/maxl);
		if(tmpsum >= m)
			break;
		else
			maxl--;
	}
/////find max L
/////become 01bag question.
	int *w=(int *)malloc(n*sizeof(int));
	for(i=0; i<n; i++)
		w[i]=a[i]/maxl;
	int bagsize=tmpsum-m;
	int** bagM;
	bagM=(int **)malloc(n*sizeof(int *));
	for(i=0; i<n; i++)
		bagM[i]=(int *)malloc((bagsize+1)*sizeof(int));

	for(i=0; i<n; i++)
	{
		for(j=0; j<bagsize+1; j++)
			bagM[i][j]=0;
	}
	

	for(i=0; i<=bagsize; i++)
	{
		for(j=0; j<n; j++)
		{
			if(w[j]>i)  ///can't load
			{
				if(j==0)
				{
					bagM[j][i]=0;
				}
				else
				{
					bagM[j][i]=bagM[j-1][i];
				}
			}
			else
			{
				if(j==0)
				{
					bagM[j][i]=a[j];
				}
				else
				{
					int tmp=bagM[j-1][i-w[j]]+a[j];
					bagM[j][i]=tmp>bagM[j-1][i]?tmp:bagM[j-1][i];
				}
			}
		}
	}

	int maxvalue=0;

	maxvalue=bagM[n-1][bagsize];
	printf("%d %d\n", maxl, sum-maxvalue);

	for(i=0; i<n; i++)
		free(bagM[i]);
	free(bagM);


	free(a);
	return 0;
}
