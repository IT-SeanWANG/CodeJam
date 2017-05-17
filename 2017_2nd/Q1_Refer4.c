#include <stdio.h>

void main()
{
    int Num;
    int Array[50];
    int opp=0,same=0; /*opp for right about and same for same direction*/

    scanf("%d",&Num);
    for (int i=1;i<=Num;i++)
        scanf("%d",&Array[i]);
    int p1 = Array[1]; /*first one is patient*/

    for(int i=1;i<=Num;i++)
    {
        if((Array[i] ^ p1) < 0){ /*right about*/
            if(Array[i]+p1<0) opp += 1; /*can meet with each other, number of patient+1*/
        }else{ /*turn around, same direction*/
            if(Array[i]<p1) same += 1; /*follow patient, can be infect*/
        }
    }

    if(opp>0) /*infect someone*/
        printf("%d\n",opp+same+1);
    else printf("1\n"); /*don't infect anyone*/
}
