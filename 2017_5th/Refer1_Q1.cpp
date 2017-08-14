#include<iostream>
using namespace std;
int sum = 1;
int s;
int a[50][50];

void judge(int x, int y){
    int tmp = a[x][y];
    a[x][y] = 0;
    if(x-1>=0 && a[x-1][y]==tmp){
        sum++;
        judge(x-1,y);
    }
    if(y-1>=0 && a[x][y-1]==tmp){
        sum++;
        judge(x,y-1);
    }
    if(x+1<s && a[x+1][y]==tmp){
        sum++;
        judge(x+1,y);
    }
    if(y+1<s && a[x][y+1]==tmp){
        sum++;
        judge(x,y+1);
    }
}

int main(){
    int m, n;
    int i, j;
    cin>>m>>n;
    cin>>s;
    for(i = 0; i < s; i++){
        for(j = 0; j < s; j++)
            cin>>a[i][j];
    }
    judge(m, n);
    cout<<sum<<endl;
    return 0;
}
