#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int R, C, Q;
    cin >> R >> C >> Q;
    vector<vector<long long>> ps(R + 1, vector<long long>(C + 1, 0));
    for (int i = 1; i <= R; ++i)
        for (int j = 1; j <= C; ++j) {
            long long v; cin >> v;
            ps[i][j] = ps[i-1][j] + ps[i][j-1] - ps[i-1][j-1] + v;
        }

    while (Q--) {
        int r1, c1, r2, c2; 
        cin >> r1 >> c1 >> r2 >> c2;
        long long s = ps[r2][c2] - ps[r1-1][c2] - ps[r2][c1-1] + ps[r1-1][c1-1];
        int area = (r2 - r1 + 1) * (c2 - c1 + 1);
        cout << s / area << '\n';
    }
    return 0;
}