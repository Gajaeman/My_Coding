#include <iostream>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    string s;
    int cnt = 0;
        while(cin>>s){
            cnt ++;
        }
    cout << cnt;
    return(0);
}


'''
#sol_2 getline을 이용해 한 줄 모두 입력

#include <iostream>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    string s;
    getline(cin, s);

    int cnt = 0;
    for(auto c : s){
        cnt += (c== ' ');
    }
    cnt -= (s[0] == ' ');
    cnt -= (s[s.length()-1] == ' ');

    cout << cnt+1 << '\n';
    
}
'''