#include <iostream>
#include <vector>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int K;
    if(!(cin >> K)) return 0;
    int n = (1 << K) - 1;

    vector<int> a(n);
    for(int i = 0; i < n; ++i) cin >> a[i];

    for(int d = 0; d < K; ++d){
        int step  = 1 << (K - d);
        int start = step >> 1;
        bool first = true;
        for(int pos = start; pos <= n; pos += step){
            if(!first) cout << ' ';
            cout << a[pos - 1];
            first = false;
        }
        cout << '\n';
    }
    return 0;
}