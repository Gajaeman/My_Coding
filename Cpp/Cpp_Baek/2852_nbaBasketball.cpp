#include <iostream>
#include <string>

using namespace std;

int toSec(const string& s){
    int m = stoi(s.substr(0,2));
    int sec = stoi(s.substr(3,2));
    return m*60 + sec;
}

string toMin(int x){
    int m = x / 60, s = x % 60;
    string res;
    if(m < 10) res += "0";
    res += to_string(m) + ':';
    if(s < 10) res += "0";
    res += to_string(s);
    return res;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N; cin >> N;

    int s1 = 0, s2 = 0;
    int lead = 0;
    int last = 0;
    int win1 = 0, win2 = 0;

    for(int i=0;i<N;i++){
        int team; string time;
        cin >> team >> time;
        int t = toSec(time);

        if(lead == 1) win1 += t - last;
        else if(lead == 2) win2 += t - last;

        if(team == 1) s1++;
        else s2++;

        if(s1 > s2) lead = 1;
        else if(s2 > s1) lead = 2;
        else lead = 0;

        last = t;
    }

    const int END = 48 * 60;
    if(lead == 1) win1 += END - last;
    else if(lead == 2) win2 += END - last;

    cout << toMin(win1) << "\n" << toMin(win2) << "\n";
    return 0;
}