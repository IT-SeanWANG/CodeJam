#include<iostream>
using namespace std;
bool runnian(int y){
    return (y%400 == 0 || (y%4 == 0 && y%100 != 0));
}

bool isDate(int d, int m, int y){
    if(d == 0 || m == 0 || y == 0)
        return false;
    if(m == 1 || m == 3 || m == 5 || m == 7 || m == 8 || m == 10 || m == 12){
        if(d <= 31){
            return true;
        }else{
            return false;
        }
    }else if(m == 4 || m == 6 || m == 9 || m == 11){
        if(d <= 30){
            return true;
        }else{
            return false;
        }
    }else if(m == 2){
        if(runnian(y) && d <=29 || !runnian(y) && d <= 28){
            return true;
        }else{
            return false;
        }
    }else{
        return false;
    }
}
bool judge(int *arr){
    int h = 0;
    int a = 0;
    for(int i = 0; i < 9; i++)
        h = h + arr[i]*(10-i) + arr[i+9]*(10-i);
    h = h % 19;
    a = h<=9?h:(19-h);
    return a == arr[18];
}

int main(){
    long long counter = 0;
    int Bnum = 0;
    int ID[19];
    int Bpos[19];
    int B[19];
    long long circle = 1;
    string str;
    string istr;
    int DD;
    int MM;
    int YYYY;
    cin>>str;
    istr = str;
    istr.erase(istr.begin()+8,istr.begin()+19);
    //cout<<istr<<endl;
    for(int i = 0; i < str.length(); i++){
        if(str[i] == 'B'){
            Bpos[Bnum] = i;
            Bnum++;
            circle *= 10;
        }else{
            ID[i] = str[i] - '0';
        }
    }

    if(Bpos[Bnum-1] == 18 && istr == "BBBBBBBB"){
        counter = (366*2424+365*(9999-2424));
        for(int i = 1; i <= Bnum-9; i++)
            counter *= 10;
    }else if(Bpos[Bnum-1] == 18){
        //cout<<"here"<<endl;
        counter = 1;
        long long circle2 = circle;
        int datenum = 0;
        int datepos = 0;
        for(int i = 0; i < Bnum; i++){
            if(Bpos[i] >= 8){
                counter *= 10;
                circle2 /= 10;
            }else{
                datepos++;
            }
        }
        counter /=10;
        //cout<<counter<<" "<<circle2<<endl;
        if(Bpos[0] == 0){
            circle2 *= 0.4;
        }
        for(int i = 0; i < circle2; i++){
            int k = i;
            for(int j = datepos-1; j >= 0; j--){
                ID[Bpos[j]] = k%10;
                k /= 10;
            }
            DD = ID[0]*10+ID[1];
            MM = ID[2]*10+ID[3];
            YYYY = ID[4]*1000+ID[5]*100+ID[6]*10+ID[7];
            if(DD == 0 || DD > 31 || MM == 0 || MM > 12 || YYYY == 0)
                continue;
            if(isDate(DD, MM, YYYY)){
                datenum++;
            }
        }
        counter *= datenum;
    }else{
        if(Bpos[0] == 0){
            circle *= 0.4;
        }
        for(int i = 0; i < circle; i++){
            int k = i;
            for(int j = Bnum-1; j >= 0; j--){
                ID[Bpos[j]] = k%10;
                k /= 10;
            }
            /*
            for(int hh = 0; hh < 19; hh++){
                cout<<ID[hh]<<" ";
            }
            cout<<endl;*/
            DD = ID[0]*10+ID[1];
            MM = ID[2]*10+ID[3];
            YYYY = ID[4]*1000+ID[5]*100+ID[6]*10+ID[7];
            if(DD == 0 || DD > 31 || MM == 0 || MM > 12 || YYYY == 0)
                continue;
            if(isDate(DD, MM, YYYY) && judge(ID)){
                counter++;
            }
        }
    }
    cout<<counter<<endl;

}
