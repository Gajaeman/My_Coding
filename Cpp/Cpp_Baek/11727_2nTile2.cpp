#include <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;
    int dp[1001] = {0, 1, 3};
    if(n <= 2) cout << dp[n];
    else{
        for(int i = 3; i <= n; i++) dp[i] = (dp[i-2] * 2 + dp[i-1]) % 10007;
        cout << dp[n];
    }
    return 0;
}