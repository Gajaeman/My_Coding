#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int N; cin >> N;
    vector<long long> v(N);
    long long total = 0;
    for (int i = 0; i < N; ++i) {
        cin >> v[i]; 
        total += v[i];
    }

    long long ans = 0;
    for (int i = 0; i < N; ++i) {
        total -= v[i];
        ans += v[i] * total;
    }
    cout << ans;
    return 0;
}