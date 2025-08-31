#include <iostream>
#include <string>
using namespace std;

int main(){
    string a, b;
    cin >> a >> b;
    int max = 0, n = b.size() - a.size();

    for(int i = 0; i<=n; i++){
        int cnt = 0;
        string comp = b.substr(i, a.size());
        
        for(int k = 0; k<a.size(); k++){
            if(a[k] == comp[k]) cnt += 1;
        }
        if(cnt > max) max = cnt;
    }
    cout << a.size() - max;
}