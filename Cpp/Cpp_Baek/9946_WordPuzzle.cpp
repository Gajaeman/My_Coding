#include <iostream>
#include <algorithm>
using namespace std;

string str, pic;
int cnt = 1;
int main(){
    while(true){
        cin >> str >> pic;
        if(str == "END" && pic == "END") break;
        sort(str.begin(), str.end());
        sort(pic.begin(), pic.end());
        if(str == pic) cout << "Case " << cnt << ": " << "same" << '\n';
        else cout << "Case " << cnt << ": " << "different" << '\n';
        cnt += 1;
    }
}