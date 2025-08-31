#include <iostream>
#include <string>
using namespace std;

int main(){
    int t;
    cin >> t;

    while(t--){
        int idx;
        string s;
        cin >> idx >> s;

        s.erase(idx - 1, 1);
        cout << s << '\n';
    }
}