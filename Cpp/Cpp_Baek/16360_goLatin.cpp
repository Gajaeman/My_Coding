#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    vector<string> rep(26);
    rep['a'-'a']="as";
    rep['i'-'a']="ios"; rep['y'-'a']="ios";
    rep['l'-'a']="les";
    rep['n'-'a']="anes";
    rep['o'-'a']="os";
    rep['r'-'a']="res";
    rep['t'-'a']="tas";
    rep['u'-'a']="us";
    rep['v'-'a']="ves";
    rep['w'-'a']="was";

    int n; 
    if(!(cin >> n)) return 0;
    while(n--){
        string s; cin >> s;
        int m = (int)s.size();

        if(m >= 2 && s[m-2]=='n' && s[m-1]=='e'){
            cout << s.substr(0, m-2) << "anes\n";
            continue;
        }
        char c = s.back();
        string suf = rep[c - 'a'];
        if(!suf.empty()){
            cout << s.substr(0, m-1) << suf << '\n';
        }else{
            cout << s << "us\n";
        }
    }
    return 0;
}