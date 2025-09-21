#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N; 
    if(!(cin >> N)) return 0;

    vector<vector<int>> g(N+1);
    g.reserve(N+1);
    for(int i=0;i<N-1;++i){
        int a,b; cin >> a >> b;
        g[a].push_back(b);
        g[b].push_back(a);
    }

    vector<int> parent(N+1, 0);
    queue<int> q;
    parent[1] = -1;
    q.push(1);

    while(!q.empty()){
        int u = q.front(); q.pop();
        for(int v : g[u]){
            if(parent[v] == 0){
                parent[v] = u;
                q.push(v);
            }
        }
    }

    for(int i=2;i<=N;++i) cout << parent[i] << '\n';
    return 0;
}