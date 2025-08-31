#include <iostream>
using namespace std;

    int gcd(int a, int b){
        if(a==0) return b;
        return gcd(b%a,a);
    }

    int lcm(int c, int d){
        return c/gcd(c,d)*d;
    }

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t;
    cin >> t;

    while (t--){
        int p, q;
        cin >> p >> q;
        cout << lcm(p,q) << ' ' << gcd(p,q) << '\n';
    }
    return 0;
}