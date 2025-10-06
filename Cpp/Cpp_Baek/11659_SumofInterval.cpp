#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M; 
    if (!(cin >> N >> M)) return 0;

    vector<long long> ps(N + 1, 0);
    for (int i = 1; i <= N; ++i) {
        long long x; cin >> x;
        ps[i] = ps[i - 1] + x;
    }

    while (M--) {
        int l, r; cin >> l >> r;
        cout << (ps[r] - ps[l - 1]) << '\n';
    }
    return 0;
}