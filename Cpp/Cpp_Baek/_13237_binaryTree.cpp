#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n; 
    if (!(cin >> n)) return 0;

    vector<vector<int>> child(n + 1);
    int root = -1;

    for (int i = 1; i <= n; ++i) {
        int p; cin >> p;
        if (p <= 0) root = i;
        else child[p].push_back(i);
    }

    vector<int> depth(n + 1, 0);
    queue<int> q;
    q.push(root);

    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (int v : child[u]) {
            depth[v] = depth[u] + 1;
            q.push(v);
        }
    }

    for (int i = 1; i <= n; ++i) cout << depth[i] << '\n';
    return 0;
}