#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, Q; 
    if(!(cin >> N >> Q)) return 0;

    vector<long long> a(N);
    for(int i=0;i<N;++i) cin >> a[i];

    sort(a.begin(), a.end());

    vector<long long> ps(N+1, 0);
    for(int i=0;i<N;++i) ps[i+1] = ps[i] + a[i];

    ostringstream out;
    while(Q--){
        int L, R; cin >> L >> R;
        out << (ps[R] - ps[L-1]) << '\n';
    }
    cout << out.str();
    return 0;
}