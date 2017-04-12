#include <iostream>
#include <string>
#include <regex>
using namespace std;
int main(){
    string str;
    int num;
    int i, index;
    int times[62] = {0};
    int avg = 0, left = 0;
    cin>>num;
    cin>>str;
    //www.ideone.com(在线编译运行)
    if(num < 2 || num > 10 || !std::regex_match (str, std::regex("\"[[:alnum:]]{1,50}\"(,\"[[:alnum:]]{1,50}\"){0,49}"))){
        cout<<-1<<","<<-1<<endl;
        return 0;
    }
    for(i = 0; i < str.size(); i++){
        if(str[i]>='0' & str[i] <= '9')
            index = str[i]-'0';
        else if(str[i]>='a' & str[i] <= 'z')
            index = str[i]-'a'+10;
        else if(str[i]>='A' & str[i] <= 'Z')
            index = str[i]-'A'+36;
        else
            index = -1;
        if(index != -1)
            times[index]++;
    }
    for(i = 0; i < 62; i++){
        if(times[i] != 0){
            avg = avg + times[i]/num;
            left = left + times[i]%num;
        }
    }
    cout<<avg<<","<<left<<endl;
    return 0;
}
