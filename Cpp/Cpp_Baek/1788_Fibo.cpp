#include <iostream>
#include <vector>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N; cin >> N;

    vector<int> fibo(2000001);
    fibo[1000000] = 0; fibo[1000001] = 1;

    for(int i = 1000002; i <= 2000000; ++i) 
        fibo[i] = (fibo[i-1] + fibo[i-2]) % 1000000000;
    for(int i = 999999; i >= 0; --i)
        fibo[i] = (fibo[i+2] - fibo[i+1]) % 1000000000;

    if (fibo[1000000 + N] < 0) cout << -1 << '\n';
    else if (fibo[1000000 + N] > 0) cout << 1 << '\n';
    else cout << 0 << '\n';

    cout << abs(fibo[1000000 + N]) << '\n';

    return 0;
}