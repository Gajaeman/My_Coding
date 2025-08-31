#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int R, C;
    cin >> R >> C;
    vector<string> g(R);
    for (int i = 0; i < R; ++i) cin >> g[i];

    vector<string> words;

    for (int r = 0; r < R; ++r) {
        string cur;
        for (int c = 0; c < C; ++c) {
            if (g[r][c] == '#') {
                if (cur.size() >= 2) words.push_back(cur);
                cur.clear();
            } else {
                cur.push_back(g[r][c]);
            }
        }
        if (cur.size() >= 2) words.push_back(cur);
    }

    for (int c = 0; c < C; ++c) {
        string cur;
        for (int r = 0; r < R; ++r) {
            if (g[r][c] == '#') {
                if (cur.size() >= 2) words.push_back(cur);
                cur.clear();
            } else {
                cur.push_back(g[r][c]);
            }
        }
        if (cur.size() >= 2) words.push_back(cur);
    }

    sort(words.begin(), words.end());
    cout << words.front() << '\n';
    return 0;
}
