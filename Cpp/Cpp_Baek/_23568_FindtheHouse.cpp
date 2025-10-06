#include <iostream>
#include <algorithm>
#include <unordered_map>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n; 
    if (!(cin >> n)) return 0;

    unordered_map<long long, pair<char, long long>> mp;
    mp.reserve(n * 2);

    for (int t = 0; t < n; ++t) {
        long long i, k; char d;
        cin >> i >> d >> k;
        mp[i] = {d, k};
    }

    long long now; 
    cin >> now;

    for (int t = 0; t < n; ++t) {
        auto [d, k] = mp[now];
        now += (d == 'R' ? +k : -k);
    }
    cout << now << '\n';
    return 0;
}