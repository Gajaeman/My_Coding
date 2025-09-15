#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    if (n == 0) { cout << 0; return 0; }

    long long a = 0, b = 1;
    for (long long i = 2; i <= n; ++i) {
        long long c = (a + b) % 1000000007;
        a = b;
        b = c;
    }
    cout << b;

    return 0;
}