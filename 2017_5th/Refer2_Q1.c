#include <stdio.h>
#include <stdlib.h>

struct point
{
	int x;
	int y;
};

int n;
int **a;
int **flag;
struct point *p;
int start_p;
int end_p;

void Push(int x, int y)
{
	struct point p1;
	p1.x=x;
	p1.y=y;
	p[end_p++]=p1;
}
void Delete(int x, int y)
{
	start_p++;
}

void Judge(int x, int y, int value)
{
	if(a[x][y]==value && flag[x][y]==0)
	{
		flag[x][y]=1;
		Push(x, y);
	}
}

void Round(int x, int y)
{
	if(x<n-1)
		Judge(x+1, y, a[x][y]);
	if(y<n-1)
		Judge(x, y+1, a[x][y]);
	if(x>0)
		Judge(x-1, y, a[x][y]);
	if(y>0)
		Judge(x, y-1, a[x][y]);
	
	Delete(x, y);
}

int main()
{
	int x, y;
	scanf("%d %d", &x, &y);
	scanf("%d", &n);
	
	a=(int **)malloc(n*sizeof(int *));
	flag=(int **)malloc(n*sizeof(int *));
	p=(struct point *)malloc(n*n*sizeof(struct point));
	start_p=0;
	end_p=0;
	int i=0;
	for(i=0; i<n; i++)
	{
		a[i]=(int *)malloc(n*sizeof(int));
		flag[i]=(int *)malloc(n*sizeof(int));
	}
	int j=0;
	for(i=0; i<n; i++)
		for(j=0; j<n; j++)
		{
			scanf("%d", &a[i][j]);
			flag[i][j]=0;
		}

	Judge(x, y, a[x][y]);
	while(start_p <end_p)
	{
		Round(p[start_p].x, p[start_p].y);
	}
	int sum=0;
	for(i=0; i<n; i++)
		for(j=0; j<n; j++)
		{
			if(flag[i][j]==1)
				sum++;
		}

	printf("%d\n", sum);

	for(i=0; i<n; i++)
	{
		free(a[i]);
		free(flag[i]);
	}
	free(a);
	free(flag);
	free(p);

	return 0;
}

