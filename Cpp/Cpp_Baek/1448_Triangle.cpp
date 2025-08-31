#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N; 
    if (!(cin >> N)) return 0;
    vector<long long> v(N);
    for (int i = 0; i < N; ++i) cin >> v[i];

    sort(v.begin(), v.end(), greater<long long>());

    for (int i = 0; i + 2 < N; ++i) {
        long long a = v[i], b = v[i+1], c = v[i+2];
        if (a < b + c) {
            cout << (a + b + c) << '\n';
            return 0;
        }
    }
    cout << -1 << '\n';
    return 0;
}