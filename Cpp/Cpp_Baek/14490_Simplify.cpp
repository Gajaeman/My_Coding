#include <iostream>
using namespace std;

    int gcd(int a, int b){
        if(a==0) return b;
        return gcd(b%a,a);
    }

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int num = 0, save = 0;
    string s;
    cin >> s;

    for(char c : s){
        if(c==':') {
            save = num;
            num = 0;
            continue;
        }
        num = num * 10 + (int) (c-'0');
    }

    int cal = gcd(num, save);
    num /= cal;
    save /= cal;

    cout << save << ':' << num;
    return 0;
}