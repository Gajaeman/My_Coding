#include <iostream>
using namespace std;

int A[17][17];
long long dp[17][17][3];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N; cin >> N;
    for (int i = 1; i <= N; ++i)
        for (int j = 1; j <= N; ++j)
            cin >> A[i][j];

    dp[1][2][0] = 1;

    for (int r = 1; r <= N; ++r) {
        for (int c = 1; c <= N; ++c) {
            if (A[r][c]) continue;

            if (c+1 <= N && A[r][c+1]==0) {
                dp[r][c+1][0] += dp[r][c][0];
                dp[r][c+1][0] += dp[r][c][2];
            }
            if (r+1 <= N && A[r+1][c]==0) {
                dp[r+1][c][1] += dp[r][c][1];
                dp[r+1][c][1] += dp[r][c][2];
            }
            if (r+1 <= N && c+1 <= N &&
                A[r][c+1]==0 && A[r+1][c]==0 && A[r+1][c+1]==0) {
                dp[r+1][c+1][2] += dp[r][c][0];
                dp[r+1][c+1][2] += dp[r][c][1];
                dp[r+1][c+1][2] += dp[r][c][2];
            }
        }
    }

    cout << (dp[N][N][0] + dp[N][N][1] + dp[N][N][2]);
    return 0;
}