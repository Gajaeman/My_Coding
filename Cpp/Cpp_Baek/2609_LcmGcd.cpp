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

    int p, q;
    cin >> p >> q;
    cout << gcd(p,q) << '\n' << lcm(p,q);

    return 0;
}