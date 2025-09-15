#include <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;
    long long dp[91] = {0, 1, 1};
    if(n <= 2) cout << dp[n];
    else {
        for(int i=3; i <= n; i++) dp[i] = dp[i-1] + dp[i-2];
        cout << dp[n];
    }
    return 0;
}