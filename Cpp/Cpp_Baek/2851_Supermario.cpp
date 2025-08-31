#include <iostream>
#include <cmath>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int ans = 0, sum = 0;
    for (int i = 0; i < 10; i++) {
        int x;
        cin >> x;
        sum += x;
        int d_new = abs(100 - sum);
        int d_old = abs(100 - ans);
        if (d_new < d_old || (d_new == d_old && sum > ans)) ans = sum;
    }
    cout << ans << '\n';
    return 0;
}