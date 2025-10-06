#include <iostream>
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
ll dp[10001];
int t, p, q;
int tc;
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    cin >> t;
    for (int i = 0; i < t; i++) {
        cin >> p >> q;
        dp[1] = 1; dp[2] = 1;
        tc += 1;
        if (p < 3) {
            cout << "Case #" << tc << ": " << dp[p] % q << '\n';
        }
        else {
            for (int i = 3; i <= p; i++) dp[i] = (dp[i - 1] + dp[i - 2]) % q;
            cout << "Case #" << tc << ": " << dp[p] << '\n';
        }
    }
}