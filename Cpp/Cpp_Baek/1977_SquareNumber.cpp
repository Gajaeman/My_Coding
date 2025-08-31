#include <iostream>
#include <cmath>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int m, n;
    cin >> m >> n;
    int sum = 0, mn = -1;
    for (int i = 1; i * i <= n; i++) {
        int sq = i * i;
        if (sq >= m && sq <= n) {
            sum += sq;
            if (mn == -1) mn = sq;
        }
    }
    if (mn == -1) cout << -1 << '\n';
    else cout << sum << '\n' << mn << '\n';
    return 0;
}