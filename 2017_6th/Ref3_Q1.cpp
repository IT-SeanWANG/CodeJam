#include<iostream>
#include<vector>
using namespace std;

int main(){
    int n, k, m;
    vector<int> v;
    cin>>n>>k>>m;
    for(int i = 0; i < n; i++){
        v.push_back(i);
    }
    int x;
    int first = v[k-1];
    x = k-1;
    if(v.size() > 2){
        v.erase(v.begin()+k-1);
        x = x+m-1;
        x %= v.size();
        //cout<<v[x]+1<<" out!"<<endl;
        v.erase(v.begin()+x);
        if(x<first){
            v.insert(v.begin()+k-2,first);
            x = x+m-1;
        }
        else{
            v.insert(v.begin()+k-1,first);
            x = x+m;
        }
    }
    while(v.size() > 2){
        x %= v.size();
        v.erase(v.begin()+x);
        x = x+m-1;
    }
    cout<<v[0]+1<<" "<<v[1]+1<<endl;
}
