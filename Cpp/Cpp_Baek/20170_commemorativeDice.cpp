#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    vector<int> d1(6), d2(6);
    for(int i=0;i<6;++i) cin >> d1[i];
    for(int i=0;i<6;++i) cin >> d2[i];
    sort(d1.begin(), d1.end());
    sort(d2.begin(), d2.end());

    int win = 0;
    for(int i=0; i<6; ++i){
        for(int j=0; j<6; ++j){
            if(d1[i] > d2[j]) ++win;
        }
    }
    int de = 36;
    int g = __gcd(win, de);
    cout << win/g << '/' << de/g << '\n';

    return 0;
}