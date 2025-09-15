#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<vector<int>> adj;
vector<bool> visited;
vector<int> order;
int cnt = 1;

void dfs(int k) {
    visited[k] = true;
    order[k] = cnt++;
    for (int nxt : adj[k]) {
        if (!visited[nxt]) dfs(nxt);
    }
}
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N, M, R;
    cin >> N >> M >> R;

    adj.resize(N + 1);
    visited.resize(N + 1);
    order.resize(N + 1);

    for (int i = 0; i < M; i++) {
        int a, b;
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    for (int i = 1; i <= N; i++) sort(adj[i].begin(), adj[i].end());
    dfs(R);
    for (int i = 1; i <= N; i++) cout << order[i] << '\n';
    return 0;
}
