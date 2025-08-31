#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int n, m, v;
vector<int> adj[1001];
bool visited[1001];

void dfs(int x) {
    visited[x] = 1;
    cout << x << ' ';
    for (int nxt : adj[x]) {
        if (!visited[nxt]) dfs(nxt);
    }
}

void bfs(int start) {
    queue<int> q;
    q.push(start);
    visited[start] = 1;
    while (!q.empty()) {
        int cur = q.front(); 
        q.pop();
        cout << cur << ' ';
        for (int nxt : adj[cur]) {
            if (!visited[nxt]) {
                visited[nxt] = 1;
                q.push(nxt);
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> m >> v;
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }
    for (int i = 1; i <= n; i++) sort(adj[i].begin(), adj[i].end());

    dfs(v);
    cout << '\n';
    fill(visited, visited + n + 1, 0);
    bfs(v);
    cout << '\n';
    return 0;
}