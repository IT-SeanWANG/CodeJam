#include<iostream>
#include<string.h>
using namespace std;
int main(){
    string str;
    int i, j;
    long long dp[501] = {0};
    int coin[10] = {0};
    int n, m;
    cin>>n;
    cin>>str;
    j = 0;
    for(i = 0; str[i] != '\0'; i++){
        if(str[i] != ',')
            coin[j] = coin[j]*10+str[i]-'0';
        else
            j++;
    }
    m = j+1;
    dp[0] = 1;
    for(i = 0; i < m; i++){
        for(j = coin[i]; j <= n; j++){
            dp[j] += dp[j-coin[i]];
        }
    }
    cout<<dp[n]<<endl;
    return 0;
}
