#include<iostream>
#include<string.h>
#include<algorithm>
using namespace std;
int main(){
    string line[9];
    int i, j, k;
    int box[9][9];
    int check[27][9];
    int tmp[10]={0};
    int flag = 1;
    for(i = 0; i < 9; i++){
        cin>> line[i];
    }
    for(i = 0; i < 9; i++){
        j = k = 0;
        while(line[i][k] != '\0'){
            if(line[i][k] == ','){
                k++;
                continue;
            }
            box[i][j] = line[i][k]-'0';
            j++;
            k++;
        }
    }
    for(i = 0; i < 9; i++){
        for(j = 0; j < 9; j++){
             check[i][j] = box[i-i%3+j/3][i%3*3+j%3];
        }
    }
    for(i = 0; i < 9; i++){
        for(j = 0; j <9; j++){
            check[i+9][j]=box[i][j];
        }
    }
    for(j = 0; j < 9; j++){
        for(i = 0; i <9; i++){
            check[j+18][i]=box[i][j];
        }
    }
    for(i = 0; i < 27; i++){
        for(j = 0; j <9; j++){
            tmp[j+1] = check[i][j];
        }
        sort(tmp,tmp+10);
        for(j = 0; j <9; j++){
            check[i][j] = tmp[j+1];
            if(tmp[j+1] == tmp[j]){
                flag = -1;
                break;
            }
        }
    }
    cout<<flag<<endl;
    return 0;
}
