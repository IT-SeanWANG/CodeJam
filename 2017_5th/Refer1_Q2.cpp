#include<iostream>
#include<algorithm>
using namespace std;

int main(){
    int m, n;//M：Lab；N：Robert
    int p[50];//P：每个机器人的性能及价格
    int k[50];//第j个机器人在安全值为L时可以管理的Lab数
    int avg;//n个机器人管理m个Lab的平均安全值
    int sum = 0;//n个机器人总性能
    int l, y;
    int i, j;
    int s;
    int cap = 0;
    int lab = 0;
    int dp[16001];
    int ans = 15001;
    cin>>m>>n;
    for(i = 1; i <= n; i++){
        cin>>p[i];
        sum += p[i];
    }
    avg = sum / m;
    sort(p+1,p+n+1);
    reverse(p+1,p+n+1);
    for(i = avg; i > 0; i--){
        int sn = 0;
        for(j = 1; j <= n; j++){
            k[j] = p[j]/i;
            sn += k[j];
        }
        if(sn >= m){
            l = i;
            s = sn;
            break;
        }
    }

    for(j = 0; j <= 16000; j++)
        dp[j] = 15001;
    dp[0] = 0;
    for(i = 1; i <= n && lab < m; i++){
        cap += p[i];
        lab += k[i];
    }

    for(i = 1; i <= n; i++){
        for(j = lab+n; j >= k[i]; j--){
            dp[j] = min(dp[j], dp[j-k[i]]+p[i]);
        }
    }

    for(j = m; j <= lab+n; j++){
        ans = ans<dp[j]?ans:dp[j];
    }
    cout<<l<<" "<<ans<<endl;

    return 0;
}
