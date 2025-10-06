#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;
    vector<vector<long long>> ps(N + 1, vector<long long>(N + 1, 0));
    for (int i = 1; i <= N; ++i)
        for (int j = 1; j <= N; ++j) {
            long long v; cin >> v;
            ps[i][j] = ps[i-1][j] + ps[i][j-1] - ps[i-1][j-1] + v;
        }

    while (M--) {
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        cout << ps[x2][y2] - ps[x1-1][y2] - ps[x2][y1-1] + ps[x1-1][y1-1] << '\n';
    }
    return 0;
}