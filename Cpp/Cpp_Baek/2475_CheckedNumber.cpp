#include <iostream>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int a, b, c, d, e;
    cin >> a >> b >> c >> d >> e;

    int res = a*a + b*b + c*c + d*d + e*e;
    cout << res % 10;

    return 0;
}