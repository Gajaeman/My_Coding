#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N; cin >> N;
    vector<int> a(N);
    for(int i=0;i<N;++i) cin >> a[i];
    int X; cin >> X;
    sort(a.begin(), a.end());
    int ans = 0;
    for(int i=0; i<N; ++i){
        for(int j=i+1; j<N; ++j){
            int sum = a[i] + a[j];
            if(sum == X) ++ans;
            else if(sum > X) break;
        }
    }
    cout << ans << '\n';
    return 0;
}