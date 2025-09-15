#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    while (true) {
        int n;
        cin >> n;
        if (n == 0) break;

        int res = 0;
        int mul = 1;
        int cnt = 1;
        while (n > 0) {
            int digit = n % 10;
            res += digit * mul;
            n /= 10;
            cnt++;
            mul *= cnt;
        }
        cout << res << '\n';
    }
    return 0;
}