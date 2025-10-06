#include <iostream>
#include <vector>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N; cin >> N;

    vector<int> deg(N+1, 0);
    for(int i=0;i<N-1;++i){
        int a,b; cin >> a >> b;
        ++deg[a]; ++deg[b];
    }

    long long ans = 0;
    for(int v=1; v<=N; ++v){
        if(deg[v] > 2) ans += deg[v] - 2;
    }
    cout << ans << '\n';
    return 0;
}