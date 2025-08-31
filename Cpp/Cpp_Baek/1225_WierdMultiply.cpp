#include <iostream>
using namespace std;

int main(){
    long long res = 0;
    string a, b;
    cin >> a >> b;
        for(int i=0; i < a.size(); i++){
            for(int k=0; k < b.size(); k++){
                res += (a[i]-'0')*(b[k]-'0');
            }
        }
        cout << res;

    return 0;
}