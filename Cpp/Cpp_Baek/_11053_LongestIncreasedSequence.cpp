#include <iostream>
using namespace std;

int A[1000];
int dp[1000];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;
    for (int i = 0; i < n; ++i) cin >> A[i];

    int ans = 0;
    for (int i = 0; i < n; ++i) {
        dp[i] = 1;
        for (int j = 0; j < i; ++j) {
            if (A[j] < A[i] && dp[j] + 1 > dp[i]) {
                dp[i] = dp[j] + 1;
            }
        }
        if (dp[i] > ans) ans = dp[i];
    }

    cout << ans << '\n';
    return 0;
}