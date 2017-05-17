#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void get_input(int *goods_num, int comb[11][11])
{
	int i =0;	
	int j =0;

	scanf("%d",goods_num);

	for (i=0;i<*goods_num;i++)
	{
		for (j=0;j<*goods_num;j++)
		{
			scanf("%d", &comb[i][j]);
		}
	}
}

void delete_com(int row, int col, int num, int comb[11][11], int res_comb[11][11])
{

	int i = 0;
	int j = 0;
	int temp1[11][11];
	int temp2[11][11];
	int temp3[11][11];
	int flag = 0;

	for (i=0;i<num;i++)
	{
		flag = 0;
		for (j=0;j<num;j++)
		{
			if (j==row)
				flag =1;
			if (flag)
				temp1[i][j]= comb[i][j+1];
			else
				temp1[i][j]= comb[i][j];
			#if DEBUG
			//printf("1temp1[%d][%d] %d\n",i,j,temp1[i][j]);
			#endif
		}
	}

	for (i=0;i<num;i++)
	{
		flag=0;
		for (j=0;j<num-1;j++)
		{
			if (j==(col-1))
				flag=1;
			if (flag)
				temp2[i][j]= temp1[i][j+1];
			else
				temp2[i][j]= temp1[i][j];

			#if DEBUG
			//printf("2temp2[%d][%d] %d\n",i,j,temp2[i][j]);
			#endif
		}
	}

	flag=0;
	for (i=0;i<num;i++)
	{
		if (i==row)
			flag=1;
		if (flag)
		{
			for (j=0;j<num-2;j++)
			{
				temp3[i][j]= temp2[i+1][j];
				#if DEBUG
				//printf("3-1temp2[%d][%d] %d\n",i,j,temp3[i][j]);
				#endif
			}
		}
		else
		{
			for (j=0;j<num-2;j++)
			{
				temp3[i][j]= temp2[i][j];
				#if DEBUG
				//printf("3-2temp2[%d][%d] %d\n",i,j,temp3[i][j]);
				#endif
			}
		}

	}

	flag=0;
	for (i=0;i<num-1;i++)
	{
		if (i==(col-1))
			flag=1;
		if (flag)
		{
			for (j=0;j<num-2;j++)
			{
				res_comb[i][j]= temp3[i+1][j];
				#if DEBUG
				//printf("4-1res_comb[%d][%d] %d\n",i,j,res_comb[i][j]);
				#endif
			}
		}
		else
		{
			for (j=0;j<num-2;j++)
			{
				res_comb[i][j]= temp3[i][j];
				#if DEBUG
				//printf("4-2res_comb[%d][%d] %d\n",i,j,res_comb[i][j]);
				#endif
			}
		}
	}
}

int get_max(int comb[11][11], int goods_num)
{
	int i = 0;
	int j = 0;
	int x = 0;
	int y = 0;

	int temp_comb[11][11];
	int temp_max=0;
	int max_price = 0;


	if (goods_num == 2)
		return comb[0][1];

	if (goods_num == 3)
	{
		temp_max = comb[0][1];
		
		if (temp_max<comb[0][2])
			temp_max = comb[0][2];

		if (temp_max < comb[1][2])
			temp_max=comb[1][2];

		return temp_max;
	}

	for (i=0;i<goods_num;i++)
	{
		for (j=0;j<goods_num;j++)
		{
			if ((j>0)&&(i!=j)&&(i<j))
			{
				delete_com(i,j,goods_num,comb,temp_comb);

				#if DEBUG
				printf ("row=%d, col=%d\n",i,j);
				for (x=0;x<goods_num-2;x++)
				{
					for (y=0;y<goods_num-2;y++)
					{
						printf("%d ", temp_comb[x][y]);
					}
					printf("\n");
				}
				#endif

				temp_max = comb[i][j]+get_max(temp_comb,goods_num-2);

				max_price = max_price > temp_max ? max_price:temp_max;

				#if DEBUG
				printf("comb[%d][%d] %d, get_max %d, max_price %d\n",
					i,j,comb[i][j],temp_max-comb[i][j],max_price);
				#endif
			}
		}
	}
	return max_price;
}

int main()
{
	int i =0;	
	int j =0;
	int goods_num=0;
	int comb_goods[11][11];
	int max=0;


	//get input
	get_input(&goods_num, comb_goods);

	#if DEBUG
	printf("goods num %d\n",goods_num);

	for (i=0;i<goods_num;i++)
	{
		for (j=0;j<goods_num;j++)
		{
			printf("%d ", comb_goods[i][j]);
		}
		printf("\n");
	}
	#endif

	max = get_max(comb_goods,goods_num);

	printf("%d\n",max);

	return 0;
}



