#include <iostream>
using namespace std;

#define MAX_P 10000
#define MAX_T 1000000000
int t_start; //start time
int t_end; //end time
int p_num; //process number
int s_arr[MAX_P]; //each process start time
int e_arr[MAX_P]; //each process end time
int p_max=0; //max number of process during the period
int p_min=0; //min number of process during the period

/*quick sort*/
int partition(int number[], int left, int right)
{
  int i, j, s;
  s = number[right];
  i = left - 1;
  int temp;
  for (j = left; j < right; j++)
  {
    if (number[j] <= s)
    {
      i++;
	  temp = number[i];
	  number[i] = number[j];
	  number[j] = temp;

    }
  }
  temp = number[i + 1];
  number[i + 1] = number[right];
  number[right] = temp;
  return i + 1;
}

void quicksort(int number[], int left, int right)
{
  int q;
  if (left < right)
  {
    q = partition(number, left, right);
    quicksort(number, left, q - 1);
    quicksort(number, q + 1, right);
  }
}
/*quick sort*/

int main()
{
	//cout<<"input start time and end time:";
	cout<<"ÊäÈë:"<<endl;
	cin>>t_start>>t_end;
	if(!(0<=t_start&&t_start<=t_end&&t_end<=MAX_T))
	{
		cout<<"invalid input for start/end time"<<endl;
		return 0;
	}
	//cout<<"input number of process:";
	cin>>p_num;
	if(!(1<=p_num&&p_num<=MAX_P))
	{
		cout<<"invalid input for number of process"<<endl;
		return 0;
	}
	for(int k=0;k<p_num;k++)
	{
		//cout<<"input process#"<<k+1<<" start and end:";
		cin>>s_arr[k]>>e_arr[k];
		if(!(0<=s_arr[k]&&s_arr[k]<=MAX_T&&0<=e_arr[k]&&e_arr[k]<=MAX_T))
		{
			cout<<"invalid input for start/end time of process"<<endl;
			return 0;
		}
	}

	//sort for process start/end time
	quicksort(s_arr, 0, p_num-1);
	quicksort(e_arr, 0, p_num-1);

	int i = 0;
	int j = 0;
	int count = 0;
	//calculate begin number of process

	//statistic all the start process and end process
	//then start minus begin equals to the number of process
	//at the moment of t_start
	while(s_arr[i]<=t_start||e_arr[j]<=t_start)
	{
		if(s_arr[i]<=t_start)
		{
			i++;
			count++;
		}
		else
		{
			j++;
			count--;
		}
	}

	p_max = p_min = count;

	//calculate max and min process during that period
	//from the moment of t_start, check the start process array and end process array in order
	//to the moment of t_end; once the count of process in same moment increase or decrease
	//compare the max process number and min process number with the count, and exchange
	while(((s_arr[i]<=t_end)||(e_arr[j]<=t_end))&&i<p_num&&j<p_num)
	{
		if(s_arr[i]<=t_end&&s_arr[i]>0&&s_arr[i]<=e_arr[j])
		{
			i++;
			count++;
		}
		else
		{
			j++;
			count--;
		}
		if(p_max<count)
			p_max = count;
		if(p_min>count)
			p_min = count;
	}

	cout<<"Êä³ö:"<<endl;
	cout<<p_min<<endl;
	cout<<p_max<<endl;
	return 0;
}