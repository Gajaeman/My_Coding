#include <iostream>
#include <vector>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    vector<vector<int>> g(13);
    vector<int> deg(13,0);

    int a, b;
    for (int i = 0; i < 12; i++){
        cin >> a >> b;
        g[a].push_back(b);
        g[b].push_back(a);
        deg[a]++; deg[b]++;
    }

    for (int i = 1; i <= 12; i++){
        if (deg[i] == 3){
            int sum = 0;
            for (int v : g[i]) {
                sum += deg[v];
            }
            if (sum == 6) {
                cout << i << '\n';
                return 0;
            }
        }
    }
    return 0;
}