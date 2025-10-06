#include <iostream>
#include <vector>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T; cin >> T;
    while(T--){
        int M, N; 
        cin >> M >> N;
        vector<vector<int>> a(M, vector<int>(N));
        for(int i=0;i<M;++i)
            for(int j=0;j<N;++j)
                cin >> a[i][j];

        long long ans = 0;
        for(int j=0;j<N;++j){
            int emptyBelow = 0;
            for(int i=M-1;i>=0;--i){
                if(a[i][j]==0) emptyBelow++;
                else ans += emptyBelow;
            }
        }
        cout << ans << '\n';
    }
    return 0;
}