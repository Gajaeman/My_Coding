#include <iostream>
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
ll dp[10001];
int t, p, q;
int tc1, tc2;
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    cin >> tc1 >> tc2;
    for (int i = 0; i < tc1; i++) {
        ll sample = 0;
        ll answer = 0;
        cin >> sample >> answer;
        if (sample != answer) {
            cout << "Wrong Answer";
            return 0;
        }
    }
    for (int i = 0; i < tc2; i++) {
        ll system = 0;
        ll ans = 0;
        cin >> system >> ans;
        if (system != ans) {
            cout << "Why Wrong!!!";
            return 0;
        }
    }
    cout << "Accepted";
    return 0;
}