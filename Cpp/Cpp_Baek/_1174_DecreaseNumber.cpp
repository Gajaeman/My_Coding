#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, a, b, m;
    cin >> n >> a >> b >> m;

    vector<vector<int>> adj(n+1);
    for (int i = 0; i < m; i++) {
        int x, y;
        cin >> x >> y;
        adj[x].push_back(y);
        adj[y].push_back(x);
    }

    vector<int> dist(n+1, -1);
    queue<int> q;
    q.push(a);
    dist[a] = 0;

    while (!q.empty()) {
        int cur = q.front(); q.pop();
        for (int nxt : adj[cur]) {
            if (dist[nxt] == -1) {
                dist[nxt] = dist[cur] + 1;
                q.push(nxt);
            }
        }
    }

    cout << dist[b] << '\n';
    return 0;
}


/* #sol_2
#include <bits/stdc++.h>
using namespace std;

int n, a, b, m;
int adj[101][101];
bool visited[101];
int ans = -1;

void dfs(int cur, int depth) {
    if (cur == b) {
        ans = depth;
        return;
    }
    visited[cur] = true;
    for (int i = 1; i <= n; i++) {
        if (adj[cur][i] && !visited[i]) {
            dfs(i, depth + 1);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> a >> b >> m;
    for (int i = 0; i < m; i++) {
        int x, y;
        cin >> x >> y;
        adj[x][y] = adj[y][x] = 1; // 양방향
    }

    dfs(a, 0);
    cout << ans << '\n';
    return 0;
}
*/