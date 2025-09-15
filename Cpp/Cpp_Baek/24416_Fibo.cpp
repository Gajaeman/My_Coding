#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n; 
    cin >> n;

    long long f[41] = {0, 1, 1};
    for (int i = 3; i <= n; ++i) f[i] = f[i-1] + f[i-2];

    cout << f[n] << ' ' << (n <= 2 ? 0 : n - 2) << '\n';
    return 0;
}