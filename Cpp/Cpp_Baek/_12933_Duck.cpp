#include <iostream>
#include <array>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s; cin >> s;

    array<int,4> cnt{0,0,0,0};
    int active = 0, answer = 0;

    for (char c : s) {
        if (c == 'q') { ++cnt[0]; ++active; answer = max(answer, active); }
        else if (c == 'u') { if (!cnt[0]) { cout << -1 << '\n'; return 0; } --cnt[0]; ++cnt[1]; }
        else if (c == 'a') { if (!cnt[1]) { cout << -1 << '\n'; return 0; } --cnt[1]; ++cnt[2]; }
        else if (c == 'c') { if (!cnt[2]) { cout << -1 << '\n'; return 0; } --cnt[2]; ++cnt[3]; }
        else if (c == 'k') { if (!cnt[3]) { cout << -1 << '\n'; return 0; } --cnt[3]; --active; }
        else { cout << -1 << '\n'; return 0; }
    }

    if (active || cnt[0] || cnt[1] || cnt[2] || cnt[3]) cout << -1 << '\n';
    else cout << answer << '\n';
    return 0;
}