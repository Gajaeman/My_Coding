#include <iostream>
#include <vector>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N; 
    cin >> N;

    vector<long long> dist(N-1);
    for(int i=0;i<N-1;++i) cin >> dist[i];

    vector<long long> price(N);
    for(int i=0;i<N;++i) cin >> price[i];

    long long cur = price[0];
    long long ans = 0;

    for(int i=0;i<N-1;++i){
        ans += cur * dist[i];
        if(price[i+1] < cur) cur = price[i+1];
    }
    cout << ans << '\n';
    return 0;
}