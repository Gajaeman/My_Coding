#include <iostream>
#include <vector>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    vector<int> tri;
    for(int n=1;;++n){
        int t = n*(n+1)/2;
        if(t > 1000) break;
        tri.push_back(t);
    }

    int T; 
    if(!(cin >> T)) return 0;
    while(T--){
        int K; cin >> K;
        bool ok = false;
        for(int i=0;i<(int)tri.size() && !ok;++i){
            for(int j=0;j<(int)tri.size() && !ok;++j){
                for(int k=0;k<(int)tri.size();++k){
                    if(tri[i]+tri[j]+tri[k] == K){ ok = true; break; }
                }
            }
        }
        cout << (ok ? 1 : 0) << '\n';
    }
    return 0;
}