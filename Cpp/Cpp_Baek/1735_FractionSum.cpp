#include <iostream>
using namespace std;

int gcd(int a, int b){
    if (b == 0) return a;
    return gcd(b, a % b);
}

int main(){
    int a, b, c, d;
    cin >> a >> b >> c >> d;

    long long ja = 1LL * a * d + 1LL * b * c;
    long long mo = 1LL * b * d;

    long long g = gcd(ja, mo);

    cout << ja / g << " " << mo / g;
}