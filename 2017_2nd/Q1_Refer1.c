#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct blind_man
{
	int position;
	int direction;
} blind;


void get_blind(blind *blind_man)
{
	int temp;
	scanf("%d",&temp);
	if (temp>0)
	{
		blind_man->position = temp;
		blind_man->direction = 1;
	}
	else
	{
		blind_man->position = 0-temp;
		blind_man->direction = 0;		
	}
}

int main()
{
	int i =0;	

	int blind_num = 0;
	blind blind_man[50];
	int illness_man = 0;
	int left_positive = 0;
	int left_opposite = 0;
	int right_positive = 0;
	int right_opposite = 0;


	//get input
	scanf("%d",&blind_num);

	#if DEBUG
	printf("blind num %d\n",blind_num);
	#endif

	get_blind(&blind_man[0]);
	#if DEBUG
    printf("i=0, position %d direction %d\n", blind_man[0].position, blind_man[0].direction);
    #endif

	for (i=1;i<blind_num;i++)
	{
		get_blind(&blind_man[i]);
		#if DEBUG
		printf("i=%d, position %d direction %d\n", i, blind_man[i].position, blind_man[i].direction);
		#endif

		if (blind_man[i].position > blind_man[0].position)
		{
			if (blind_man[i].direction==1)
				right_positive++;
			else
				right_opposite++;
		}
		else
		{
			if (blind_man[i].direction==1)
				left_positive++;
			else
				left_opposite++;
		}
	}

	if (blind_man[0].direction==1)
	{
		if (right_opposite>0)
			illness_man = right_opposite+left_positive+1;
		else
			illness_man = 1;
	}
	else
	{
		if (left_positive>0)
			illness_man = left_positive+right_opposite+1;
		else
			illness_man = 1;
	}

	#if DEBUG
	printf("illness_man %d\n",illness_man);
	#else
	printf("%d\n",illness_man);
	#endif
	

	return 0;
}

